---
title: PDF에서 첨부 파일 제거하기
linktitle: 기존 PDF에서 첨부 파일 제거하기
type: docs
weight: 30
url: /ko/cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF for C++는 PDF 문서에서 첨부 파일을 제거할 수 있습니다. Aspose.PDF 라이브러리를 사용하여 PDF 파일에서 첨부 파일을 제거하는 C++ PDF API를 사용하세요.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF는 PDF 파일에서 첨부 파일을 제거할 수 있습니다. PDF 문서의 첨부 파일은 Document 객체의 EmbeddedFiles 컬렉션에 저장됩니다.

PDF 파일과 관련된 모든 첨부 파일을 삭제하려면:

1. [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) 컬렉션의 [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843) 메서드를 호출합니다.
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 Save 메서드를 사용하여 업데이트된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 첨부 파일을 제거하는 방법을 보여줍니다.

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // 문서 열기
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // 모든 첨부 파일 삭제
 pdfDocument->get_EmbeddedFiles()->Delete();

 // 업데이트된 파일 저장
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```