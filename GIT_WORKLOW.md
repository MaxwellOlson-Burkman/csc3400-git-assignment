Teams ranching strategy:
Master Branch(Master) -- Contains the cleaned up code
feature branches(feature/something)-- developes individual tasks on these
release branch(release/versipn) -- this is what gets ushes as current "final product"

Commit messege conventions:
try to keep it clear and short and have a header that decries what it is aboot
feature: a new feature
fix: fixed a bug
and so on

Code review process:
have teammates look over and try to run pushed code from branches

Release workflow
create a release/vsomething that branches from main
do final tests 
tag release
merge the release 
push to remote

Common git commands
`git clone <url>` – Clone a repository
`git status` – Check changes
`git add <file>` – Stage changes
`git commit -m "message"` – Commit staged changes
`git pull` – Update local branch
`git push` – Push changes to remote
`git branch` – List branches
`git checkout <branch>` – Switch branches
`git merge <branch>` – Merge branch
`git stash` – Temporarily save changes
`git log --oneline --graph` – View commit history