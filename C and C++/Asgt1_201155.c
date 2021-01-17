#include <stdio.h>
/*  STUDENT NAME : MOHAMAD FARIS AIMAN BIN MOHD FAIZAL 			MATRIC NO : 201155
	DESCRIPTION : SIMPLE PROGRAM THAT READS MARKS FROM 0-100 FROM USER IN A LOOP AND RETURNS EACH GROUP OF GRADE UNTIL INPUT N IS READ. 
*/

int main()
{
	int mark,a,b,c,d,e;
	char input;
	c = 0;
	d = 0;
	e = 0;
	
	do{
	printf("Enter marks:");
	scanf("%d",&mark);
	if (mark >= 80 && mark <=100)
	{
		printf("Correspending grade is A\n");
		a++;
	}
	else if(mark >= 60 && mark <= 79)
	{
		printf("Correspending grade is B\n");
		b++;
	}
	else if (mark >= 50 && mark <=59)
	{
		printf("Correspending grade is C\n");
		c++;
	}
	else if (mark >= 40 && mark <= 49)
	{
		printf("Correspending grade is D\n");
		d++;
	}
	else if (mark == 999)
	{
		printf("Invalid.\n");
		printf("Analysis:\n");
		printf("%d student(s) obtained A\n",a);
		printf("%d student(s) obtained B\n",b);
		printf("%d student(s) obtained C\n",c);
		printf("%d student(s) obtained D\n",d);
		printf("%d student(s) obtained E\n",e);
		printf("Do you want to continue: YES- Y or NO - N:");
		scanf(" %c",&input);
	}
	else if (mark >= 0 && mark <40)
	{
		printf("Correspending grade is E\n");
		e++;
	}

	}while(input!='n');

return 0;
}	