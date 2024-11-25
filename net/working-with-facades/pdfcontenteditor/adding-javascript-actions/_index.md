---
title: Adding Javascript actions PDF 
type: docs
weight: 10
url: /net/adding-javascript-actions/
description: This section explains how to add Javascript actions to existing PDF file with Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) class present underAspose.Pdf.Facades package provides the flexibility to add Javascript actions to a PDF file. You can create a link with the serial actions corresponding to execute a menu item in the PDF viewer. This class also provides the feature to create additional actions for document events. 

First of all, an object is drawn in the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), in our example a [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle). And set the action [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) to the Rectangle. After you may save your document.

```csharp
public static void AddingJavascriptActions()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(dataDir + "sample.pdf");
    // create Javascript link
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
    String code = "app.alert('Welcome to Aspose!');";
    editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
    // save the output file
    editor.Save(dataDir + "JavaScriptAdded_output.pdf");
}
```