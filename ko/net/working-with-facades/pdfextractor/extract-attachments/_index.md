---
title: PDF 파일에서 첨부 파일 추출
type: docs
weight: 10
url: /ko/net/extract-attachments/
description: 이 섹션에서는 PdfExtractor 클래스를 사용하여 pdf에서 첨부 파일을 추출하는 방법에 대해 설명합니다.
lastmod: "2021-06-05"
---

[Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)의 추출 기능 중 주요 카테고리 중 하나는 첨부 파일 추출입니다. 이 카테고리는 첨부 파일을 추출하는 데 도움을 줄 뿐만 아니라 첨부 파일 관련 정보를 제공하는 메서드도 제공하는 일련의 메서드를 제공합니다. 즉, [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) 및 [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) 메서드는 각각 첨부 파일 정보 및 첨부 파일 이름을 제공합니다. 첨부 파일을 추출하고 가져오기 위해 [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) 및 [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment) 메서드를 사용합니다.

다음 코드 스니펫은 PdfExtractor 메서드를 사용하는 방법을 보여줍니다:

```csharp
public static void ExtractAttachments()
{
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample-attach.pdf");

    // 첨부 파일 추출
    pdfExtractor.ExtractAttachment();

    // 첨부 파일 이름 가져오기
    if (pdfExtractor.GetAttachNames().Count > 0)
    {
         Console.WriteLine("추출 및 저장 중...");
         // 추출된 첨부 파일 가져오기
         pdfExtractor.GetAttachment(_dataDir);
    }
}
```