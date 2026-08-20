---
title: Java로 PDF 파일 만들기
linktitle: PDF 문서 만들기
type: docs
weight: 10
url: /java/create-pdf-document/
description: Aspose.PDF를 사용하여 Java에서 PDF 파일을 만들고 검색 가능한 PDF를 작성하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일 및 검색 가능한 PDF 문서 만들기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서를 만드는 방법을 보여줍니다. 처음부터 새 PDF를 만들고 외부 OCR 엔진에서 HOCR 출력을 제공하여 이미지 기반 문서를 검색 가능한 PDF로 변환하는 방법을 다룹니다.
---
Aspose.PDF for Java는 간단한 문서 생성과 OCR 지원 검색 가능한 PDF 워크플로우를 모두 지원합니다.


## 
새 PDF 문서 만들기



처음부터 간단한 PDF 파일을 생성해야 하는 경우 이 접근 방식을 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)를 생성하여 페이지에 추가하세요.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## 
검색 가능한 PDF 만들기



`createSearchablePdf` 예제에서는 `CallBackGetHocr` 구현과 함께 `Document.convert(...)`을 사용합니다. 콜백은 소스 이미지를 임시 파일에 쓰고, `hocr` 옵션으로 Tesseract를 호출하고, 생성된 HOCR 마크업을 읽고, Aspose.PDF로 반환합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. `CallBackGetHocr` 콜백을 생성하고 소스 문서를 검색 가능한 PDF 콘텐츠로 변환합니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```

## 
문서 창 설정 가져오기



이 예를 사용하여 기존 PDF 문서에 저장된 현재 뷰어 기본 설정을 검사합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 문서에서 필요한 창과 표시 속성을 읽습니다.

1. 
검사 또는 디버깅을 위한 현재 설정을 출력합니다.


```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## 
문서 창 기본 설정 지정



이 예에서는 호환되는 뷰어에서 PDF를 열 때 PDF가 표시되는 방법을 업데이트합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 필요한 창, 레이아웃 및 페이지 모드 기본 설정을 지정합니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## 
기존 PDF에 글꼴 포함



다른 시스템에서 보다 안정적인 렌더링을 위해 문서에 필요한 글꼴을 포함해야 하는 경우 이 접근 방식을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 표준 글꼴 포함을 활성화하고 각 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에서 사용되는 글꼴을 반복합니다.

1. 
포함되지 않은 [글꼴](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 개체를 포함용으로 표시합니다.

1. 
업데이트된 문서를 저장합니다.


```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
새 PDF를 만들 때 글꼴 포함



이 예에서는 새 PDF를 만들고 처음부터 텍스트 내용에 포함된 글꼴을 할당합니다.

1. 새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
필요한 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/) 및 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/)를 만듭니다.

1. 
저장소에서 대상 [글꼴](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/)을 확인하고 포함된 것으로 표시합니다.

1. 
페이지에 텍스트 내용을 추가하고 출력 문서를 저장합니다.


```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## 
PDF 출력의 기본 글꼴 설정

저장된 문서가 출력 생성 중에 특정 글꼴로 대체되어야 하는 경우 이 패턴을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/)를 만들고 기본 글꼴 이름을 설정합니다.

1. 
구성된 저장 옵션으로 문서를 저장합니다.


```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## 
PDF에 사용된 모든 글꼴 가져오기

이 예에서는 파일을 내보내거나 업데이트하기 전에 글꼴 사용을 감사할 수 있도록 문서에서 감지된 모든 글꼴을 나열합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
문서 글꼴 유틸리티에서 반환된 글꼴을 열거합니다.

1. 
감지된 각 [글꼴](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/)의 이름을 출력합니다.


```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## 
글꼴 하위 설정을 통해 글꼴 포함 개선

문서 사용에 맞게 포함된 글꼴 데이터를 유지하면서 글꼴 페이로드를 줄이려는 경우 이 접근 방식을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
필요한 [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) 값을 사용하여 문서 글꼴 유틸리티를 통해 글꼴 하위 설정을 실행합니다.

1. 
최적화된 문서를 저장합니다.


```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## 
문서 열기 확대/축소 비율 설정

이 예에서는 PDF를 열 때 적용해야 하는 초기 확대/축소 수준을 구성합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/)을 사용하여 [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/)을 만듭니다.

1. 
작업을 문서 열기 작업으로 지정하고 결과를 저장합니다.


```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## 
문서 열기 확대/축소 비율 가져오기

이 예를 사용하여 PDF가 열린 작업에 대해 명시적인 확대/축소 수준을 이미 정의했는지 여부를 검사합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
열려 있는 작업이 [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/)이 있는 [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/)인지 확인하세요.

1. 
구성된 확대/축소 값을 출력하거나 확대/축소가 설정되지 않았음을 보고합니다.

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```
