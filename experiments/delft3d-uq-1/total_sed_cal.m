load('nesting.txt');
Nfs=vs_use('trim-WLD.dat');
DPS=vs_let(Nfs,'map-sed-series',{1:278},'DPS',{1:243 0});
area=vs_let(Nfs,'map-const','GSQS',{1:243 0});

for l=1:12393
    for j=70:336
        for k=30:240
            if (j==nesting(l,1)&(k==nesting(l,2)))
                for m=1:278
                sed(l,m)=DPS(m,k,j);
                end
                grid(l)=area(1,k,j);
            end
        end
    end
    end
    
    for i=1:12393
        tot_sed(i)=sed(i,188)-sed(i,89);
    end
    
    
    total_sed1=0;
    for i=1:12295
       total_sed1=total_sed1+tot_sed(i)*grid(i);
    end
    
    total_ero=0.0;
    total_agr=0.0;
    for i=1:12393
        if (tot_sed(i)>=0.0)
            total_agr=total_agr+tot_sed(i)*grid(i);
        else
            total_ero=total_ero+tot_sed(i)*grid(i);
        end
    end
