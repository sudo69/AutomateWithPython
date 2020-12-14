# This Script For Input Values in List as User Input number of list item
import time
import sys
try:
    UserList = []
    print(UserList)             # This code will print empty list
    input_str = int(input('Please enter a Number Of List''\n'))         # this will determine how many items will be in the list
    print('please enter', input_str, 'Values')      # this code will request number of item the determined before

    for i in range(0, input_str):   # this loop will keep going as user input
        item = int(input())         # this variable will keep the value
        UserList.append(item)       # this code will append the values in UserList

    print('user list is: ', UserList)       # this code will print the list with new item as user input
    time.sleep(5)                           # this code will wait 5 sec to see your input

except KeyboardInterrupt:
    sys.exit()                              # this exception will wait until the user press Ctrl + C
