


import tkinter.filedialog


def getTimeFromCsv(string):
    time=0;

    tmp_str = string.split('_');
    strtime = tmp_str[1].split(':');
#   print(f"strtime={strtime}")
#    print(f'\nstrtime={strtime}')
#    print(f'\n{int(strtime[0])*3600}')
 #   print(f'\n{int(strtime[1])*60}')
 #   print(f'\n{float(strtime[2])}')
    time = (int(strtime[0]))*3600 + (int(strtime[1]))*3600+ float(strtime[2]);
 #   print(f"time={time}")
    return time;

filename_input = tkinter.filedialog.askopenfilename()
#filename_input=r"C:\Users\Administrator\Desktop\CH1_1232021-01-07_10-29-10.csv"

print(f"filename is {filename_input}")
file_needopen = filename_input;

filedest=''

ret=[];
ret=file_needopen.split('.');

print(f"name={ret}")
file_dest=ret[0]+'.asc';
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

    time_begin=getTimeFromCsv(str1.split(',')[0]);
    print(f"time_begin={'%.3f'%time_begin}")
    strtime=[]

    i=1;
    while i<num:
        str1=list_all[i];
        i=i+1;

        ret=str1.split(',');
        #if((ret[2]=='0x60000000')):
         #   continue;

        retdest=[];
        time_line=getTimeFromCsv(ret[0]);
        time_line-=time_begin;
        tmp_str='%.3f'%(time_line);
        retdest.append(tmp_str);
        retdest.append('1');
        retdest.append(ret[2]);
        retdest.insert(3,'Rx');
        retdest.insert(4, 'd');
        retdest[5:]=ret[4:]

        if(i==1):
            print(f"ret[1]={retdest[5:]}")
            print(f"ret[1]={ret[4:]}")
        if(len(retdest[2])<6):
            retdest[2]=retdest[2][2:];
        else:
            retdest[2]=retdest[2][2:]+'x';

        if (len(retdest[2]) != 9) or (retdest[2][:-1]=='60000000'):
            retdest=[];
            continue;

        retdest.append('\n');

        str1='  '+retdest[0]+' '+retdest[1]+'  '+retdest[2]+'       '+retdest[3];
        str1=str1+'   '+retdest[4]+' '+retdest[5]+' ';
        rettmp=[];
        rettmp=retdest[6:];
        str2=' '.join(retdest[6:])
        fpdest.write(str1+str2)


str1="End TriggerBlock"
fpdest.write(str1);
fpdest.close();