---
title: 将图像转换为PDF在Python中
linktitle: 将图像转换为PDF文件
type: docs
weight: 10
url: zh/python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: 本主题向您展示如何使用Aspose.PDF for Python via C++库将图像转换为PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

我们的库展示了用于转换最流行的图像格式 - JPEG 的代码片段。您可以通过以下步骤非常轻松地使用Aspose.PDF for Python via C++将JPG图像转换为PDF：

## 将图像转换为PDF

您可以通过以下步骤非常轻松地使用Aspose.PDF for C++将JPG图像转换为PDF：

1. 使用PIL库打开输入图像文件
2. 获取图像的宽度和高度
3. 使用AsposePDFPythonWrappers库创建一个新的Document实例
4. 设置图像的固定高度和宽度
5. 向文档添加新页面
6. 将图像添加到页面
7. 使用'document.save'方法保存输出PDF。

下面的代码片段展示了如何使用Python via C++将JPG图像转换为PDF：

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# 设置数据文件的目录路径
dataDir = os.path.join(os.getcwd(), "samples")

# 设置输入文件路径
input_file = os.path.join(dataDir, "sample.jpg")

# 设置输出文件路径
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# 使用PIL库打开输入图像文件
pil_img = Image.open(input_file)

# 获取图像的宽度和高度
width, height = pil_img.size

# 使用AsposePDFPythonWrappers库创建一个新的Document实例
document = apw.Document()

# 使用AsposePDFPythonWrappers库创建一个新的Image实例
image = apw.Image()

# 设置图像的文件路径
image.file = input_file

# 设置图像的固定高度和宽度
image.fix_height = height
image.fix_width = width

# 向文档添加新页面
page = document.pages.add()

# 向页面添加图像
page.paragraphs.add(image)

# 将文档保存到输出文件路径
document.save(output_file)
```