---
title: Extract Links from the PDF File 
linktitle: Extract Links
type: docs
weight: 30
url: /cpp/extract-links/
description: Extract links from PDF with C#. This topic explain you how to extract links using AnnotationSelector class. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Links from the PDF File

Links are represented as annotations in a PDF file, so to extract links, extract all the [LinkAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) objects.

1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object.
1. Get the [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) you want to extract links from.
1. Use the [AnnotationSelector](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) class to extract all the [LinkAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) objects from the specified page.
1. Pass the [AnnotationSelector](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) object to the Page object’s Accept method.
1. Get all the selected link annotations into an IList object using the [AnnotationSelector](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) object’s Selected property.

The following code snippet shows you how to extract links from a PDF file.

```cpp
void ExtractLinksFromThePDFFile() {
   
    // Load the PDF file
    String _dataDir("C:\\Samples\\");

    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);


    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"Annotation located: {0}", annot->get_Rect());
    }
}
```
