#define SIZE 200

bool isIsomorphic(char * s, char * t){
    if (strlen(s) != strlen(t)) {
        return false;
    }
    if (strlen(s) == 1) {
        return true;
    }
    
    // initialize the dict array with 0
    int dict[SIZE];
    for (int i = 0; i < SIZE; i++) {
        dict[i] = 0;
    }
    
    for (int i = 0; i < strlen(s); i++) {
        if (dict[s[i]] == 0) { // first time, map the char to the char in t
            // check if this t[i] already had a mapping
            for (int j = 0; j < strlen(s); j++) {
                if (dict[s[j]] == t[i]) {
                    return false;
                }
            }
            dict[s[i]] = t[i];
        } else { // already had the mapping
            if (dict[s[i]] != t[i]) { // the mapping is wrong, return false
                return false;
            }
        }
    }
    return true;
}
