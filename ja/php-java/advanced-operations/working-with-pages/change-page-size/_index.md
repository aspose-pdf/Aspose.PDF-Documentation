---
title: PDFページサイズをプログラムで変更する 
linktitle: PDFページサイズを変更する
type: docs
weight: 50
url: /ja/php-java/change-page-size/
description: PHPを使用してPDFファイルのページサイズを変更します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFページサイズを変更する

Aspose.PDF for PHP via Javaを使用すると、Javaアプリケーション内で簡単なコード行でPDFページサイズを変更できます。 このトピックでは、既存のPDFファイルのページ寸法（サイズ）を更新/変更する方法を説明します。

[Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) クラスには、ページサイズを設定できるSetPageSize(...)メソッドが含まれています。 以下のコードスニペットは、いくつかの簡単なステップでページ寸法を更新します：

1. ソースPDFファイルをロードします。
1. ページを[pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection)オブジェクトに取得します。
1. 指定されたページを取得します。
1. setPageSize(..)メソッドを呼び出してその寸法を更新します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスの save(..) メソッドを呼び出して、更新されたページ寸法の PDF ファイルを生成します。

次のコードスニペットは、PDF ページの寸法を A4 サイズに変更する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
      
    // ページコレクションを取得
    $pageCollection = $document->getPages();

    // 特定のページを取得
    $page = $pageCollection->get_Item(1);

    // ページサイズを A4 (11.7 x 8.3 インチ) に設定し、Aspose.Pdf では 1 インチ = 72 ポイント
    // したがって、ポイントでの A4 寸法は (842.4, 597.6) になります
    $page.setPageSize(597.6, 842.4);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## PDF ページサイズを取得

Java を介した PHP 用 Aspose.PDF を使用して、既存の PDF ファイルの PDF ページサイズを読み取ることができます。次のコードサンプルは、PHP を使用して PDF ページ寸法を読み取る方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
      
    // 空白ページを PDF ドキュメントに追加
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // ページの高さと幅の情報を取得
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // ページを 90 度回転
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // ページの高さと幅の情報を取得
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```