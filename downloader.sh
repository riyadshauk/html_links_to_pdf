#!/bin/bash

# This file uses the wkhtmltopdf commandline tool to download all the html as
# pdfs, stored in the links outputed from getLinks.py
# TODO: Create a cover page too?, prob with python...

foldername=$(echo "pdfs_")				# prefix of foldername
foldername=$foldername$(date +%s)		# make a unique foldername to store pdfs in
mkdir $foldername
declare -i i 		# i is now declared as an integer, so works with atoi() in C
i=0
echo $foldername >> foldername.txt 		# purely for output / history
touch $foldername/cover.html
python3 getLinks.py | while read line
do
	echo line$i: $line 		# purely for output / example
   python3 getContent.py $line > $foldername/$i.html
   let "i++"
   echo "$i" > num_of_files.txt 	# subshells flush vars when while-read finishes
done
let i=$(cat num_of_files.txt)+1		# number of files

stripped_url=$(sed -n "s/^url = //p" user_defined_parameters.py | sed "s/\"//g")
echo "<h1>Cover Page (currently blank)</h1><h2>"$stripped_url"</h2>" >> $foldername/cover.html

# Should create the pdf with cover and TOC; something like this:
# wkhtmltopdf cover cover.html toc 0.html 1.html 2.html $foldername/textbook.pdf
gcc -v command_generator.c -o generator
echo "#!/bin/bash" > textbook_create.sh
./generator $i $foldername >> textbook_create.sh
sh textbook_create.sh

# cleanup:
# rm $foldername/*.html
# rm num_of_files.txt
# rm generator
# rm textbook_create.sh
# rm foldername.txt

echo $foldername