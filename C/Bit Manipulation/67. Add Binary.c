

char * addBinary(char * a, char * b){
    int lenA = strlen(a);
    int lenB = strlen(b);
    int lenC = lenA > lenB ? lenA : lenB;
    lenC += 2; // one for '\0', and one for possible carry
    int tmp = 0;
    
    char *res = (char*)malloc(sizeof(char) * lenC);
    
    // index
    lenA--;
    lenB--;
    lenC--;
    res[lenC] = '\0';
    lenC--;
    
    while (lenC >= 0) {
        if (lenA >= 0) {
            tmp += a[lenA] - '0'; // char - char = int 也就是他们相差的数字
            lenA--;
        } else {
            tmp += 0;
        }
        if (lenB >= 0) {
            tmp += b[lenB] - '0'; // char - char = int 也就是他们相差的数字
            lenB--;
        } else {
            tmp += 0;
        }
        res[lenC] = tmp % 2 + '0'; // int 得加基准char才能制度偏移量-得到相应的char
        tmp /= 2; // get the carry if there is any
        lenC--;
    }
    // if there is no carry for the whole number, return the address + 1 to avoid the first 0
    if (res[0] == '0') {
        return res + 1;
    }
    return res;
}
