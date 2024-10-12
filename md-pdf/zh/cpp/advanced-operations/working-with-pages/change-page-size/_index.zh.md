---
title: Change PDF Page Size Programmatically 
linktitle: Change PDF Page Size
type: docs
weight: 40
url: /cpp/change-page-size/
description: 使用C++库更改PDF文件的页面大小。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF是一种静态布局的可打印格式，这就是为什么它在商业生活中变得广泛使用的原因。

然而，当您需要调整PDF文档的大小，因为页面大小大于纸张大小时，您可能会有这样的任务。但是怎么做呢？

不用担心。在此页面上，您将找到解决任务的方法。

但首先，让我们记住有页面大小系列。

世界上广泛采用了两种页面大小系列。
当然，还有许多格式，但以下是最常用的。
第一个是ISO纸张尺寸。 Series A4 用于标准打印和文具。信纸尺寸用于海报、墙表等。美国、加拿大和部分墨西哥采用了第二页尺寸系列，它们是目前唯一尚未广泛使用 ISO 标准纸张尺寸的工业化国家。

现在让我们看看 Aspose.PDF 如何提示您使用 C++ 库调整页面大小。

## 更改 PDF 页面大小

Aspose.PDF for C++ 允许您在 C++ 应用程序中通过简单的代码行更改 PDF 页面大小。本主题解释如何更新/更改现有 PDF 文件的页面尺寸（大小）。

[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 类包含 SetPageSize(...) 方法，该方法允许您设置页面大小。下面的代码片段通过几个简单的步骤更新页面尺寸：

1. 加载源 PDF 文件。
1. 将页面获取到 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 对象中。
1. 获取指定页面。
1. 调用 SetPageSize(..) 方法来更新其尺寸。
1. 调用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类的 Save(..) 方法，以生成具有更新页面尺寸的 PDF 文件。

以下代码片段显示了如何将 PDF 页面尺寸更改为 A4 大小。

```cpp
void ChangePageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");
    String outputFileName("UpdateDimensions_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 获取特定页面
    auto pdfPage = document->get_Pages()->idx_get(1);

    // 设置页面大小为 A4 (11.7 x 8.3 in)，在 Aspose.Pdf 中，1 英寸 = 72 点
    // 因此 A4 尺寸以点为单位为 (842.4, 597.6)
    pdfPage->SetPageSize(597.6, 842.4);
    // 保存更新后的文档
    document->Save(_dataDir + outputFileName);
}
```

## 获取 PDF 页面大小

您可以使用 Aspose.PDF for C++ 读取现有 PDF 文件的页面大小。 以下代码示例演示了如何使用C++读取PDF页面尺寸。

```cpp
void GetPDFPageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 获取特定页面
    auto page = document->get_Pages()->idx_get(1);

    // 获取页面高度和宽度信息
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());
    // 将页面旋转90度
    page->set_Rotate(Rotation::on90);
    // 获取页面高度和宽度信息
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());

}
```