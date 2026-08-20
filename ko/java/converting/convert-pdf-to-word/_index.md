---
title: PDF를 Java의 Word로 변환
linktitle: PDF를 Word로 변환
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-06-16"
description: 보다 쉬운 문서 편집 및 재사용을 위해 Aspose.PDF를 사용하여 Java에서 PDF 파일을 DOC 및 DOCX로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF를 Word로 변환하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일을 Microsoft Word 형식으로 변환하는 방법을 설명합니다. `DocSaveOptions`을 통한 DOC 출력, DOCX 출력, 향상된 흐름 DOCX 변환, 줄바꿈 보존, 글머리 기호 인식 및 이미지 해상도 제어를 다룹니다.
---
Aspose.PDF for Java는 다양한 인식 및 레이아웃 옵션을 사용하여 PDF 문서를 Microsoft Word 형식으로 내보낼 수 있습니다. PDF 텍스트, 목록 및 이미지가 Word 출력에 매핑되는 방식을 제어하려면 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)을 사용하세요.


## 
PDF를 DOC로 변환



PDF 문서를 기존 DOC 형식으로 내보내야 하는 경우 이 예를 사용하십시오. 코드는 `DocSaveOptions`을 생성하고, 형식을 `Doc`으로 설정하고, 옵션을 공유 저장 방법에 전달합니다.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)을 만들고 형식을 `Doc`으로 설정합니다.
1. `document.save(outputFile.toString(), saveOptions)`으로 전화하면 PDF가 Microsoft Word 바이너리 문서 형식으로 내보내집니다.

1. 
변환된 DOC 파일을 저장합니다.


```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 DOCX로 변환



PDF 문서를 DOCX 파일로 내보내야 하는 경우 이 예를 사용하십시오. DOCX는 광범위하게 지원되고 편집이 더 쉽기 때문에 대부분의 새로운 워드 프로세싱 작업 흐름에서 선호되는 형식입니다.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.
1. [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)을 만들고 형식을 `DocX`으로 설정합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 PDF 콘텐츠가 Office Open XML Word 문서로 내보내집니다.

1. 
결과 DOCX 파일을 저장합니다.


```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
향상된 흐름 인식을 통해 PDF를 DOCX로 변환



Word 내보내기에서 고정된 시각적 레이아웃 대신 흐르는 편집 가능한 콘텐츠를 선호해야 하는 경우 이 예를 사용하세요.

1. [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
`DocX` 출력을 위한 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)을 만듭니다.

1. 
`setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)`을 활성화하면 변환기가 DOCX 생성 중에 향상된 흐름 인식을 사용합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`을 호출하고 변환된 DOCX 출력을 저장합니다.


```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
줄 바꿈을 유지하면서 PDF를 DOCX로 변환

소스 PDF의 줄 끝을 Word 출력에 유지해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
`DocX` 내보내기를 위해 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)을 만듭니다.

1. 
`setAddReturnToLineEnd(true)`을 활성화하면 변환 중에 명시적인 줄 바꿈이 유지됩니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화해서 DOCX 파일을 저장하세요.

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 글머리 기호 인식 기능을 사용하여 PDF를 DOCX로 변환



소스 PDF의 목록 글머리 기호를 Word에서 목록 구조로 인식하고 보존해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
`DocX` 내보내기를 위해 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)을 만듭니다.

1. 
`setRecognizeBullets(true)`을 활성화하면 목록 형식의 PDF 콘텐츠가 변환 중에 글머리 기호 목록으로 인식됩니다.
1. `document.save(outputFile.toString(), saveOptions)`으로 전화해서 DOCX 파일을 저장하세요.


```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
사용자 정의 이미지 해상도를 사용하여 PDF를 DOCX로 변환



변환 중에 생성된 DOCX 내부의 이미지 충실도를 제어해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
`DocX` 내보내기를 위해 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)을 만듭니다.
1. `setImageResolutionX(300)` 및 `setImageResolutionY(300)`을 설정하면 래스터 콘텐츠가 요청된 해상도로 생성됩니다.

1. 
`document.save(outputFile.toString(), saveOptions)`을 호출하고 DOCX 출력을 저장합니다.

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
