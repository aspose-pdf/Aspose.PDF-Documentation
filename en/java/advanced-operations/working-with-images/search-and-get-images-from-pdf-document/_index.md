---
title: Get and Search Images in PDF
linktitle: Get and Search Images
type: docs
weight: 40
url: /java/search-and-get-images-from-pdf-document/
description: Learn how to search for and inspect images in PDF documents in Java.
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: Search and inspect images in PDF files with Java
Abstract: This article shows how to search for and inspect images in PDF documents using Aspose.PDF for Java. It covers reading image placement geometry, detecting color type, extracting alternative text, and calculating effective image resolution from page operators.
---
Aspose.PDF for Java can inspect image placement information as well as lower-level drawing data.

## Extract image placement parameters

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create an [ImagePlacementAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/imageplacementabsorber/) and visit the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Inspect each [ImagePlacement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/imageplacement/) and read the returned geometry and resolution values.

```java
public static void extractImageParams(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("image width: " + imagePlacement.getRectangle().getWidth());
            System.out.println("image height: " + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX: " + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY: " + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution: " + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution: " + imagePlacement.getResolution().getY());
        }
    }
}
```
