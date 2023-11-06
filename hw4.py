# import csv
# with open('file.csv', 'r') as csvfile:
#     file_reader = csv.reader(csvfile, delimiter=',')
#     content = list(file_reader)
#     c = 0
#     l = []
#     for r in content:
#         for i in range(len(r)):
#             res = r[i] + '-' + str(r.count(r[i]))
#
#             if res not in l:
#                 l.append(res)
#     for cha in l:
#         print(cha)




# with open('movie.txt', 'r') as file:
#     movie = file.readlines()
#     for c in range(len(movie)):
#         movie[c] = movie[c][0:len(movie[c])-2]
#     movie_dict = {}
#     for i in movie:
#         movie_dict[i[:2]] = i[3:]
#     sorted_list = dict(sorted(movie_dict.items()))
#     # print(sorted_list)
#
# with open('output_keys.txt', 'w') as file:
#     for item in sorted_list:
#         file.write(item + ': ' + sorted_list[item] + '\n')



with open('grade.txt', 'r') as grade:
    grade_list = grade.readlines()
    for i in range(len(grade_list)):
        grade_list[i] = grade_list[i][:-1]
    for c in range(len(grade_list)):
        grade_list[c] = grade_list[c].split(' ')

    ave = 0
    for i in range(len(grade_list)):
        Sum = 0
        for x in range(2, len(grade_list[i])):
            grade_list[i][x] = int(grade_list[i][x])
        for x in range(2, len(grade_list[i])):
            Sum += grade_list[i][x]
        ave = Sum / (len(grade_list[i])-2)
        if ave >= 90:
            grade_list[i].append('A')
        elif ave >= 80:
            grade_list[i].append('B')
        elif ave >= 70:
            grade_list[i].append('C')
        elif ave >= 60:
            grade_list[i].append('D')
        else:
            grade_list[i].append('F')

    print(grade_list)

    ave2 = 0
    ave_list = []
    for i in range(2, len(grade_list)):
        sum1 = 0
        for x in range(len(grade_list)):
            sum1 += grade_list[x][i]
        ave2 = sum1 / 5
        ave_list.append('{:.2f}'.format(ave2))


with open('report.txt', 'w') as report:
    for i in grade_list:
        for x in i:
            report.write(str(x) + ' ')
        report.write('\n')
    report.write('Averages: midterm1 '+str(ave_list[0])+', midterm2 '+str(ave_list[1])+', final '+str(ave_list[2]))
