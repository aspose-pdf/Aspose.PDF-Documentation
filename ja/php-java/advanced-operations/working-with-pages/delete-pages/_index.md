---
title: PDFページをプログラムで削除 
linktitle: PDFページを削除
type: docs
weight: 40
url: /ja/php-java/delete-pages/
description: PHPを使用してPDFファイルからページを削除できます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルからページを削除

1. deleteメソッドを呼び出し、ページのインデックスを指定します
1. saveメソッドを呼び出して、更新されたPDFファイルを保存します
次のコードスニペットは、PHPを使用してPDFファイルから特定のページを削除する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // 特定のページを削除
    $pages->delete(2);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```