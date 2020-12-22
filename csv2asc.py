


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
    while i<num:
        str1=list_all[i];
        i=i+1;

        ret=str1.split();
        retdest=[];

        #retdest[0:2]=ret[0:2];

        retdest.append(str(float(ret[0])/1000));
        retdest.append('1');
        retdest.append(ret[2]);
        #retdest[3]='Rx';
        retdest.insert(3,'Rx');
        #retdest[4]='d'
        retdest.insert(4, 'd');
        retdest[5:13]=ret[4:12];

        if(len(retdest[2])<6):
            retdest[2]=retdest[2][2:];
        else:
            retdest[2]=retdest[2][2:]+'X';

        retdest.append('\n');

        str1='   '.join(retdest);
        fpdest.write(str1)


str1="End TriggerBlock"
fpdest.write(str1);
fpdest.close();