---
title: Extract Chart objects from PDF document (facades)
type: docs
weight: 20
url: /java/extract-chart-objects/
description: This section explains how to extract chart objects from PDF with Aspose.PDF Facades using PdfExtractor Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Chart objects from PDF document (facades)

The PDF allow to group page content into elements named as **Marked Content**. Adobe Acrobat shows them as "containers". The Chart objects are placed in such objects. We have introduced a new method extractMarkedContentAsImages() in PdfExtractor class to extract these object. This method render every **Marked Content** into a separate image. Please note all the charts are not fully placed into one container. Because of this some charts will be saved into separate images by parts.

Please note that the correct grouping of content into containers is the responsibility of a PDF document designer. If you want to get charts with header or other objects you should either edit/create the PDF document where whole chart is placed in one container.

```java

 //Open document

Document document = new Document("sample.pdf");

//instantiate PdfExtractor

PdfExtractor pdfExtractor = new PdfExtractor();

//Extract Chart objects as image in a folder

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```

