import os
import glob

carFilePath = ""  # File path to cars folder
rootFilePath = ""  # File path to root folder where this file lives

carsFolder = glob.glob(carFilePath)
rootFolder = glob.glob(rootFilePath)

f = open("fxmanifest.lua", "w")
f.write("fx_version 'adamant' \n")
f.write("games { 'gta5' } \n \n")
f.write("files {" + "\n")
print("files {" + "\n")

# Files
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

# Data Files
for folder in carsFolder:
    f.write("\n--" + os.path.basename(folder) + "\n")
    print("\n--" + os.path.basename(folder))
    fileInFolder = glob.glob(folder + "/*.meta")
    ytypInFolder = glob.glob(folder + "/*.ytyp")
    for fif in fileInFolder:
        if("handling" in fif):
            print("data_file 'HANDLING_FILE' 'cars/" + os.path.basename(folder) +
                  "/" + os.path.basename(fif))
            f.write("data_file 'HANDLING_FILE' 'cars/" + os.path.basename(folder) +
                    "/" + os.path.basename(fif) + "'\n")
        elif("vehicles" in fif):
            print("data_file 'VEHICLE_METADATA_FILE' 'cars/" + os.path.basename(folder) +
                  "/" + os.path.basename(fif) + "'\n")
            f.write("data_file 'VEHICLE_METADATA_FILE' 'cars/" + os.path.basename(folder) +
                    "/" + os.path.basename(fif) + "'\n")
        elif("carcols" in fif):
            print("data_file 'CARCOLS_FILE' 'cars/" + os.path.basename(folder) +
                  "/" + os.path.basename(fif) + "'\n")
            f.write("data_file 'CARCOLS_FILE' 'cars/" + os.path.basename(folder) +
                    "/" + os.path.basename(fif) + "'\n")
        elif("carvariations" in fif):
            print("data_file 'VEHICLE_VARIATION_FILE' 'cars/" + os.path.basename(folder) +
                  "/" + os.path.basename(fif) + "'\n")
            f.write("data_file 'VEHICLE_VARIATION_FILE' 'cars/" + os.path.basename(folder) +
                    "/" + os.path.basename(fif) + "'\n")
        elif("contentunlocks" in fif):
            print("data_file 'CONTENT_UNLOCKING_META_FILE' 'cars/" + os.path.basename(folder) +
                  "/" + os.path.basename(fif) + "'\n")
            f.write("data_file 'CONTENT_UNLOCKING_META_FILE' 'cars/" + os.path.basename(folder) +
                    "/" + os.path.basename(fif) + "'\n")
        elif("vehiclelayouts" in fif):
            print("data_file 'VEHICLE_LAYOUTS_FILE' 'cars/" + os.path.basename(folder) +
                  "/" + os.path.basename(fif) + "'\n")
            f.write("data_file 'VEHICLE_LAYOUTS_FILE' 'cars/" + os.path.basename(folder) +
                    "/" + os.path.basename(fif) + "'\n")

    for ytypFile in ytypInFolder:
        if(ytypFile.endswith(".ytyp")):
            print("data_file 'DLC_ITYP_REQUEST' '" +
                  os.path.basename(ytypFile) + "'\n")
            f.write("data_file 'DLC_ITYP_REQUEST' '" +
                    os.path.basename(ytypFile) + "'\n")
