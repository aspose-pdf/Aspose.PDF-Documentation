---
title: 使用C++创建PDF文档
linktitle: 创建
type: docs
weight: 10
url: /zh/cpp/create-document/
description: 使用PDF文件的最受欢迎和基本的任务是从头开始创建文档。使用Aspose.PDF for C++库。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** API允许C++应用程序开发人员在其应用程序中嵌入PDF文档处理功能。可以在不需要在底层机器上安装任何其他软件的情况下创建和读取PDF文件。Aspose.PDF for C++可以用于各种C++应用程序类型，如QT、MFC和控制台应用程序。

## 如何使用C++创建PDF文件

要使用C++创建PDF文件，可以使用以下步骤。

1. 实例化一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象
1. 向文档对象添加一个[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) 创建一个[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)对象
1. 将[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)添加到页面的[Paragraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/)集合中
1. 保存生成的PDF文档

```cpp
void CreatePDF() {
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串。
    String filename("sample-new.pdf");

    // 初始化文档对象
    auto document = MakeObject<Document>();
    // 添加页面
    auto page = document->get_Pages()->Add();

    // 向新页面添加文本
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);

    // 保存更新的PDF
    String outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```