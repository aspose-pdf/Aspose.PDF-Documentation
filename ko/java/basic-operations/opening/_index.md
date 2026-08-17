---
title: 프로그래밍 방식으로 PDF 문서 열기
linktitle: PDF 열기
type: docs
weight: 20
url: /java/open-pdf-document/
description: 파일 경로, 스트림 또는 비밀번호에서 Aspose.PDF를 사용하여 Java에서 PDF 파일을 여는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서 열기
Abstract: 이 문서에서는 Aspose.PDF를 사용하여 Java에서 기존 PDF 문서를 여는 방법을 보여줍니다. 파일 경로로 PDF 열기, InputStream에서 PDF 열기, 비밀번호로 보호된 문서 열기를 다루고 있으며, 각 예제는 로드된 문서에서 페이지 수를 읽습니다.
---

Aspose.PDF for Java는 소스 데이터의 출처에 따라 기존 PDF 문서를 로드하는 여러 가지 방법을 지원합니다.


## 
Java에서 PDF 문서 열기



PDF 문서를 열 수 있습니다.


1. 
파일 경로에서 직접 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
`InputStream`에서 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
비밀번호를 입력하여 암호화된 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.


## 
파일에서 문서 열기


```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## 
스트림에서 문서 열기


```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## 
암호화된 문서 열기

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
