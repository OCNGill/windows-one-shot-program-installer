# Requirements: Windows One-Shot Program Installer

## User Stories (US)
- **US-001**: As a user, I want to search for programs by name so I can add them to my install list.
- **US-002**: As a user, I want to view the list of selected programs before installing.
- **US-003**: As a user, I want to initiate the installation process with a single action.
- **US-004**: As a user, I want the installation to proceed automatically without further interaction.
- **US-005**: As a user, I want to run the tool easily (e.g., double-click a file).

## Functional Requirements (FR)
- **FR-001**: The system shall allow the user to search for applications using `winget`.
- **FR-002**: The system shall maintain a list of selected applications (ID and Name).
- **FR-003**: The system shall execute the installation command for each selected application.
- **FR-004**: The system shall provide a Web-based Interface (Streamlit) with structured search results (Table/Grid).
- **FR-005**: The system shall support silent installation arguments (`--silent` or equivalent) where available via `winget`.
- **FR-006**: The system shall display the user's available disk space.
- **FR-007**: The system shall estimate and display the size of selected applications (where available).
- **FR-008**: The system shall warn the user if selected applications exceed available disk space.

## Technical Requirements (TR)
- **TR-001**: The system shall be written in Python 3.x using the `streamlit` library.
- **TR-002**: The system shall use `subprocess` to execute shell commands.
- **TR-003**: The system shall use `winget` as the package manager backend.
- **TR-004**: The system shall be launchable via a `.bat` file that installs dependencies and runs the app.
- **TR-005**: The system shall handle errors gracefully and display them in the UI.
- **TR-006**: The system shall use `shutil` to monitor disk usage.
