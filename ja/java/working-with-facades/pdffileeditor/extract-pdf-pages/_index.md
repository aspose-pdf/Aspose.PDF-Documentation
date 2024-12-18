---
title: PDFページを抽出
type: docs
weight: 20
url: /ja/java/extract-pdf-pages/
description: このセクションでは、PdfFileEditorクラスを使用してcom.aspose.pdf.facadesでPDFページを抽出する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## ファイルパスを使用して2つの番号間のPDFページを抽出

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) クラスの [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) メソッドを使用すると、PDFファイルから指定されたページ範囲を抽出できます。このオーバーロードを使用すると、ディスクからPDFファイルを操作しながらページを抽出できます。このオーバーロードには次のパラメータが必要です: 入力ファイルパス、開始ページ、終了ページ、および出力ファイルパス。開始ページから終了ページまでのページが抽出され、出力がディスクに保存されます。次のコードスニペットは、ファイルパスを使用して2つの番号間のPDFページを抽出する方法を示しています。

```java
  public static void Extract_PDFPages_FilePaths() {
        // PdfFileEditorオブジェクトを作成
        PdfFileEditor pdfEditor = new PdfFileEditor();

        // ページを抽出
        pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
    }
```


## ファイルパスを使用してPDFページの配列を抽出

特定のページセットを抽出したい場合、[Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) メソッドを使用することでそれが可能です。まず、抽出する必要があるすべてのページ番号を含む整数配列を作成する必要があります。このオーバーロードの [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) メソッドは、次のパラメータを取ります: 入力PDFファイル、抽出するページの整数配列、そして出力PDFファイル。以下のコードスニペットは、ファイルパスを使用してPDFページを抽出する方法を示しています。

```java
 public static void Extract_ArrayPDFPages_FilePaths() {
        // PdfFileEditor オブジェクトを作成
        PdfFileEditor pdfEditor = new PdfFileEditor();
        int[] pagesToExtract = new int[] { 1, 2 };
        // ページを抽出
        pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
    }
```


## ストリームを使用して2つの番号間のPDFページを抽出する

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) クラスの [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) メソッドは、ストリームを使用してページの範囲を抽出することを可能にします。このオーバーロードには次のパラメータを渡す必要があります: 入力ストリーム、開始ページ、終了ページ、および出力ストリーム。開始ページと終了ページの間の範囲で指定されたページは、入力ストリームから抽出され、出力ストリームに保存されます。以下のコードスニペットは、ストリームを使用して2つの番号間のPDFページを抽出する方法を示しています。

```java
public static void Extract_PDFPages_Streams()
    {
         // PdfFileEditorオブジェクトの作成
            PdfFileEditor pdfEditor = new PdfFileEditor();
         // ストリームの作成
         using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
         using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
         // ページの抽出
         pdfEditor.Extract(inputStream, 1, 3, outputStream);

    }
```


## ストリームを使用してPDFページの配列を抽出

ページの配列は、PDFストリームから抽出して出力ストリームに保存することができます。[Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-)メソッドの適切なオーバーロードを使用します。ページの範囲を抽出するのではなく、特定のページのセットを抽出したい場合、[Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-)メソッドを使用することができます。最初に、抽出する必要のあるすべてのページ番号を含む整数配列を作成する必要があります。この[Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-)メソッドのオーバーロードは、入力ストリーム、抽出するページの整数配列、および出力ストリームのパラメータを受け取ります。以下のコードスニペットは、ストリームを使用してPDFページを抽出する方法を示しています。

```java
public static void Extract_ArrayPDFPages_Streams()
        {
            // PdfFileEditorオブジェクトを作成
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