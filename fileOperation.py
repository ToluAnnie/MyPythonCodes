f = open('myfile.txt', 'r')

first_line = f.readline()
second_line = f.readline()

print(first_line, end='')
print(second_line)

for line in f:
    print(line, end='')



f = open('myfile.txt', 'a')
f.write('\nI\'m about to append this shit bro')
f.write('\nPython is fun!')


input_file = open('myfile.txt', 'r')
output_file = open('outputfile.txt', 'w')
msg = input_file.read(10)

while len(msg):
    output_file.write(msg + '\n')
    msg = input_file.read(10)

input_file.close()
output_file.close()

input_file = open('myimage.jpg', 'rb')
output_file = open('myoutputimage.jpg', 'wb')
msg = input_file.read()
output_file.write(msg)

input_file.close()
output_file.close()

from os import remove, rename

remove('outputfile.txt')
rename('myfile.txt', 'hisfile.txt')