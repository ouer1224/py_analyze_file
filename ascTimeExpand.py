

import  tkinter.filedialog

def getCurFromdat(str1):
    pos_dat=5;
    return 0;


filename_input='';r'E:/CANData/CAN0_CHANNEL/CH0_11-25-precharge-errCANData0.asc';
if(filename_input==''):
    filename_input = tkinter.filedialog.asko
    penfilename();
print(f"filename is {filename_input}")
file_needopen = filename_input;

filedest=''

ret=[];
ret=file_needopen.split('.');

print(f"name={ret}")
file_dest=ret[0]+'back'+'.asc';
print(f"filedest={file_dest}")

fpdest=open(file_dest,'w+');
str1="date 0 12 21 11:54:56 2020 \n";
fpdest.write(str1);
str1="base hex timestamps absolute \n";
fpdest.write(str1);
str1="internal events logged\n";
fpdest.write(str1);
str1="//version 0.0.0\n";
fpdest.write(str1);
str1="Begin Triggerblock 0 12 21 11:54:56 2020\n";
fpdest.write(str1);
str1="  0.000000 Start of measurement\n";
fpdest.write(str1);

with open(file_needopen,'r') as fp:
    list_all=fp.readlines();

    print(f"{list_all[1]}")
    num = list_all.__len__();
    print(f"num={num}")
    print(f"last={list_all[num - 1]}")
    pos_firstdat = 5;
    i=0;
    time_begin=0;
    str1=list_all[1];

    print(f'\nstr1={str1}\n')

   # time_begin=getTimeFromCsv(str1.split(',')[0]);
    print(f"time_begin={'%.3f'%time_begin}")
    strtime=[]

    i=0;
    while i<num:
        str1=list_all[i];
        i=i+1;
        ret=[]
        ret=str1.split('\t')
        #print(f"ret={ret}")
        try:
            time=(float(ret[0]))*10;
        except:
            print(f"---drop the {i-1} line---")
            continue;



        strtime='%.3f'%time;
        #print(f"strtime={strtime}")
        ret[0]=strtime;
        #print(f"strtime={ret[0]}")
        str1='\t'.join(ret);
        #print(f"{str1}")


        fpdest.write(str1)

str1="End TriggerBlock"
fpdest.write(str1);
fpdest.close();