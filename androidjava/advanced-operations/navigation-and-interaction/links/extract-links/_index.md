---
title: Extract Links from the PDF File with Aspose.PDF for Java
linktitle: Extract Links
type: docs
weight: 30
url: /java/extract-links/
description: Extract links from PDF with Java. This topic explain you how to extract links using AnnotationSelector class. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Links from the PDF File

Links are represented as annotations in a PDF file, so to extract links, extract all the [LinkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) objects.

1. Create a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object.
1. Get the [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) you want to extract links from.
1. Use the [AnnotationSelector](https://apireference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) class to extract all the [LinkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) objects from the specified page.
1. Pass the [AnnotationSelector](https://apireference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) object to the Page object’s Accept method.
1. Get all the selected link annotations into an IList object using the [AnnotationSelector](https://apireference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) object’s [getSelected](https://apireference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) method.

The following code snippet shows you how to extract links from a PDF file.

```java
    public static void ExtractLinksFromThePDFFile() {        
        // Load the PDF file
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("Annotation located: " + annot.getRect());
        }
                
        // Save the document with updated link
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```
