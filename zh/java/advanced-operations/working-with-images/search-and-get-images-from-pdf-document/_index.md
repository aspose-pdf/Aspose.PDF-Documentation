---
title: 获取和搜索 PDF 中的图像
linktitle: 获取和搜索图像
type: docs
weight: 40
url: /java/search-and-get-images-from-pdf-document/
description: 了解如何使用 Java 搜索和检查 PDF 文档中的图像。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 搜索和检查 PDF 文件中的图像
Abstract: 本文介绍如何使用 Aspose.PDF for Java 搜索和检查 PDF 文档中的图像。它涵盖读取图像放置几何形状、检测颜色类型、提取替代文本以及从页面运算符计算有效图像分辨率。
---
Aspose.PDF for Java 可以检查图像放置信息以及较低级别的绘图数据。

## 获取图像放置参数

当您需要检查页面上的图像几何形状和有效分辨率时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) 收集图像展示位置。
1. 输出每个放置图像的尺寸、坐标和分辨率。

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

## 检测图像颜色类型

当您需要计算 PDF 页面中的灰度和 RGB 图像时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) 迭代页面图像。
1. 读取每个图像的 [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/) 并输出总数。

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

## 提取图像替代文本

当您需要检查与页面图像关联的辅助功能文本时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) 收集图像展示位置。
1. 读取每个图像的替代文本并输出结果。

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

## 从页面算子计算图像信息

当您需要从低级页面内容运算符获取有效图像大小和分辨率时，请使用此示例。

1. 打开源PDF[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)并收集图像资源名称。
1. 在迭代页面运算符时跟踪图形状态。
1. 解析每个图像绘制操作并计算其有效尺寸和分辨率。

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
