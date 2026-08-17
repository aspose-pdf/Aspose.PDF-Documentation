---
title: 프로그래밍 방식으로 PDF 문서 저장
linktitle: PDF 저장
type: docs
weight: 30
url: /java/save-pdf-document/
description: Aspose.PDF를 사용하여 Java의 PDF 문서를 파일, 스트림 또는 PDF 표준으로 저장하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서 저장
Abstract: 이 문서에서는 Aspose.PDF를 사용하여 Java에서 PDF 문서를 저장하는 방법을 설명합니다. 파일 경로에 저장, OutputStream에 저장 및 PDF/X 표준 파일로 저장하기 전에 문서를 변환하는 방법을 다룹니다.
---

Aspose.PDF for Java는 대상 대상 및 출력 요구 사항에 따라 문서를 저장하는 여러 가지 방법을 제공합니다.


## 
Java로 PDF 문서 저장



문서를 저장할 수 있습니다:


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 디스크의 파일에 직접 저장합니다.

1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 `OutputStream`에 저장합니다.

1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/)로 변환하고 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/)과 같은 표준 형식으로 저장합니다.


## 
문서를 파일로 저장


```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## 
스트림에 문서 저장


```java
public static void saveDocumentToStream(Path inputFile, Path outputFile) throws Exception {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        document.save(stream);
    } finally {
        document.close();
    }
}
```

## 
문서를 PDF/X로 저장

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
