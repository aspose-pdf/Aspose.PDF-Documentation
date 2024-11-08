---

title: 使用Python以编程方式拆分PDF
linktitle: 拆分PDF文件
type: docs
weight: 20
url: /zh/python-cpp/split-pdf-document/
keywords: 将pdf拆分为多个文件, 将pdf拆分为单独的pdf, 拆分pdf python
description: 本主题展示如何在Python中通过C++应用程序将PDF页面拆分为单个PDF文件。
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

拆分PDF页面对于想要将大型文件拆分为单独页面或页面组的人来说是一个有用的功能。

## 实时示例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) 是一个在线的免费网络应用程序，允许您研究演示拆分功能的工作原理。

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

本主题展示如何在您的Python C++应用程序中将PDF页面拆分为单个PDF文件。要使用Python将PDF页面拆分为单页PDF文件，可以按照以下步骤进行：

代码片段设置了必要的目录和文件路径，打开一个PDF文档，然后遍历文档的每一页。
 对于每个页面，它创建一个新文档，将当前页面复制到新文档，并将新文档另存为具有特定命名约定的单独PDF文件。

1. 打开输入文档
1. 初始化页面计数
1. 遍历文档的所有页面

## 在Python中将PDF拆分为多个文件或单独的PDF

以下Python代码片段向您展示如何将PDF页面拆分为单个PDF文件。

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # 打开文档
    document = apw.Document(inputFile)

    pageCount = 1

    # 遍历所有页面

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```