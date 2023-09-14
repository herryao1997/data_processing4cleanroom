#!/bin/bash

# 遍历当前文件夹中的所有.txt文件
for file in *.txt; do
  # 检查文件是否存在
  if [ -e "$file" ]; then
    # 使用sed命令替换文件内容中的"_"为"-"
    sed -i 's/_/-/g' "$file"
    echo "已将文件 '$file' 中的 '_' 替换为 '-'."
  fi
done

echo "完成替换操作"
