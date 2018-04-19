 # Bat Thumbnails\par
\par
This project is  part of a bigger web application. My part of the project was to create thumbnails for pictures in the images folder that didn't have one. The table itself was made by executing a sql file in a Unix terminal (I did NOT make this initial file).  The python script will , when executed:\par
1. Create a new column to this table, thumbnailExists  \par
2. Look to see if a given file has a thumbnail for it.\par
3. If so records that file's name. \par
 3. thumbnail gets turned from false to true for that image entry.\par
\par
## Getting Started
\par
You will need to be running a Unix terminal.   \par
 Use the following copy commands, if you're not using scotch box, you should change the destination directory to your home directory:\par
\par
cp /var/www/2017_bat.tar /home/vagrant/static/images\par
cp /var/www/bat_thumbs.tar /home/vagrant/static/images/thumbs\par
cp /var/www/bats.sql /home/vagrant\par
Run the following commands to extract the image files you need.\par
cd /home/vagrant/static/images\par
tar xvf 2017_bat.tar\par
\par
Then you need to run mySQL and use the bats.sql file to build the initial table. \par
Run the command \par
SET SESSION sql_mode = ' '; \par
so you can alter the table without getting errors about invalid default formats.\par
import the static/images/thumbs folders to your home directory (/home/ . . .). \par
You can then make the python file executable, copy it to /usr/lib/cgi-bin (using sudo command)\par
Change directories to the cgi-bin and execute the python file.\par
\par
## Testing
\par
You can change directories to /home/<systemname>/static/images/thumbs and run the ls command to make sure you see the thumbnails made after runniing the python script.\par
You can also run \par
USE bat_pics;\par
SELECT * FROM bats \par
In MySQL to make sure that the filenames were recorded, and the thumbnailExists column was made and it has 1s ather than 0 for the files with thumbnails\par
\par
## Built With\par
\par
* [Python]({{\field{\*\fldinst{HYPERLINK https://www.python.org/ }}{\fldrslt{https://www.python.org/\ul0\cf0}}}}\f0\fs22 - Programming language used\par
* [MySQL]({{\field{\*\fldinst{HYPERLINK https://www.mysql.com/ }}{\fldrslt{https://www.mysql.com/\ul0\cf0}}}}\f0\fs22 ) - Database used.\par
* [ScotchBox]({{\field{\*\fldinst{HYPERLINK https://github.com/scotch-io/scotch-box }}{\fldrslt{https://github.com/scotch-io/scotch-box\ul0\cf0}}}}\f0\fs22 ) If you don't have a Unix environment, you can download this , Vagrant, and a virtual machine (VirtualBox is what I used) to run a virtual Unix environment. \par
* ({{\field{\*\fldinst{HYPERLINK https://jonathanbossenger.com/setting-up-a-local-development-environment-with-scotch-box/ }}{\fldrslt{https://jonathanbossenger.com/setting-up-a-local-development-environment-with-scotch-box/\ul0\cf0}}}}\f0\fs22 ) This will walk you through setting up a Vagrant Scotchbox environment.\par
*[Vagrant]({{\field{\*\fldinst{HYPERLINK https://www.vagrantup.com/ }}{\fldrslt{https://www.vagrantup.com/\ul0\cf0}}}}\f0\fs22 ) Allows  you to run virtual  lightweightenvironments like ScotchBox.\par
*[VirtualBox]({{\field{\*\fldinst{HYPERLINK https://www.virtualbox.org/ }}{\fldrslt{https://www.virtualbox.org/\ul0\cf0}}}}\f0\fs22 ) Virtual Machine maker.\par
\par
\par
## Authors\par
\par
Lissette Ramos\par
bats.sql file made by Jerry Reed.\par
\par
## License\par
\par
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details\par
\par
## Acknowledgments\par
\par
* Hat tip to anyone who's code was used\par
* Inspiration\par
* etc\par
}
