---
title: Java를 사용하여 PDF 파일에서 이미지 추출
linktitle: 이미지 추출
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: Java에서 PDF 파일에 포함된 이미지를 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에서 이미지 추출
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 이미지를 추출하는 방법을 보여줍니다. 페이지에서 특정 이미지 리소스를 저장하고 선택한 직사각형 영역 내에 있는 이미지를 내보내는 방법을 다룹니다.
---

Aspose.PDF for Java는 직접적인 이미지 리소스 추출 및 배치 기반 필터링을 지원합니다.


## 
인덱스별로 삽입된 이미지 추출



PDF 페이지에서 특정 이미지 리소스를 저장해야 할 때 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 리소스에서 대상 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/)에 액세스합니다.

1. 
이미지 스트림을 출력 파일에 저장합니다.


```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## 
특정 페이지 영역에서 이미지 추출



선택한 직사각형 내부에 배치된 이미지만 내보내야 하는 경우 이 예를 사용하십시오.


1. 
대상 [사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 정의하고 소스 PDF를 엽니다.

1. 
[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/)를 사용하여 페이지의 이미지 배치를 검사하세요.

1. 
선택한 영역 내에 위치가 맞는 이미지만 저장합니다.

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
