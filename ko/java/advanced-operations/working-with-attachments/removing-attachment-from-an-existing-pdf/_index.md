---
title: 기존 PDF에서 첨부 파일 제거
linktitle: 기존 PDF에서 첨부 파일 제거
type: docs
weight: 30
url: ko/java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF는 PDF 문서에서 첨부 파일을 제거할 수 있습니다. Aspose.PDF 라이브러리를 사용하여 Java PDF API로 PDF 파일의 첨부 파일을 제거하세요.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF는 PDF 파일에서 첨부 파일을 제거할 수 있습니다. PDF 문서의 첨부 파일은 Document 객체의 EmbeddedFiles 컬렉션에 저장됩니다.

PDF 문서의 첨부 파일은 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) 컬렉션에 저장됩니다.

PDF 파일과 관련된 모든 첨부 파일을 삭제하려면:

1. [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) 컬렉션의 delete(..) 메서드를 호출하세요.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 저장 메소드를 사용하여 업데이트된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 모든 첨부 파일을 삭제하는 방법을 보여줍니다.

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // 문서 열기
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 모든 첨부 파일 삭제
  pdfDocument.getEmbeddedFiles().delete();
  // 업데이트된 파일 저장
  pdfDocument.save("output.pdf");

    }
```