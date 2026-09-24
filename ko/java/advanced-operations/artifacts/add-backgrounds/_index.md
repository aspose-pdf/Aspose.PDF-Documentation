---
title: Java에서 PDF 배경 추가
linktitle: 배경 추가
type: docs
weight: 20
url: /java/add-backgrounds/
description: Aspose.PDF와 함께 `BackgroundArtifact`을 사용하여 Java에서 PDF 페이지에 배경 이미지 또는 배경색을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에 배경을 추가하는 방법
Abstract: 이 문서에서는 Aspose.PDF를 사용하여 Java에서 PDF 페이지 배경을 추가하거나 제거하는 방법을 설명합니다. 배경 이미지 추가, 이미지 불투명도 조정, 배경색 적용 및 페이지에서 배경 아티팩트 제거를 다룹니다.
---
배경 아티팩트를 사용하면 논리적 문서 텍스트를 변경하지 않고도 기본 페이지 콘텐츠 뒤에 콘텐츠가 아닌 시각적 요소를 배치할 수 있습니다.


## 
PDF에 배경 이미지 추가



페이지에서 이미지를 배경 아티팩트로 표시해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)와 이미지 입력 스트림을 엽니다.

1. 
[BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/)를 생성하고 이미지 스트림을 할당합니다.
1. 대상 페이지에 아티팩트를 추가하고 출력 PDF를 저장합니다.


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

## 
불투명도가 있는 배경 이미지 추가



이 예에서는 페이지 콘텐츠 뒤에 반투명 배경 이미지를 배치합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 및 이미지 스트림을 엽니다.

1. 
[BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/)를 생성하고 이미지를 할당한 후 불투명도를 설정하세요.
1. 페이지에 아티팩트를 추가하고 문서를 저장합니다.


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

## 
PDF에 배경색 추가



페이지에서 이미지 대신 단색 배경색을 사용해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/)를 생성하고 배경색을 지정합니다.
1. 페이지에 아티팩트를 추가하고 출력 파일을 저장합니다.


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

## 
배경 아티팩트 제거



기존 배경 아티팩트를 페이지에서 삭제해야 하는 경우 이 접근 방식을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 아티팩트 컬렉션을 역순으로 반복합니다.
1. 유형이 페이지 매김이고 하위 유형이 배경인 이슈를 삭제한 후 문서를 저장합니다.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
