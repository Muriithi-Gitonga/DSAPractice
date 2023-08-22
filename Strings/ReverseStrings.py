def reverseWord(word):
    # your code here
    word_list = list(word)

    start = 0
    end = len(word_list) - 1

    while start < end:
        word_list[start], word_list[end] = word_list[end], word_list[start]
        start += 1
        end -= 1

    return ''.join(word_list)


print(reverseWord('tosh'))
