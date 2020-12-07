
import matplotlib.pyplot as plt
import str2num as getnum

def can_1ceb1009(str,type='t',color='a',pos_firstdat=5):
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




def can_1ceb2a0c(str,type='t',color='a',pos_firstdat=5):
    return;