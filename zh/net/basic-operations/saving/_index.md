---
title: 以编程方式保存PDF文档
linktitle: 保存PDF
type: docs
weight: 30
url: /zh/net/save-pdf-document/
description: 学习如何在C# Aspose.PDF for .NET PDF库中保存PDF文件。将PDF文档保存到文件系统、流和Web应用程序中。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

下一个代码片段也适用于新的图形界面[Aspose.Drawing](/pdf/zh/net/drawing/)。

## 将PDF文档保存到文件系统

您可以使用`Document`类的`Save`方法将创建或操作的PDF文档保存到文件系统。
如果您不提供格式类型（选项），则文档将以Aspose.PDF v.1.7 (*.pdf)格式保存。

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // 进行一些操作，例如添加新的空白页
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```
## 将PDF文件保存到流

您还可以通过使用`Save`方法的重载将创建或操作的PDF文件保存到流。

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // 进行一些操作，例如添加新的空白页
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## 在Web应用程序中保存PDF文件

要在Web应用程序中保存文档，您可以使用上述方法。此外，`Document`类为与[HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8)类一起使用重载了`Save`方法。

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// 进行一些操作，例如添加新的空白页
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```
有关更详细的说明，请参阅[展示](/pdf/zh/net/showcases/)部分。

## 保存PDF/A或PDF/X格式

PDF/A是针对在档案保存和长期保存电子文件中使用的便携式文档格式（PDF）的ISO标准化版本。
PDF/A与PDF的不同之处在于它禁止了不适合长期存档的功能，例如字体链接（与字体嵌入相对）和加密。PDF/A查看器的ISO要求包括颜色管理指南、嵌入式字体支持和用于阅读嵌入式注释的用户界面。

PDF/X是PDF ISO标准的一个子集。PDF/X的目的是促进图形交换，因此它有一系列与标准PDF文件不适用的与打印相关的要求。

在这两种情况下，都使用`Save`方法来存储文档，而文件必须使用`Convert`方法来准备。

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```

