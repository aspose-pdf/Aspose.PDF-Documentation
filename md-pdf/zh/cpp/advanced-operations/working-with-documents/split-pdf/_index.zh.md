---
title: 用编程方式拆分 PDF
linktitle: 拆分 PDF 文件
type: docs
weight: 60
url: /cpp/split-pdf-document/
description: 本主题展示如何使用 C++ 将 PDF 页面拆分为单独的 PDF 文件。
lastmod: "2022-09-01"
sitemap:
    changefreq: "monthy"
    priority: 0.7
---

## 实时示例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) 是一个在线免费网络应用程序，它允许您研究演示文稿拆分功能的工作方式。

[![Aspose 拆分 PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

本主题展示如何在您的 C++ 应用程序中将 PDF 页面拆分为单独的 PDF 文件。要使用 C++ 将 PDF 页面拆分为单页 PDF 文件，可以按照以下步骤：

1. 通过 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象的 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 集合循环遍历 PDF 文档的页面
1. 为每次迭代，创建一个新的 Document 对象，并将单个 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 对象复制到空文档中 1. 使用 Save 方法保存新的 PDF

以下 C++ 代码片段向您展示如何将 PDF 页面拆分为单独的 PDF 文件。

```cpp
void SplittingDocuments() {
    // 路径名的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String documentFileName("sample.pdf");
    
    // 打开文档
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // 遍历所有页面
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->CopyPage(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```