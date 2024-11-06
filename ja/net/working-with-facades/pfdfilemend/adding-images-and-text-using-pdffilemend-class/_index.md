---
title: 画像とテキストの追加 
type: docs
weight: 10
url: ja/net/adding-images-and-text-using-pdffilemend-class/
description: このセクションでは、PdfFileMend クラスを使用して画像とテキストを追加する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) クラスを使用すると、既存の PDF ドキュメントに指定された場所で画像やテキストを追加することができます。 ```
それは、[AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index)と[AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index)という名前の2つのメソッドを提供します。
``` [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) メソッドを使用すると、JPG、GIF、PNG、および BMP タイプの画像を追加できます。[AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) メソッドは、[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) クラスの型の引数を受け取り、既存の PDF ファイルに追加します。画像とテキストは、左下と右上の座標によって指定された矩形領域に追加できます。画像を追加する際には、画像ファイルのパスまたは画像ファイルのストリームのいずれかを指定できます。画像またはテキストを追加するページ番号を指定するために、これらのメソッドの両方がページ番号の引数を提供します。したがって、指定された場所に画像やテキストを追加するだけでなく、指定されたページにも追加できます。

画像は PDF ドキュメントの内容の重要な部分です。 画像の操作は、PDFファイルを扱う人々にとって一般的な要件です。この記事では、既存のPDFファイル内の画像をどのように操作できるかを、[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)と[Aspose.PDF for .NET](/pdf/net/)の助けを借りて探ります。[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)に関連するすべての画像操作はこの記事に統合されています。

## 実装の詳細

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)を使用すると、既存のPDFファイルに新しい画像を追加できます。 既存の画像を置き換えたり削除したりすることもできます。PDFファイルは画像に変換することもできます。個々のページをそれぞれ1つの画像に変換することも、PDFファイル全体を1つの画像に変換することもできます。JPEG、BMP、PNG、TIFFなどの形式をサポートしています。PDFファイルから画像を抽出することもできます。これらの操作を実装するために、[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)の4つのクラス、すなわち、[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend)、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)、[PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter)を使用することができます。

## 画像操作

このセクションでは、これらの画像操作について詳しく見ていきます。 私たちは関連するクラスとメソッドの使用を示すコードスニペットも見ていきます。まず最初に、既存のPDFファイルに画像を追加する方法を見てみましょう。[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) クラスの [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) メソッドを使用して新しい画像を追加できます。このメソッドを使用すると、画像を追加したいページ番号だけでなく、画像の位置も指定できます。

## 既存のPDFファイルに画像を追加する (Facades)

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) クラスの [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) メソッドを使用できます。 The [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) メソッドは追加する画像、画像を追加するページ番号、および座標情報を必要とします。その後、[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) メソッドを使用して更新されたPDFファイルを保存します。

次の例では、imageStreamを使用してページに画像を追加します:

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

![Add Image](/pdf/net/images/add_image1.png)


[CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1) の助けを借りて、1つの画像を別の画像の上に重ねることができます。
```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // ストリームに画像を読み込む
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // 出力ファイルを保存
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

![Add Image](/pdf/net/images/add_image2.png)

PDFファイルに画像を格納する方法は複数あります。以下の例でその一つを示します：

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // ストリームに画像を読み込む
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // 出力ファイルを保存
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // 画像をストリームに読み込む
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // 出力ファイルを保存する
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## 既存のPDFファイルにテキストを追加する（ファサード）

いくつかの方法でテキストを追加できます。 最初の方法を考えます。[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)を取得してページに追加します。その後、左下隅の座標を示し、ページにテキストを追加します。

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

どのように見えるか確認してください：

![Add Text](/pdf/net/images/add_text.png)

[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)を追加するもう一つの方法です。さらに、テキストが収まるべき矩形を示します。

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // save the output file
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```
第三の例では、指定されたページにテキストを追加する機能を提供します。私たちの例では、ドキュメントの1ページ目と3ページ目にキャプションを追加します。

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("Welcome to Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // 出力ファイルを保存
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```