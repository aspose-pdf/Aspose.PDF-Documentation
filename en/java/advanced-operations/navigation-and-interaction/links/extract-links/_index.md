---
title: Extract Links from the PDF File 
linktitle: Extract Links
type: docs
weight: 30
url: /java/extract-links/
description: Extract links from PDF with Java. This topic explain you how to extract links using AnnotationSelector class. 
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Extracting links in a PDF file using Aspose.PDF for Java
Abstract: The Extract Links section of the Aspose.PDF for Java documentation provides guidelines on retrieving hyperlinks from PDF documents programmatically. It explains how to identify and extract all links embedded within a PDF, including their associated URLs, destinations, and properties. The documentation also demonstrates how to process link annotations and navigate through different link types. With practical code examples and step-by-step instructions, developers can efficiently automate link extraction in their Java applications for tasks such as data analysis, content validation, and hyperlink management.
SoftwareApplication: java    
---

## Extract Links from the PDF File

Links are represented as annotations in a PDF file, so to extract links, extract all the [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) objects.

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object.
1. Get the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) you want to extract links from.
1. Use the [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) class to extract all the [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) objects from the specified page.
1. Pass the [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) object to the Page object's Accept method.
1. Get all the selected link annotations into an IList object using the [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) object's [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) method.

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
