---
title: Java를 사용하여 기존 PDF 파일의 이미지 바꾸기
linktitle: 이미지 교체
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: Java에서 기존 PDF 파일에 포함된 이미지를 바꾸는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 기존 PDF 파일의 이미지를 Java로 교체
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서의 이미지를 바꾸는 방법을 보여줍니다. 리소스 인덱스로 이미지를 교체하고 ImagePlacementAbsorber로 찾은 첫 번째 일치 이미지 배치를 교체하는 방법을 다룹니다.
---

이미지를 얼마나 정확하게 타겟팅해야 하는지에 따라 페이지 이미지 컬렉션 또는 배치 기반 검색을 사용하세요.


## 
리소스 인덱스로 이미지 교체


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)의 이미지 리소스에 접근합니다.

1. 
대상 이미지 리소스를 새 이미지 파일로 바꿉니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## 
`ImagePlacementAbsorber`을 사용하여 이미지 교체


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/)를 만들고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 방문하세요.

1. 
대상 [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/)을 가져와 새 이미지 스트림으로 바꿉니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

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
