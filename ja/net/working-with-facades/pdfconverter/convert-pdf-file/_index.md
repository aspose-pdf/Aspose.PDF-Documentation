---
title: PDFファイルの変換
type: docs
weight: 30
url: ja/net/convert-pdf-file/
description: このセクションでは、PdfConverterクラスを使用してAspose.PDF FacadesでPDFファイルを変換する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFページを異なる画像形式に変換する (Facades)

PDFページを異なる画像形式に変換するには、[PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用してPDFファイルを開く必要があります。 その後、初期化タスクのために[DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert)メソッドを呼び出す必要があります。その後、[HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage)および[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6)メソッドを使用してすべてのページをループすることができます。[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6)メソッドを使用すると、特定のページの画像を作成することができます。このメソッドにImageFormatを渡す必要があり、特定のタイプ、すなわちJPEG、GIF、PNGなどの画像を作成します。最後に、[PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter)クラスの[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close)メソッドを呼び出します。次のコードスニペットは、PDFページを画像に変換する方法を示しています。

```csharp
 public static void ConvertPdfPagesToImages01()
        {
            // PdfConverterオブジェクトを作成
            PdfConverter converter = new PdfConverter();

            // 入力pdfファイルをバインド
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // 変換プロセスを初期化
            converter.DoConvert();

            // ページが存在するか確認してから、1つずつ画像に変換
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // PdfConverterオブジェクトを閉じる
            converter.Close();
        }
```
次のコードスニペットでは、いくつかのパラメータを変更する方法を示します。[CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype)でフレーム「CropBox」を設定します。また、インチあたりのドット数を指定して[Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution)を変更することもできます。次に[FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - フォームプレゼンテーションモードです。次に変換の開始ページ番号を設定する[StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage)を指定します。また、範囲を設定して最後のページを指定することもできます。

```csharp
  public static void ConvertPdfPagesToImages02()
        {
            // PdfConverterオブジェクトを作成する
            PdfConverter converter = new PdfConverter();

            // 入力PDFファイルをバインドする
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // 変換プロセスを初期化する
            converter.DoConvert();
            converter.CoordinateType = PageCoordinateType.CropBox;
            converter.Resolution = new Devices.Resolution(600);
            converter.FormPresentationMode = Devices.FormPresentationMode.Production;
            converter.StartPage = 2;
            // converter.EndPage = 3;
            // ページが存在するか確認し、1枚ずつ画像に変換する
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // PdfConverterオブジェクトを閉じる
            converter.Close();
        }
```

## See also

Aspose.PDF for .NETは、PDFドキュメントをさまざまな形式に変換したり、他の形式からPDFに変換したりすることができます。また、Aspose.PDF変換アプリを使用してAspose.PDFの変換品質を確認し、結果をオンラインで確認することもできます。[変換](/pdf/net/converting/)セクションを学んで、タスクを解決してください。