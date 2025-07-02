# Installation Guide

## Prerequisites

- **Git** installed [Download Git for Windows](https://git-scm.com/download/win)
- **Python 3** installed [Download Python for Windows](https://www.python.org/downloads/windows/)

## 1. Setting up the Repository

1. **Verify Installations for Requirements**

    ```cmd
   git --version
    ```
   ```cmd
   python --version
    ```
   
    **Note: The actual command for running a python script may vary depending on the system configuration.**
   
    Ensure that versions are displayed to confirm proper installation.


2. **Clone the Repository**
    ```cmd
   git clone https://github.com/kimm310/git-with-features-experiment.git
    ```


3. **Run the Python Script**
    ```cmd
   python -m src.main
    ```
   Running the script will not be required during the experiment, but it can help you understand the project's functionality.

## 2. Setting up the Tool

1. **Install the Tool**
    ```cmd
   python -m pip install dist/git_tool-1.0.11-py3-none-any.whl
    ```
   
2. **Test the Installation**

      Run the following command to display all available feature commands:
     ```cmd
     git feature
     ```
      You should be able to see an output similar to:
     ```cmd
     Branch feature-metadata created locally from origin.
     ```

3. **Set Up Git Hooks**

   The hooks are required to ensure that feature information is added before committing files. This step can be skipped 
   if you plan to add feature information only to existing commits using the `git feature commit` command, bypassing the 
   need for `git feature add` and its subcommands.
   - **Find the Tool Path**
   
     This will output a path ending with `__init__.py`
     ```cmd
     python -c "import git_tool; print(git_tool.__file__)"
     ```
   - **Locate the Hooks Directory**
   
     Remove `__init__.py` from the path and append `hooks` instead. The path should look similar to:
     ```cmd
     C:\Users\YourName\AppData\Local\Programs\Python\Python39\Lib\site-packages\git_tool\hooks
     ```
   - **Set the Hooks Path**
   
     Replace `<path>` with the path you found in the previous step.
     ```cmd
     git config core.hooksPath <path>
     ```
   - **Check the Git Hooks Path**
   
     Display the path you set in the previous step using following command:
     ```cmd
     git rev-parse --git-path hooks
     ```
