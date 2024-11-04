---
title: PDFにページスタンプを追加する
linktitle: PDFファイルのページスタンプ
type: docs
weight: 30
url: /php-java/page-stamps-in-the-pdf-file/
description: PdfPageStampクラスを使用してPDFファイルにページスタンプを追加する方法をPHPで説明します。
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ページスタンプを追加する

[PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) は、グラフィック、テキスト、テーブルを含む合成スタンプを適用する必要がある場合に使用できます。以下の例では、Adobe InDesign、Illustrator、Microsoft Wordのように文房具を作成するためにスタンプを使用する方法を示します。入力ドキュメントがあり、青色とプラム色の2種類の境界線を適用したいと仮定します。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // 出力ドキュメントを保存する
    $document->save($outputFile);
    $document->close();  
```