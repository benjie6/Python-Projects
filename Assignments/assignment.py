import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    our = conn.cursor()
    our.execute("CREATE TABLE IF NOT EXISTS tbl_persons(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('test.db')
#tuple of names
fileList = ('information.docx','hello.txt','myImage.png',\
                 'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_persons (col_fname)VALUES (?)", (x,))
            print(x)
conn.close()
    

    
