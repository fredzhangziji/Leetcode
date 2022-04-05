#include <stdlib.h>
#include <stdio.h>

int main() 
{
      long a = 21474836460;
      printf("%d\n", INT_MAX);
      printf("%lld\n", a);
      printf("%d", a > INT_MAX);
}