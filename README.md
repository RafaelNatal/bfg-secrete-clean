# bfg-secrete-clean


https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
https://rtyley.github.io/bfg-repo-cleaner/



java -jar bfg-1.14.0.jar --replace-text passwords.txt allos-databricks

git reflog expire --expire=now --all && git gc --prune=now --aggressive

git push --force


git log --grep=benefit_error_handling
git log -Gbenefit_error_handling
