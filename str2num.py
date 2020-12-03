



a={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0};
def hex2int(str):
    sum=0;
    i=0;
    l=len(str);
    while(i<l):
        sum = sum * 16;
        sum=sum+a[str[i]];
        i+=1;
    return sum;