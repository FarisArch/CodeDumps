#include <stdio.h>

int main()
{
  int marks,size,b,sum,mark,average,pass,fail;

  printf("Enter size of class:");
  scanf("%d",&size);

  for (b = 1,sum = 0 ,pass = 0 ,fail = 0; b <= size ; b = b + 1)
  {
    do
    {
      printf("Student #%d mark:",b);
      scanf("%d",&mark);
    } while(!(mark >= 0 && mark <= 100));

    if(mark >= 50)
    {
      pass = pass + 1;
    }
    else
    {
      fail = fail + 1;
    }

    sum = (sum + mark);
  }

  average = sum / size;
  printf("Total pass : %d \n", pass);
  printf("Total fail : %d \n", fail);
  printf("Average mark is : %d",average);

}
