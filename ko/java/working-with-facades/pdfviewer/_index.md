---
title: PDFViewer 클래스
linktitle: PDFViewer 클래스
type: docs
weight: 135
url: /java/pdfviewer-class/
description: Java에서 PdfViewer 파사드를 사용하여 PDF 페이지를 디코딩하고 뷰어 관련 설정을 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 페이지를 디코딩하고 PdfViewer를 사용하여 Java에서 뷰어 데이터를 검사합니다.
Abstract: 이 섹션에서는 페이지 디코딩 및 뷰어 관련 검사 작업을 위해 Java용 Aspose.PDF에서 PdfViewer 파사드를 사용하는 방법을 설명합니다. 현재 Java 예제에서는 모든 페이지를 이미지로 렌더링하고, 특정 페이지를 디코딩하고, 페이지 수, 좌표 유형, 해상도 및 바인딩된 뷰어 설정을 검사합니다.
---

Java `PdfViewerExamples` 클래스는 Facades API를 통해 사용할 수 있는 기본 뷰어 작업 흐름을 보여줍니다.


## 
모든 PDF 페이지 디코딩



원본 PDF의 모든 페이지를 이미지로 렌더링해야 하는 경우 이 작업 흐름을 사용하세요.


### 
단계


1. 
`PdfViewer` 인스턴스를 생성하고 구성합니다.

2. 
`bindPdf`으로 소스 PDF를 바인딩합니다.

3. 
`decodeAllPages()`을 호출하여 문서를 `BufferedImage` 배열로 렌더링합니다.

4. 
디코딩된 각 페이지를 출력 이미지 파일에 저장합니다.

5. 
바인딩된 PDF 파일을 닫습니다.


### 
자바 예


```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## 
특정 PDF 페이지 디코딩



한 페이지만 이미지로 렌더링해야 하는 경우 이 워크플로우를 사용하십시오.


### 
단계


1. 
`PdfViewer` 인스턴스를 생성하고 구성합니다.

2. 
소스 PDF를 바인딩합니다.

3. 
렌더링하려는 페이지에 대해 `decodePage()`을 호출하세요.

4. 
디코딩된 페이지를 출력 이미지 파일에 저장합니다.

5. 
뷰어를 닫습니다.


### 
자바 예


```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## 
PDF 메타데이터 검사



렌더링하거나 인쇄하기 전에 뷰어 관련 문서 정보가 필요한 경우 이 워크플로우를 사용하십시오.


### 
단계


1. 
`PdfViewer` 인스턴스를 생성하고 구성합니다.

2. 
소스 PDF를 바인딩합니다.

3. 
페이지 수, 좌표 유형 및 렌더링 해상도를 읽습니다.

4. 
검색된 값을 사용하거나 인쇄합니다.

5. 
바인딩된 PDF 파일을 닫습니다.


### 
자바 예


```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## 
바운드 뷰어 설정 검사



PDF를 바인딩한 후 뷰어 동작을 확인하거나 조정해야 하는 경우 이 작업 과정을 사용하십시오.


### 
단계


1. 
`PdfViewer` 인스턴스를 생성하고 구성합니다.

2. 
소스 PDF를 바인딩합니다.

3. 
자동 크기 조정, 자동 회전, 인쇄 대화 상자 표시 등의 뷰어 옵션을 설정합니다.

4. 
활성 뷰어 설정 및 페이지 수를 읽습니다.

5. 
뷰어를 닫습니다.


### 
자바 예

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```
