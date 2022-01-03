# Pore-Structure-Visible
<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/python-v3.7%2B-green" alt="license">
  </a>
  <a href="https://github.com/Yang9999999/Go-CQHTTP-YesBot/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/LICENSE-MIT-orange" alt="action">
  </a>
</p>

## 1 下载代码
>3D模型绘制需要下载安装blender并打开script窗口运行脚本
>
>测试用blender版本为3.0.0
>
>代码注释详尽 按序修改

## 2 环境配置(py,plt模块)
```shell
pip install -r requirements.txt
```

## 3 输入输出说明

/get_csv

.xsd---xsd_to_csv.pl-----┐

.xyz---xyz_to_csv.py-----├---->>filename.csv（坐标文件）
                                                                           
.pdb---pdb_to_csv.py---┘

### 3.1 数据转换

filename.csv（坐标文件）---csv_to_np.py--->>filename_atom.csv（矩阵文件）
                                                                           
### 3.2 数据分析analysis/

filename.csv（坐标文件）---numcsv _to_csv.py--->>filename_atom_data.csv（详细分析文件）
                                                                           
filename.csv（坐标文件）---numcsv_to_txt.py--->>filename_atom.txt（简略分析文件）

### 3.3 截面作图draw_2D/

filename.csv（坐标文件）---python_2d.py--->>filename_atom.svg（所有层矢量图片）
                                                                           
filename_atom.csv（矩阵文件）---npcsv_to_fbx_cut.py--->>filename_atom.fbx（单层模型文件）

### 3.4 模型draw_3D/
                                                                           
filename.csv（坐标文件）---draw3D(python).py（plt绘图3d，复杂则卡顿）
                                                                           
filename_atom.csv（矩阵文件）---npcsv_to_fbx(blender).py--->>filename_atom.fbx（模型文件）

## 4 目录设置
data/
                                                                           
├── filename.csv
                                                                           
└── XXXX.py

>注：python_2d.py目录下还需放置csv_to_np.py文件

data_more/
                                                                           
├── filename1.csv

├── filename2.csv

├── filename....csv

└── XXXX(loop).py

## 5 运行项目

修改.py文件中：文件名、晶格长度(埃)、最小精度（埃）即可进行运行
>晶格长度/最小精度--可视为模型被切片层数

npcsv_to_fbx_cut.py与npcsv_to_fbx(blender).py则需要blender软件打开运行

## 6 样例
sample/15nm-0_xyz.csv（坐标文件）
