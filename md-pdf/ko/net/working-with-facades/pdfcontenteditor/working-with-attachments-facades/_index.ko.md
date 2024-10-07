---
title: 첨부 파일 작업 - 파사드
type: docs
weight: 50
url: /net/working-with-attachments-facades/
description: 이 섹션에서는 PdfContentEditor 클래스를 사용하여 첨부 파일 - 파사드 작업 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

이 섹션에서는 Aspose.PDF for .NET Facades를 사용하여 PDF에서 첨부 파일을 다루는 방법을 설명합니다. 첨부 파일은 기본 문서에 첨부된 추가 파일로, pdf, word, 이미지 또는 기타 파일 유형일 수 있습니다. pdf에 첨부 파일을 추가하고, 첨부 파일의 정보를 얻고, 파일로 저장하며, C#을 사용하여 프로그램적으로 PDF에서 첨부 파일을 삭제하는 방법을 배우게 됩니다.

## 기존 PDF에 파일에서 첨부 파일 추가

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스를 사용하여 기존 PDF 파일에 첨부 파일을 추가할 수 있습니다. 문서의 첨부 파일은 파일 경로를 사용하여 디스크의 파일에서 추가할 수 있습니다. [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 메서드를 사용하여 첨부 파일을 추가할 수 있습니다. 이 메서드는 두 개의 인수를 받습니다: 파일 경로와 첨부 파일 설명입니다. 먼저, 기존 PDF 파일을 열고 첨부 파일을 추가해야 합니다. 그런 다음 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메서드를 사용하여 출력 PDF 파일을 저장할 수 있습니다.

다음 코드 스니펫은 파일에서 첨부 파일을 추가하는 방법을 보여줍니다. 예를 들어, MP3 파일을 추가해 봅시다.

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```
## 기존 PDF에 스트림에서 첨부 파일 추가하기

첨부 파일은 [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 메서드를 사용하여 스트림 – FileStream –에서 PDF 파일에 추가할 수 있습니다. 이 메서드는 세 가지 인수를 받습니다: 스트림, 첨부 파일 이름 및 첨부 파일 설명. 첨부 파일을 추가하려면 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 메서드를 호출하여 첨부 파일을 추가할 수 있습니다. 마지막으로, Save 메서드를 호출하여 업데이트된 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 스트림에서 첨부 파일을 추가하는 방법을 보여줍니다.

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## 기존 PDF 파일에서 모든 첨부 파일 삭제하기

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) 메소드를 사용하면 기존 PDF 파일에서 모든 첨부 파일을 삭제할 수 있습니다. [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) 메소드를 호출합니다. 마지막으로 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메소드를 호출하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에서 모든 첨부 파일을 삭제하는 방법을 보여줍니다.

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
```