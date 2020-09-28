from playsound import playsound
import datetime
import time


# files to be played during opertation:
notify_sound = "water.mp3"


# some start of the program
print("\n\n\n=======================================================================")
print("||===================|| HEALTHY PROGRAMMER ||=======================||")
print("=======================================================================")
print("\nthis program will remind you to drink water and do eyes-exercise every 30 \nand physical exercise every 45 minutes \nPlease don't close the program. Minimise it, so that it can run in the\nbackground...")

# taking out the time in int form for comparison
present_time = str(datetime.datetime.now())
str_time = present_time[10:13]
int_time = int(str_time)


date_for_logs = "\n"+present_time[0:16] 
water_logs = date_for_logs + "==> Drinked Water"
eyes_ex_logs = date_for_logs + "==> Done eye exercises"
physical_ex_log = date_for_logs + "==> Done exercises"

print("The app will remind you in next 30 min from now")
while int_time>=9 and int_time<=17:
    for i in range(16):     
        time.sleep(1800)
        print("Water reminder")
        playsound(notify_sound)
        usr_resp = str(input("Press D if you have drinked water\n"))        
        if usr_resp == "d" or usr_resp == "E":
            logs = open("logss.txt","a")
            logs.write(water_logs)
            logs.close()
            print("Your Response have saved successfully in a log file")
            print("the app will remind you to do eyes exercises in next 15 min")

        else:
            usr_conf = str(input(("please input b/w the provided choices only\nif you want to exit then press e or to continue press any key\n")))
            if usr_conf == "e" or usr_conf == "E":
                exit()
            else:
                continue

        time.sleep(900)
        print("Eyes exercise reminder")
        playsound(notify_sound)
        usr_resp = str(input("Press D if you have done eyes exercises\n"))
        
        if usr_resp == "d" or usr_resp == "E":
            logs = open("logss.txt","a")
            logs.write(eyes_ex_logs)
            logs.close()
            print("Your Response have saved successfully in a log file")
            print("the app will remind you to do physical exercises in next 15 min")

        else:
            usr_conf = str(input(("please input b/w the provided choices only\nif you want to exit then press e or press any key to continue\n")))
            if usr_conf == "e" or usr_conf == "E":
                exit()
            else:
                continue

        time.sleep(1)
        print("physical exercise reminder")
        playsound(notify_sound)
        usr_resp = str(input("Press D if you have done physical exercises\n"))

        if usr_resp == "d" or usr_resp == "E":
            logs = open("logss.txt","a")
            logs.write(physical_ex_log)
            logs.close()
            print("Your Response have saved successfully in a log file")
            print("the app will remind you to do physical exercises in next 15 min")

        else:
            usr_conf = str(input(("please input b/w the provided choices only\nif you want to exit then press e or press any key to continue\n")))
            if usr_conf == "e" or usr_conf == "E":
                exit()
            else:
                continue    
else:
    print("\n* Please open the program between 9am - 5pm *")
