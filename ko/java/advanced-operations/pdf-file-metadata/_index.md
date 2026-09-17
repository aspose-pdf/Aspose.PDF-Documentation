---
title: Java에서 PDF 파일 메타데이터 작업
linktitle: PDF 파일 메타데이터
type: docs
weight: 200
url: /java/pdf-file-metadata/
description: Aspose.PDF를 사용하여 Java에서 PDF 파일 메타데이터, 문서 정보 및 XMP 속성을 추출, 업데이트 및 관리하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF 문서 정보 및 XMP 메타데이터 가져오기 및 설정
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 메타데이터로 작업하는 방법을 설명합니다. 작성자, 제목 및 키워드와 같은 문서 정보를 읽고, 파일 속성을 업데이트하고, PDF 버전 및 권한을 검사하고, XMP 메타데이터 필드를 설정하고, DOM 및 Facade API를 통해 메타데이터를 저장하는 방법을 알아보세요.
---
Aspose.PDF for Java는 메타데이터 작업을 위한 두 가지 주요 방법을 제공합니다.


- 
`Document`, `DocumentInfo` 및 `document.getMetadata()`을 통한 DOM API.

- 
`PdfFileInfo`을 통한 Facade API.


## 
PDF 파일 정보 얻기



작성자, 제목, 주제, 키워드 등 표준 문서 정보 필드를 읽어야 할 때 이 예를 사용하세요.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[문서정보](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) 개체에 접근합니다.

1. 
필수 메타데이터 필드를 읽고 해당 값을 출력합니다.


```java
public static void getPdfFileInformation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();

        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
}
```

## 
네임스페이스 접두사로 메타데이터 설정



등록된 네임스페이스 접두사를 사용하여 XMP 속성을 추가하거나 업데이트해야 하는 경우 이 예를 사용하십시오.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
필수 XMP 네임스페이스를 등록하고 메타데이터 항목을 추가합니다.

1. 
업데이트된 문서를 저장합니다.


```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
    System.out.println("Prefix metadata saved to " + outputFile);
}
```

## 
문서 정보 필드 업데이트



작성자, 제목, 제작자 또는 생성 날짜와 같은 표준 PDF 파일 속성을 작성하려는 경우 이 예를 사용하십시오.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/)에 액세스하여 새 메타데이터 값을 할당하세요.

1. 
업데이트된 파일 정보로 문서를 저장합니다.


```java
public static void setFileInformation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();
        Date now = new Date();

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(now);
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(now);
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");
        docInfo.setProducer("Custom producer");
        docInfo.setCreator("Custom creator");

        document.save(outputFile.toString());
    }
    System.out.println("File information saved to " + outputFile);
}
```

## 
XMP 메타데이터 속성 설정



사용자 정의 메타데이터 값을 포함하여 추가 XMP 항목을 저장해야 하는 경우 이 예를 사용하십시오.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
`document.getMetadata()`을 통해 필수 XMP 메타데이터 항목을 추가합니다.

1. 
출력 파일을 저장합니다.

```java
public static void setXmpMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().addItem("xmp:CreateDate", OffsetDateTime.now().toString());
        document.getMetadata().addItem("xmp:Nickname", "Nickname");
        document.getMetadata().addItem("xmp:CustomProperty", "Custom Value");
        document.save(outputFile.toString());
    }
    System.out.println("XMP metadata saved to " + outputFile);
}
```
