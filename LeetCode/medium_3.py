def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    if len(s) == 0:
        return s
    
    res_lst = []
    max_palin_len = 0
    nr_of_chars_count = 0
    palindrome_longest = ''
    all_substrings_lst = get_all_substrings(s)
    for subs in all_substrings_lst:
        res_lst = [ch for ch in subs]
        nr_of_chars_count = len(res_lst)
        if res_lst == list(reversed(res_lst)):
            if nr_of_chars_count > max_palin_len:
                max_palin_len = nr_of_chars_count
                palindrome_longest = subs
                
    return palindrome_longest

def get_all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

print(longestPalindrome('abcbadc'))