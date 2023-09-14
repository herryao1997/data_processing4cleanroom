#!/bin/bash

# 遍历当前文件夹中的所有.txt文件
for file in *.txt; do
  # 检查文件是否存在
  if [ -e "$file" ]; then
    # 获取文件名（不包括扩展名）
    filename=$(basename "$file" .txt)
    # 将文件名中的"_"替换为"% "
    new_filename="${filename//_/\% }"
    # 生成新的文件名
    new_file="${new_filename}.txt"

    # 重命名文件
    mv "$file" "$new_file"
    echo "将文件 '$file' 重命名为 '$new_file'"
  fi
done

echo "完成替换操作"
