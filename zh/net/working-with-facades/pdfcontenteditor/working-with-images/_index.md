---
title: 使用 PdfContentEditor 处理图像
type: docs
weight: 50
url: /zh/net/working-with-images-in-pdf
description: 本节介绍如何使用 Aspose.PDF Facades 和 PdfContentEditor 类添加和删除图像。
lastmod: "2021-06-24"
---

## 从 PDF 的特定页面删除图像 (Facades)

为了从特定页面删除图像，您需要调用 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) 方法，并传递 pageNumber 和 index 参数。 参数 index 表示一个整数数组——要删除的图像的索引。首先，你需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的对象，然后调用 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) 方法。之后，你可以使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法保存更新后的 PDF 文件。

以下代码片段向您展示了如何从 PDF 的特定页面删除图像。

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## 从 PDF 文件中删除所有图像 (Facades)

可以使用 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 的 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) 方法从 PDF 文件中删除所有图像。 调用 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) 方法——没有任何参数的重载——来删除所有图像，然后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法保存更新后的 PDF 文件。

以下代码片段显示了如何从 PDF 文件中删除所有图像。

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## 替换 PDF 文件中的图像 (Facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 允许您替换 PDF 文件中的图像，为此调用 [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) 方法，并保存结果。

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```