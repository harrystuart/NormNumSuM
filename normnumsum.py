import numpy as np

def find_longest_substring_slice(str1, str2, len_str1, len_str2):
    num = np.zeros(shape=(len_str1, len_str2))

    max_substring_len = 0
    last_substring_begin = 0

    for i in range(len_str1):
        for j in range(len_str2):
            # Extend substring
            if str1[i] == str2[j]:
                if i == 0 or j == 0:
                    num[i][j] = 1
                else:
                    num[i][j] = 1 + num[i - 1][j - 1]

                # Found new best substring
                if num[i][j] > max_substring_len:
                    max_substring_len = num[i][j]

                    this_substring_begin = i - num[i][j] + 1

                    if this_substring_begin != last_substring_begin:
                        last_substring_begin = this_substring_begin

    begin = last_substring_begin
    end = last_substring_begin + max_substring_len - 1

    return int(begin), int(end)

def normnumsum(str1, str2):
    str1 = str1.strip()
    str2 = str2.strip()

    len_str1 = len(str1)
    len_str2 = len(str2)

    if len_str1 > len_str2:
        shorter_str = str2
        len_shorter_str = len_str2
        longer_str = str1
        len_longer_str = len_str1
    else:
        shorter_str = str1
        len_shorter_str = len_str1
        longer_str = str2
        len_longer_str = len_str2

    num_substring_movements = 0

    current_len_shorter_str = len_shorter_str

    while current_len_shorter_str > 0:
        substring_begin, substring_end = \
            find_longest_substring_slice(shorter_str, longer_str, current_len_shorter_str, len_longer_str)

        if substring_end <= 0:
            num_substring_movements += len(shorter_str.replace(" ", ""))
            break
        else:
            num_substring_movements += 1
            shorter_str = (shorter_str[:substring_begin] + " " + shorter_str[substring_end + 1:]).strip()
            current_len_shorter_str = len(shorter_str)

    return num_substring_movements / len_shorter_str if num_substring_movements > 1 else 0

