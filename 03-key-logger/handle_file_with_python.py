'''
What this script does is when a key is clicked, it takes it and puts it in a text file.
Concepts Covered
    1. File Handling: open(name of file, mode) - if this file doesn't exist, open will create the file automaticlally,
        mode can be read (r), write (w) or append (a)
    2. Listeners: Listens to keystrokes
    3. with keyword realeases resources automatically so that we don't have to use file.close()
    
'''
'''
# without with
file = open("log.txt", 'w')
file.write("ka boom!!!")
print("Keylogger started...")

file.close()

'''

# with 'with'
with open("log.txt", 'a') as f:
    f.write("Hello Again!")


