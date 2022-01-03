# Pore-Structure-Visible


-.xsd---xsd_to_csv.pl---┐
-.xyz---xyz_to_csv.py---├---->>filename.csv（坐标文件）
-.pdb---pdb_to_csv.py---┘

-filename.csv（坐标文件）---csv_to_np.py--->>filename_atom.csv（矩阵文件）

-filename.csv（坐标文件）---numcsv _to_csv.py--->>filename_atom_data.csv（详细分析文件）
-filename.csv（坐标文件）---numcsv_to_txt.py--->>filename_atom.txt（简略分析文件）

-filename.csv（坐标文件）---python_2d.py--->>filename_atom.svg（所有层矢量图片）
-filename_atom.csv（矩阵文件）---npcsv_to_fbx_cut.py--->>filename_atom.fbx（单层模型文件）
-filename.csv（坐标文件）---draw3D(python).py（plt绘图3d，复杂则卡顿）
-filename_atom.csv（矩阵文件）---npcsv_to_fbx(blender).py--->>filename_atom.fbx（模型文件）


-data/
-├── filename.csv
-└── XXXX.py

-注：python_2d.py目录下还需放置csv_to_np.py文件
