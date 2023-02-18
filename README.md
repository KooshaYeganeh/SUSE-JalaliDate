# SUSE-JalaliDate
JalaliDate For SUSE 









## Install




### Create Installer File

```
pyinstaller jcal.py -n mycal --onefile && sudo cp dist/mycal /usr/bin && rm -rf dist build && rm mycal.spec && echo "Installer File Created [ OK ]"
```


## Run


Normal Run :

```
mycal
```

-v or --verbose

```
mycal --verbose
```

-i or --info

```
mycal --info
```

-d or --digit

```
mycal --digit
```


## Remove 

```
sudo rm /usr/bin/mycal
```
