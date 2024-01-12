


def count_letters(word,letter):
    count = 0
    new_lst = []
    for i in range(0, len(word), 1):
        new_lst.append(word[i : i + 3])
    print(new_lst)

    for i in new_lst:
        if i == letter:
            count += 1
    return print(count)


count_letters("hello world", "wor")
