// 因为是找最后一个单词的长度，所以应该直接从右往左遍历
int lengthOfLastWord(char * s) {
    int len = strlen(s);
    if (len == 0) {
        return 0;
    }
    
    int res = 0;
    
    for (int i = len-1; i >= 0; i--) {
        if (s[i] == ' ' && res == 0) {  // 说明这个空格是字符串最后的空格（还没有开始计数）
            continue;
        } else if (s[i] != ' ') {
            res++;
        } else if (s[i] == ' ' && res != 0) { // 说明这个空格是最后一个单词前面的空格
            return res;
        }
    }
    return res;
    
}

// 这是从左往右遍历，不方便，不是最佳做法
// int lengthOfLastWord(char * s){
//     int len = strlen(s);
//     if (len == 0) {
//         return 0;
//     }
//     char last[len];
//     last[0] = s[0];
//     int ptr = 1;
//     for (int i = 1; i < len; i++) {
//         if (s[i] == ' ') {
//             continue;
//         } else if (s[i] != ' ' && s[i-1] == ' ') {
//             ptr = 0;
//             last[ptr] = s[i];
//             ptr++;
//         } else if (s[i] != ' ' && s[i-1] != ' ') {
//             last[ptr] = s[i];
//             ptr++;
//         }
//     }
    
//     int res = 0;
//     for (int i = 0; i < ptr; i++) {
//         if (last[i] != ' '){
//             res++;
//         } else {
//             return res;
//         }
//     }
//     return res;
// }
