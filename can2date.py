
import matplotlib.pyplot as plt
import str2num as getnum

def can_0x1ceb1009(str,type='t',color='a',pos_firstdat=5):
    ret = str.split();
    id='1ceb1009';
    x=-1;
    y=-1;
    if(type=='a'):
        id='x'+'id';

    if (ret[2] == 'Error'):
        return x,y;
    elif (ret[2] == id):
        x=(float(ret[0]) / 1000)
        y=(getnum.hex2int(ret[pos_firstdat + 0]))
    return x,y;




def can_getInsAD1(str,type='t',color='a',pos_firstdat=5):
    ret=str.split();
    id='0x1CEB1007'
    x=-1;
    y=-1;
    if(type=='a'):
        id=id[1:-1];
    if(ret[2]=='Error'):
        return x,y;
    elif (ret[2]==id):
        x=(float(ret[0]) / 1000)
        y=(getnum.hex2int(ret[pos_firstdat + 2]))*256+(getnum.hex2int(ret[pos_firstdat + 3]));
    return x,y;

def can_getInsAD0(str,type='t',color='a',pos_firstdat=5):
    ret=str.split();
    id='0x1CEB1007'
    x=-1;
    y=-1;
    if(type=='a'):
        id=id[1:-1];
    if(ret[2]=='Error'):
        return x,y;
    elif (ret[2]==id):
        x=(float(ret[0]) / 1000)
        y=(getnum.hex2int(ret[pos_firstdat + 0]))*256+(getnum.hex2int(ret[pos_firstdat + 1]));
    return x,y;


def can_getInsTime(str,type='t',color='a',pos_firstdat=5):
    ret=str.split();
    id='0x1CEB1007'
    x=-1;
    y=-1;
    if(type=='a'):
        id=id[1:-1];
    if(ret[2]=='Error'):
        return x,y;
    elif (ret[2]==id):
        x=(float(ret[0]) / 1000)
        y=(getnum.hex2int(ret[pos_firstdat + 7]));
        y=y*100;
    return x,y;



def can_0x1ceb2a2e(str,type='t',color='a',pos_firstdat=5):
    ret=str.split();
    id='0x1CEB2A2E'
    x=-1;
    y=-1;
    if(type=='a'):
        id=id[1:-1];
    if(ret[2]=='Error'):
        return x,y;
    elif (ret[2]==id):
        x=(float(ret[0]) / 1000)
        y=(getnum.hex2int(ret[pos_firstdat + 0])) or (getnum.hex2int(ret[pos_firstdat + 1]));
        y=y*200
    return x,y;

def can_getInsVal(str,type='t',color='a',pos_firstdat=5):
    ret=str.split();
    id='0x1CEB2A04'
    x=-1;
    y=-1;
    if(type=='a'):
        id=id[1:-1];
    if(ret[2]=='Error'):
        return x,y;
    elif (ret[2]==id):
        x=(float(ret[0]) / 1000)
        #y=(getnum.hex2int(ret[pos_firstdat + 4]));
        y=(getnum.hex2int(ret[pos_firstdat + 5]));
        y = y * 256 + (getnum.hex2int(ret[pos_firstdat + 6]));
        y = y * 256 + (getnum.hex2int(ret[pos_firstdat + 7]));
        y=y/1000;
    return x,y;