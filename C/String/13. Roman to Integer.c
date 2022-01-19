// use array to be a dictionary
// the char will be converted to int, which can be the index of the array
int table['X'+1] = {
    ['I'] = 1,
    ['V'] = 5,
    ['X'] = 10,
    ['L'] = 50,
    ['C'] = 100,
    ['D'] = 500,
    ['M'] = 1000  
};

int romanToInt(char * s){
    int res = 0;
    // when the string pointer is not pointing to the end of the string
    while (*s != '\0') {
        if (table[*s] < table[*(s+1)]) {
            res -= table[*s];
        } else {
            res += table[*s];
        }
        s++;
    }
    return res;
}