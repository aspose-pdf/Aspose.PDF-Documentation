---
title: Change PDF Page Size in Java
linktitle: Changing Page Size
type: docs
weight: 40
url: /java/change-page-size/
description: Learn how to read and change PDF page dimensions in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read and update page dimensions and boxes with Java
Abstract: This article demonstrates how to read and modify PDF page dimensions using Aspose.PDF for Java. It covers getting page size, measuring page size with rotation applied, and updating the first page to a new size while printing the box dimensions before and after the change.
---
Aspose.PDF for Java can both report page dimensions and update them.

## Change the page size

Use this example when you need to resize an existing page and inspect the page boxes before and after the change.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Get the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) and print its current box values.
1. Set the new page size and save the document.

```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## Get the page size

Use this example when you need to read the visible dimensions of a page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Get the page rectangle with rotation handling enabled.
1. Output the page width and height.

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## Get the page size with rotation applied

Use this example when you need to compare page dimensions before and after accounting for rotation.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Rotate the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Read the page rectangle with and without rotation handling and output both values.

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```
