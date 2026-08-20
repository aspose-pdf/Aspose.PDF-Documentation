---
title: Java에서 PDF를 HTML로 변환
linktitle: PDF를 HTML 형식으로 변환
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2026-06-16"
description: 다중 페이지 출력, 외부 이미지 폴더, SVG 처리 및 계층화된 HTML 렌더링을 포함하여 Aspose.PDF를 사용하여 Java에서 PDF를 HTML로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Java에서 PDF를 HTML로 변환하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일을 HTML로 변환하는 방법을 설명합니다. 이미지 폴더, 페이지 분할, SVG 출력, 압축된 SVG 그래픽, PNG 페이지 배경, 본문 전용 마크업, 투명 텍스트 렌더링 및 문서 레이어 변환에 대한 옵션과 함께 기본 HTML 내보내기를 다룹니다.
---
Java용 Aspose.PDF는 이미지, SVG, 페이지 분할, 투명도 및 레이어 렌더링 옵션과 함께 HTML 내보내기를 지원합니다. PDF 페이지, 리소스 및 마크업이 HTML 출력에 기록되는 방식을 제어하려면 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 사용하세요.


## 
PDF를 HTML로 변환



PDF를 표준 HTML 문서로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
표준 HTML 직렬화를 위한 기본값 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 만듭니다.
1. `document.save(outputFile.toString(), saveOptions)`을 호출하면 PDF 페이지 콘텐츠가 HTML 마크업으로 내보내집니다.

1. 
생성된 HTML 출력을 저장합니다.


```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 HTML로 변환하고 이미지를 별도로 저장



HTML 내보내기 중에 추출된 이미지를 별도의 파일로 작성해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 만들고 `setSpecialFolderForAllImages(...)`을 전용 이미지 출력 디렉터리로 설정합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`을 호출하면 래스터 이미지가 인라인 전용 출력 대신 별도의 리소스 파일로 내보내집니다.

1. 
생성된 이미지 자산과 함께 HTML 출력을 저장합니다.


```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 다중 페이지 HTML로 변환



각 PDF 페이지를 HTML 출력에서 별도로 표시해야 하는 경우 이 예를 사용하십시오.

1. [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 만들고 `setSplitIntoPages(true)`을 활성화합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 각 PDF 페이지가 별도의 HTML 출력으로 작성됩니다.

1. 
생성된 HTML 파일을 저장합니다.


```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 HTML로 변환하고 SVG를 별도로 저장

벡터 콘텐츠를 별도의 SVG 리소스로 내보내야 하는 경우 이 예를 사용하세요.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 만들고 `setSpecialFolderForSvgImages(...)`을 외부 SVG 리소스 디렉터리로 설정합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 벡터 그래픽이 기본 HTML 파일 외부에 저장됩니다.

1. 
HTML 출력 및 SVG 자산을 저장합니다.

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 압축된 SVG를 사용하여 PDF를 HTML로 변환



HTML을 내보내는 동안 SVG 출력을 최적화해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 생성하고 SVG 리소스 전용 폴더를 구성합니다.

1. 
`setCompressSvgGraphicsIfAny(true)`을 활성화하면 내보내는 동안 SVG 자산이 압축됩니다.
1. `document.save(outputFile.toString(), saveOptions)`으로 전화해서 변환된 HTML 파일을 저장하세요.


```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        saveOptions.setCompressSvgGraphicsIfAny(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PNG 페이지 배경을 사용하여 PDF를 HTML로 변환



HTML 출력에서 페이지 배경을 PNG 이미지로 렌더링해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 만들고 래스터 이미지 저장 모드를 PNG 페이지 배경으로 설정합니다.
1. `document.save(outputFile.toString(), saveOptions)`을 호출하면 페이지 배경 콘텐츠가 PNG 지원 HTML 레이어로 내보내집니다.

1. 
변환된 HTML 출력을 저장합니다.


```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setRasterImagesSavingMode(
                HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 HTML 본문 내용으로만 변환



전체 HTML 문서 셸 대신 본문 마크업만 필요한 경우 이 예제를 사용하세요.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 만들고 마크업 생성 모드를 `WriteOnlyBodyContent`으로 설정합니다.

1. 
본문만 출력해야 하는 경우에도 `setSplitIntoPages(true)`을 활성화된 상태로 유지하세요.

1. 
`document.save(outputFile.toString(), saveOptions)`을 호출하고 HTML 출력을 저장합니다.


```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setHtmlMarkupGenerationMode(
                HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
투명한 텍스트 렌더링을 사용하여 PDF를 HTML로 변환



HTML 내보내기에서 투명한 텍스트를 유지해야 하는 경우 이 예를 사용하십시오.

1. [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 만들고 투명 및 그림자 텍스트 보존을 활성화합니다.

1. 
투명도 관련 텍스트 모양이 HTML 결과에 유지되도록 `document.save(outputFile.toString(), saveOptions)`을 호출하세요.

1. 
변환된 HTML 출력을 저장합니다.


```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSaveTransparentTexts(true);
        saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
문서 레이어 렌더링을 사용하여 PDF를 HTML로 변환

PDF 레이어 가시성이 HTML 결과에 반영되어야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)을 만들고 `setConvertMarkedContentToLayers(true)`을 활성화합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 표시된 PDF 콘텐츠가 HTML 레이어에 매핑됩니다.

1. 
내보낸 HTML 파일을 저장합니다.

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setConvertMarkedContentToLayers(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
