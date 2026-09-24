---
title: PDF를 Java의 PowerPoint로 변환
linktitle: PDF를 파워포인트로 변환
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
description: 편집 가능한 PPTX 슬라이드, 이미지 기반 슬라이드 및 사용자 정의 이미지 해상도를 포함하여 Aspose.PDF를 사용하여 PDF 파일을 Java의 PowerPoint로 변환하는 방법을 알아보세요.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF를 PowerPoint로 변환하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일을 PowerPoint 프레젠테이션으로 변환하는 방법을 설명합니다. `PptxSaveOptions`을 통한 표준 PPTX 변환, 이미지 슬라이드 출력 및 이미지 해상도 제어를 다룹니다.
---
Aspose.PDF for Java는 슬라이드 렌더링 옵션을 사용하여 PDF 페이지를 편집 가능한 PowerPoint 프레젠테이션으로 내보내는 것을 지원합니다. PDF 페이지가 PowerPoint 슬라이드에 매핑되는 방식을 제어하려면 [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/)을 사용하세요.


## 
PDF를 PPTX로 변환



PDF 문서를 표준 PowerPoint 프리젠테이션으로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
편집 가능한 PowerPoint 내보내기를 위한 기본값 [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/)을 만듭니다.
1. `document.save(outputFile.toString(), saveOptions)`으로 전화하면 PDF 페이지가 `.pptx` 프리젠테이션으로 직렬화됩니다.

1. 
변환된 PPTX 파일을 저장합니다.


```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
슬라이드를 이미지로 사용하여 PDF를 PPTX로 변환



각 PDF 페이지가 이미지 기반 PowerPoint 슬라이드가 되어야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.
1. [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/)을 만들고 `setSlidesAsImages(true)`을 활성화합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 각 PDF 페이지가 프레젠테이션에서 이미지 기반 슬라이드로 렌더링됩니다.

1. 
생성된 PPTX 파일을 저장합니다.


```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setSlidesAsImages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
사용자 정의 이미지 해상도를 사용하여 PDF를 PPTX로 변환



PDF를 PPTX로 내보내는 동안 슬라이드 이미지 품질을 제어해야 하는 경우 이 예를 사용하십시오.

1. [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
더 높은 슬라이드 이미지 충실도를 위해 [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/)을 만들고 `setImageResolution(300)`을 설정하세요.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 래스터화된 슬라이드 콘텐츠가 요청된 해상도로 생성됩니다.

1. 
출력 프레젠테이션을 저장합니다.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setImageResolution(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
