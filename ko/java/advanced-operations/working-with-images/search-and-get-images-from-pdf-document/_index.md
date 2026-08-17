---
title: PDF에서 이미지 가져오기 및 검색
linktitle: 이미지 가져오기 및 검색
type: docs
weight: 40
url: /java/search-and-get-images-from-pdf-document/
description: Java에서 PDF 문서의 이미지를 검색하고 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일의 이미지 검색 및 검사
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 이미지를 검색하고 검사하는 방법을 보여줍니다. 이미지 배치 기하학 읽기, 색상 유형 감지, 대체 텍스트 추출, 페이지 운영자로부터 효과적인 이미지 해상도 계산 등을 다룹니다.
---

Aspose.PDF for Java는 이미지 배치 정보는 물론 하위 수준의 도면 데이터도 검사할 수 있습니다.


## 
이미지 배치 매개변수 가져오기



페이지의 이미지 구조와 유효 해상도를 검사해야 할 때 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/)를 사용하여 이미지 배치를 수집하세요.

1. 
배치된 각 이미지의 크기, 좌표, 해상도를 출력합니다.


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

## 
이미지 색상 유형 감지



PDF 페이지에서 회색조 및 RGB 이미지 수를 계산해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 이미지를 반복하려면 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/)를 사용하세요.

1. 
각 이미지의 [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/)을 읽어서 총합을 출력합니다.


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

## 
이미지 대체 텍스트 추출



페이지 이미지와 관련된 접근성 텍스트를 검사해야 할 때 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/)를 사용하여 이미지 배치를 수집하세요.

1. 
각 이미지의 대체 텍스트를 읽고 결과를 출력합니다.


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

## 
페이지 운영자로부터 이미지 정보 계산



낮은 수준의 페이지 콘텐츠 연산자에서 효과적인 이미지 크기와 해상도를 파생해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 이미지 리소스 이름을 수집합니다.

1. 
페이지 연산자를 반복하면서 그래픽 상태를 추적합니다.

1. 
각 이미지 그리기 작업을 해결하고 유효 크기와 해상도를 계산합니다.

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
