---
title: 使用C++通过Python设置PDF的大小
linktitle: 设置PDF大小
type: docs
weight: 30
url: zh/python-cpp/get-and-set-page-properties/
description: 本节介绍如何使用Python通过C++获取或设置PDF页面属性，例如文档的大小。
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 设置PDF文件的大小

Aspose.PDF for Python通过C++允许您在Python应用程序中读取和设置PDF文件中页面的属性。

下面的代码片段打开一个PDF文件，通过调整**裁剪框**（裁剪框是您的PDF文档在Adobe Acrobat中显示的“页面”大小）来调整第一页的大小，并将修改后的文档保存到一个新文件中。

1. 从输入文件创建一个文档对象
1. 使用[document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)从文档中获取页面集合

1. 从页面集合中获取第一页，使用[page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)
1. 使用[page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)从页面获取裁剪框矩形
1. 计算裁剪框的新坐标
1. 使用新值更新裁剪框坐标
1. 使用'document.save'方法将修改后的文档保存到输出文件

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # 获取当前工作目录并创建到“samples”目录的路径
    dataDir = os.path.join(os.getcwd(), "samples")

    # 创建输入和输出文件路径
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # 从输入文件创建文档对象
    doc = apCore.document_create_from_file(inputFile)

    # 从文档中获取页面集合
    pages = apCore.document_get_pages(doc)

    # 从页面集合中获取第一页
    page = apCore.page_collection_get_page(pages, 1)

    # 从页面获取裁剪框矩形
    crop_box = apCore.page_get_rectangle(page)

    # 计算裁剪框的新坐标
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # 使用新值更新裁剪框坐标
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # 将修改后的文档保存到输出文件
    apCore.document_save(doc, output_file)

    # 关闭文档句柄
    apCore.close_handle(doc)
```