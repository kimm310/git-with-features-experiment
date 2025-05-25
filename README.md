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


2. **Clone the Repository (if not done already)**
    ```cmd
   git clone git@github.com:tabeatheunicorn/git-with-features-experiment.git
    ```


3. **Run the Python Script**
    ```cmd
   python -m src.main
    ```
   Running the script will not be required during the experiment, but it can help you understand the project's functionality.

## 2. Setting up the Tool (upload on pipIndex?)

1. **Download the [git_tool] put google drive link here**


2. **Install the Tool**
    ```cmd
   python -m pip install <prefix>/git_tool-<version>-py3-none-any.whl
    ```
   
3. **Test the Installation**
   - **Display Feature Commands**

      Run the following command to see all available feature commands:
     ```cmd
     python -m src.main
     ```
      You should see an output similar to:
     ```cmd
     Branch feature-metadata successfully created.
     ```

4. **Set Up Git Hooks**

   The hooks are required to ensure that feature information is added before committing files. This step can be skipped 
   if you plan to add feature information only to existing commits using the `git feature commit` command, bypassing the 
   need for `git feature add` and its subcommands. Information about the subcommands can be found [here]().
   - **Find the Tool Path**
   
     This will output a path ending with `__init__.py`
     ```cmd
     python -c "import git_tool; print(git_tool.__file)"
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
