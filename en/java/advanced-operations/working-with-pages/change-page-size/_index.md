---
title: Change PDF Page Size in Java
linktitle: Changing Page Size
type: docs
weight: 40
url: /java/change-page-size/
description: Learn how to read and change PDF page dimensions in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read and update page dimensions and boxes with Java
Abstract: This article demonstrates how to read and modify PDF page dimensions using Aspose.PDF for Java. It covers getting page size, measuring page size with rotation applied, and updating the first page to a new size while printing the box dimensions before and after the change.
---
## Set a page size

1. Load the PDF document or object that will be updated.
2. Apply the settings shown in the example to set a page size.
3. Save the document if the change should persist.

```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setPageSize(597.6, 842.4);
        document.save(outputFile.toString());
    }
}
```


