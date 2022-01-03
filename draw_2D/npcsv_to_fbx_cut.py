import bpy
import csv
import numpy as np

def clear_sean():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    for i in bpy.data.materials:
        bpy.data.materials.remove(i)
    for i in bpy.data.meshes:
        bpy.data.meshes.remove(i)

def read_csv(file_name):
    file_path = file_name + '.csv'
    with open(file_path,encoding = 'utf-8') as f:
        """读取文件，int，跳过首行，读取索引为1，2，3的列"""
        data = np.loadtxt(f,int,delimiter = ",", skiprows = 1, usecols = (0,1,2,3))
        """**************可能有空行注意,本例取前十行所有列***********"""
        # data = data[:10,::]
    return data

def data_trans(data):
    data_num = data[...,3]
    num_max = np.amax(data_num)
    len = int(pow(data.shape[0], 1/3) + 0.5)
    new_data = np.zeros([len,len,len], dtype = int)
    for i in range(len):
        for j in range(len):
            for k in range(len):
                new_data[i][j][k] = data_num[k + len * j + len * len * i]
    return (int(num_max), len, new_data)

def new_material(num,toumingdu):
    caizhi = bpy.data.materials.new(name=f'material_{num}')
    caizhi.diffuse_color = (0, 1, 1, 1)
    caizhi.blend_method ='BLEND'
    caizhi.use_nodes = True
    caizhi.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value[0] = 0
    caizhi.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value[1] = 1
    caizhi.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value[2] = 1
    caizhi.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value[3] = 0

    caizhi.node_tree.nodes['Principled BSDF'].inputs['Subsurface Color'].default_value[0] = 0
    caizhi.node_tree.nodes['Principled BSDF'].inputs['Subsurface Color'].default_value[1] = 1
    caizhi.node_tree.nodes['Principled BSDF'].inputs['Subsurface Color'].default_value[2] = 1
    caizhi.node_tree.nodes['Principled BSDF'].inputs['Subsurface Color'].default_value[3] = 0

    caizhi.node_tree.nodes['Principled BSDF'].inputs['Alpha'].default_value = toumingdu
    return

def blender_cube_draw(max_density, len, new_data, k):
    # Number of cubes.
    count = len
    # Size of grid.
    extents = 10
    # Size of each cube.
    size_start = (2 * extents / (count - 1))
    # Spacing between cubes.
    padding = size_start / 10
    # Size of each cube indeed.
    sz = size_start - padding
    # To convert abstract grid position within loop to real-world coordinate.
    iprc = 0.0
    jprc = 0.0
    kprc = 0.0
    countf = 1.0 / (count - 1)
    diff = extents * 2
    # Position of each cube.
    z = 0.0
    y = 0.0
    x = 0.0
    # Center of grid.
    centerz = 0.0
    centery = 0.0
    centerx = 0.0
    # Loop through grid z axis.
    for i in range(0, count):
        print(f'{round(i/len*100, 2)}%,plrase wait')
        # Convert from index to percent in range 0 .. 1,
        # then convert from prc to real world coordinate.
        # Equivalent to map(val, lb0, ub0, lb1, ub1).
        iprc = i * countf
        z = -extents + iprc * diff
        # Loop through grid y axis.
        for j in range(0, count):
            jprc = j * countf
            y = -extents + jprc * diff
            # Loop through grid x axis.
            # for k in range(0, count):
            kprc = k * countf
            x = -extents + kprc * diff
            num = int(new_data[k][j][i])
            if (num > 0):
                # Add grid world position to cube local position.
                bpy.ops.mesh.primitive_cube_add(location=(centerx + x, centery + y, centerz + z), size=sz)
                # Cache the current object being worked on.
                current = bpy.context.object
                # Equivalent to Java's String.format. Placeholders
                # between curly braces will be replaced by value of k, j, i.
                current.name = 'Cube ({0}, {1}, {2})'.format(k, j, i)
                current.data.name = 'Mesh ({0}, {1}, {2})'.format(k, j, i)
                # Asppend a material.
                current.data.materials.append(bpy.data.materials[f'material_{num}'])
    print('100.00%, Object creat finish')

def save_fbx(file_path_my):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_scene.fbx(filepath=f'./{file_path_my}.fbx')

def main(file_path, layer):
    """读取CSV，CSV输入为name,x,y,z"""
    data = read_csv(file_path)
    """数据转换为np数组，得到最大值、维度与数组"""
    (num_max, len, new_data) = data_trans(data)
    print(f'cube len ->> {len}')
    """创建不同透明度的材质"""
    new_material(0,0.2)
    for num in range(num_max):
        touming = 0.3 + (0.7 / num_max) * num
        touming = round(touming, 2)
        new_material(num + 1,touming)
    print(f'Add {num_max} materials')
    """创建物体并应用材质"""
    blender_cube_draw(num_max, len, new_data, layer)
    """另存为FBX格式模型"""
    # save_fbx(file_path)
    print("Successful & Finish!!!!!")

if __name__ == '__main__':
    """CSV文件路径，仅文件名"""
    file_path = '15nm-20_xyz_4_B_P_L'
    """提取层数"""
    layer = 0
    clear_sean()
    main(file_path, layer)
