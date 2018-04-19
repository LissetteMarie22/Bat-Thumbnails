import datetime
import mysql.connector
from PIL import Image
import glob, os
from os import listdir
from os.path import isdir, isfile, join
import datetime
db = mysql.connector.connect(host='localhost',database='bat_pics',user='root',password='root')
cursor = db.cursor ( )
thumbnail_column = (" ALTER TABLE bats ADD COLUMN thumbnailExists bool")
cursor.execute(thumbnail_column)


query_files = glob.glob('/home/vagrant/static/images/*.jpg')
needs_thumbnail = []
thumbnail_exists = ("INSERT INTO bats (filename,thumbnailExists) VALUES (%s, %s)")

for i in query_files:
    if os.path.isfile(i):
            ROOT = "/home/vagrant/static"
            in_dirs = [path for (path, dirs, filenames)
                      in os.walk(ROOT)
                      if i in filenames]

    if i in in_dirs:
        data = (i, 1)
        cursor.execute(thumbnail_exists, data) 
    else:
        needs_thumbnail.append(i)
size = (120,120)
counter = 0

for pic in needs_thumbnail:
    m = Image.open(pic)
    m.load()
    m.thumbnail(size)
    m.save("/home/vagrant/static/images/thumbs/thumbnail_%s.jpg" % (counter))
    data = (pic, 1)
    cursor.execute(thumbnail_exists, data) 
    counter +=1
