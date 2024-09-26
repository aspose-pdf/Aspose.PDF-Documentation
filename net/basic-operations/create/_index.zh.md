---
title: 以编程方式创建PDF文档
linktitle: 创建PDF
type: docs
weight: 10
url: /net/create-document/
description: 本页面描述了如何从头开始使用Aspose.PDF库创建PDF文档。
---

Aspose.PDF for .NET API允许您使用C#和VB.NET创建和读取PDF文件。该API可以在各种.NET应用程序中使用，包括WinForms、ASP.NET等。在本文中，我们将展示如何在.NET应用程序中使用Aspose.PDF for .NET API轻松生成和读取PDF文件。

## 如何使用C#创建PDF文件

使用C#创建PDF文件，可以使用以下步骤。

1. 创建[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)类的对象
1. 将[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)对象添加到Document对象的[Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages)集合中
1.
1. 保存生成的PDF文件

下一个代码示例也适用于新的图形 [Aspose.Drawing](/pdf/net/drawing/) 接口。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// 初始化文档对象
Document document = new Document();
// 添加页面
Page page = document.Pages.Add();
// 向新页面添加文本
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// 保存更新的PDF
document.Save(dataDir + "HelloWorld_out.pdf")
```

在这个例子中，我们创建了一个A4大小的PDF单页文档，页面方向为竖向。我们的页面将在页面左上角包含一个“Hello, World”。
