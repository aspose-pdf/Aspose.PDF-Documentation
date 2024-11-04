---
title: 提取 PDF 页
type: docs
weight: 40
url: /net/extract-pdf-pages/
description: 本节介绍如何使用 Aspose.PDF Facades 和 PdfFileEditor 类提取 PDF 页。
lastmod: "2021-06-05"
draft: false
---

## 使用文件路径提取两个数字之间的 PDF 页

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法允许您从 PDF 文件中提取指定范围的页面。此重载允许在从磁盘操作 PDF 文件时提取页面。此重载需要以下参数：输入文件路径、起始页、结束页和输出文件路径。从起始页到结束页的页面将被提取，并且输出将保存到磁盘。以下代码片段向您展示如何使用文件路径提取两个数字之间的 PDF 页。

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // 创建 PdfFileEditor 对象
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // 提取页面
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## 提取PDF页面数组使用文件路径

如果您不想提取页面范围，而是提取一组特定页面，[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法也允许您这样做。您首先需要创建一个包含所有需要提取的页码的整数数组。[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法的这个重载需要以下参数：输入PDF文件、要提取的页面的整数数组和输出PDF文件。以下代码段向您展示了如何使用文件路径提取PDF页面。

```csharp
public static void Extract_PDFPages_Streams()
{
    // 创建 PdfFileEditor 对象
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // 创建流
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        // 提取页面
        pdfEditor.Extract(inputStream, 1, 3, outputStream);
}
```

## 使用流提取两个数字之间的PDF页面

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法允许您使用流提取一系列页面。您需要将以下参数传递给此重载：输入流、开始页面、结束页面和输出流。指定的开始页面和结束页面之间的范围内的页面将从输入流中提取并保存到输出流中。以下代码片段向您展示了如何使用流提取两个数字之间的PDF页面。

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // 创建 PdfFileEditor 对象
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // 提取页面
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## 使用流提取PDF页面数组

从PDF流中提取一组页面，并使用适当的[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)方法重载将其保存到输出流中。如果您不想提取页面范围，而是提取一组特定的页面，[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)方法也可以让您这样做。您首先需要创建一个包含所有需要提取的页码的整数数组。[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)方法的此重载需要以下参数：输入流、要提取页面的整数数组和输出流。
以下代码片段向您展示了如何使用流提取PDF页面。

```csharp
public static void Extract_ArrayPDFPages_Streams()
{
    // 创建 PdfFileEditor 对象
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // 创建流
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
    {
        int[] pagesToExtract = new int[] { 1, 2 };
        // 提取页面
        pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
    }
}
```