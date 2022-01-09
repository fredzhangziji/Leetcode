

char * longestCommonPrefix(char ** strs, int strsSize){
    // edge cases
    if (strsSize == 0) {
        return "";
    }
    
    if (strsSize == 1) {
        return strs[0];
    }
    
    int commonLen = 0;  
    int minLen = strlen(strs[0]);
    
    // iterate and find the minimum length of the string in the array
    for (int i = 1; i < strsSize; i++) {
        if (strlen(strs[i]) < minLen) {
            minLen = strlen(strs[i]);
        }
    }
    
    for (int i = 0; i < minLen; i++) {  // start from first character comparison
        for (int j = 0; j < strsSize - 1; j++) {    // compare all the strings in the strs
            // check and update the minLen
            if (strs[j][i] == strs[j+1][i]) {
                // we need every string's prefix to be the same
                if (j == strsSize - 2) {
                    commonLen++;
                }
            } else {
                goto breakPart;
            }
        }
    }
    
    breakPart:
    if (commonLen > 0) {
        // here we need commonLen + 1 since later we will add a '\0' at the end
        // otherwise it will overflow the heap size
        char *res = (char *)malloc(sizeof(char)*(commonLen+1));
        
        //char *res = malloc(sizeof(int)*commonLen); or we can use this
        
        strs[0][commonLen] = '\0';
        strcpy(res, strs[0]);
        return res;
    } else {
        return "";
    }
}