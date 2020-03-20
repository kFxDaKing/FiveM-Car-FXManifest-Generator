# FiveM-FXManifest-Generator
This script will automatic the fxmanifest.lua file

This script has only been tested with Windows. It should work with Linux but is unknown.

## How to Run

Make sure Python is install on your computer.

In a terminal run
```bash
python init.py
```

## Changes

I had my cars in the "cars" folder. If your folder is a different name and/or a different place than the root file path you will need to change this. My cars directory was one down (/cars) so if yours is /folder/to/cars then replace "cars/" with "folder/to/cars".

```python
for folder in carsFolder:
    f.write("\n--" + os.path.basename(folder) + "\n")
    print("\n--" + os.path.basename(folder))
    fileInFolder = glob.glob(folder + "/*.meta")
    for fif in fileInFolder:
        if folder == carsFolder[-1]:
            if fif == fileInFolder[-1]:
                print("cars/" + os.path.basename(folder) +
                      "/" + os.path.basename(fif) + "\n \n }")
                f.write("'cars/" + os.path.basename(folder) +
                        "/" + os.path.basename(fif) + "'\n \n } \n \n")
            else:
                print("cars/" + os.path.basename(folder) +
                      "/" + os.path.basename(fif) + "', \n")
                f.write("'cars/" + os.path.basename(folder) +
                        "/" + os.path.basename(fif) + "', \n")
        else:
            print("'cars/" + os.path.basename(folder) +
                  "/" + os.path.basename(fif) + "',")
            f.write("'cars/" + os.path.basename(folder) +
                    "/" + os.path.basename(fif) + "', \n")

```


