---
title: Get and Search Images in PDF
linktitle: Get and Search Images
type: docs
weight: 40
url: /java/search-and-get-images-from-pdf-document/
description: Learn how to search for and inspect images in PDF documents in Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Search and inspect images in PDF files with Java
Abstract: This article shows how to search for and inspect images in PDF documents using Aspose.PDF for Java. It covers reading image placement geometry, detecting color type, extracting alternative text, and calculating effective image resolution from page operators.
---
Aspose.PDF for Java can inspect image placement information as well as lower-level drawing data.

## Get image placement parameters

Use this example when you need to inspect image geometry and effective resolution on a page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Use [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) to collect image placements.
1. Output the size, coordinates, and resolution for each placed image.

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

## Detect image color types

Use this example when you need to count grayscale and RGB images in a PDF page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Use [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) to iterate over page images.
1. Read the [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/) of each image and output the totals.

```java
public static void extractImageTypesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        int grayscaled = 0;
        int rgb = 0;

        document.getPages().get_Item(1).accept(absorber);

        System.out.println("--------------------------------");
        System.out.println("Total Images = " + absorber.getImagePlacements().size());

        int imageCounter = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            ColorType colorType = imagePlacement.getImage().getColorType();
            if (colorType == ColorType.Grayscale) {
                grayscaled++;
                System.out.println("Image " + imageCounter + " is Grayscale...");
            } else if (colorType == ColorType.Rgb) {
                rgb++;
                System.out.println("Image " + imageCounter + " is RGB...");
            }
            imageCounter++;
        }

        System.out.println("--------------------------------");
        System.out.println("Grayscale Images = " + grayscaled);
        System.out.println("RGB Images = " + rgb);
    }
}
```

## Extract image alternative text

Use this example when you need to inspect accessibility text associated with page images.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Use [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) to collect image placements.
1. Read the alternative text for each image and output the result.

```java
public static void extractImageAltText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("Name in collection: " + imagePlacement.getImage().getNameInCollection());
            List<String> lines = imagePlacement.getImage().getAlternativeText(document.getPages().get_Item(1));
            if (!lines.isEmpty()) {
                System.out.println("Alt Text: " + lines.get(0));
            } else {
                System.out.println("Alt Text: ");
            }
        }
    }
}
```

## Calculate image information from page operators

Use this example when you need to derive effective image size and resolution from low-level page content operators.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and collect image resource names.
1. Track the graphics state while iterating through page operators.
1. Resolve each image draw operation and calculate its effective dimensions and resolution.

```java
public static void extractImageInformationFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int defaultResolution = 72;
        List<Matrix> graphicsState = new ArrayList<>();
        List<String> imageNames = Arrays.asList(document.getPages().get_Item(1).getResources().getImages().getNames());

        graphicsState.add(new Matrix(1, 0, 0, 1, 0, 0));

        for (Operator operator : document.getPages().get_Item(1).getContents()) {
            if (operator instanceof GSave) {
                graphicsState.add(new Matrix(graphicsState.get(graphicsState.size() - 1)));
            } else if (operator instanceof GRestore) {
                graphicsState.remove(graphicsState.size() - 1);
            } else if (operator instanceof ConcatenateMatrix concatenateMatrix) {
                Matrix current = graphicsState.get(graphicsState.size() - 1);
                graphicsState.set(graphicsState.size() - 1, current.multiply(concatenateMatrix.getMatrix()));
            } else if (operator instanceof Do doOperator) {
                if (imageNames.contains(doOperator.getName())) {
                    Matrix lastCtm = graphicsState.get(graphicsState.size() - 1);
                    int index = imageNames.indexOf(doOperator.getName()) + 1;
                    XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(index);

                    double scaledWidth = Math.sqrt(Math.pow(lastCtm.getA(), 2) + Math.pow(lastCtm.getB(), 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCtm.getC(), 2) + Math.pow(lastCtm.getD(), 2));

                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    String info = String.format(
                            "%s image %s (%.2f:%.2f): res %.2f x %.2f",
                            inputFile,
                            doOperator.getName(),
                            scaledWidth,
                            scaledHeight,
                            resHorizontal,
                            resVertical);
                    System.out.println(info);
                }
            }
        }
    }
}
```
