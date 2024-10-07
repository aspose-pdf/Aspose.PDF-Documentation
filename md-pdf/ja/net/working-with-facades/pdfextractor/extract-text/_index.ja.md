---
title: PDFファイルからテキストを抽出
type: docs
weight: 30
url: /net/extract-text/
description: このセクションでは、PdfExtractorクラスを使用してPDFからテキストを抽出する方法を説明します。
lastmod: "2021-06-05"
---

この記事では、PDFファイルからテキストを抽出する詳細を見ていきます。これらすべての抽出機能は、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスで一か所に提供されています。これらの機能をコードでどのように使用するかを見ていきます。

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスは、3種類の抽出機能を提供します。これら3つのカテゴリーは、テキスト、画像、および添付ファイルです。これらの3つのカテゴリーのそれぞれで抽出を行うために、PdfExtractorは最終的な出力を得るために一緒に機能するさまざまなメソッドを提供します。

例えば、テキストを抽出するためには、3つのメソッドを使用できます。すなわち、 [ExtractText、GetText、HasNextPageText、GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index)。 さて、テキストを抽出し始めるためには、まず[ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index)メソッドを呼び出す必要があります。これにより、PDFファイルからテキストが抽出され、メモリに保存されます。その後、[GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index)メソッドがこの抽出されたテキストを取得し、指定された場所のファイルにディスクに保存します。[HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext)は各ページをループして次のページにテキストがあるかどうかを確認するのに役立ちます。もしテキストを含んでいる場合、[GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index)が個々のページのテキストをファイルに保存するのを手助けします。

```csharp
public static void ExtractText()
{
    bool WholeText = true;
    // PdfExtractorクラスのオブジェクトを作成
    PdfExtractor pdfExtractor = new PdfExtractor();

    // 入力PDFをバインド
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // テキストを抽出
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // テキストを個別のファイルに抽出
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
以下のコードを使用して、テキスト抽出モードを抽出します。

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // PdfExtractorクラスのオブジェクトを作成します
    PdfExtractor pdfExtractor = new PdfExtractor();

    // 入力PDFをバインドします
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // テキストを抽出します
    // pdfExtractor.ExtractTextMode = 0; //ピュアモード
    pdfExtractor.ExtractTextMode = 1; //生モード
    pdfExtractor.ExtractText();


    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // テキストを別々のファイルに抽出します
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```