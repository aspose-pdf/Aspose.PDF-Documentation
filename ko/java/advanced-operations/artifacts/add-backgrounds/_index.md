---
title: Java에서 PDF 배경 추가
linktitle: 배경 추가
type: docs
weight: 20
url: /ko/java/add-backgrounds/
description: Java에서 PDF 페이지에 이미지 및 단색 배경을 추가하고 이미지 투명도를 조정합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 배경 추가
Abstract: Java에서 PDF 페이지에 이미지 및 단색 배경을 추가하고 이미지 투명도를 조정합니다.
---
배경 아티팩트를 사용하면 논리적 문서 텍스트를 변경하지 않고 주요 페이지 콘텐츠 뒤에 내용이 아닌 시각 요소를 배치할 수 있습니다.

## PDF에 배경 이미지를 추가합니다.

페이지가 이미지를 배경 아티팩트로 표시해야 할 때 이 예제를 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 열고 이미지 스트림을 여세요.
1. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) 개체를 만들고 이미지 스트림을 지정하세요.
1. 아티팩트를 대상 페이지에 추가하고 출력 PDF를 저장하세요.

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## 불투명도가 있는 배경 이미지 추가

이 예제는 페이지 내용 뒤에 반투명 배경 이미지를 배치합니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 열고 이미지 스트림을 여세요.
1. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) 개체를 만들고 이미지와 불투명도를 설정하세요.
1. 아티팩트를 페이지에 추가하고 문서를 저장하세요.

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## PDF에 배경 색을 추가합니다

페이지가 이미지 대신 단색 배경 색을 사용해야 할 때 이 예제를 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) 개체를 만들고 배경색을 설정하세요.
1. 아티팩트를 페이지에 추가하고 출력 파일을 저장하세요.

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## 관련 항목

- [배경 제거](/pdf/ko/java/remove-backgrounds/)
- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
