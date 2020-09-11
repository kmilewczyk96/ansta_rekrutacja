def missing_elements(entry_list: list, n: int):
    return [i for i in range(1, n + 1) if i not in entry_list]


if __name__ == '__main__':
    print(missing_elements([2, 3, 7, 4, 9], 10))
