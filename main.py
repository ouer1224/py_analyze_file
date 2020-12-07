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





import matplotlib.pyplot as plt
import  str2num as getnum
import  can2date as anayid
import tkinter.filedialog




'''
put the canid into id_analyze
eg:
can_1ceb1009
can_1ceb2a0c
'''
id_analyze=[
    anayid.can_1ceb1009,
    anayid.can_1ceb2a0c
            ];

############################################################################################
############################################################################################

file_needopen=""#"E:\CANData\CAN0_CHANNEL\CH0_11-25-precharge-errCANData0.txt"
if(file_needopen==''):
    filename_input=tkinter.filedialog.askopenfilename()
    print(f"filename is {filename_input}")
    file_needopen=filename_input;#"E:\CANData\CAN0_CHANNEL\CH0_11-25-precharge-errCANData0.txt"



figur_x=[]
figur_y=[]

num= len(id_analyze);
print(f"---num={num}")
while num>0:
    num=num-1;
    figur_x.append([])
    figur_y.append([])


with open(file_needopen,'r') as fp:
    list_all=fp.readlines();

    print(f"{list_all[1]}")
    i=4;

    num=list_all.__len__();
    print(f"num={num}")
    print(f"last={list_all[num-1]}")
    
    pos_firstdat=5;
    while(i<num):
        str1=list_all[i];
        i+=1;
        ret=str1.split();

        if(ret[2]=='Error'):
            continue

        tmp1,tmp2=anayid.can_1ceb1009(str1);
        if((tmp1==-1)and(tmp2==-1)):
           continue;
        else:
            figur_x[0].append(tmp1);
            figur_y[0].append(tmp2);

        '''
        if ((ret[2]=="1ceb1009")):
            figur_x[0].append(float(ret[0]) / 1000)
            figur_y[0].append(getnum.hex2int(ret[pos_firstdat + 0]))
        elif((ret[2]=='1ceb2a06')):
            continue;
        elif ((ret[2] == '1ceb2a0c')):
            figur_x[1].append(float(ret[0]) / 1000)
            figur_y[1].append(getnum.hex2int(ret[pos_firstdat + 1]))
        else:
            continue;
        '''
    print(f"end,find ---- can data\n")


    plt.figure()
    #plt.subplot(211);
    plt.plot(figur_x[0], figur_y[0],'b-', lw =1)
    #plt.legend(['mode'], ncol=1)
    #plt.title("mode");
    #plt.subplot(212);
    plt.plot(figur_x[1], figur_y[1], 'r-', lw=1)
    #plt.title("relay");
    #plt.legend(['relay'], ncol=1)

    plt.legend(['mode','relay'],ncol=2);
    plt.show()
