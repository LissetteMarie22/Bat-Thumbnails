# Bat Thumbnails

This project is one part of a bigger web application. My part of the project was to create thumbnails for pictures in the images folder that didn't have one. The table itself was made by executing a sql file in a Unix terminal (I did NOT make this initial file).  The python script will , when executed:
1. Create a new column to this table, thumbnailExists  
2. Look to see if a given file has a thumbnail for it.
3. If so records that file's name. 
 3. thumbnail gets turned from false to true for that image entry.

## Getting Started

You will need to be running a Unix teerminal. Download this file system so that you have all of the files you need and the correct folder tree structure.  
Then use the following copy comands, if you're not using scotch box, you should change the destination directory to your home directory:

cp /var/www/2017_bat.tar /home/vagrant/static/images

cp /var/www/bat_thumbs.tar /home/vagrant/static/images/thumbs

cp /var/www/bats.sql /home/vagrant
Run the following commands to extract the image files you need.

cd /home/vagrant/static/images

tar xvf 2017_bat.tar

Then you need to run mySQL and use the bats.sql file to build the initial table. 
Run the command 
SET SESSION sql_mode = ' '; 


so you can alter the table without getting errors about invalid default formats.
import the static/images/thumbs folders to your home directory (/home/ . . .). 
You can then make the python file executable, copy it to /usr/lib/cgi-bin (using sudo command)
Change directories to the cgi-bin and execute the python file.

## Testing

You can change directories to /home/<systemname>/static/images/thumbs and run the ls command to make sure you see the thumbnails made after runniing the python script.
You can also run 

USE bat_pics;
 
SELECT * FROM bats;

In MySQL to make sure that the filenames were recorded, and the thumbnailExists column was made and it has 1s ather than 0 for the files with thumbnails

## Built With

* [Python](https://www.python.org/)- Programming language used
* [MySQL](https://www.mysql.com/) - Database used.
* [ScotchBox](https://github.com/scotch-io/scotch-box) If you don't have a Unix environment, you can download this , Vagrant, and a         virtual machine (VirtualBox is what I used) to run a virtual Unix environment.) 
* [ScotchBox Set up Guide](https://jonathanbossenger.com/setting-up-a-local-development-environment-with-scotch-box/) This will walk you through setting up a Vagrant Scotchbox environment.

* [Vagrant](https://www.vagrantup.com/) Allows  you to run virtual  lightweightenvironments like ScotchBox.
* [VirtualBox](https://www.virtualbox.org/) Virtual Machine maker.


## Authors

Lissette Ramos
bats.sql file made by Jerry Reed.
