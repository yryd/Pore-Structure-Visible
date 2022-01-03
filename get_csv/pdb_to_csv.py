import csv

"""读取XYZ文件"""
def readpdb(file_name):
    """初始化数据存储"""
    data = []
    with open(file_name,encoding = 'utf-8') as file:
        for line in file:
            list = line.split( )
            # print(list)
            """去除非数据行"""
            if (len(list) > 10):
                name = "".join(line[76:78].split())
                X = float(line[30:38])
                Y = float(line[38:46])
                Z = float(line[46:54])
                data.append([name,X,Y,Z])
            if (list[0] == 'CONECT'):
                break
    return data

"""写入csv文件"""
def writecsv(data,file_name):
    """写入文件列名"""
    headers = ['Name','X','Y','Z']
    """输出文件名"""
    output = file_name[:-4] + '_xyz'
    rows = []
    for i in data:
        name = i[0]
        X = i[1]
        Y = i[2]
        Z = i[3]
        """row为每行数据"""
        row = [name,X,Y,Z]
        rows.append(row)
    """rows写入csv"""
    with open(output + '.csv','w', newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

def main(file_name):
    file_name = file_name + '.pdb'
    data = readpdb(file_name)
    print('读取pdb完毕...')
    print(data[0])
    writecsv(data,file_name)
    print('写入CSV成功...')


if __name__ == '__main__':
    """所读取pdb文件名，仅文件名"""
    file_name = 'H2O_In_PA'
    main(file_name)
