% A MATLAB script to calculate response statistics from Delft3D output.
%
% Call with:
% >> total_sed_cal
% or
% $ matlab -nodisplay -nosplash -r "total_sed_cal; exit"
%
% Fei Xing
% Modified by Mark Piper (mark.piper@colorado.edu)

% Include Delft3D library routines in path.
delft3d_lib_path = '/scratch/mapi8461/Delft3D-MATLAB'
addpath(genpath(delft3d_lib_path));

% Array indices.
i_max_map_sed_series = 2; % 23; % 278;
i_max_DPS = 242;
i_max_GSQS = 242; % 23 
i0_sed = 1; % 89
i1_sed = 2; % 23; % 188

% Load grid cells used in calculations.
grid_cells_file = strcat(pwd, '/nesting.txt')
if exist(grid_cells_file, 'file')
    load(grid_cells_file);
else
    fprintf('Error: file does not exist: %s\n', grid_cells_file);
    exit(1)
end

% Load Delft3D output using Delft3D-MATLAB tools.
delft3d_output_file = strcat(pwd, '/trim-WLD.dat')
if exist(delft3d_output_file, 'file')
    Nfs = vs_use(delft3d_output_file);
else
    fprintf('Error: file does not exist: %s\n', delft3d_output_file);
    exit(1)
end
DPS = vs_let(Nfs, 'map-sed-series', {1:i_max_map_sed_series}, ...
	     'DPS', {1:i_max_DPS 0}, 'quiet!');
area = vs_let(Nfs, 'map-const', 'GSQS', {1:i_max_GSQS 0}, 'quiet!');

% Extract sediment values from grid.
for l=1:12393
    for j=70:336
        for k=30:240
            if ( j==nesting(l,1) && k==nesting(l,2) )
                for m=1:i_max_map_sed_series
                    sed(l,m)=DPS(m,k,j);
                end
                grid(l)=area(1,k,j);
            end
        end
    end
end

% Calculate total sediment values.
for i=1:12393
    tot_sed(i)=sed(i,i0_sed)-sed(i,i1_sed);
end
total_sed1=0;
for i=1:12295
    total_sed1=total_sed1+tot_sed(i)*grid(i);
end

% Calculate total erosion and accretion values.
total_ero=0.0;
total_agr=0.0;
for i=1:12393
    if (tot_sed(i)>=0.0)
        total_agr=total_agr+tot_sed(i)*grid(i);
    else
        total_ero=total_ero+tot_sed(i)*grid(i);
    end
end

% Save results to a text file.
s = dbstack()
save(strcat(s.name, '.out'), 'total_sed1', 'total_agr', 'total_ero', '-ascii')

