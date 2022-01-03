import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import sys
sys.setrecursionlimit(1000000)

class dfs_simple_digital_chacpt(object):
    def __init__(self,arr):
        self.white = True
        self.row_num = arr.shape[0]
        self.col_num = arr.shape[0]
        self.walked_set = set()
        self.roming_set = set()
        self.dfs_num = 0
        self.array = arr.astype(bool)
        self.list = []
        self.xy_list = []

    def dfs(self, x, y, rgb):
        '''
        desc:用递归实现搜索范围内相同rgb值的像素
        :param x:
        :param y:
        :param char:
        :return:
        '''
        self.roming_set.add(tuple([x, y]))
        # if 0 > x or 0 > y or x >= self.row_num or y >= self.col_num: # 越界检查
        #     return
        if tuple([x,y]) in self.walked_set: # 重复遍历检查
            return
        if rgb != self.array[x][y]: # 目标rgb值检查
            return

        self.walked_set.add(tuple([x, y]))
        if (x == self.col_num - 1):
            self.dfs(0, y, rgb)# x
        else:
            self.dfs(x + 1, y, rgb)# x
        if (y == self.row_num - 1):
            self.dfs(x, 0, rgb)  # y
        else:
            self.dfs(x, y + 1, rgb)  # y
        if (x == - self.col_num):
            self.dfs(self.col_num - 1, y, rgb)  # -x
        else:
            self.dfs(x - 1, y, rgb)  # -x
        if (y == -self.row_num):
            self.dfs(x, self.row_num - 1, rgb)  # -y
        else:
            self.dfs(x, y - 1, rgb)  # -y
        # self.dfs(x + 1, y + 1, rgb)  # Ⅰ
        # self.dfs(x + 1, y - 1, rgb)  # Ⅱ
        # self.dfs(x - 1, y - 1, rgb)  # Ⅲ
        # self.dfs(x - 1, y + 1, rgb)  # Ⅳ
        return

    def walk(self):
        '''
        desc:
        :return:
        '''
        for y in range(self.col_num):
            for x in range(self.row_num):
                rgb = self.array[x][y]
                if tuple([x, y]) in self.roming_set:
                    continue
                if rgb != self.white:
                    self.dfs(x, y, rgb)
                    num = len(self.walked_set)
                    self.list.append(num)
                    self.xy_list.append([x,y])
                    self.walked_set.clear()
        self.roming_set.clear()
        return (self.list,self.xy_list)

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

def get_data(file_name,bead_name_list,cell_length,Rc):
    data = read_csv(file_name)
    rev_data = data_processing(data,bead_name_list)
    (distribute, bool_distribute) = tj_3(rev_data,cell_length,Rc)
    data_int = distribute.astype(int)
    length = data_int.shape[0]
    return (length, data_int)

def plant_analysis(xy_data,csv_data,col,line,Rc):
    """孔径计算可能出现错误，检查孔径过大，尝试改为(avarage, count) = (0,1)"""
    (avarage, count) = kjjs(xy_data)
    index_list = np.nonzero(xy_data)
    none_zero = index_list[0].size
    len = xy_data.shape[0]
    zero = len * len - none_zero
    # print(f'X方向第{col+1}层空点格{zero}个')
    zero_in_vol = zero / (len * len)
    # print(f'X方向第{col+1}层空格率{zero_in_vol}个')
    # print(f'X方向第{col+1}层非零点格{none_zero}个')
    max = np.max(xy_data)
    # print(f'X方向第{col+1}最大密度为{max}')
    var2 =  np.var(xy_data)
    # print(f'X方向第{col+1}层含零方差为{var2}')
    one_line = []
    for deny in range(len):
        for denx in range(len):
            if xy_data[denx][deny] != 0:
                one_line.append(xy_data[denx][deny])
    var3 =  np.var(np.asarray(one_line))
    # print(f'X方向第{col+1}层不含零方差为{var3}')

    """平均孔径"""
    csv_data[line + 1][col] = round(avarage, 3) * Rc / 10
    """单面孔数"""
    csv_data[line + 5][col] = round(count, 3)
    """孔面积"""
    csv_data[line + 9][col] = round(zero, 3) * Rc * Rc / 100
    """孔隙率"""
    csv_data[line + 13][col] = round(zero_in_vol, 3)
    """含零方差"""
    csv_data[line + 17][col] = round(var2, 3)
    """非零方差"""
    csv_data[line + 21][col] = round(var3, 3)
    """最大密度"""
    csv_data[line + 25][col] = round(max, 3)
    return

"""孔径计算"""
def kjjs(data):
    pore_size_obj = dfs_simple_digital_chacpt(data)
    (list,xy_list) = pore_size_obj.walk()
    myset = set(list)
    size_all = 0
    count = 0
    for item in myset:
        # print("the %d has found %d" %(item,list.count(item)))
        size_all += item * list.count(item)
        count += list.count(item)
    avarage = size_all / count
    return (avarage, count)

def write_txt(output, str):
    with open(f'{output}.txt',"w",encoding='UTF-8') as file:
        file.write(str)
    print(f'已输出结果...->>{output}.txt')

def csv_write(csv_data,length, output):
    headers_0 = ['孔径(nm)']
    headers_1 = []
    headers_2 = ['AVE','SUM_AVE']
    first_col_list = ['X','Y','Z','孔数','X','Y','Z','孔面积(nm^2)','X','Y','Z','孔隙率','X','Y','Z','含零密度方差','X','Y','Z','非零密度方差','X','Y','Z','最大密度','X','Y','Z']
    rows = []
    for len in range(length):
        headers_1.append(len + 1)
    headers = headers_0 + headers_1 + headers_2
    for i in range(28 - 1):
        row = [first_col_list[i]]
        for j in range(length + 2):
            num = csv_data[i + 1][j]
            row.append(num)
        rows.append(row)
    # print(headers)
    # print(rows)
    with open(output + '.csv','w', newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
    print(f'已写入{output}.csv')

def main(file_name,bead_name_list,cell_length,Rc,output):
    data = read_csv(file_name)
    (length, new_data) = get_data(file_name,bead_name_list,cell_length,Rc)
    # print(f'切面点格总数{length*length}')
    print_csv_data = np.zeros([28,length + 2], dtype = float)
    # print(new_data[0,::,::])
    # print(new_data[::,0,::])
    for i in range(length):
        yz_data = new_data[i,::,::]
        xz_data = new_data[::,i,::]
        xy_data = new_data[::,::,i]
        data_list = [yz_data, xz_data, xy_data]
        line = 0
        """第几层"""
        for my_loop in range(7):
            print_csv_data[line + my_loop * 4][i] = i + 1
        for data_one in data_list:
            plant_analysis(data_one, print_csv_data, i, line, Rc)
            line += 1
    ave_list = np.mean(print_csv_data, axis = 1)
    for ave in range(28):
        print_csv_data[ave][length] = ave_list[ave] * (length + 2) / length
    for sum in range(7):
        sum_ave = (ave_list[1 + sum * 4] + ave_list[2 + sum * 4] + ave_list[3 + sum * 4]) / 3
        print_csv_data[1 + sum * 4][length + 1] = sum_ave * (length + 2) / length
    csv_write(print_csv_data,length,output)
    # print(print_csv_data)

def dir_file_list():
    path = os.getcwd()
    name_list = os.listdir(path)
    csv_list = []
    for name in name_list:
        if(name[-3:] == 'csv'):
            csv_list.append(name[:-4])
    return csv_list

if __name__ == '__main__':
    name_list = dir_file_list()
    print(name_list)
    for i in name_list:
        """源文件名"""
        file_name = i
        """晶格长度"""
        cell_length = 150
        """最小精度"""
        Rc = 5
        """筛选珠子名显示"""
        """list1 = ['B','P','L','A2','SS','QS'], list2 = ['sh','C2']"""
        bead_name_list = ['B','P','L']
        """输出文件名"""
        select_name = '_'.join(bead_name_list)
        output = f'{file_name[:-4]}_{Rc}_{select_name}_data(nm)'
        main(file_name,bead_name_list,cell_length,Rc,output)
