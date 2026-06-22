---
title: Work with PDF Layers using Java
linktitle: Work with PDF layers
type: docs
weight: 50
url: /java/working-with-pdf-layers/
description: Learn how to add, lock, extract, flatten, and merge PDF layers in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage PDF layers with Java
Abstract: This article explains how to work with PDF layers, also known as Optional Content Groups, using Aspose.PDF for Java. Learn how to add layers to a page, lock an existing layer, extract layer content to files or streams, flatten layered content, and merge layers into one.
---
Aspose.PDF for Java exposes PDF layers through the `Layer` API on each page. You can create optional content groups, modify their behavior, and export or flatten their content when needed.

## Add layers to a PDF page

1. Create a new PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) to the document.
1. Create and configure the required [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) objects on the page.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLayers(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Layer layer = new Layer("oc1", "Red Line");
        layer.getContents().add(new SetRGBColorStroke(1, 0, 0));
        layer.getContents().add(new MoveTo(500, 700));
        layer.getContents().add(new LineTo(400, 700));
        layer.getContents().add(new Stroke());
        page.getLayers().add(layer);

        document.save(outputFile.toString());
    }
}
```

The full example creates three separate layers with red, green, and blue line content.

## Lock a layer

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Access the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and get its [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) collection.
1. Lock the target [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void lockLayer(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        if (!page.getLayers().isEmpty()) {
            Layer layer = page.getLayers().getFirst();
            layer.lock();
            document.save(outputFile.toString());
        }
    }
}
```
