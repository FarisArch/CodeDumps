#include <stdio.h>
#define COST_PER 30.00
int main()
{
  char programme[100];
  char line[1] = "*";
  int attendance;
  float totalMeal,courseFee,totalPayment;

  printf("Enter type of course:");
  scanf("%s",&programme);

  printf("Enter number of person attending the course:");
  scanf("%d",&attendance);

  printf("Enter course fee per person (RM) :");
  scanf("%f",&courseFee);

  printf("*****************************************************\n");


  totalMeal = attendance * COST_PER;
  totalPayment = (courseFee * attendance) + totalMeal;

  printf("Number of attendance :%d Person\n Course fee : RM%.2f\n Meals : RM%.2f\n Overall payment : RM%.2f\n",attendance,courseFee,totalMeal,totalPayment);

  return 0;

}
