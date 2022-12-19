#include<stdio.h>
#include<conio.h>
int main()
{
    int n=5,m=3,i,j,k,z;
    int alloc[5][3]={
        {0,1,0},
        {2,0,0},
        {3,0,2},
        {2,1,1},
        {0,0,2}
    };
    int max[5][3]={
        {7,5,3},
        {3,2,2},
        {9,0,2},
        {2,2,2},
        {4,3,3}
    };
    int avail[3]={3,3,2};

    int f[n],ans[n],ind=0;
    for(i=0;i<n;i++){
        f[i]=0;
    }
    int need[5][3];
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            need[i][j]=max[i][j]-alloc[i][j];
        }
    }
    for(k=0;k<n;k++){
        for(i=0;i<n;i++){
            if(f[i]==0){
                int flag=0;
                for(j=0;j<m;j++){
                    if(need[i][j]>avail[j]){
                        flag=1;
                        break;
                    }
                } 
                if(flag==0){
                    ans[ind++]=i;
                    f[i]=1;
                    for(z=0;z<m;z++){
                        avail[z]+=alloc[i][z];
                    }
                }
            }
        }
    }

    int flagd=1;

    for(i=0;i<n;i++){
        if(f[i]==0){
            flagd=0;
            printf("The following system is not safe");
            break;
        }
    }

    if(flagd==1)
    {
        printf("The following is safe sequence :\n");
        for(i=0;i<n-1;i++){
            printf("P%d->",ans[i]);
        }
        printf("P%d",ans[n-1]);
    }

    getch();
    return 0;
}