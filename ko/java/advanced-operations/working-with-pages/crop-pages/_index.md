---
title: Java에서 PDF 페이지 자르기
linktitle: PDF 페이지 자르기
type: docs
weight: 70
url: /java/crop-pages/
description: Java에서 PDF 페이지를 자르고 자르기, 다듬기, 도련 및 미디어 상자를 조정하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일의 페이지 자르기 및 페이지 상자 조정
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 페이지를 자르는 방법을 설명합니다. 자르기, 다듬기, 아트 및 도련 상자에 새 자르기 직사각형을 할당하고 감지된 이미지 내용을 기반으로 페이지를 자동으로 자르는 방법을 다룹니다.
---

Aspose.PDF for Java를 사용하면 명시적인 상자 좌표나 감지된 콘텐츠를 기준으로 페이지를 자를 수 있습니다.


## 
페이지 상자를 설정하여 페이지 자르기



기본 페이지 상자에 동일한 자르기 영역을 적용해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
새 자르기 [직사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 만듭니다.

1. 
자르기 관련 페이지 상자에 사각형을 적용하고 문서를 저장합니다.


```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## 
감지된 콘텐츠로 페이지 자르기



페이지에서 처음 감지된 이미지에서 자르기 영역을 파생해야 하는 경우 이 예를 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/)를 사용하여 이미지 배치를 감지하세요.

1. 
이미지 직사각형이 있으면 자르기 상자를 이미지 직사각형으로 설정한 다음 문서를 저장합니다.

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
