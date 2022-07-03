# Making a git commit into a single command 
# This is bad practice 
# takes user input for commit message 

# USE: " sh pushAll.sh "Commit message here" "

# Commits to Main branch
git add .
git commit -m "$1"
git status
git push origin Main

# Copies cookBook.pdf into ignored /coverPage/ folder
cp -f cookBook.pdf coverPage/cookBook.pdf

# Changes to gh-pages branch
git checkout gh-pages

# Copies /coverPage/cookBook.pdf into gh-pages 
cp -f  coverPage/cookBook.pdf cookBook.pdf

# Commits into gh-pages branch
git add cookBook.pdf
git commit -m "$1"
git push origin gh-pages

# Returns to Main branch
git checkout Main 
