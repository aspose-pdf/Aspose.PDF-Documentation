---
title: Java에서 PDF의 첨부 파일 제거
linktitle: 기존 PDF에서 첨부 파일 제거
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF를 사용하여 Java의 PDF 문서에 포함된 첨부 파일 하나 또는 모두를 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 프로그래밍 방식으로 PDF 첨부 파일 삭제
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일에서 첨부 파일을 제거하는 방법을 보여줍니다. 예제에서는 업데이트된 문서를 저장하기 전에 키별로 포함된 파일 하나를 삭제하고 전체 EmbeddedFiles 컬렉션을 지우는 방법을 보여줍니다.
---
PDF 문서에 저장된 첨부 파일은 `EmbeddedFiles` 컬렉션을 통해 개별적으로 제거하거나 한꺼번에 제거할 수 있습니다.


## 
단일 첨부 파일 제거



PDF에서 이름이 포함된 파일 하나를 삭제해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
포함된 파일 컬렉션에서 해당 키로 첨부 파일을 삭제합니다.
1. 업데이트된 출력 문서를 저장합니다.


```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## 
모든 첨부 파일 제거



전체 포함된 파일 컬렉션을 지워야 하는 경우 이 접근 방식을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
포함된 파일 컬렉션에서 모든 항목을 삭제합니다.
1. 정리된 출력 문서를 저장합니다.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
