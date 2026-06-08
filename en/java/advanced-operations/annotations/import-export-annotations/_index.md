---
title: Import and Export Annotations using Java
linktitle: Import and Export Annotations
type: docs
weight: 80
url: /java/import-export-annotations/
description: Learn how to copy annotations from one PDF document into another PDF document using Aspose.PDF for Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transfer PDF annotations between documents in Java.
Abstract: This article explains how to copy annotations from a source PDF and export them into a new PDF document using Aspose.PDF for Java. The workflow loads the source file, creates the destination document, adds a page, copies annotations from the first source page, and saves the result.
---
## Copy annotations from one PDF to another

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the destination [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add each [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) to the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Read or iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) items on the target page.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Enumerate the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) items on the first source page and add each one to the destination page.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
