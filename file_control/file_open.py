"""
open() is a built-in Python function used to open a file and return a file object. Normally it take two parameter
first is file name and second is file mode. This two parameter are string.

When the mode is not given, Python uses "r" by default, which means read mode.
"""

f = open('code.txt')

"""
This means Python tries to open code.txt as a text file for reading. The file is searched in the current working 
directory first, not automatically in Desktop or any other folder.

If the File Does Not Exist in the given file location, Python does not create a new file. Instead, an error is raised.
like : FileNotFoundError

So in read mode, the file must already exist.
"""

"""
# Current Working Directory (CWD)
"code.txt" is a relative path. Relative path means the file location is decided from the current folder where the 
Python program is running.
"""

import os
print(os.getcwd())

"""
print(os.getcwd()), this returns: /Users/aubdurrobanik/Desktop/allfile/python_code/file_control

then open("code.txt") means : /Users/aubdurrobanik/Desktop/allfile/python_code/file_control/code.txt

So, to open a file from a specific folder, the full path must be used like :
"""

f = open("/Users/aubdurrobanik/Desktop/allfile/python_code/file_control/code.txt")

"""
Or in a cleaner form:
"""

from pathlib import Path
# print("full path : ", Path.home() / "Desktop/allfile/python_code/file_control/code.txt")
f = open(Path.home() / "Desktop/allfile/python_code/file_control/code.txt")

"""
Q : What is File Descriptor?
-> A file descriptor is a small integer used internally by the OS to represent the open file.

A file descriptor is not the file itself. It is only an internal ID used by the operating system.
"""

# Example :
print("File Descriptor : ", f.fileno())

"""
The output something like: 3. This 3 is the file descriptor number.
"""

"""
# Internal Working of open()
open() does not directly read the disk by itself. Python asks the operating system to open the file. The operating system checks 
whether the file exists and whether permission is allowed.

If the file is found, the operating system creates a file descriptor. After that Python wraps that file descriptor inside a 
file object. That file object is what gets stored in f.

So conceptually: file name -> OS file descriptor -> Python file object
"""

"""
# Cursor Position
When a file is opened, the file cursor starts at position 0. That means reading begins from the first character.
After f.read(), the cursor moves to the end of the file.
"""

print("First Read Start : ", f.read())
print("Second Read Start : ", f.read())

"""
The first read() consumes the content. The second read() finds nothing left to read.
The cursor can be moved back using fileObject.seek(0)
"""

f.seek(0)
print("Third Read Start : ", f.read())

"""
# close()
close() tells Python and the operating system that file work is finished. When a file is opened the system keeps some 
resources reserved for that file. These resources include:
  - a file descriptor
  - a buffer
  - internal OS tracking for the open file
Those resources stay active until the file is closed.
"""

f.close()

"""
When f.close() runs:
  - the buffer is finalized
  - any pending data is written out
  - the file descriptor is released
  - the file object is marked as closed

Q : What means by `any pending data is written out`?
When we run f.write("Hello") :
  - "Hello" is placed into a buffer in RAM
  - It is NOT immediately guaranteed to be on disk
  - The file object keeps track of this buffered data

in this time if run f.close():
  - Python checks Is there any data in buffer not yet written?
  - If YES, Python forces a flush operation
  - Flush operation:
      1. Sends buffered data to OS
      2. OS writes data to disk file
   - After that:
      1. Buffer becomes empty
      2. File descriptor is released
      3. File is safely closed

So, 
- Pending data = data already given to write() but still stored in a memory buffer (RAM) and not yet physically written 
to the disk file.

- Written out = that buffered data is forced to be sent from memory to disk storage.
"""

"""
After closing file by close(), f still exists as a Python variable but the file behind it is no longer open.
So, if we run f.read() for f.write("Anik") after close a file object it show error like : 
             ValueError: I/O operation on closed file

Because after close() function call : 
  - the file descriptor is already released
  - the file object is closed
  - read/write operations are no longer valid
  
Think of a file like a door:
1. open() = open the door
2. file operations = work inside the room
3. close() = shut the door and return the key
After the door is shut, the room is not available through that same connection anymore.
"""

print(f.read())


# standard format
with open("code.txt", "r") as f:
    print(f.read())

"""
# with statement
 - with is used to automatically manage resources
 - It ensures the file is properly closed after the block ends
 - Even if an error occurs, Python closes the file automatically

# Automatic file close
 - After the with block ends, Python automatically does : f.close()
 - No manual close() is needed
 - After this point, f cannot be used for reading or writing
"""
