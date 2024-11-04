---
title: 在 PDF 中添加页面使用 C++
linktitle: 添加页面
type: docs
weight: 10
url: /cpp/add-pages/
description: 本文介绍如何在 PDF 文件的指定位置插入（添加）页面。学习如何使用 C++ 移动、删除（删除）PDF 文件中的页面。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

本节介绍如何使用 **Aspose.PDF for C++** 库向 PDF 中添加页面。

Aspose.PDF for C++ API 提供了使用 C++ 处理 PDF 文档页面的完全灵活性。

它将 PDF 文档的所有页面保存在 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 中，可以用于处理 PDF 页面。
Aspose.PDF for C++ 允许您在文件中的任意位置插入页面到 PDF 文档中，并且可以将页面添加到 PDF 文件的末尾。

## 在 PDF 文件中添加或插入页面

Aspose.PDF for C++ 允许您在文件中的任意位置插入页面到 PDF 文档中，并且可以将页面添加到 PDF 文件的末尾。

### 在 PDF 文件的指定位置插入空白页面

以下代码示例向您解释了如何在 PDF 文档中添加页面。

1. 使用输入的 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类对象。
1. 调用 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 集合的 [Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) 方法，指定索引。
1. 保存输出 PDF

以下代码片段向您展示了如何在 PDF 文件中插入页面。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void InsertEmptyPageAtDesiredLocation() {
    // 打开文档
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 在 PDF 中插入一个空白页
    document->get_Pages()->Insert(2);

    // 保存输出文件
    document->Save(_dataDir + outputFileName);
}
```

以下是代码示例，您可以通过复制指定页面的参数，将空白页面插入到所需位置：

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // 打开文档
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // 在 PDF 中插入一个空白页面
    auto pageNew = document->get_Pages()->Insert(2);

    // 从第 1 页复制页面参数
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // 保存输出文件
    document->Save(_dataDir + outputFileName);
}
```

### 在 PDF 文件末尾添加一个空白页面

有时，您希望确保文档以一个空白页面结束。 这个主题解释了如何在PDF文档的末尾插入一个空白页。

要在PDF文件的末尾插入一个空白页：

1. 使用输入PDF文件创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类对象。
1. 调用[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)集合的[Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1)方法，不带任何参数。
1. 使用Save方法保存输出PDF。

以下代码片段向您展示如何在PDF文件的末尾插入一个空白页。

```cpp
void AddEmptyPageEnd() {
    // 打开文档
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 在PDF文件末尾插入一个空白页
    document->get_Pages()->Add();

    // 保存输出文件
    document->Save(_dataDir + outputFileName);
}
```