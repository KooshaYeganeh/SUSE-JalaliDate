# SUSE-JalaliDate
JalaliDate For SUSE 


![openSUSE](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/OpenSUSE_Logo.svg/400px-OpenSUSE_Logo.svg.png?20210522053639)
![calender](https://icons.iconarchive.com/icons/aha-soft/large-calendar/256/Calendar-icon.png)
## Install

```
wget https://github.com/KooshaYeganeh/SUSE-JalaliDate/archive/refs/heads/main.zip && unzip main.zip && cd SUSE-JalaliDate.main && sudo cp mycal /usr/bin && echo "mycal installed [ OK ]"
```

### Create Installer File

```
pyinstaller jcal.py -n mycal --onefile && sudo cp dist/mycal /usr/bin && rm -rf dist build && rm mycal.spec && echo "Installer File Created [ OK ]"
```


## Run


**Normal Run :**

```
mycal
```

**-v** or **--verbose**

```
mycal --verbose
```

**-i** or **--info**

```
mycal --info
```

**-d** or **--digit**

```
mycal --digit
```


## Remove 

```
sudo rm /usr/bin/mycal
```
