# 2021DAflask
Flask introductory exercises

c:\Python37> python -m pip install flask  

# ex1 - First Flask app

# ex2 - Routing

# ex3 - Using variables eg an ID for a database query

## accepted variable types
string - (default) text (without a slash)

int -  positive integers

float - positive floating point values

path - similar to string , allows slashes

uuid  - UUID strings

# ex4 - Using URLs with redirection

# ex5 - HTTP methods and request object

## http methods supported
GET	    This is used to send the data in an without encryption of the form to the server.  
HEAD	provides response body to the form  
POST	Sends the form data to server. Data received by POST method is not cached by server.  
PUT	    Replaces current representation of target resource with URL.  
DELETE	Deletes the target resource of a given URL  

# ex6 - Static files and templates

# ex7 - Jinja2 templating

# ex8 - Json api response

# ex9 - Json api request and response

# ex10  - sessions



# References

## http methods
GET	    This is used to send the data in an without encryption of the form to the server.  
HEAD	provides response body to the form  
POST	Sends the form data to server. Data received by POST method is not cached by server.  
PUT	    Replaces current representation of target resource with URL.  
DELETE	Deletes the target resource of a given URL  

## error codes
400 – For Bad Request  
401 – For Unauthenticated  
403 – For Forbidden request  
404 – For Not Found  
406 – For Not acceptable  
425 – For Unsupported Media  
429 – Too many Requests  


# setup RPi
# image the Raspberry Pi
raspberry Pi imager v1.72    
Raspberry pi OS (32-bit) to SDHC card 16Gig 
in options set to enable ssh , and set your Wifi SSID , etc    

# OR connect device and first boot
https://www.raspberrypi.com/documentation/computers/getting-started.html
Connect up hdmi , keyboard, mouse and boot 
Select country, language , timezone 
Confirm screen display 
Wifi search - select ssid and enter password 
Software update – download updates, install updates 
Restart 

# configure Rpi
## SSH install (If not done by installer)  

```
$sudo systemctl enable ssh 
$sudo systemctl start ssh 
$ip a    - note down ip address eg 10.0.0.67
```
## SSH into Rpi
```
C:>putty.exe -ssh pi@10.0.0.67 22

```
## RDP install – remote desktop protocol 
```
#sudo apt install xrdp 
#sudo service xrdp start 
```
# RDP into Rpi to setup dev environment
on windows start rdp client
c:>mstsc.exe /v:10.0.0.67:3389

## install VScode
```
$sudo apt install code -y
$sudo apt install git
```

## clone repository 2021DAflask  
```
$git clone https://github.com/SteveGaleComputingStudies/2021DAflask.git  

```

## run vscode with cloned project
```
$cd 2021DAflask  
$code .
```
Install extensions - Python extension 

## install python libraries (can be done from VScode terminal window)
```
$sudo apt install python3-pip
$python3 -m pip install flask
$python3 -m pip install --upgrade flask
```

## run project (can be done from VScode terminal window)
```
$sudo python3 xxx.py
```

## update project and re-run
```
C:>putty.exe -ssh pi@10.0.0.67 22
$cd 2021DAflask  
$git pull
$sudo python3 xxx.py 
```

# run Flask app as cron task
https://www.raspberrypi.org/documentation/linux/usage/cron.md
```
$crontab –e 

@reboot sudo python3 /home/pi/2021DAflask/xxx.py & 

$sudo reboot 
```
# Enable I2C 
```
Preferences > Raspberry Pi Configuration – Interfaces 
I2C * Enable [OK] 
```
## Test I2c and look for device addresses
```
#sudo apt-get install -y i2c-tools 
#i2cdetect -y 1 

    0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f 

00:          -- -- -- -- -- 08 -- -- -- -- -- -- --  
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- 1e --  
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
60: 60 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
70: -- -- -- -- -- -- -- --  
```
```

