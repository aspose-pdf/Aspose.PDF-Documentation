---
title: Get and Set PDF Page Properties in Java
linktitle: Getting and Setting Page Properties
type: docs
weight: 90
url: /java/get-and-set-page-properties/
description: Learn how to inspect PDF page properties such as count, boxes, rotation, and color information in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspect page count, boxes, and color type in PDF files with Java
Abstract: This article explains how to inspect page properties using Aspose.PDF for Java. It covers reading the page count, generating paragraphs and checking the resulting count before saving, printing all major page box values, and identifying the color type of each page.
---
Aspose.PDF for Java can inspect page count, page boxes, rotation, and page color type.

## Get the page count

Use this example when you need to read the total number of pages in a PDF.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Read the size of the page collection.
1. Output the total page count.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## Get the page count before saving

Use this example when you need to know how many pages generated content will produce before writing the file.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add content to a page.
1. Process the paragraphs to force layout calculation.
1. Read the resulting page count and output it.

```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## Get page box properties

Use this example when you need to inspect all major box dimensions and page rotation values.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and access the target page.
1. Collect the page box values into a map.
1. Output the dimensions and page rotation information.

```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## Get the color type of each page

Use this example when you need to identify whether pages are black and white, grayscale, or RGB.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Iterate through all pages and read each page [ColorType](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/colortype/).
1. Convert the enum value into readable text and output the result.

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```
