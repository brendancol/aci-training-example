# Initial Clone (from an existing repository)
```bash
git clone <my repo url>
```

# Start a new Git Repository
```bash
git init
```

# Add local Git Repo to Github Repo
```bash
1. Create a new repo within Github
2. Run command `git remote add origin <my github repo url>
```

# Adding changes to Github
```bash
git add my_changed_file.py
git commit -m 'changed an important file'
git push
```

# Getting changes to Github
```bash
git pull
```

# Create a new branch (and check it out)
```bash
git checkout -b new_feature_branch
```

# Switch between branches
```bash
git checkout <branch name>
```

# Checkout the last branch used
```bash
git checkout -
```

# Git config setting to push to remote branch of same name
```bash
git config --global push.default current
```

# Merge a feature branch into master
```bash
1. git checkout <the branch you want to merge INTO>
2. git merge <branch you want to merge FROM>
```

# Stash changes that you don't want commit...but don't want to lose
```bash
git stash
```

# Grab changes from the stash and re-apply to your project
```bash
git stash pop --index 1 # notice the index argument to grab a specific stashed change
```

# Look at Git History (and find a commit hash)
```bash
git log

```
# Go back to an earlier commit
```bash
git checkout <commit hash you found in `git log`>
```
#### The many uses of `git checkout`

##### change between branches
`git checkout my_new_feature`

##### undo changes to any existing file which was not commited (or added...)
`git checkout my_changed_file.py`

##### go back in time to an earlier commit
`git checkout a234bf452092` (we got the commit hash from `git log`)








