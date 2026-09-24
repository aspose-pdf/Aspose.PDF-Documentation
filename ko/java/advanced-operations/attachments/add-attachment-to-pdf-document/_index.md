---
title: Java에서 PDF에 첨부 파일 추가
linktitle: PDF 문서에 첨부 파일 추가
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: Aspose.PDF를 사용하여 Java에서 PDF 문서에 파일 첨부를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 문서에 포함된 파일 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 외부 파일을 첨부하는 방법을 보여줍니다. 이 예제에서는 기존 PDF를 열고, 첨부 파일에 대한 FileSpecification을 만들고, 이를 문서의 EmbeddedFiles 컬렉션에 추가하고, 업데이트된 파일을 저장합니다.
---
PDF에 파일을 첨부하려면 소스 문서를 로드하고 `FileSpecification`을 생성하여 포함된 파일 컬렉션에 추가하고 결과를 저장합니다.


## 
PDF 문서에 첨부 파일 추가



외부 파일을 기존 PDF에 포함해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
포함하려는 파일에 대한 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/)을 만듭니다.
1. `EmbeddedFiles` 컬렉션에 파일 사양을 추가하고 업데이트된 문서를 저장합니다.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
