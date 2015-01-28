# A MATLAB to calculate response statistics from Delft3D output.
#
# Fei Xing
# Modified by Mark Piper (mark.piper@colorado.edu)

p = '/scratch/fexi8823/delft3d_openearth/applications/delft3d_matlab'
addpath(genpath(p))
load('nesting.txt');

output_file = '/scratch/mapi8461/delft3d-01/trim-WLD.dat'
Nfs=vs_use(output_file);
DPS=vs_let(Nfs,'map-sed-series',{1:278},'DPS',{1:242 0});
area=vs_let(Nfs,'map-const','GSQS',{1:242 0});

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
        tot_sed(i)=sed(i,89)-sed(i,188);
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
