import matplotlib.pyplot as plt
import numpy as np
import csv
import csv_to_np

# 读取坐标csv
def read_csv(file_name):
    file_path = file_name + '.csv'
    with open(file_path,encoding = 'utf-8') as f:
        """读取文件，int，跳过首行，读取索引为1，2，3的列"""
        data = np.loadtxt(f,int,delimiter = ",", skiprows = 1, usecols = (0,1,2,3))
        """**************可能有空行注意,本例取前十行所有列***********"""
        # data = data[:10,::]
    return data

# 坐标数据转矩阵
def data_trans(data):
    data_num = data[...,3]
    num_max = int(np.amax(data_num))
    len = int(pow(data.shape[0], 1/3) + 0.5)
    new_data = np.zeros([len,len,len], dtype = int)
    for i in range(len):
        for j in range(len):
            for k in range(len):
                new_data[i][j][k] = data_num[k + len * j + len * len * i]
    return (int(num_max), len, new_data)

# python画图
def draw(max_density, len, new_data, ax1):
    length = 50 # 总长总宽
    size_start = length / len # 每个方块加空隙大小
    padding = size_start / 10 # 间隙10%
    size = size_start - padding # 方块实际大小
    for i in range(0, len):
        y = - (length / 2) + size_start * i + padding / 2
        for j in range(0, len):
            x = - (length / 2) + size_start * j + padding / 2
            num = int(new_data[j][i])
            if (num > 0):
                touming = 0.1 + (0.9 / max_density) * num
                touming = round(touming, 3)
                """设置坐标、大小、颜色、透明度"""
                new_rect = plt.Rectangle((x, y), size, size, color = 'cyan', alpha = touming)
                ax1.add_patch(new_rect)

def main(file_name):
    data = read_csv(file_name)
    (num_max, len, new_data) = data_trans(data)
    """图纸大小100*120"""
    fig = plt.figure(figsize=(100,120))
    for i in range(len):
        """图共6行5列"""
        ax = fig.add_subplot(6, 5, i + 1)
        draw(num_max, len, new_data[i],ax)
        plt.xlim(-25, 25)
        plt.ylim(-25, 25)
        plt.xticks([])
        plt.yticks([])
    plt.savefig(f'{file_name}_cut.svg',dpi=300)
    # plt.show()

def main_only():
    """源文件名"""
    file_name = '15nm-0_xyz'
    """晶格长度"""
    cell_length = 150
    """最小精度"""
    Rc = 5
    """筛选珠子名显示"""
    """list1 = ['B','P','L'], list2 = ['sh']"""
    bead_name_list = ['B','P','L']
    """输出文件名"""
    select_name = '_'.join(bead_name_list)
    output = f'{file_name[:-4]}_{Rc}_{select_name}'
    csv_to_np.main(file_name,bead_name_list,cell_length,Rc,output)
    main(output)
if __name__ == "__main__":
    # file_name = '10nm-0_1.3_4_B_P_L'
    # main(file_name)
    main_only()
