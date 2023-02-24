import csv

class StudentFailedException(Exception):
    def __init__(self,value):
        self.value = value

with open('student_grades.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        try:
            if line_count == 0:
                print(f'Columns names are {", ".join(row)}')
                line_count += 1
            else:
                average = (int(row[1]) + int(row[2]) + int(row[3])) / 3
                print(f'{row[0]}\'s average score is {average}')
                line_count += 1
                if average < 70:
                    raise StudentFailedException (f'Student {row[0]} failed')
        except ValueError:
            print('invalid input')
        except StudentFailedException as error:
            print(error)

print(f'Processed {line_count} lines.')


