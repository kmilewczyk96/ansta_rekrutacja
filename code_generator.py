def code_generator(code_1: str, code_2: str):
    result = []
    code_1 = f'{code_1[0: 2]}{code_1[3: 6]}'
    code_2 = f'{code_2[0: 2]}{code_2[3: 6]}'

    for i in range(int(code_1) + 1, int(code_2)):
        i = str(i)
        result.append(i[0: 2] + '-' + i[2: 5])

    return result


if __name__ == '__main__':
    print(code_generator('79-900', '80-155'))
