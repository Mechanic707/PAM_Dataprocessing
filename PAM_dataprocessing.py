import colormap as cp
import struct
from tqdm import tqdm

print(len(cp.MAPcmap))

# 定义文件路径、数据尺寸和限制值
file_path = '01.bin'
width = 1000
height = 1000
segment_size = 1024
lim_max = 65535  # 可根据实际情况调整
lim_min = 0      # 可根据实际情况调整

# 初始化point_mapvalue列表
point_mapvalue = []

# 打开二进制文件
with open(file_path, 'rb') as file:
    # 循环处理每个段
    # for _ in range(width * height):
    # 计算总的段数
    total_segments = width * height
    # 使用tqdm创建进度条
    for _ in tqdm(range(total_segments), desc="Processing segments", unit="segment"):
        # 读取1024个16位数据
        data = file.read(segment_size * 2)  # 每个16位数据占2字节
        # 将二进制数据按小端模式解包为整数
        values = struct.unpack('<' + 'H' * segment_size, data)
        
        # 找到段内的最大值和最小值
        max_value = max(values)
        min_value = min(values)
        
        # 根据lim_max和lim_min调整最大值和最小值
        if max_value > lim_max:
            max_value = lim_max
        if min_value < lim_min:
            min_value = lim_min
        
        # 计算delta和lim_delta
        delta = max_value - min_value
        lim_delta = lim_max - lim_min
        
        # 计算point_mapvalue
        point_value = int((delta / lim_delta) * 255.0)
        point_mapvalue.append(point_value)

# 现在point_mapvalue列表包含了1000 * 1000个point_value
print(len(point_mapvalue))  # 输出列表长度，应该是1000 * 1000