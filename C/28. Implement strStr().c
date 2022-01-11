

int strStr(char * haystack, char * needle){
    if (strlen(needle) == 0) {
        return 0;
    }
    
    int lenNee = strlen(needle);
    int lenHay = strlen(haystack);
    
    int ptr1 = 0;
    int ptr2 = 0;
    int i;
    
    for (i = 0; i <= lenHay - lenNee; i++) {        
        ptr1 = i;
        for (int j = 0; j < lenNee; j++) {
            if (*(haystack+ptr1) != *(needle+ptr2)) {
                ptr2 = 0;
                break;
            } else {
                ptr1++;
                ptr2++;
            }
        }
        if (ptr2 == lenNee) {
            return i;
        }
    }
    
    return -1;
}
