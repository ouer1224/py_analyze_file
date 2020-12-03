
import matplotlib.pyplot as plt
import str2num as ouer

def can_1ceb1009(str,type='t',color='a',pos_firstdat=5):
    ret = str.split();
    id='1ceb1009';
    x=0;
    y=0;
    if(type=='a'):
        id='x'+'id';
    if (ret[2] == 'Error'):
        return;
    elif (ret[2] == id):
        x=(float(ret[0]) / 1000)
        y=(ouer.hex2int(ret[pos_firstdat + 0]))
    else:
        return;

    plt.plot(x, y, 'g-', lw=1)


