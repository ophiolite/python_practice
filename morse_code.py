def morse_converter(string):
    '''Takes in string of morse code and return number based on
    morse coding.
    1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 -----'''
    n = 5
    number_lst = []
    morse_lst = [string[i:i+n] for i in range(0, len(string), n)]
    for each in morse_lst:
        if each == '.----':
            number_lst.append(1)
        if each == '..---':
            number_lst.append(2)
        if each == '...--':
            number_lst.append(3)
        if each == '....-':
            number_lst.append(4)
        if each == '.....':
            number_lst.append(5)
        if each == '-....':
            number_lst.append(6)
        if each == '--...':
            number_lst.append(7)
        if each == '---..':
            number_lst.append(8)
        if each == '----.':
            number_lst.append(9)
        if each == '-----':
            number_lst.append(0)
    return int(''.join(str(x) for x in number_lst))

if __name__ == '__main__':
    morse_converter("..----------...")
