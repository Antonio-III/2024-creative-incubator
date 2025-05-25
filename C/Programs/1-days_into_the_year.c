// A program that calculates how many days has it been since Dec 31.
// (How far along is the date to day 365)
#include <stdio.h>
#include <stdlib.h>

#define OFFSET -1

#define MONTH_OF_FEB 2
#define MONTH_OF_APR 4
#define MONTH_OF_JUNE 6
#define MONTH_OF_SEP 9 
#define MONTH_OF_NOV 11

#define LEAP_YEAR 4
#define HUNDRED_YEARS 100
#define FOUR_HUNDRED_YEARS 400

int main(int argc, char *argv[]){
	int dd, mm, yyyy;
	int len_of_feb, day_no, month;

	printf("Enter date in dd/mm/yyyy format: \n");

	if (scanf( "%d/%d/%d", &dd, &mm, &yyyy )!=3){

		printf("Invalid input\n");

		exit(EXIT_FAILURE);
	}


	len_of_feb = 28 + (yyyy % LEAP_YEAR == 0 && (yyyy % HUNDRED_YEARS != 0 || yyyy % FOUR_HUNDRED_YEARS == 0));
	day_no = dd;
	for (int curr_mm = 0; curr_mm < mm - 1; curr_mm += 1){
		if (curr_mm == MONTH_OF_FEB + OFFSET){
			day_no += len_of_feb;
		}
		else if (curr_mm == MONTH_OF_APR + OFFSET || curr_mm == MONTH_OF_JUNE + OFFSET || curr_mm == MONTH_OF_SEP + OFFSET || curr_mm == MONTH_OF_NOV + OFFSET ){
			day_no += 30;
		}
		else{
			day_no += 31;
		}
	}
	printf("You are %d days into the year. \n", day_no);
}
