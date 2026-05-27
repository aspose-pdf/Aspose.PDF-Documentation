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

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## Get page count without saving

`getPageCountWithoutSaving` creates many paragraphs on a new page, calls `document.processParagraphs()`, and then reads the page count from the in-memory document.

## Get page properties and box values

`getPageProperties` prints the dimensions and coordinates of the `ArtBox`, `BleedBox`, `CropBox`, `MediaBox`, `TrimBox`, and `Rect`, then reads the page number and rotation.

## Get page color type

`getPageColorType` loops through all pages and reports whether each page is black and white, grayscale, RGB, or undefined.
