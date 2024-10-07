---
title: 添付ファイルの操作 - ファサード
type: docs
weight: 50
url: /net/working-with-attachments-facades/
description: このセクションでは、PdfContentEditorクラスを使用して添付ファイルの操作 - ファサードについて説明します。
lastmod: "2021-06-05"
draft: false
---

このセクションでは、Aspose.PDF for .NET ファサードを使用してPDFの添付ファイルを操作する方法を説明します。添付ファイルとは、親ドキュメントに追加される追加ファイルのことで、pdf、word、画像、その他のファイルなど、さまざまなファイルタイプが可能です。PDFに添付ファイルを追加する方法、添付ファイルの情報を取得してファイルに保存する方法、C#を使用してPDFから添付ファイルをプログラムで削除する方法を学びます。

## 既存のPDFにファイルから添付ファイルを追加する

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスを使用して、既存のPDFファイルに添付ファイルを追加できます。 添付ファイルはファイルパスを使用してディスク上のファイルから追加できます。[AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) メソッドを使用して添付ファイルを追加できます。このメソッドは2つの引数を取ります: ファイルパスと添付ファイルの説明。まず、既存のPDFファイルを開き、そこに添付ファイルを追加する必要があります。それから、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) の [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) メソッドを使用して出力PDFファイルを保存できます。

次のコードスニペットは、ファイルから添付ファイルを追加する方法を示しています。例えば、MP3ファイルを追加してみましょう。

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```
## 既存のPDFにストリームから添付ファイルを追加する

添付ファイルは、FileStream を使用して [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) メソッドを使って PDF ファイルに追加できます。このメソッドは3つの引数を取ります: ストリーム、添付ファイル名、および添付ファイルの説明です。添付ファイルを追加するためには、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) メソッドを使用して入力 PDF ファイルをバインドします。その後、[AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) メソッドを呼び出して添付ファイルを追加できます。最後に、Save メソッドを呼び出して更新された PDF ファイルを保存できます。以下のコードスニペットは、ストリームから添付ファイルを追加する方法を示します。

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## 既存のPDFファイルからすべての添付ファイルを削除する

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスの [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) メソッドを使用すると、既存のPDFファイルからすべての添付ファイルを削除できます。[DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) メソッドを呼び出します。最後に、更新されたPDFファイルを保存するために [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) メソッドを呼び出す必要があります。次のコードスニペットは、既存のPDFファイルからすべての添付ファイルを削除する方法を示しています。

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
```