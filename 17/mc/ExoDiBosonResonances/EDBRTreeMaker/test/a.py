SUBMITFAILED=['crab_M1500_R0-4_off', 'crab_M1500_R0-7_off', 'crab_M2500_R0-5_off', 'crab_M3500_R0-5_off', 'crab_M3000_R0-6_off', 'crab_M3000_R0-7_off', 'crab_M3500_R0-6_off', 'crab_M3500_R0-9_off', 'crab_M4000_R0-06_off', 'crab_M4000_R0-3_off', 'crab_M4000_R0-6_off', 'crab_M4500_R0-9_off', 'crab_M3000_R0-5_off']
import os

for i in SUBMITFAILED:
        os.system("crab kill "+i);
        os.system("rm -r "+i);
        submitf=i.replace("crab_","");
        submitf=submitf.replace("_off","");
        submitf=submitf.replace("R","R_");
        print "crab submit -c crab3_analysis"+submitf+".py"
        os.system("crab submit -c crab3_analysis"+submitf+".py");
