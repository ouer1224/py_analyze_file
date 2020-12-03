# This is a sample Python script.

# Press F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
import tkinter.filedialog

filename_input=tkinter.filedialog.askopenfilename()
print(f"filename is {filename_input}")
"""

import matplotlib.pyplot as plt
import  str2num as ouer
import  can2date as anayid

x = []
y = []
x1=[]
y1=[]

plt.figure()



str_to_find="1ceb1009";
#name_file_needopen="CH0_11-27-1CANData0.txt"
#dir_file_needopen="/e/CANData/CAN0_CHANNEL"
file_needopen="E:\CANData\CAN0_CHANNEL\CH0_11-25-precharge-errCANData0.txt"#dir_file_needopen+name_file_needopen;


str_destfile="./"+str_to_find+".txt"
dest=open("./all.txt","w+")
dest.close()
#dest=open("./dest.txt","w+")
dest=open(str_destfile,"w+");
dest.close()
tmpfile=open("./3.txt","w+");
tmpfile.close();

with open(file_needopen,'r') as fp:
    list_all=fp.readlines();
#    for list in list_all:
#        print(f"{list}")
    print(f"{list_all[1]}")
    i=4;
    #for list in list_all:
    #    str=list;
    num=list_all.__len__();
    print(f"num={num}")
    print(f"last={list_all[num-1]}")

    all_file = open("./all.txt", 'a+')
    dest_file = open(str_destfile, "a+")
    pos_firstdat=5;


    count_need = 0;

    while(i<num):
        str1=list_all[i];
        i+=1;
        ret=str1.split();

        if(ret[2]=='Error'):
            continue
        #if(ret[1]=='2'):
        #    all_file.write(str1);

        #anayid.can_1ceb1009(str1);
        if ((ret[2]=="1ceb1009")):
            x.append(float(ret[0]) / 1000)
            y.append(ouer.hex2int(ret[pos_firstdat + 0]))
        elif((ret[2]=='1ceb2a06')):
            continue;
        elif ((ret[2] == '1ceb2a0c')):
            x1.append(float(ret[0]) / 1000)
            y1.append(ouer.hex2int(ret[pos_firstdat + 1]))
        else:
            continue;

        #y.append(hex2int(ret[pos_firstdat + 0])/2.55)
        sumerr = 0;
        '''
        sumerr+= hex2int(ret[pos_firstdat+0])
        sumerr += hex2int(ret[pos_firstdat+1])
        sumerr += hex2int(ret[pos_firstdat+2])
        sumerr += hex2int(ret[pos_firstdat+3])
        sumerr += hex2int(ret[pos_firstdat+4])
        sumerr += hex2int(ret[pos_firstdat+5])
        sumerr += hex2int(ret[pos_firstdat+6])
        sumerr += hex2int(ret[pos_firstdat+7])
        '''
        #if(sumerr!=0):
        #if(ret[pos_firstdat+7]!='02'):
        #if(ret[pos_firstdat+0]!='06'):
        #if((ret[pos_firstdat+1]!='01') or (ret[pos_firstdat+0]!='01')):
        if(True):
            dest_file.write('***'+str1);
            count_need+=1;

            #x1.append(float(ret[0]) / 1000)
            #y1.append(hex2int(ret[pos_firstdat + 0]))
            #print(f"ret={ret}")
            #print("%d" % (i))
        else:
            dest_file.write(str1);

            #x1.append(float(ret[0]) / 1000)
            #y1.append(hex2int(ret[pos_firstdat + 0]))

    print(f"end,find --- {count_need} -- can data\n")
    all_file.close();
    dest_file.close();
    plt.subplot(211);
    plt.plot(x, y,'b-', lw =1)
    plt.legend(['mode'], ncol=1)
    plt.title("mode");
    plt.subplot(212);
    plt.plot(x1, y1, 'r-', lw=1)
    plt.title("relay");
    plt.legend(['relay'], ncol=1)

    plt.show()
