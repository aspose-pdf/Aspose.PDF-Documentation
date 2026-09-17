---
title: Java를 사용하여 PDF 머리글 및 바닥글 관리
linktitle: PDF 머리글 및 바닥글 관리
type: docs
weight: 70
url: /java/artifacts-header-footer/
description: Java용 Aspose.PDF를 사용하여 PDF 문서에서 머리글 및 바닥글 아티팩트를 추가하고 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 머리글 및 바닥글을 추가, 사용자 정의 및 제거하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서의 머리글 및 바닥글 아티팩트를 관리하는 방법을 설명합니다. 사용자 정의 텍스트 상태 및 정렬을 사용하여 재사용 가능한 `HeaderArtifact` 및 `FooterArtifact` 개체를 생성하고, 이를 페이지에 추가하고, 기존 머리글 및 바닥글 아티팩트를 삭제하는 방법을 다룹니다.
---
머리글 및 바닥글 아티팩트는 반복되는 레이블, 페이지 식별자 및 레이아웃 프레임에 일반적으로 사용되는 비콘텐츠 페이지 매김 요소입니다.


## 
헤더 아티팩트 생성



일관된 텍스트 스타일과 정렬을 갖춘 재사용 가능한 헤더 아티팩트가 필요할 때 이 도우미를 사용하세요.


1. 
[HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/)를 생성합니다.

1. 
텍스트, 글꼴 설정 및 전경색을 설정합니다.
1. 수평 정렬을 구성하고 아티팩트를 반환합니다.


```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## 
바닥글 아티팩트 생성



이 도우미는 헤더 아티팩트와 동일한 스타일 패턴을 사용하여 재사용 가능한 바닥글 아티팩트를 생성합니다.


1. 
[FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/)를 만듭니다.

1. 
텍스트, 텍스트 상태 및 전경색을 설정합니다.
1. 정렬을 구성하고 아티팩트를 반환합니다.


```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## 
헤더 아티팩트 추가



페이지에 재사용 가능한 헤더 아티팩트가 표시되어야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
도우미 메서드를 통해 헤더 아티팩트를 만듭니다.
1. 페이지에 아티팩트를 추가하고 출력 파일을 저장합니다.


```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## 
바닥글 아티팩트 추가



페이지에 재사용 가능한 형식의 바닥글 아티팩트를 표시해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
도우미 메서드를 통해 바닥글 아티팩트를 만듭니다.
1. 페이지에 아티팩트를 추가하고 출력 파일을 저장합니다.


```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## 
머리글 및 바닥글 아티팩트 삭제



기존 머리글 및 바닥글 아티팩트를 페이지에서 제거해야 하는 경우 이 접근 방식을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 아티팩트 컬렉션을 역순으로 반복합니다.
1. 하위 유형이 머리글 또는 바닥글인 페이지 매김 아티팩트를 삭제한 다음 문서를 저장하십시오.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
