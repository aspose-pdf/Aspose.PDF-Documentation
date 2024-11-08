---
title: PDFドキュメントを開く
linktitle: 開く
type: docs
weight: 20
url: /ja/php-java/open-pdf-document/
description: Aspose.PDF for PHPを介してJavaでPDFファイルを開く方法を学びます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 既存のPDFドキュメントを開く

PDFファイル、またはポータブルドキュメントフォーマットファイルは、ドキュメント交換のためのユニバーサル標準となっています。これらは、ドキュメントの形式を保存するために広く使用されています。しかし、PHPを介してJavaを使用してプログラミング言語でPDFファイルを扱うことは少し難しい場合があります。この記事では、PDFを迅速かつ簡単に開くことができるAspose.PDF for PHP via Javaライブラリを紹介します。

```php

    $document = new Document($inputFile,"mypassword");
    $responseData = "ドキュメントが正常に開かれました。ファイルサイズ: " . filesize($inputFile);
```