# SUSE-JalaliDate

**JalaliDate** For **SUSE**


![openSUSE](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/OpenSUSE_Logo.svg/400px-OpenSUSE_Logo.svg.png?20210522053639)
![calender](https://icons.iconarchive.com/icons/aha-soft/large-calendar/256/Calendar-icon.png)
## Install

```
cd /tmp && wget https://github.com/KooshaYeganeh/SUSE-JalaliDate/archive/refs/heads/main.zip && unzip main.zip && cd SUSE-JalaliDate-main && sudo cp susejcal /usr/bin && cd /tmp && echo "susejcal installed [ OK ]"
```

**Note :** To continue **Developing** the JalaliDate, the development environment must be created :

After downloading and going to the software directory 

**1- install virtualenv and the next step is to install pip packages.**  
**2- activate virtual enviroment**  
**3- Install python Packages**

> My pip is pip3.9

```
sudo pip3.9 install virtualenv && source venv/bin/activate && pip3.9 install -r requirements.txt
```
### Create Installer File

```
pyinstaller susejcal.py -n susejcal --onefile && sudo cp dist/susejcal /usr/bin && rm -rf dist build && rm susejcal.spec && echo "Installer File Created [ OK ]"
```


## Run


**Normal Run :**

```
susejcal
```

**-v** or **--verbose**

```
susejcal --verbose
```

**-i** or **--info**

```
susejcal --info
```

**-d** or **--digit**

```
susejcal --digit
```


## Remove 

```
sudo rm /usr/bin/susejcal
```
