# Issue handling instructions

Follow this workflow when completing issues in this repository.

## 1. Understand the issue

- Read the issue description and comments, then inspect the relevant files and repository instructions.
- Identify the requested outcome and keep changes focused on it.
- Resolve routine implementation choices independently. Ask for clarification only when missing information materially affects the outcome.

## 2. Create a branch

- Create a new branch from the latest `main` before changing files.
- Use a lowercase prefix and a lowercase, hyphen-separated version of the issue title:

  | Change type | Prefix | Example |
  | --- | --- | --- |
  | New functionality | `feature/` | `feature/add-tool-runner` |
  | Documentation | `docs/` | `docs/create-read-me-file` |
  | Urgent bug fix | `hotfix/` | `hotfix/fix-tool-timeout` |

- Do not commit issue work directly to `main`.
- If a branch name already exists, add the issue number or another descriptive suffix to create a distinct branch.

## 3. Implement and verify

- Complete the requested work on the issue branch.
- Update relevant documentation when behavior or usage changes.
- Review the diff and run checks appropriate to the change. For documentation-only work, verify accuracy, formatting, links, and examples; executable tests are not required unless relevant.
- Fix failures caused by the change before merging. Report any unresolved blockers or checks that could not be run.

## 4. Commit and open a pull request

- Commit the completed changes to the issue branch with a clear message describing the work.
- Push the branch and open a pull request targeting `main`.
- Give the PR a descriptive title and explain what changed, why, and how it was verified.
- Include `Closes #<issue-number>` when the PR fully resolves the issue. For partial work, reference the issue without a closing keyword.

## 5. Merge and preserve the branch

- Once verification and required repository checks pass, merge the PR as part of completing the requested issue workflow.
- Respect branch protection and required reviews. Do not bypass them; report blockers if they prevent merging.
- Keep the issue branch after the merge. Do not delete it, and ensure automatic branch deletion will not remove it.
- Confirm the PR is merged, the changes are present on `main`, and the branch still exists.
- Confirm a fully resolved linked issue is closed; leave partially completed issues open.

## 6. Report completion

- Provide the PR link and branch name.
- Briefly summarize the completed work, verification results, and any remaining limitations.
