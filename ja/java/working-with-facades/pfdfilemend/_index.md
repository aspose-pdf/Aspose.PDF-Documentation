---
title: PdfFileMend クラス
type: docs
weight: 20
url: /ja/java/pdffilemend-class/
description: このセクションでは、PdfFileMend クラスを使用して Aspose.PDF Facades を操作する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

元の編集可能なバージョンのドキュメントがある場合、[FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) を PDF ドキュメントに挿入することは難しい作業ではないように思えます。ドキュメントを作成した後、別の行を追加する必要があることを思い出した場合や、より多くの文書の量について話している場合、どちらの場合でも Aspose.PDF Facades が役立ちます。[PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) クラスを使用して既存の PDF ファイルにテキストを追加する可能性を考えてみましょう。

## 既存の PDF ファイルにテキストを追加する (facades)

いくつかの方法でテキストを追加できます。
 最初の方法を考えます。[FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) を取得し、ページに追加します。その後、左下隅の座標を指定し、テキストをページに追加します。

```java
    public static void AddText01()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Welcome to Aspose!");

        mender.AddText(message, 1, 10, 750);

        // 出力ファイルを保存
        mender.Save(_dataDir + "PdfFileMend01_output.pdf");
    }
```

見た目を確認してください:

![Add Text](/pdf/ja/net/images/add_text.png)

[FormattedText](https://reference.aspose.com/pdf//java/com.aspose.pdf.facades/formattedtext) を追加する2番目の方法です。さらに、テキストが収まるべき矩形を指定します。

```java
public static void AddText02()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

        mender.AddText(message, 1, 10, 700, 55, 810);
        mender.WrapMode = WordWrapMode.ByWords;

        // 出力ファイルを保存
        mender.Save(_dataDir + "PdfFileMend02_output.pdf");
    }
```

第三の例では、指定されたページにテキストを追加する機能を提供します。例として、ドキュメントのページ1と3にキャプションを追加してみましょう。

```java
public static void AddText03()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(document);
        FormattedText message = new FormattedText("Asposeへようこそ!");
        int[] pageNums = new int[] { 1, 3 };
        mender.AddText(message, pageNums, 10, 750, 310, 760);

        // 出力ファイルを保存
        mender.Save(_dataDir + "PdfFileMend03_output.pdf");
    }
```

## 既存のPDFファイルに画像を追加する (facades)

既存のPDFファイルに画像を追加しようとしたことはありますか？
 私たちは、これが簡単な作業ではないことを知っていると確信しています。おそらく、オンラインでフォームに記入していて、身分証明のための写真を添付する必要があるか、既存の履歴書に自分の写真を添付する必要があります。以前は、このような作業は写真を作成し、文書に添付し、さらにスキャンして送信することで解決されていました。このプロセスは非常に面倒で時間がかかりました。

既存のPDFファイルに画像やテキストを追加することは一般的な要件であり、com.aspose.pdf.facades名前空間はこの要件を非常によく満たしています。クラス[PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend)を提供しており、PDFファイルに画像を追加することができます。

この記事では、com.aspose.pdf.facadesを使用してPDFに画像を挿入する方法を紹介します。PDFに画像を追加するためのいくつかのオプションもあります。

四角形のパラメータを設定してPDF文書に画像を挿入します。

```java
public static void AddImage01()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        PdfFileMend mender = new PdfFileMend();

        // ストリームに画像を読み込む
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        mender.AddImage(imageStream, 1, 10, 650, 110, 750);

        // 出力ファイルを保存
        mender.Save(_dataDir + "PdfFileMend04_output.pdf");
    }
```

![画像を追加](/pdf/ja/net/images/add_image1.png)

2番目のコードスニペットを考えてみましょう。[CompositingParameters](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters) クラスのパラメーターのバリエーションを使用することで、様々なデザイン効果を得ることができます。そのうちの一つを試しました。

```java
 public static void AddImage02()
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
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // 出力ファイルを保存する
        mender.Save(_dataDir + "PdfFileMend05_output.pdf");
    }
```


![Add Image](/pdf/ja/net/images/add_image2.png)

次のコードスニペットでは、[ImageFilterType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageFilterType) を使用します。ImageFilterType は、エンコーディングに使用されるストリームコーデックのタイプを示します。デフォルトでは Jpeg です。PNG 形式から画像を読み込むと、ドキュメントには JPEG (または指定した他の形式) で保存されます。

```java
    public static void AddImage03()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // 画像をストリームにロード
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


次のコードスニペットでは、[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) メソッドの使用を確認できます。

[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) はフラグであり、元の画像の透明性を実現するために画像にマスクを適用するかどうかを示します。

```java
public static void AddImage04()
{
    Document document = new Document(_dataDir + "sample_color.pdf");
    PdfFileMend mender = new PdfFileMend();
    // ストリームに画像をロード
    var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
    mender.BindPdf(document);
    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;
    CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
    mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    // 出力ファイルを保存
    mender.Save(_dataDir + "PdfFileMend07_output.pdf");
}
```