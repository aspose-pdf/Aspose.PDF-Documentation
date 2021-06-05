---
title: Extract Links from the PDF File with Aspose.PDF for .NET
linktitle: Extract Links
type: docs
weight: 30
url: /net/extract-links/
description: Extract links from PDF with C#. This topic explain you how to extract links using AnnotationSelector class. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Links from the PDF File

Links are represented as annotations in a PDF file, so to extract links, extract all the [LinkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) objects.

1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Get the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) you want to extract links from.
1. Use the [AnnotationSelector](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) class to extract all the [LinkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) objects from the specified page.
1. Pass the [AnnotationSelector](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) object to the Page object’s Accept method.
1. Get all the selected link annotations into an IList object using the [AnnotationSelector](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) object’s Selected property.

The following code snippet shows you how to extract links from a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Open document
Document document = new Document(dataDir+ "ExtractLinks.pdf");
// Extract actions
Page page = document.Pages[1];
AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));
page.Accept(selector);
IList<Annotation> list = selector.Selected;
Annotation annotation = (Annotation)list[0];
dataDir = dataDir + "ExtractLinks_out.pdf";
// Save updated document
document.Save(dataDir);
```
