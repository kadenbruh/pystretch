# pystretch
A basic Python GUI that stretches your resolution. Meant for new Linux users who play competitive PC games.

![screenshot](https://cdn.discordapp.com/attachments/1040887503420395604/1071304466319552604/image.png)

## Prerequisites
* Python (99% you will have this already)
* pip
* git
* xrandr (99% you will have this already)

## Install
1. Get PySimpleGUI
```
pip install PythonSimpleGUI
```
2. Clone repo and run
```
git clone https://github.com/atkbrz/pystretch
cd pystretch
python pystretch.py
```

## Configuration 
Default configuration file included was made for my setup. Please change to your needs. The configuration file is very self explanatory even for those who are new to Linux. As long as you have done stretched resolution modifications on Windows before, it should be straightforward. 
```
cd pystretch
sudo nano config.sh
```
Need help finding what your monitor is?
```
xrandr | grep " connected " | awk '{ print$1 }'
```
