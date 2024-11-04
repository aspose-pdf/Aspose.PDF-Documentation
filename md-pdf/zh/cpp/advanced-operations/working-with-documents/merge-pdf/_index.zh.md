---
title: 使用 C++ 合并 PDF
linktitle: 合并 PDF 文件
type: docs
weight: 50
url: /cpp/merge-pdf-documents/
description: 本页解释如何使用 C++ 将多个 PDF 文档合并为单个 PDF 文件。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

合并 PDF 文件不是一项简单的任务，但非常流行。您可以使用 Aspose.PDF for C++ 库快速轻松地将 PDF 文件合并为一个文档。

## 使用 C++ 合并 PDF 文件

要连接两个 PDF 文件：

1. 创建两个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象，每个对象包含一个输入 PDF 文件。
1. 然后调用 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 集合的 Add 方法，用于将其他 PDF 文件添加到目标 Document 对象。
1. 将第二个文档的 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 添加到第一个文件。
1. 最后，使用 Save 方法保存输出 PDF 文件。

以下代码片段展示了如何连接 PDF 文件。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // 打开文档
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // 将第二个文档的页面添加到第一个文档
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // 保存合并后的输出文件
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## 实时示例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) 是一个免费的在线 web 应用程序，允许您研究演示合并功能的工作原理。

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)