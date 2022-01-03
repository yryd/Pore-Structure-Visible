# Pore-Structure-Visible

-.xsd---xsd_to_csv.pl---┐

-.xyz---xyz_to_csv.py---├---->>filename.csv（坐标文件）
 基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)，使用[NoneBot](https://docs.nonebot.dev/guide/)框架 
<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/python-v3.7%2B-green" alt="license">
  </a>
  <a href=https://docs.nonebot.dev/guide/">
    <img src="https://img.shields.io/badge/OneBot-v11-blue?style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="cqhttp">
  </a>
  <a href="https://github.com/Yang9999999/Go-CQHTTP-YesBot/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/LICENSE-MIT-orange" alt="action">
  </a>
</p>

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
