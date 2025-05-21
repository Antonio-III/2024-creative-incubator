// A program that calculates how many days has it been since Dec 31.
// (How far along is the date to day 365)
#include <stdio.h>
#include <stdlib.h>
#define OFFSET -1

int main(int argc, char *argv[]){
	int dd, mm, yyyy;
	int len_of_feb, day_no, month;

	printf("Enter date in dd/mm/yyyy format: \n");

	if (scanf( "%d/%d/%d", &dd, &mm, &yyyy )!=3){

		printf("Invalid input\n");

		exit(EXIT_FAILURE);
	}


	len_of_feb = 28 + (yyyy%4==0 && (yyyy%100!=0 || yyyy%400==0));
	day_no = dd;
	for (int i=0; i<mm-1;i+=1){
		if (i==2-1){
			day_no+=len_of_feb;
		}
		else if (i==4+OFFSET || i==6+OFFSET || i==9+OFFSET || i==11+OFFSET ){
			day_no+=30;
		}
		else{
			day_no+=31;
		}
	}
	printf("You are %d days into the year. \n", day_no);
}
