---
title: 使用Python通过C++旋转PDF页面
linktitle: 旋转PDF页面
type: docs
weight: 20
url: /zh/python-cpp/rotate-pages/
description: 本主题描述如何通过Python使用C++以编程方式旋转现有PDF文件中的页面方向。
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

有时候，由于扫描或创建问题，PDF页面可能有错误的方向。旋转页面可以确保它们以正确的方向显示，以便于阅读和查看。

旋转PDF页面有助于在不同设备和平台上保持一致的查看体验。

旋转PDF页面可以便利编辑任务，例如添加注释、评论或签名。通过将页面旋转到所需的方向，可以使编辑和审阅过程更加高效。

此外，在打印PDF文档时，确保页面方向正确以避免对齐错误或裁剪问题也很重要。
 在打印之前根据需要旋转页面有助于优化打印输出，并确保内容按预期显示。  
旋转 PDF 页面是一个有用的功能，可以帮助提高文档在各种环境和用途中的可读性、一致性和展示效果。

本主题描述了如何使用 Python 以编程方式更新或更改现有 PDF 文件中的页面方向。

## 更改页面方向

Aspose.PDF for Python via C++ 支持一些很棒的功能，比如更改页面方向

1. 从输入文件创建文档对象
1. 使用 'apCore.document_get_pages' 从文档中获取页面集合
1. 使用 'apCore.page_collection_get_page' 从页面集合中获取第一页
1. 使用 'apCore.page_set_rotate' 将页面顺时针旋转 90 度
1. 使用 'document.save' 方法将修改后的文档保存到输出文件

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # 创建包含示例文件的目录路径
    dataDir = os.path.join(os.getcwd(), "samples")

    # 创建输入和输出文件的路径
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "rotated_document.pdf")

    # 通过加载输入文件创建文档对象
    doc = apCore.document_create_from_file(inputFile)

    # 获取文档中的页面集合
    pages = apCore.document_get_pages(doc)

    # 从集合中获取第一页
    page = apCore.page_collection_get_page(pages, 1)

    # 将页面顺时针旋转 90 度
    apCore.page_set_rotate(page, apCore.Rotation(apCore.on90))

    # 将修改后的文档保存到输出文件
    apCore.document_save(doc, output_file)

    # 关闭文档句柄以释放资源
    apCore.close_handle(doc)
```