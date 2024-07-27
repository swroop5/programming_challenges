def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    if len(s) == 0:
        return 0
    lis = [ch for ch in s]
    res_lst = []
    max_subs_len = 0
    nr_of_chars_count = 0
    for ind, ch in enumerate(lis):
        if ch in res_lst:
            if nr_of_chars_count > max_subs_len:
                max_subs_len = nr_of_chars_count
            
            res_lst = res_lst[res_lst.index(ch)+1:]
            res_lst.append(ch)
            
            nr_of_chars_count = len(res_lst)
            
            continue
        res_lst.append(ch)
        nr_of_chars_count += 1
    if nr_of_chars_count > max_subs_len:
        max_subs_len = nr_of_chars_count
    return max_subs_len

print(lengthOfLongestSubstring("dvdf"))