---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /cpp/posting-acroform-data/
description: 您可以使用 Aspose.PDF for C++ 中的 Aspose.Pdf.Facades 命名空间将表单数据导入和导出到 XML 文件。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm 是 PDF 文档的一种重要类型。 您不仅可以使用 [Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) 创建和编辑 AcroForm，还可以将表单数据导入和导出到 XML 文件。Aspose.PDF for C++ 中的 Aspose.Pdf.Facades 命名空间允许您实现 AcroForm 的另一个功能，该功能帮助您将 AcroForm 数据发布到外部网页。然后，该网页读取发布的变量并使用这些数据进行进一步处理。在您不仅希望将数据保存在 PDF 文件中，而是希望将其发送到服务器并保存在数据库等情况下，此功能非常有用。

{{% /alert %}}

## 实现细节

在本文中，我们尝试使用 [Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) 和 [FormEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form_editor/) 类创建一个 AcroForm。我们还添加了一个提交按钮，并设置了其目标 URL。

以下代码片段向您展示了如何创建表单，然后在网页上接收发布的数据。
```cpp
using namespace System;
using namespace Aspose::Pdf;

void PostingExample() {

    // String _dataDir("C:\\Samples\\");
    // 创建一个FormEditor类的实例并绑定输入和输出pdf文件
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // 创建AcroForm字段 - 为简单起见，我只创建了两个字段
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // 添加一个提交按钮并设置目标URL
    editor->AddSubmitBtn(u"submitbutton", 1, u"Submit", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // 保存输出pdf文件
    editor->Save();
}
```