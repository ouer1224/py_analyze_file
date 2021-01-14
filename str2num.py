



a={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0};
def hex2int(str):
    sum=0;
    i=0;
    l=len(str);
    while(i<l):
        sum = sum * 16;
        sum=sum+a[str[i]];
        i+=1;
    return sum;