---
title: PDFページの抽出
type: docs
weight: 40
url: ja/net/extract-pdf-pages/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFページを抽出する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## ファイルパスを使用して2つの番号の間のPDFページを抽出する

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドを使用すると、PDFファイルから指定された範囲のページを抽出できます。このオーバーロードを使用すると、ディスクからPDFファイルを操作しながらページを抽出できます。このオーバーロードには、入力ファイルパス、開始ページ、終了ページ、および出力ファイルパスが必要です。開始ページから終了ページまでのページが抽出され、出力がディスクに保存されます。以下のコードスニペットは、ファイルパスを使用して2つの番号の間のPDFページを抽出する方法を示しています。

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // PdfFileEditorオブジェクトを作成
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // ページを抽出
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## ファイルパスを使用してPDFページの配列を抽出する

特定のページのセットを抽出したい場合、[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドを使用することでそれを実現できます。まず、抽出する必要があるすべてのページ番号を含む整数の配列を作成する必要があります。この[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドのオーバーロードは、次のパラメータを取ります: 入力PDFファイル、抽出するページの整数配列、および出力PDFファイル。以下のコードスニペットは、ファイルパスを使用してPDFページを抽出する方法を示しています。

```csharp
public static void Extract_PDFPages_Streams()
{
    // PdfFileEditorオブジェクトを作成
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // ストリームを作成
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        // ページを抽出
        pdfEditor.Extract(inputStream, 1, 3, outputStream);
}
```

## ストリームを使用して2つの番号の間のPDFページを抽出する

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドを使用すると、ストリームを使用してページの範囲を抽出できます。このオーバーロードには、入力ストリーム、開始ページ、終了ページ、および出力ストリームのパラメータを渡す必要があります。開始ページと終了ページの間の範囲で指定されたページは、入力ストリームから抽出され、出力ストリームに保存されます。次のコードスニペットは、ストリームを使用して2つの番号の間のPDFページを抽出する方法を示しています。

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // PdfFileEditorオブジェクトを作成
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // ページを抽出
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## ストリームを使用してPDFページの配列を抽出する

以下のコードスニペットを使用して、PDF ストリームからページの配列を抽出し、対応する [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) メソッドのオーバーロードを使用して出力ストリームに保存できます。ページの範囲ではなく特定のページのセットを抽出したい場合は、[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) メソッドを使用してそれを行うこともできます。最初に、抽出する必要のあるすべてのページ番号を含む整数配列を作成する必要があります。この [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) メソッドのオーバーロードは、入力ストリーム、抽出するページの整数配列、および出力ストリームというパラメータを取ります。

```csharp
public static void Extract_ArrayPDFPages_Streams()
{
    // PdfFileEditor オブジェクトを作成
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // ストリームを作成
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
    {
        int[] pagesToExtract = new int[] { 1, 2 };
        // ページを抽出
        pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
    }
}
```