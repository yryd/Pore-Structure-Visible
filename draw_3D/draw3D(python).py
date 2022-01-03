import matplotlib.pyplot as plt
import numpy as np
import csv

# 输入CSV文件，得到矩阵data，散点云图
def read_csv(file_name):
    file_path = file_name + '.csv'
    with open(file_path,encoding = 'utf-8') as f:
        """读取文件，支持str，跳过首行，读取索引为1，2，3的列"""
        data = np.loadtxt(f,str,delimiter = ",", skiprows = 1, usecols = (0,1,2,3))
        """**************可能有空行注意,本例取前十行所有列***********"""
        # data = data[:10,::]
        return data

# 处理CSV数据
def data_processing(data,name_list):
    index = data[...,0]
    content = data[...,1:]
    all_list = []
    for name in name_list:
        row = np.where(index == name)
        all_list = all_list + row[0].tolist()
    use_line = np.array(all_list)
    content = content[use_line,...]
    """注意以字符串读取进来的要转换回数据"""
    rev_data = content.astype(np.float64)
    return rev_data

# 统计频率直方图，二维
def tj_2(data):
    # 制造x，y轴，前两参数为起始与结束，第三个参数为等分个数
    """"坐标轴范围与精度"""
    gridx = np.linspace(0, 10, 10)
    gridy = np.linspace(0, 10, 10)
    # 取data第0列第1列为xy
    x = data[::,0]
    y = data[::,1]
    grid, _, _ = np.histogram2d(x, y, bins=[gridx, gridy])
    plt.figure()
    plt.pcolormesh(gridx, gridy, grid)
    plt.plot(y, x, 'ro')
    plt.colorbar()
    plt.show()

# 统计三维频率直方图
def tj_3(data_rev,len,Rc):
    len_int = int(len)
    num_int = int(len/Rc) + 1
    gridx = np.linspace(0, len_int, num_int)
    gridy = np.linspace(0, len_int, num_int)
    gridz = np.linspace(0, len_int, num_int)
    density, edges = np.histogramdd(data_rev, bins=[gridx, gridy,gridz])
    print(gridz)
    density_bool = density.astype(bool)
    return (density, density_bool)

# CSV写入
def csv_write(cube_data, cube_data_bool, output):
    headers = ['X','Y','Z','number']
    rows = []
    for i in range(cube_data.shape[0]):
        for j in range(cube_data.shape[1]):
            for k in range(cube_data.shape[2]):
                num = cube_data[i][j][k]
                row = [i,j,k,num]
                rows.append(row)
    with open(output + '.csv','w', newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

# 绘制方块堆积图，输入布尔矩阵[bool_distribute]
def draw(bool_distribute):
    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(bool_distribute)
    plt.show()


if __name__ == '__main__':
    """源文件名"""
    file_name = '15nm-20_xyz'
    """晶格长度"""
    cell_length = 150
    """最小精度"""
    Rc = 4
    """筛选珠子名显示"""
    """list1 = ['B','P','L'], list2 = ['Hex']"""
    bead_name_list = ['B','P','L']
    """输出文件名"""
    select_name = '_'.join(bead_name_list)
    output = file_name + '_' + select_name + '_blender'

    data = read_csv(file_name)
    rev_data = data_processing(data,bead_name_list)
    (distribute, bool_distribute) = tj_3(rev_data,cell_length,Rc)
    # draw(bool_distribute)
    csv_write(distribute, bool_distribute, output)
