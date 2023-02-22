import csv

class StudentFailException:
    print('Student failed')


with open('student_grades.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Columns names are {", ".join(row)}')
            line_count += 1
        else:
            average = (int(row[1]) + int(row[2]) + int(row[3])) / 3
            print(f'{row[0]}\'s average score is {average}')
            if average < 70:
                raise StudentFailException
            line_count += 1


print(f'Processed {line_count} lines.')


