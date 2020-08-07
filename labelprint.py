import requests
import json
import os
import time


global url, link, response, value, aName, aTag, aLink, headers, querystring

print('''######################################## 

SnipeIT Brother Label Printer PT-E550W 0.5v Beta 
Coded By : mK (MuneebKalathil@yahoo.com)

#########################################''')


url = "http://snipiturl/api/v1/hardware/"
link = "http://snipiturl/hardware/"

querystring = {"limit": "2", "offset": "0", "sort": "created_at", "order": "desc"}

# querystring = {"limit":"5","offset":"0","sort":"created_at","order":"desc","location_id":"5"}

headers = {
    'authorization': "Bearer API_KEY",
    'accept': "application/json",
    'content-type': "application/json"
}

#url = url + str(idInput)


# print("\n")




def menu():
    global idInput, printInput



    print("\nEnter the Asset ID")
    idInput = input()

    url2 = url + idInput
    response = requests.request("GET", url2, headers=headers, params=querystring)
    # print(response.text)
    value = json.loads(response.text)

    print("\n")
    print("Asset Details")
    print("-------------")
    print(value["name"])
    print(value["asset_tag"])
    print(link + str(value["id"]))





    printInput = 1
    while True:
        try:
            # Swap raw_input for input in Python 3.x
            printInput = int(input("\nPlease Number of Prints (1 - 3 - Default : 1 ) : ") or "1")
            #print(printInput)
            if  printInput !=1 and printInput > 3:
                raise ValueError  # this will send it to the print message and back to the input option

            else:
                #print(printInput)
                url2 = url + idInput
                response = requests.request("GET", url2, headers=headers, params=querystring)
                #print(response.text)
                value = json.loads(response.text)

                aName = value["name"]
                aTag = value["asset_tag"]
                aLink = link + str(value["id"])


                userInput(aName,aTag,aLink)
        except ValueError:
                #print(printInput)
                print("Enter between 1-3")




def userInput(aName,aTag,aLink):


    f1 = open('labelscript.vbs', 'r')
    f2 = open('new.vbs', 'w')

    checkWords = ("$ANAME", "$ATAG", "$ALINK")
    repWords = (aName,aTag,aLink)

    for line in f1:
        for check, rep in zip(checkWords, repWords):
            line = line.replace(check, rep)
        f2.write(line)
    f1.close()
    f2.close()
    for i in range(printInput):
        print("Printing  " + str(i + 1) + " time")
        time.sleep(1.5)


        #os.system(r"C:\Windows\system32\cmd.exe /k c:\windows\SysWOW64\cscript.exe  C:\Users\muneeb.kalathil\PycharmProjects\moodledownload\vcconverter\labelprint\new.vbs")
        #subprocess.call("run.bat")
        #Popen("run.exe")
        os.system("run.exe")
    menu()


menu()





