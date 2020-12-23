


import tkinter.filedialog

filename_input = tkinter.filedialog.askopenfilename()
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
    str1=list_all[0];
    ret=str1.split();
    time_begin=float(ret[0]);
    while i<num:
        str1=list_all[i];
        i=i+1;

        ret=str1.split();
        retdest=[];
        #retdest[0:2]=ret[0:2];
        tmp_str=str((float(ret[0])-time_begin)/1000);
        tmp_ret=tmp_str.split('.');
        tmp_str=tmp_ret[0]+'.'+tmp_ret[1][:3]
        retdest.append(tmp_str);
        retdest.append('1');
        retdest.append(ret[2]);
        #retdest[3]='Rx';
        retdest.insert(3,'Rx');
        #retdest[4]='d'
        retdest.insert(4, 'd');
        #retdest[5:14]=ret[4:13];
        retdest[5:]=retdest[4:]

        if(i==1):
            print(f"ret[1]={retdest[5:]}")
            print(f"ret[1]={ret[4:]}")
        if(len(retdest[2])<6):
            retdest[2]=retdest[2][2:];
        else:
            retdest[2]=retdest[2][2:]+'x';

        if (len(retdest[2]) != 9):
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