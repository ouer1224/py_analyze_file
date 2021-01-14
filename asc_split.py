

import tkinter.filedialog
import str2num as fnnum
from tqdm import  tqdm

def creatNewFile(dir,en=0):
    fp_dest=None;
    fp_dest = open(dir, 'w+', encoding='utf-8');
    if(en==0):
        fp_dest.close();
        return None;
    else:
        return fp_dest;

def getCurAndTimeFromLine(strline):
    time=0;
    cur=0;
    cur2=0;
    fangxiang='x';
    ID='';
    pos_dat=6;
    ret=strline.split();
    #print(f'line={ret}')
    if(ret[0][0].isdigit()!=True):
        return -1, -1, fangxiang,ID;
    time=float(ret[0]);
    ID=ret[2];
    if(ID=='181B2C07x'):
        cur=(fnnum.hex2int(ret[pos_dat+0]))*256+(fnnum.hex2int(ret[pos_dat+1]));
        fangxiang='+';
        if(cur>(65536/2)):
            cur=65536-cur;
            fangxiang='-'
        #print(f"----{time},{cur}----")
        return time, cur, fangxiang,ID;
    elif (ID=='181B2C08x'):
        cur = (fnnum.hex2int(ret[pos_dat + 0])) * 256 + (fnnum.hex2int(ret[pos_dat + 1]));
        cur2 =((fnnum.hex2int(ret[pos_dat + 4])) <<24)+((fnnum.hex2int(ret[pos_dat + 5])) <<16)+((fnnum.hex2int(ret[pos_dat + 6])) <<8) + (fnnum.hex2int(ret[pos_dat + 7]));
        fangxiang = '+';
        if (cur > (65536 / 2)):
            cur = 65536 - cur;
            fangxiang = '-';
        if(cur2>0x80000000):
            cur2=0xffffffff-cur2+1;

        cur=(cur<<16)+cur2;
        return time, cur, fangxiang, ID;
    elif (ID=='181B2C05x'):
        cur = (fnnum.hex2int(ret[pos_dat + 0])) * 256 + (fnnum.hex2int(ret[pos_dat + 1]));
        fangxiang = '+';
        if (cur > (65536 / 2)):
            cur = 65536 - cur;
            fangxiang = '-'
        return time, cur, fangxiang, ID;
    elif (ID=='181B2C06x'):
        cur = (fnnum.hex2int(ret[pos_dat + 0])) * 256 + (fnnum.hex2int(ret[pos_dat + 1]));
        fangxiang = '+';
        if (cur > (65536 / 2)):
            cur = 65536 - cur;
            fangxiang = '-'
        return time, cur, fangxiang, ID;
    else:
        return -1,-1,fangxiang,ID;



name_fp_input="E:/feiqiu_rcv/feiq/Recv Files/Rec202119_173249.asc"
if(name_fp_input==None):
    name_fp_input=tkinter.filedialog.askopenfilename();

print(f'name_open={name_fp_input}')
ret=name_fp_input.split('/');
ret_name=[];
ret_name[:]=ret[:];

##2c07
ret_name[-1]='2c07_'+ret[-1];
name_fp_dest='/'.join(ret_name);
print(f'\nname_dest={name_fp_dest}')
fp_2c07=creatNewFile(name_fp_dest,1);
##2c05
ret_name[-1]='2c05_'+ret[-1];
name_fp_dest='/'.join(ret_name);
print(f'\nname_dest={name_fp_dest}')
fp_2c05=creatNewFile(name_fp_dest,1);
##2c06
ret_name[-1]='2c06_'+ret[-1];
name_fp_dest='/'.join(ret_name);
print(f'\nname_dest={name_fp_dest}')
fp_2c06=creatNewFile(name_fp_dest,1);
##2c08_1
ret_name[-1]='2c08_1_'+ret[-1];
name_fp_dest='/'.join(ret_name);
print(f'\nname_dest={name_fp_dest}')
fp_2c08_1=creatNewFile(name_fp_dest,1);
##2c08_2
ret_name[-1]='2c08_2_'+ret[-1];
name_fp_dest='/'.join(ret_name);
print(f'\nname_dest={name_fp_dest}')
fp_2c08_2=creatNewFile(name_fp_dest,1);


fp_tmp=open('./tmp.txt','w+',encoding='utf-8');

i=0;

pbar = tqdm(total=1000)

with open(name_fp_input) as fp:

    pre_cur=0;
    cur=0;
    ID='';
    while(1):
        strline=fp.readline();

        if((i%100000)==0):
            pbar.update(1);

        if(strline==''):
            print("\narrive end line")
            break;
        i = i + 1;
        if(i<30):
            continue;
        time=0;
        cur=0;
        fangxiang='';

        time,cur,fangxiang,ID=getCurAndTimeFromLine(strline);
        #print(f"{cur},{fangxiang}")

        #if(i>1000000):
         #   break;
        #if(time<0):
        #    continue;
        if(fangxiang!='x'):
            dat_line='%.3f'%time;
            dat_line=dat_line+'\t'+str(cur)+'\t'+fangxiang+'\n';

            '''
            flag_start=0;
            flag_end=0;
            if((pre_cur<10) and (cur>10)) :
                flag_start=1;
            if( (pre_cur>10) and (cur<10)):
                flag_end=1;

            pre_cur=cur;
            
            if(flag_start==1):
                #print(f"start--{dat_line}")
                fp_tmp.write(f"start--{dat_line}")
            if(flag_end==1):
                #print(f"end--{dat_line}")
                fp_tmp.write(f"end--{dat_line}")
            '''
            if (ID == '181B2C07x'):
                if(cur>1):
                    fp_2c07.write(dat_line);
            elif (ID == '181B2C05x'):
                if (cur > 1):
                    fp_2c05.write(dat_line);
            elif (ID == '181B2C06x'):
                if (cur > 1):
                    fp_2c06.write(dat_line);
            elif (ID == '181B2C08x'):
                if ((cur>>16) > 10):
                    dat_line = '%.3f' % time;
                    dat_line = dat_line + '\t' + str(cur>>16) + '\t' + fangxiang + '\n';
                    fp_2c08_1.write(dat_line);
                    dat_line = '%.3f' % time;
                    dat_line = dat_line + '\t' + '%.0f'%(((cur&0xffff)*6/100)) + '\t' + fangxiang + '\n';
                    #dat_line = dat_line + '\t' + str(cur) + '\t' + fangxiang + '\n';
                    fp_2c08_2.write(dat_line);

#fp_dest.close();
fp_2c07.close();
fp_2c05.close();
fp_2c06.close();
fp_2c08_1.close();
fp_2c08_2.close();
fp_tmp.close();
print("\n-------- end ----------")
