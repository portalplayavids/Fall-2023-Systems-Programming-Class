# Setting Up your GitHub Repository

### Open & prepare a new VSCode window.
#### - Open a new terminal window in VSCode. 
    * In the top menu: Terminal > New Terminal *
### In the terminal window, ...
## BEGIN SETUP:
**Step 1:** Navigate to your `$ /HOME/"Username"/` directory.

        - Type: '$ cd ~' to navigate to your home directory.

        - Type: '$ pwd' to confirm the path you are in.

**Step 2:** Clone the repository: `git clone [https://github.com/.../"repo-name".git]`

        - Note: The OMARControlApp repo is `https://github.com/portalplayavids/OMARControlApp.git` 

**Step 3:** Navigate to the newly cloned repository: `$ cd "repo-name"`

        - In this case, `$ cd OMARControlApp`

**Step 4:** install any dependencies: `$ flutter packages get`
    
        - Note: This will install all the dependencies listed in the pubspec.yaml file.

**Step 5:** Setup your account profile: `$ git config --global ...`

- *Part A:* `$ git config --global user.email "their@email.com"`

        - This is the email associated with your GitHub account.
    
- *Part B:* `$ git config --global user.name "Your Name"`

        - This can be any name you want to associate with your I.D. for making commits. 

**Step 6:** Create a new branch: `$ git checkout -b "branch-name"`
    
        - Note: This branch will be an isolated branch.
            
            Meaning, you can make changes to the code without affecting the master branch.

### - You can now make changes to any code file in the Repo.
#

# Committing your changes to the Repository

To commit changes to the repository, you must first add the files you want to commit, to the ***staging area***.

- There are many ways to do this, but the ***easiest*** way, in the terminal is to...

  - **Stage all files:** `$ git add .` -- **OR** -- **Stage a specific file:** `$ git add "file-name"`

    ***Then...***

  - **Commit the changes:** `$ git commit -m "commit message"`

        *** Note: The commit message should be a short description of the changes you made. ***

    ***Lastly...***

  - **Push the changes to the repository:** `$ git push origin "branch-name"`

        - This will push the changes you made to the branch "branch-name".
            
            ** ALWAYS push to the branch YOU made to WORK IN; NOT the master branch **


###### Made By: [Elijah Guzman]  - Last Updated: 09/16/2023