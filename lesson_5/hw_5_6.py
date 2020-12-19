
with open('text_5_6.txt') as predmet:
    subj = {}
    for line in predmet:
        name = line.split(' ', 1)
        elements = len(line)
        my_list = []
        ind = 0
        while ind < elements:
            s_int = ''
            a = line[ind]
            while '0' <= a <= '9':
                s_int += a
                ind += 1
                if ind < elements:
                    a = line[ind]
                else:
                    break
            ind += 1
            if s_int != '':
                my_list.append(int(s_int))

        subj[name[0]] = sum(my_list)
    print(f'Общее количество часов по предметам:\n{subj}')
