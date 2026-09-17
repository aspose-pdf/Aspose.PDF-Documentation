---
title: 스탬프 수업
linktitle: 스탬프 수업
type: docs
weight: 150
url: /java/stamp-class/
description: Java에서 Stamp 클래스를 사용하여 PDF 문서에 이미지, PDF 및 텍스트 기반 스탬프를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF 문서에 이미지, PDF 및 텍스트 스탬프 추가
Abstract: 이 섹션에서는 PDF 문서에 재사용 가능한 스탬프 콘텐츠를 추가하기 위해 Java용 Aspose.PDF의 PdfFileStamp와 함께 Stamp 클래스를 사용하는 방법을 설명합니다. 현재 Java 예제에는 이미지 스탬프, PDF 페이지 스탬프, 사용자 정의 TextState가 있는 텍스트 스탬프, 페이지별 스탬프, 불투명도, 크기 및 회전 설정이 있는 배경 이미지 스탬프가 포함됩니다.
---
Java `StampExamples` 클래스는 Facades API를 통해 사용할 수 있는 주요 스탬프 작성 작업 흐름을 보여줍니다.


## 
이미지 스탬프 추가



이미지 파일을 PDF에 스탬프로 배치해야 하는 경우 이 작업 과정을 사용하세요.


### 
단계


1. 
`PdfFileStamp` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.
2. `Stamp` 객체를 생성하고 이를 이미지 파일에 바인딩합니다.

3. 
스탬프 식별자와 배치 원점을 설정합니다.

4. 
문서에 스탬프를 추가합니다.

5. 
결과를 저장하고 Facade 객체를 닫습니다.


### 
자바 예

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## PDF 페이지를 스탬프로 추가



다른 PDF 페이지의 컨텐츠를 스탬프 컨텐츠로 재사용해야 하는 경우 이 작업 과정을 사용하십시오.


### 
단계


1. 
`PdfFileStamp` 인스턴스를 생성하고 대상 PDF를 바인딩합니다.

2. 
`Stamp` 개체를 만듭니다.
3. 다른 PDF 파일의 특정 페이지에 스탬프를 바인딩합니다.

4. 
배치할 대상 페이지 번호와 출처를 설정합니다.

5. 
스탬프를 추가하고 출력을 저장한 다음 Facade 객체를 닫습니다.


### 
자바 예


```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 
TextState를 사용하여 텍스트 스탬프 추가

스탬프에 이미지가 아닌 스타일이 지정된 텍스트가 포함되어야 하는 경우 이 작업 흐름을 사용하십시오.


### 
단계


1. 
`PdfFileStamp` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.

2. 
`Stamp` 개체를 만듭니다.

3. 
`FormattedText` 로고와 사용자 정의 `TextState`을 스탬프에 바인딩합니다.
4. 스탬프 원점과 회전을 설정합니다.

5. 
스탬프를 추가하고 출력을 저장한 다음 Facade 객체를 닫습니다.


### 
자바 예


```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 
특정 페이지에 스탬프 추가



스탬프가 전체 문서가 아닌 선택한 페이지에만 나타나야 하는 경우 이 작업 흐름을 사용하십시오.

### 단계


1. 
`PdfFileStamp` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.

2. 
`Stamp` 객체를 생성하고 이를 이미지 파일에 바인딩합니다.

3. 
대상 페이지 목록, 원본, 이미지 크기를 설정합니다.

4. 
문서에 스탬프를 추가합니다.
5. 결과를 저장하고 Facade 객체를 닫습니다.


### 
자바 예


```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 
배경 이미지 스탬프 추가



불투명도와 회전이 제어된 페이지 콘텐츠 뒤에 스탬프를 표시해야 하는 경우 이 작업 흐름을 사용하세요.


### 
단계

1. `PdfFileStamp` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.

2. 
`Stamp` 객체를 생성하고 이를 이미지 파일에 바인딩합니다.

3. 
스탬프를 배경 콘텐츠로 표시합니다.

4. 
불투명도, 품질, 회전, 크기 및 원점을 구성합니다.

5. 
스탬프를 추가하고 출력을 저장한 다음 Facade 객체를 닫습니다.

### 자바 예

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
