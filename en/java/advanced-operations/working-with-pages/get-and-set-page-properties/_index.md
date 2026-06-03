---
title: Get and Set PDF Page Properties in Java
linktitle: Getting and Setting Page Properties
type: docs
weight: 90
url: /java/get-and-set-page-properties/
description: Learn how to inspect PDF page properties such as count, boxes, rotation, and color information in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspect page count, boxes, and color type in PDF files with Java
Abstract: This article explains how to inspect page properties using Aspose.PDF for Java. It covers reading the page count, generating paragraphs and checking the resulting count before saving, printing all major page box values, and identifying the color type of each page.
---
## Get the page count

1. Open the PDF document used in this example.
2. Use the Aspose.PDF API calls shown here to get the page count.
3. Read the returned values or continue with your next processing step.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```


