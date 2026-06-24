---
title: Replace Image in Existing PDF File using Java
linktitle: Replace Image
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: Learn how to replace embedded images in existing PDF files in Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Replace images in existing PDF files with Java
Abstract: This article shows how to replace images in PDF documents using Aspose.PDF for Java. It covers replacing an image by its resource index and replacing the first matched image placement found with ImagePlacementAbsorber.
---
Use either the page image collection or placement-based search depending on how precisely you need to target the image.

## Replace an image by resource index

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Access the image resources on the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Replace the target image resource with the new image file.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## Replace an image using `ImagePlacementAbsorber`

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create an [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) and visit the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Get the target [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) and replace it with the new image stream.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImageWithAbsorber(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        if (absorber.getImagePlacements().size() > 0) {
            ImagePlacement imagePlacement = absorber.getImagePlacements().get_Item(1);
            try (InputStream imageStream = Files.newInputStream(imageFile)) {
                imagePlacement.replace(imageStream);
            }
        }

        document.save(outputFile.toString());
    }
}
```
