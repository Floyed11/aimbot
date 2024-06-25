# import yaml
# import os
# from collections import Counter
# import matplotlib.pyplot as plt

# # 步骤1: 解析.yaml文件
# with open('/Users/linto/Documents/AI基础/aimbot/datasets/CS Detect.v1i.yolov9/data.yaml', 'r') as file:
#     data_config = yaml.safe_load(file)

# # 假设你已经有一个函数来获取每个目录中的图像数量
# def count_images_in_directory(directory):
#     # 获取脚本所在的目录
#     script_dir = os.path.dirname(__file__)
#     # 将相对路径转换为绝对路径
#     abs_directory_path = os.path.abspath(os.path.join(script_dir, directory))
#     print(directory)
#     # 计算并返回图像数量
#     return len([name for name in os.listdir(abs_directory_path) if os.path.isfile(os.path.join(abs_directory_path, name))])

# # 步骤2: 读取图像数据并分析
# image_counts = {category: count_images_in_directory(data_config[category]) for category in ['train', 'val', 'test']}

# # 步骤3: 分析每个类别的图像数量（这里简化处理，仅计算总数）
# total_images = sum(image_counts.values())

# # 步骤4: 绘制图表
# plt.bar(image_counts.keys(), image_counts.values())
# plt.title('Dataset Distribution')
# plt.xlabel('Category')
# plt.ylabel('Number of Images')
# plt.show()
import os
import yaml
from collections import Counter
import matplotlib.pyplot as plt

# 步骤1: 解析.yaml文件
with open('/Users/linto/Documents/AI基础/aimbot/datasets/CS Detect.v1i.yolov9/data.yaml', 'r') as file:
    data_config = yaml.safe_load(file)

# 修改后的函数，用于统计每个类别的图像数量
def count_categories_in_labels(directory):
    # 获取脚本所在的目录
    script_dir = os.path.dirname(__file__)
    # 构建标注文件夹的绝对路径
    abs_label_path = os.path.abspath(os.path.join(script_dir, directory, 'labels'))
    category_counts = Counter()
    # 遍历标注文件夹中的所有.txt文件
    for label_file in os.listdir(abs_label_path):
        if label_file.endswith('.txt'):
            with open(os.path.join(abs_label_path, label_file), 'r') as file:
                for line in file:
                    category = line.split()[0]  # 假设类别ID在每行的第一个位置
                    category_counts[category] += 1
    return category_counts

# 步骤2: 读取图像数据并分析
category_counts = Counter()
for category in ['train', 'val', 'test']:
    category_counts += count_categories_in_labels(data_config[category])

# 步骤3: 绘制图表
# 将类别ID和数量分别转换为列表，并按类别ID排序
sorted_categories = sorted(category_counts.items(), key=lambda x: int(x[0]))
categories, counts = zip(*sorted_categories)  # 解压为两个列表

plt.bar(categories, counts)
plt.title('Dataset Distribution by Category')
plt.xlabel('Category ID')
plt.ylabel('Number of Images')
plt.show()