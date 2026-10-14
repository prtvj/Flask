## Git and GitHub Commands Cheat Sheet

| Task | Command |
|---|---|
| Initialize Git | `git init` |
| Check current branch | `git branch --show-current` |
| Check changes | `git status` |
| Stage all eligible changes | `git add .` |
| Stage a specific file | `git add app.py` |
| Commit changes | `git commit -m "message"` |
| Connect GitHub remote | `git remote add origin <URL>` |
| View remote repository | `git remote -v` |
| Rename current branch to main | `git branch -M main` |
| Push main for the first time | `git push -u origin main` |
| Create and switch to a new branch | `git checkout -b routing` |
| Switch to an existing branch | `git checkout routing` |
| Push a new branch to GitHub | `git push -u origin routing` |
| Switch to main | `git checkout main` |
| Merge routing into main | `git merge routing` |
| Push subsequent commits | `git push` |
| Download and merge remote changes | `git pull` |
| View commit history | `git log --oneline` |
| Compare changes | `git diff` |

### Typical Workflow

**1. Push a project to GitHub for the first time**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <URL>
git push -u origin main
```

**2. Create a new branch and push changes**

```bash
git checkout -b routing
git add .
git commit -m "Add Flask routing"
git push -u origin routing
```

**3. Push additional changes to the same branch**

```bash
git add .
git commit -m "Update Flask application"
git push
```

**4. Merge a feature branch into main**

```bash
git checkout main
git pull origin main
git merge routing
git push origin main
```

> **Note:** Replace `routing` with your branch name and `<URL>` with your GitHub repository URL. Run `git remote add origin <URL>` only if a remote is not already configured. The merge workflow assumes your local `main` branch exists and you intend to merge the feature directly; you can also use a GitHub pull request.