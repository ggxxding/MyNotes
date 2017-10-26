# README
# TIPS


## how to delete NAME and history

then git push origin master --force


* cd
* git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch NAME' --prune-empty --tag-name-filter cat -- --all
* then git push origin master --force

uptest