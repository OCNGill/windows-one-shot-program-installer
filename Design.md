# Design: Windows One-Shot Program Installer

## Architecture
The system follows a simple flat structure for ease of use and maintenance.

### Components

1.  **Launcher (`make_my_computer_great_again.bat`)**
    *   **Responsibility**: Check for Python, install `streamlit` if missing, and launch `streamlit run app.py`.
    *   **TR Implemented**: TR-004

2.  **Streamlit App (`app.py`)**
    *   **Responsibility**: Render the Web UI, handle user input, manage session state (selected programs), and trigger installs.
    *   **FR Implemented**: FR-004, FR-006, FR-008
    *   **TR Implemented**: TR-001, TR-006

3.  **Program Manager (`manager.py`)**
    *   **Responsibility**: Maintain the state of selected programs (Name, ID, Size). Calculate totals.
    *   **FR Implemented**: FR-002, FR-007

4.  **Winget Wrapper (`winget_wrapper.py`)**
    *   **Responsibility**: Construct and execute `winget` commands. **Parse output into structured data.**
    *   **FR Implemented**: FR-001, FR-003, FR-005, FR-007
    *   **TR Implemented**: TR-002, TR-003

## Data Flow
1.  User starts `make_my_computer_great_again.bat`.
2.  Browser opens with Streamlit app.
3.  Sidebar shows "Disk Space: X GB Free".
4.  User types in "Search" box.
5.  `app.py` calls `winget_wrapper.search_package()`.
6.  **Wrapper parses stdout and returns list of dicts.**
7.  Results displayed in a Grid/Table.
8.  User clicks "Add" on a row.
9.  `app.py` calls `winget_wrapper.get_package_details()` to find size (if possible).
10. Program added to `st.session_state['selected_packages']`.
11. Sidebar updates with list and **Running Total Size**.
12. User clicks "Install All".

## Detailed Design

### `winget_wrapper.py`
- `search_package(query: str) -> list[dict]`: Returns `[{'Name':..., 'Id':..., 'Version':..., 'Source':...}]`.
- `get_package_details(id: str) -> dict`: Returns `{'Size': ...}`.
- `install_package(package_id: str) -> bool`: Returns success/failure.

### `manager.py`
- `add_package(package: dict)`: Stores full dict.
- `remove_package(package_id: str)`
- `get_total_size() -> str`
- `get_selected_packages() -> list`

### `app.py`
- `render_sidebar()`: Disk usage, list of apps, total size.
- `render_search()`: Search input.
- `render_results()`: **Iterate results and show "Add" button for each.**
- `format_size(bytes)`: Helper.
