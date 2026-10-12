#!/usr/bin/env python3
"""Generate one app into a new repository subdirectory, without overwriting files."""
import argparse
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
DEFAULT_NEXT_VERSION = "16.4.0"


def scaffold(root, platform, app_dir=None, name="StarterApp", bundle_id="com.example.starterapp", next_version=DEFAULT_NEXT_VERSION):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Repository root must be a directory")
    app_dir = app_dir or ("web" if platform == "web" else "mobile")
    if not re.fullmatch(r"[a-z][a-z0-9-]*", app_dir):
        raise ValueError("App directory must be a lowercase directory name, without path separators")
    if platform not in ("web", "mobile"):
        raise ValueError("Platform must be web or mobile")
    if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", name):
        raise ValueError("App name must start with an uppercase letter and contain only letters/digits")
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9-]*(\.[A-Za-z][A-Za-z0-9-]*)+", bundle_id):
        raise ValueError("Bundle ID must be a reverse-DNS identifier")
    if not re.fullmatch(r"\d+\.\d+\.\d+", next_version):
        raise ValueError("Next.js generator version must be an exact stable version, such as 16.4.0")
    destination = root / app_dir
    if destination.exists() or destination.is_symlink():
        raise ValueError(f"Refusing to overwrite existing destination: {destination}")
    with tempfile.TemporaryDirectory(prefix=".scaffold-", dir=root) as staging:
        app = Path(staging) / app_dir
        if platform == "web":
            subprocess.run([
                "npx", "--yes", f"create-next-app@{next_version}", str(app),
                "--ts", "--eslint", "--app", "--src-dir", "--no-tailwind",
                "--no-react-compiler", "--no-cache-components", "--no-agent-feedback",
                "--use-npm", "--import-alias", "@/*", "--disable-git", "--yes",
            ], check=True)
            # Overlay only the starter files in the freshly generated, isolated app.
            shutil.copytree(ASSETS / "web", app, dirs_exist_ok=True)
            package_path = app / "package.json"
            package = json.loads(package_path.read_text())
            package.setdefault("scripts", {}).update({"typecheck": "tsc --noEmit", "lint": "eslint ."})
            package_path.write_text(json.dumps(package, indent=2) + "\n")
            with (app / ".gitignore").open("a") as ignore:
                ignore.write("\n# Keep the public environment template tracked.\n!.env.example\n")
            manifest = {"platform": platform, "generator": "create-next-app", "generatorVersion": next_version}
        else:
            shutil.copytree(ASSETS / "mobile", app)
            for path in app.rglob("*"):
                if path.is_file():
                    path.write_text(path.read_text().replace("__APP_NAME__", name).replace("__BUNDLE_ID__", bundle_id))
            manifest = {"platform": platform, "appName": name, "bundleId": bundle_id, "minimumIOS": "17.0"}
        (app / "scaffold.json").write_text(json.dumps(manifest, indent=2) + "\n")
        # Recheck after the generator runs; never replace a concurrently created app.
        if destination.exists() or destination.is_symlink():
            raise ValueError(f"Destination appeared during generation: {destination}")
        app.rename(destination)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=["web", "mobile"])
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--app-dir")
    parser.add_argument("--name", default="StarterApp")
    parser.add_argument("--bundle-id", default="com.example.starterapp")
    parser.add_argument("--next-version", default=DEFAULT_NEXT_VERSION)
    args = parser.parse_args()
    try:
        output = scaffold(args.repo, args.platform, args.app_dir, args.name, args.bundle_id, args.next_version)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Scaffolding failed: {error}\n")
    print(f"Created {output}. Read the platform reference for build and verification commands.")


if __name__ == "__main__":
    main()
