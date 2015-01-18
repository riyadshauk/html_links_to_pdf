/* This generator should output to stdout something like the below example command:
	wkhtmltopdf cover cover.html toc 0.html 1.html 2.html $foldername/textbook.pdf
	Parameters:
		1: Number of files
		2: Name of destination
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv) {
	int files = 10;
	files = (int)atol(argv[1]);
	char * destination = argv[2];
	// printf("\nfiles - 1: %d\ndestination: %s\n\n", files, destination);
	printf("wkhtmltopdf --page-size Letter cover %s/cover.html toc ", destination);
	int i = 0;
	for(i = 0; i < files; i++) {	// file0.html up to fileN.html
		printf("%s/%d.html ", destination, i);
	}
	printf("%s/text_letter.pdf", destination);
	return 0;
}