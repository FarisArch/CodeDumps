#include <stdio.h>
// DECLARING FUNCTIONS
int day(int days);
int month (int months);
int year (int years);

int a,b,c,retd,retm,rety;

int main()
{
  a = 30;
  b = 1;
  c = 2020;
  rety = year(c);
  retm = month(b);
  retd = day(a);

  if (retd <= 31 && retm >= 1)
  {
    if (retm == 1 ||retm == 3 ||retm == 5 ||retm == 8 ||retm == 10 ||retm == 12)
    {
         if (retm == 1)
          printf("%d January %d",retd,rety);
         else if (retm == 3)
          printf("%d March %d",retd,rety);
         else if (retm == 5)
          printf("%d May %d",retd,rety);
         else if (retm == 8)
          printf("%d August %d",retd,rety);
         else if (retm == 10)
          printf("%d October %d",retd,rety);
         else if (retm == 12)
          printf("%d December %d",retd,rety);
    }
    else
    {
      if (retd <= 30 )
      {
        if (retm == 2)
        printf("%d February %d",retd,rety);
        else if (retm == 4)
          printf("%d April %d",retd,rety);
        else if (retm == 6)
          printf("%d June %d",retd,rety);
        else if (retm == 7)
          printf("%d July %d",retd,rety);
        else if (retm == 9)
          printf("%d September %d",retd,rety);
        else if (retm == 11)
          printf("%d November %d",retd,rety);
      }
      else
      {
        printf("Cannot exceed 30 days");
      }
    }
  }
  else
  {
    printf("Invalid month or day!");
  }
  return 0;
}

// FUNCTION
int year(int years)
{
  int d = years;
  return d;

}
int month(int months)
{
  int e = months;
  if (e >= 1 && e <= 12)
  {
    return e;
  }
  else
  {
    return 1;
  }
}
int day (int days)
{
  int f = days;
  if (f >=1 && f<= 31)
  {
    return f;
  }
  else
  {
    return 1;
  }
}
