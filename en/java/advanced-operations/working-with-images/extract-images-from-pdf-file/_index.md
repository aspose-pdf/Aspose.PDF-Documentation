---
title: Extract Images from PDF File using Java
linktitle: Extract Images
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: Learn how to extract embedded images from PDF files in Java.
lastmod: "2026-06-04"
TechArticle: true
AlternativeHeadline: Extract images from PDF files with Java
Abstract: This article shows how to extract images from PDF documents using Aspose.PDF for Java. It covers saving a specific image resource from a page and exporting images that fall inside a selected rectangular region.
---
Aspose.PDF for Java supports direct image-resource extraction and placement-based filtering.

## Extract a single embedded image

1. Open the source PDF document.
1. Access the image resources on the target page.
1. Save the updated PDF document.
1. Write the extracted output or inspect the returned values.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## Extract images from a specific region

1. Open the source PDF document.
1. Create an ImagePlacementAbsorber and visit the target page.
1. Save the updated PDF document.
1. Write the extracted output or inspect the returned values.

```java
public static void extractImageFromSpecificRegion(Path inputFile, Path outputFile) throws Exception {
    Rectangle rectangle = new Rectangle(0, 0, 590, 590, true);

    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        int index = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            Point point1 = new Point(imagePlacement.getRectangle().getLLX(), imagePlacement.getRectangle().getLLY());
            Point point2 = new Point(imagePlacement.getRectangle().getURX(), imagePlacement.getRectangle().getURX());
            if (rectangle.contains(point1, true) && rectangle.contains(point2, true)) {
                Path indexedOutputFile = Path.of(outputFile.toString().replace("index", String.valueOf(index)));
                try (OutputStream outputImage = Files.newOutputStream(indexedOutputFile)) {
                    imagePlacement.getImage().save(outputImage);
                }
                index++;
            }
        }
    }
}
```
