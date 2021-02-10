---
title: PDF Text Annotation
linktitle: Text Annotation
type: docs
weight: 11
url: /net/pdf-annotation-in-existing-pdf-file/
description: This page describes how to add an annotation in an existing PDF file. Also, you may delete all or particular annotations from a page of a PDF file.
lastmod: "2021-01-13"
draft: true
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Add, Delete, and Get Annotation are similar for different kinds of annotations. Let take as example a Text Annotation.

## How to add Text Annotation into existing PDF file

A Text Annotation is an annotation attached to a specific location in a PDF document. When closed, the annotation is displayed as an icon; when opened, it should display a pop-up window containing the note text in the font and size chosen by the reader.

Annotations are contained by the [Annotations](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page#getAnnotations--) collection of a particular Page. This collection contains the annotations for that individual page only; every page has its own Annotations collection.

To add an annotation to a particular page, add it to that page’s Annotations collection with the [Add](https://apireference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection#add-com.aspose.pdf.Annotation-) method.

1. First, create an annotation that you want to add to the PDF.
1. Then open the input PDF.
1. Add the annotation to the [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) object's Annotations collection.

The following code snippet shows you how to add an annotation in a PDF page.

```java
private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

public static void AddTextAnnotation()
{
    // Load the PDF file
    Document document = new Document(_dataDir + "sample.pdf");
    Page page = document.getPages().get_Item(1);
    Rectangle rect = new Rectangle(200, 750, 400, 790);
    TextAnnotation textAnnotation = new TextAnnotation(page, rect);

    textAnnotation.setTitle("Aspose User");
    textAnnotation.setSubject("Sample Subject");
    textAnnotation.setState (AnnotationState.Accepted);
    textAnnotation.setContents("Sample contents for the annotation");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);

    Border border = new Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    textAnnotation.setRect(rect);

    page.getAnnotations().add(textAnnotation);
    document.save(_dataDir + "sample_textannot.pdf");
}
```
