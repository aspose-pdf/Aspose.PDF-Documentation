---
title: 使用Python替换现有PDF文件中的图像
linktitle: 替换图像
type: docs
weight: 70
url: /zh/python-net/replace-image-in-existing-pdf-file/
description: 本节介绍如何使用Python库替换现有PDF文件中的图像。
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: 在PDF中替换图像
Abstract: Aspose.PDF for Python via .NET 文档提供了关于在现有PDF文件中替换图像的完整指南。此功能对于在不更改文本内容的情况下更新PDF文档中的标志、图形或其他视觉元素等任务至关重要。
---

## 在PDF中替换图像

如何在PDF页面上用新图像替换已有图像？使用 Aspose.PDF for Python via .NET 实现此功能。

1. 导入必要的模块（aspose.pdf、os.path、FileIO）。
1. 为以下项定义路径：
- 输入PDF（infile）
- 新图像文件（image_file）
- 输出PDF（outfile）
1. 使用 'apdf.Document(path_infile)' 加载PDF文档。
1. 以二进制读取模式打开新的图像文件。
1. 替换首页上的第一张图像：
- 'document.pages[1].resources.images.replace(1, image_stream)'
1. 将更新后的PDF保存至 'path_outfile'。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## 替换特定图像

本示例演示如何通过图像位置检测定位并替换PDF页面上的特定图像。

1. 使用 'apdf.Document()' 加载PDF。
1. 创建一个 'ImagePlacementAbsorber' 来收集页面上的所有图像位置。
1. 在首页接受吸收器（'document.pages[1].accept(absorber)'）。
1. 检查页面上是否存在图像位置。
1. 选择第一个图像位置 (absorber.image_placements[1]) 并进行替换。
1. 将修改后的PDF保存至 'path_outfile'。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```
