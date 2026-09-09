---
title: Java에서 PDF에 이미지 스탬프 추가
linktitle: PDF 파일의 이미지 스탬프
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Java에서 PDF 페이지에 이미지 스탬프를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 페이지에 이미지 스탬프 및 이미지 배경 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일에 이미지 스탬프를 추가하는 방법을 설명합니다. 위치 지정, 회전, 불투명도 및 품질 관리 기능을 갖춘 이미지 스탬프를 다루고 이미지를 플로팅 박스의 배경으로 사용합니다.
---
Java용 Aspose.PDF는 이미지 스탬프를 오버레이 및 이미지 기반 레이아웃 요소로 지원합니다.


## 
이미지 스탬프 추가



페이지에 맞춤 배치 및 불투명도가 포함된 이미지 스탬프를 표시해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/)를 생성하고 모양을 구성합니다.
1. 페이지에 스탬프를 추가하고 문서를 저장하세요.


```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 
품질 관리를 통해 이미지 스탬프 추가



이미지 스탬프의 렌더링 품질을 조정해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/)를 생성하고 품질 값을 설정하세요.
1. 페이지에 스탬프를 추가하고 결과를 저장하세요.


```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 
이미지를 부동 상자 배경으로 사용



이미지가 스타일이 지정된 레이아웃 컨테이너의 배경 역할을 해야 하는 경우 이 예제를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 대상 페이지에 접속합니다.

1. 
텍스트 및 테두리 설정을 사용하여 [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/)를 만듭니다.
1. 배경 이미지를 설정하고 페이지에 상자를 추가한 후 문서를 저장합니다.

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```
