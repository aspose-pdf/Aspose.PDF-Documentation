---
title: PDFファイルにテキストを追加する 
linktitle: PDFファイルにテキストを追加する
type: docs
weight: 10
url: /php-java/add-text-to-pdf-file/
description: この記事では、Aspose.PDFでのテキスト操作のさまざまな側面について説明します。PDFにテキストを追加したり、HTMLフラグメントを追加したり、カスタムOTFフォントを使用する方法を学びます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

既存のPDFファイルにテキストを追加するには:

1. Documentオブジェクトを使用して入力PDFを開きます。
1. テキストを追加したい特定のページを取得します。
1. 内容が "Aspose.PDF" のテキストフラグメントを作成します。
1. ページ上のテキストフラグメントの位置を設定します。
1. テキストフラグメントのテキストプロパティを設定します。
1. ページのためにTextBuilderオブジェクトを作成します。
1. PDFページにテキストフラグメントを追加します。
4. 結果のPDFドキュメントを出力ファイルとして保存します。

## テキストを追加する

次のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // 特定のページを取得
    $page = $document->getPages()->add();
    
    // テキストフラグメントを作成
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // テキストプロパティを設定
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // TextBuilderオブジェクトを作成
    $textBuilder = new TextBuilder($page);
    // PDFページにテキストフラグメントを追加
    $textBuilder->appendText($textFragment);

    // 結果のPDFドキュメントを保存    
    $document->save($outputFile);
    $document->close();
```