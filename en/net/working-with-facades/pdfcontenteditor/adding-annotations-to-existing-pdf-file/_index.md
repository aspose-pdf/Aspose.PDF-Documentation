---
title: Adding Annotations to existing PDF file
type: docs
weight: 80
url: /net/adding-annotations-to-existing-pdf-file/
description: This section explains how to add Annotations to existing PDF file with Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Free Text Annotation in an Existing PDF File (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) allows you to add annotations of different types in an existing PDF file. You can use the respective method to add a particular annotation. For example, in the following code snippet, we have used [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method add [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) type annotation. 

Any type of annotations can be added to the PDF file in the same way. First of all, you need to create an object of type [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)  and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Secondly, you have to create a Rectangle object to specify the area of the annotatation. 

After that, you can call [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method to add [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) annotation, and then use [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file.


The following code snippet shows you how to add free text annotation in a PDF file.

```csharp
public static void AddFreeTextAnnotation()
{
    var document = new Document(_dataDir + "sample.pdf");
    PdfContentEditor editor = new PdfContentEditor(document);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
    tfa.Visit(document.Pages[1]);

    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number
    editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
}
```

## Add Text Annotation in an Existing PDF File (facades)

In this example also, you need to create an object of type [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Secondly, you have to create a Rectangle object to specify the area of the annotation. After that, you can call [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method to add FreeText annotation, create title of your annotations, and the page number on which the annotation is located.

```csharp
public static void AddTextAnnotation()
{
    var document = new Document(_dataDir + "sample.pdf");
    PdfContentEditor editor = new PdfContentEditor(document);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
    tfa.Visit(document.Pages[1]);

    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
    editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
}
```

## Add Line Annotation in an Existing PDF File (facades)

We also specify the Rectangle, coordinates of the beginning and end of the line, page number, thickness, style and color of the annotation frame, type of line dash, type of start and end of the line.

```csharp
public static void AddLineAnnotation()
{
    var document = new Document(_dataDir + "Appartments.pdf");
    PdfContentEditor editor = new PdfContentEditor(document);
    // Create Line Annotation
    editor.CreateLine(
        new System.Drawing.Rectangle(550, 93, 562, 439),
        "Test",
        556, 99, 556, 443, 1, 2,
        System.Drawing.Color.Red,
        "dash",
        new int[] { 1, 0, 3 },
        new[] { "Open", "Open" });
    editor.Save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
}
```