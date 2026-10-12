# Swift mobile scaffold

## Layout and prerequisites

Generate source on any host with Python; build on macOS with Xcode and an installed compatible iOS Simulator. Install XcodeGen separately if absent (for example `brew install xcodegen` on a Homebrew-equipped Mac). The scaffold targets iOS 17+ for Observation and uses XcodeGen's version-controlled `project.yml` rather than hand-editing a `.pbxproj` or pretending a Swift package is a complete iOS app.

```text
mobile/
  App/StarterApp.swift           @main app entry point
  Features/Home/HomeView.swift   SwiftUI presentation
  Features/Home/HomeModel.swift  @MainActor @Observable state
  Core/Models/Counter.swift      Testable domain logic
  Tests/CounterTests.swift       Unit test target
  project.yml                   App, test target, shared scheme
  scaffold.json                 Name and bundle identifier
```

Keep app composition in `App/`, feature-specific presentation in `Features/`, and truly shared domain/infrastructure in `Core/`. Add protocol-based async networking and injected services only when a feature needs them; keep credentials off-device unless they are appropriate user credentials. Do not store server secrets in app resources. Keep persistence and authentication choices explicit rather than adding unused dependencies.

## Generate the project and verify on macOS

From `mobile/`, use the app name chosen during scaffolding (replace `StarterApp` below):

```bash
xcodegen generate --spec project.yml
xcodebuild -list -project StarterApp.xcodeproj
xcodebuild -showdestinations -project StarterApp.xcodeproj -scheme StarterApp
```

Select an installed simulator ID from the final command, then run:

```bash
xcodebuild -project StarterApp.xcodeproj -scheme StarterApp -destination 'platform=iOS Simulator,id=SIMULATOR_UUID' CODE_SIGNING_ALLOWED=NO build test
```

Open the generated project in Xcode and verify that Increment changes the counter and Reset returns it to zero. The template includes an XCTest check for repeated increments and reset. Run the app on an iPhone and iPad simulator to verify layout. Configure a development team, a unique bundle identifier, app icons, and distribution settings before device distribution. The generated project is ignored and reproducible from `project.yml`; commit the spec and source. Do not claim simulator validation from a Linux host.

## Official sources

Checked October 12, 2026:

- [Apple SwiftUI app structure](https://developer.apple.com/documentation/swiftui/app)
- [Apple model data and Observation (iOS 17+)](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app)
- [XcodeGen project specification (upstream)](https://github.com/yonaskolb/XcodeGen/blob/master/Docs/ProjectSpec.md)
- [XcodeGen installation (upstream)](https://github.com/yonaskolb/XcodeGen)

Confirm XcodeGen supports your Xcode project format before upgrading the toolchain.
