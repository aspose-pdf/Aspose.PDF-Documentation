---
title: PDFページをプログラムで回転
linktitle: PDFページを回転
type: docs
weight: 60
url: /php-java/rotate-pages/
description: Javaを使用してページの向きを変更し、新しいページの向きに合わせてページコンテンツを調整します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ページの向きを変更

この記事では、既存のPDFファイルのページの向きを更新または変更する方法について説明します。

Aspose.PDF for PHP via Javaには、ページの向きを横向きから縦向きに、またはその逆に変更する機能があります。

1. 指定された入力ファイルを使用してドキュメントを開きます。
1. ドキュメントのすべてのページを取得します。
1. 各ページを反復処理して、回転を90度に設定します。
1. 変更されたドキュメントを指定された出力ファイルに保存します。
1. ドキュメントを閉じます。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);                
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // すべてのページをループする
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
       
        $page->setRotate((new Rotation())->On90);
    }

    // 出力ドキュメントを保存する
    $document->save($outputFile);
    $document->close();
```