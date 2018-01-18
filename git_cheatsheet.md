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
