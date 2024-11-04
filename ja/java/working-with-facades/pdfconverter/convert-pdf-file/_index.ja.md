---
title: PDFファイルの変換
type: docs
weight: 20
url: /java/convert-pdf-file/
description: このセクションでは、PdfConverterクラスを使用してAspose.PDF FacadesでPDFファイルを変換する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFページをさまざまな画像形式に変換する (Facades)

PDFページをさまざまな画像形式に変換するためには、[PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter)オブジェクトを作成し、[bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-)メソッドを使用してPDFファイルを開く必要があります。

その後、初期化タスクのために[doConvert](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--)メソッドを呼び出す必要があります。
 次に、[hasNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) および [getNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-) メソッドを使用して、すべてのページをループ処理できます。getNextImage メソッドを使用すると、特定のページの画像を作成できます。また、このメソッドには ImageType を渡して、JPEG、GIF、PNG などの特定のタイプの画像を作成する必要があります。

最後に、[PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) クラスの close メソッドを呼び出します。

次のコードスニペットは、PDF ページを画像に変換する方法を示しています。

```java
public static void ConvertPdfPagesToImages01() {
        // PdfConverter オブジェクトを作成
        PdfConverter converter = new PdfConverter();

        // 入力 PDF ファイルをバインド
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // 変換プロセスを初期化
        converter.doConvert();
        
        int count=0;

        // ページが存在するか確認し、1つずつ画像に変換
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // PdfConverter オブジェクトを閉じる
        converter.close();
    }
```

次のコードスニペットでは、いくつかのパラメータを変更する方法を示します。[setCoordinateType](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-)を使用して、フレーム[CropBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox)を設定します。また、解像度を指定することで、インチあたりのドット数を変更できます。[setResolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-)。次に、フォームのプレゼンテーションモード[setFormPresentationMode](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-)を設定します。そして、変換の開始ページ番号を指定する[setStartPage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-)を示します。範囲を設定して最後のページを指定することもできます。

```java
public static void ConvertPdfPagesToImages02()
    {
        // PdfConverterオブジェクトを作成
        PdfConverter converter = new PdfConverter();

        // 入力pdfファイルをバインド
        converter.bindPdf(_dataDir + "sample.pdf");

        // 変換プロセスを初期化
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // ページが存在するか確認し、次々と画像に変換
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // PdfConverterオブジェクトを閉じる
        converter.close();
    }
```