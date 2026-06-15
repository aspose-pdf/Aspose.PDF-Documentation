---
title: Use FloatingBox for PDF Layout in Java
linktitle: Using FloatingBox
type: docs
weight: 30
url: /java/floating-box/
description: Learn how to use FloatingBox for text layout, multi-column content, and precise positioning in PDF documents with Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Create and position styled FloatingBox containers in PDF with Java
Abstract: This article explains how to use FloatingBox in Aspose.PDF for Java. It covers placing text in bordered floating containers, creating repeating multi-column layouts, using background colors, absolute offsets, and horizontal or vertical alignment options.
---
Aspose.PDF for Java uses `FloatingBox` to build reusable text containers and column-based layouts.

## Create and add a floating box

Use this example when text should be placed inside a bordered floating container.

1. Create a new PDF document and add a page.
1. Create a `FloatingBox`, set its size and border, and add text content.
1. Add the box to the page and save the document.

```java
public static void createAndAddFloatingBox(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           FloatingBox box = new FloatingBox(400, 30);
           box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
           box.setNeedRepeating(false);
           String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
           box.getParagraphs().add(new TextFragment(phrase));

           page.getParagraphs().add(box);
           document.save(outputFile.toString());
       }
   }
```

## Create a repeating multi-column layout

Use this example when long text should flow across multiple columns inside one floating box.

1. Create a page and configure margins.
1. Calculate the column widths and configure the `FloatingBox` column settings.
1. Add repeated text fragments to the box and save the document.

```java
public static void multiColumnLayout(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            box.getParagraphs().add(new TextFragment(phrase));
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Start each fragment as the first item in a column

Use this example when each inserted fragment should begin a fresh column flow segment.

1. Create a page and configure the multi-column `FloatingBox`.
1. Create text fragments and mark them with `setFirstParagraphInColumn(true)`.
1. Add the box to the page and save the PDF.

```java
public static void multiColumnLayout2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            TextFragment text = new TextFragment(phrase);
            text.setFirstParagraphInColumn(true);
            box.getParagraphs().add(text);
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Add a floating box with background color

Use this example when the floating container should have a visible background fill.

1. Create a new PDF document and add a page.
1. Create a `FloatingBox`, set its background color, and add text.
1. Place the box on the page and save the document.

```java
public static void backgroundSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBackgroundColor(Color.getLightGreen());
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("text example"));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Position a floating box with absolute offsets

Use this example when the floating box must appear at an exact offset on the page.

1. Create a page and prepare the surrounding text content.
1. Create a `FloatingBox`, set absolute positioning, and assign top and left offsets.
1. Add the content to the page and save the document.

```java
public static void offsetSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setTop(45);
        box.setLeft(15);
        box.setPositioningMode(ParagraphPositioningMode.Absolute);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.getParagraphs().add(new TextFragment("text example 1"));

        page.getParagraphs().add(new TextFragment("text example 2"));
        page.getParagraphs().add(box);
        page.getParagraphs().add(new TextFragment("text example 3"));

        document.save(outputFile.toString());
    }
}
```

## Align text inside floating boxes

Use this example when floating boxes should demonstrate different vertical alignments with the same horizontal alignment.

1. Create a new PDF document and add a page.
1. Create multiple `FloatingBox` objects with different alignment settings.
1. Add them to the page and save the result.

```java
public static void alignTextToFloat(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox floatBox = new FloatingBox(100, 100);
        floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
        floatBox.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
        floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox);

        FloatingBox floatBox2 = new FloatingBox(100, 100);
        floatBox2.setVerticalAlignment(VerticalAlignment.Center);
        floatBox2.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox2.getParagraphs().add(new TextFragment("FloatingBox_center"));
        floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox2);

        FloatingBox floatBox3 = new FloatingBox(100, 100);
        floatBox3.setVerticalAlignment(VerticalAlignment.Top);
        floatBox3.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox3.getParagraphs().add(new TextFragment("FloatingBox_top"));
        floatBox3.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox3);

        document.save(outputFile.toString());
    }
}
```
