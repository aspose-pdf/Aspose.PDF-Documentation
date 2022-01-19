---
title: Work with Images using PdfContentEditor
type: docs
weight: 50
url: /net/working-with-images-in-pdf
description: This section explains how to add and delete Images with Aspose.PDF Facades using PdfContentEditor Class.
lastmod: "2021-06-24"
---

## Delete Images from a Particular Page of PDF (Facades)

In order to delete the images from a particular page, you need to call [DeleteImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method with pageNumber and index parameter. The index parameter represents an array of integers – the indexes of the images to be deleted. First of all, you need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and then call the [DeleteImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method. After that, you can save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method.

The following code snippet shows you how to delete images from a particular page of PDF.

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## Delete All the Images from a PDF File (Facades)

All the images can be deleted from a PDF file using [DeleteImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method of the [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Call the [DeleteImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method – the overload without any parametes – to delete all the images, and then save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method.

The following code snippet shows you how to delete all the images from a PDF file.

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## Replace Image in a PDF File (Facades)

the [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) allows you replace your image in a PDF file, call for this the [ReplaceImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) method, and Save the result.

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```
