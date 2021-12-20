import os
import shutil
import datetime
import schedule
import time

root_src_dir = "Y:\\1_Einkauf"
year = 2018
counter = 0

### WENN VERSCHOBEN WERDEN SOLL auskommentieren##

#alte_dateien = f"{root_src_dir}\\old_files"
#if not os.path.exists(alte_dateien):
    #os.mkdir(alte_dateien)


def old_files_(root_src_dir,year):
    for src_dir, dirs, files in os.walk(root_src_dir):  # os.walkthrough
        filename = src_dir.split("\\")[-1]

        for file_ in files:
            date = os.path.getmtime(f"{src_dir}\\{file_}")
            v = datetime.datetime.fromtimestamp(date)
            x = v.strftime('%Y\\%m\\%d')
            if x < str(year):
                ### WENN VERSCHOBEN WERDEN SOLL auskommentieren##
                #if os.path.samefile(f"{src_dir}\\{file_}", alte_dateien):
                    #continue
                #print(f"File \"{file_}\" from {x}")
                #shutil.copy(f"{src_dir}\\{file_}",alte_dateien)

                ###############################################

                os.remove(f"{src_dir}\\{file_}")
                counter += 1

        #### LEERE ORDNER LÖSCHEN ########
        if len(os.listdir(src_dir)) == 0:
            print(f"{filename} ist leer")
            os.rmdir(src_dir)

    ### AUSGABE DER GELÖSCHTEN DATEIEN ############
    print(counter)
    datei = open(f'{root_src_dir}\\anzahl_dateien.txt','w')
    datei.write(f"Insgesamt gelöschte Dateien: {counter}")
    datei.close()
 
old_files_(root_src_dir,year)
