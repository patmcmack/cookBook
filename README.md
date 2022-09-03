# Personal Cookbook
## cookBook.pdf
Open [``` cookBook.pdf```](https://patmcmack.github.io/cookBook/cookBook.pdf) to view. 

This is a cookbook I wrote simply to keep track of recipes that I enjoy, taken from multiple sources. Written in *LaTex* with design inspiration from **ORLY** textbooks.

Also an excuse for me to practice using GitHub.

The original cover template was adapted from GitHub user [johnjohnlin](https://github.com/johnjohnlin/oreilly_cover)

## \image2text
Originally I kept track of these recipes in a spreadsheet using screenshots. This was not extensible or easy to manage. 

To save time when covering said screenshots to text, I wrote a short Python script that used ```pytesseract``` to export the images to a simple .txt file. From that, I could simply cut into my .tex file to produce the cookbook 

## pushAll.sh
Bash script to push changes to this github Main branch as well as push just the .pdf file to the gh-pages branch. Probably both lazy and bad practice to reduce this to a single script 