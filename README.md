# html_links_to_pdf

This is a tool to convert multiple texts (in html) on different pages into one combined text, as a pdf.

Languages:
	- BASH
	- C
	- Python 3

Dependency: 
	- https://github.com/wkhtmltopdf/wkhtmltopdf

Usage:
Simply modify user_defined_parameters.py by using your favorite html-inspecting 
tools or methods. Run downloader.sh. This will create a folder with a file named 
"text_letter.pdf" as the combined pdf (tip: the foldername will be in the repo 
directory and is easily find-able with a command like "ls -t | sed -n 1p").

Current Problems:
This tool does not work with all websites, as some sites do not have content-
identifiable html elements (such as class or id tags). I'm considering creating 
a local mapping of the important html elements and restructuring this tool to 
work while applying this generalized fix. I also have yet to add a GUI. I'm 
considering a browser plugin, or something like QT or even something as simple 
as AppleScript (though that only works on Mac OS).

P.S. -- My little blurb:
This tool can be useful for viewing the contents found in various links 
by scrolling through one pdf. My favorite pdf-viewing platforms are: Google 
Chrome (using the left- and right-arrows to quickly traverse pages), iBooks (for iOS: useful for viewing various pages of a pdf on one screen). I like these platforms for viewing text in a pdf because they are time-efficient.