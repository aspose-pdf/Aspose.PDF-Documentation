---
title: PDFをMicrosoft PowerPointに変換する
linktitle: PDFをPowerPointに変換する
type: docs
weight: 30
url: ja/php-java/convert-pdf-to-powerpoint/
lastmod: "2024-05-20"
description: Aspose.PDFを使用すると、PHPでPDFをPowerPoint形式に変換できます。PDFをPPTXに変換する際にスライドを画像として扱う方法があります。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for PHP** では、PDFからPPTXへの変換の進行状況を追跡できます。PPT/PPTXプレゼンテーションを作成および操作する機能を提供するAspose.SlidesというAPIがあります。このAPIは、PPT/PPTXファイルをPDF形式に変換する機能も提供します。Aspose.PDF for PHPでは、PDFドキュメントをPPTX形式に変換する機能を導入しています。この変換中に、PDFファイルの個々のページがPPTXファイルの個別のスライドに変換されます。

PDFからPPTXへの変換中、テキストは選択/更新可能なテキストとしてレンダリングされ、画像としてレンダリングされるわけではありません。
   PDFファイルをPPTX形式に変換するために、Aspose.PDFはPptxSaveOptionsというクラスを提供しています。PptxSaveOptionsクラスのオブジェクトは、Document.save(..)メソッドの第二引数として渡されます。

PDFをPowerPoint形式に変換するタスクを解決するための次のコードスニペットを確認してください：

```php
// 入力PDFドキュメントを読み込む
$document = new Document($inputFile);

// PptxSaveOptionsのインスタンスを作成
$saveOption = new PptxSaveOptions();

// PDFドキュメントをPPTXファイルとして保存
$document->save($outputFile, $saveOption);
```

## スライドを画像としてPDFをPPTXに変換

検索可能なPDFを選択可能なテキストではなく、画像としてPPTXに変換する必要がある場合、Aspose.PDFはAspose.Pdf.PptxSaveOptionsクラスを通じてそのような機能を提供します。 この目的を達成するために、[PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) クラスのプロパティ SlidesAsImages を以下のコードサンプルに示すように 'true' に設定します。

次のコードスニペットは、PDFファイルをPPTX形式のスライドとして画像に変換するプロセスを示しています。

```php
// 入力PDFドキュメントをロードする
$document = new Document($inputFile);

// PptxSaveOptionsのインスタンスを作成する
$saveOption = new PptxSaveOptions();
$saveOption->setSlidesAsImages(true);

// PDFドキュメントをPPTXファイルとして保存する
$document->save($outputFile, $saveOption);

    public static void ConvertPDFtoPPTX_SlideAsImages() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX_out.pptx").toString();

        // PDFドキュメントをロードする
        Document doc = new Document(pdfDocumentFileName);
        // PptxSaveOptionsのインスタンスを作成する
        PptxSaveOptions pptx_save = new PptxSaveOptions();
        // 出力をPPTX形式で保存する
        pptx_save.setSlidesAsImages(true);

        doc.save(pptxDocumentFileName, pptx_save);
    }
```

{{% alert color="success" %}}
**PDFをPowerPointにオンラインで変換してみてください**

Aspose.PDF for PHPは、オンラインで無料で利用できるアプリケーション["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF PDFからPPTXへの変換を無料アプリで](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}