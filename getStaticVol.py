
import tkinter.filedialog
from tqdm import tqdm
import str2num



fname_input='E:/tmp/soc_adjust/static_vol.csv';
if fname_input=='':
    fname_input=tkinter.filedialog.askopenfilename()

print(f"fileOpen={fname_input}")

fname_dest='';
ret=fname_input.split('.');
fname_dest=ret[0]+'_dealed_dat'+'.'+'txt';

#fpDest=open(fname_dest,'w+',encoding='utf-8');
#fpDest.close()

with open(fname_input,'r',encoding='utf-8') as fpInput:
    lines=[]
    i=-1;
    onestr=''
    oneline=[]
    timeline=0;
    curline=0;
    pre_curl=0;
    socline=0;
    maxVolline=0;
    minVolline=0;
    maxVl_start=0;
    minVl_start=0;
    maxtempline=0;
    mintempline=0;
    line_saved=[];

    flag_into_static=0;
    startT_static=0;
    endT_static=0;
    time_have_staic=0;
    flag_need_save=0;
    file_num=0;
    dat_start=[];
    dat_delta=[];
    avr_delta=0;




    lines=fpInput.readlines()
    tmp=lines[2].split('\t');
    print(f"len={len(tmp)}")
    print(f"tmp=\n\n{tmp}")
    datNum_need =len(tmp);

    pbar=tqdm(total=len(lines))
    for onestr in lines:
        i=i+1;
        pbar.update(1);
        if(i==0):
            continue
        pre_curl=curline;
        oneline=onestr.split('\t')

        timeline=float(oneline[0]);
        curline=float(oneline[1]);
        socline=float(oneline[2]);
        maxVolline=float(oneline[3])
        minVolline=float(oneline[4])

        if((pre_curl<0) or (pre_curl>5)):
            if(curline>=0) and (curline<=5):
                flag_into_static=1;
                flag_need_save=1;

        if((pre_curl>=0) and (pre_curl<=5)):
            if((curline>5) or (curline<0)):
                flag_into_static=-1;
                flag_need_save=0;


        if(flag_into_static==1):
            startT_static=timeline;
            maxVl_start = maxVolline;
            minVl_end = minVolline;
            dat_start[:]=oneline[:];
            flag_into_static=0;
        if(flag_into_static==-1):
            endT_static=timeline;
            flag_into_static=0;
            time_have_staic=endT_static-startT_static;
            if(time_have_staic>=20):
                #print(f"start={startT_static},end={endT_static},duration={time_have_staic}")
                file_num += 1;

                with open(fname_dest.split('.')[0]+'_'+str(file_num)+'.txt','w+',encoding='utf-8') as fpDest:
                    for tmpstr in line_saved:
                        fpDest.write(tmpstr);
                    line_saved.clear();
                    fpDest.write(f"------start={startT_static},end={endT_static},"
                                 f"duration={time_have_staic},cur={curline},pre_cur={pre_curl}---\n\n")
                    #print(f"------start={startT_static},end={endT_static},"
                     #            f"duration={time_have_staic},cur={curline},pre_cur={pre_curl}---\n\n")


        if(flag_need_save==1):
            num=datNum_need;
            avr_delta=0;
            tmp_ret=[]
            junfang_delta=0;
            for j in range(num):
                val_tmp=float(oneline[j])-float(dat_start[j]);
                dat_delta.append('%.3f' % (val_tmp));
                if(j>=7):
                    avr_delta+=val_tmp;
                    tmp_ret.append(val_tmp);

            avr_delta=avr_delta/num;
            for j in tmp_ret:
                junfang_delta=junfang_delta+(j-avr_delta)**2;

            junfang_delta/=num;
            junfang_delta=junfang_delta**(1/2);
            tmp_ret.sort()
            leng=len(tmp_ret)
            leng=leng//2;
            val_m=(tmp_ret[leng]+tmp_ret[~leng])/2;
            onestr=onestr[:-1]+onestr[-1][:-1]+'\t'+'||'+'\t';

            onestr=onestr+'\t'.join(dat_delta)+'\t';
            onestr=onestr+'||||'+'\t'+('%.3f'%avr_delta)+'\t'+('%.3f'%val_m)+'\t'+('%.3f'%junfang_delta)
            onestr=onestr+'\n';
            dat_delta.clear()

            line_saved.append(onestr)
        else:
            line_saved.clear();



#fpDest.close()









