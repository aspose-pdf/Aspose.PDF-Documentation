---
title: PDF Watermark Annotation using C#
linktitle: Watermark Annotation
type: docs
weight: 130
url: /net/watermark-annotation/
description: The Watermark Annotation in the text uses to represent graphics on the page. Check code snippet to resolve this task.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Watermark Annotation

A watermark annotation shall be used to represent graphics that shall be printed at a fixed size and position on a page, regardless of the dimensions of the printed page.

You can add Watermark Text using [WatermarkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/watermarkannotation) at a specific position of the PDF page. The opacity of Watermark can also be controlled by using opacity property.

Please check the following code snippet to add WatermarkAnnotation.

```csharp
 //Load a Document
Aspose.PDF.Document doc = new Aspose.PDF.Document("source.pdf");

//Load Page object to add Annotation
Page page = doc.Pages[1];

//Create Annotation
WatermarkAnnotation wa = new WatermarkAnnotation(page, new Aspose.PDF.Rectangle(100, 500, 400, 600));

//Add annotaiton into Annotation collection of Page
page.Annotations.Add(wa);

//Create TextState for Font settings
Aspose.PDF.Text.TextState ts = new Aspose.PDF.Text.TextState();

ts.ForegroundColor = Aspose.PDF.Color.Blue;
ts.Font = FontRepository.FindFont("Times New Roman");

ts.FontSize = 32;

//Set opacity level of Annotaiton Text

wa.Opacity = 0.5;
//Add Text in Annotation

wa.SetTextAndState(new string[] { "HELLO", "Line 1", "Line 2" }, ts);

//Save the Document
doc.Save("Output.pdf");
```
