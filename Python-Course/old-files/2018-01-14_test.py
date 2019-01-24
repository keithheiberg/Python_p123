import os
print(os.listdir( 'c:\\PyProjects\\' ))
basepath = 'c:\\PyProjects\\'
fname = 'Test.txt'
for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    print( path )
    print(os.path.getmtime( path ))
    filename, file_extension = os.path.splitext( path )
    if file_extension == '.txt':
        f = open(path, 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
