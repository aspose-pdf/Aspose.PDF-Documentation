---
title: PDF 문서에 첨부 파일 추가하기 
linktitle: PDF 문서에 첨부 파일 추가하기 
type: docs
weight: 10
url: /ko/java/add-attachment-to-pdf-document/
description: 이 페이지는 Java를 사용하여 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

첨부 파일은 다양한 정보를 포함할 수 있으며 다양한 파일 유형일 수 있습니다. 이 글에서는 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다.

1. 첨부하려는 파일과 파일 설명을 포함하는 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 객체를 생성합니다.

1. [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 객체를 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) 컬렉션에 [add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 메소드를 사용하여 추가합니다. [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) 컬렉션은 PDF 파일에 추가된 모든 첨부 파일을 포함합니다.

다음 코드 스니펫은 PDF 문서에 첨부 파일을 추가하는 방법을 보여줍니다.

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // 문서 열기
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 첨부 파일로 추가할 새 파일 설정
  FileSpecification fileSpecification = new FileSpecification("sample.txt", "샘플 텍스트 파일");
  // 문서의 첨부 파일 컬렉션에 첨부 파일 추가
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // 업데이트된 문서 저장
  pdfDocument.save("output.pdf");
    }
}
```