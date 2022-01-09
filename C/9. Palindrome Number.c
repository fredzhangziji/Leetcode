#include <stdbool.h>

bool isPalindrome(int x){
    if (x < 0) {
        return false;
    }
    
    int originX = x;
    long long int res = 0;
    
    while (x > 0) {
        res = res * 10 + x % 10; // 新数*10，老数取个位
        x = x / 10; // 更新原数
    }
    printf("good");
    return res == originX;
}