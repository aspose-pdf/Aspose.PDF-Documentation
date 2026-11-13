---
title: Java에서 PDF 머리글 및 바닥글 추가
linktitle: 머리글 및 바닥글 추가
type: docs
weight: 70
url: /ko/java/artifacts-header-footer/
description: 스타일이 지정된 머리글 및 바닥글 아티팩트를 생성하고 Java에서 PDF 페이지에 추가합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 머리글 및 바닥글 추가
Abstract: 스타일이 지정된 머리글 및 바닥글 아티팩트를 생성하고 Java에서 PDF 페이지에 추가합니다.
---
머리글 및 바닥글 아티팩트는 반복 레이블, 페이지 식별자 및 레이아웃 프레이밍에 일반적으로 사용되는 비콘텐츠 페이지 매김 요소입니다.

## 헤더 아티팩트 만들기

일관된 텍스트 스타일링과 정렬을 가진 재사용 가능한 헤더 아티팩트가 필요할 때 이 도우미를 사용하세요.

1. [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/) 개체를 만드세요.
1. 텍스트, 글꼴 설정 및 전경 색을 설정하세요.
1. 수평 정렬을 구성하고 아티팩트를 반환하세요.

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

## 푸터 아티팩트 생성

이 도우미는 헤더 아티팩트와 동일한 스타일 패턴을 가진 재사용 가능한 푸터 아티팩트를 생성합니다.

1. [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/) 개체를 만드세요.
1. 텍스트, 텍스트 상태 및 전경 색상을 설정하세요.
1. 정렬을 구성하고 아티팩트를 반환하세요.

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

## 헤더 아티팩트를 추가합니다.

페이지가 재사용 가능한 헤더 아티팩트를 표시해야 할 때 이 예제를 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. 도우미 메서드를 통해 머리글 아티팩트를 생성하세요.
1. 아티팩트를 페이지에 추가하고 출력 파일을 저장하세요.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## 푸터 아티팩트 추가

페이지에 재사용 가능한 서식이 적용된 푸터 아티팩트를 표시해야 할 경우 이 예제를 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. 도우미 메서드를 통해 바닥글 아티팩트를 생성하세요.
1. 아티팩트를 페이지에 추가하고 출력 파일을 저장하세요.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## 관련 항목

- [머리글 및 바닥글 제거](/pdf/ko/java/remove-headers-footers/)
- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
