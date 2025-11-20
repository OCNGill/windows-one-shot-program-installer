# Project Definition: Windows One-Shot Program Installer

## Overview
A Python-based automation tool designed to simplify the process of reinstalling Windows applications. The tool allows a user to search for programs, build a list, and execute a bulk installation with minimal interaction.

## Goals
- Provide a simple CLI interface for non-technical users (wrapped in a script).
- Automate the retrieval and installation of software.
- Minimize user interaction during the installation phase.

## Scope
- **OS**: Windows 11
- **Language**: Python 3.x
- **Package Manager**: Winget (Windows Package Manager)
- **Interface**: Command Line Interface (CLI)

## Key Features
1.  **Program Search**: Query the `winget` repository for application names.
2.  **Selection List**: Add found programs to a queue/list.
3.  **Bulk Install**: Iterate through the list and install programs silently.
4.  **Easy Launch**: A `.bat` file to handle environment setup and script execution.
