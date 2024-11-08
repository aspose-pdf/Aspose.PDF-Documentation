---
title: PDFドキュメントを保存する 
linktitle: 保存
type: docs
weight: 30
url: /ja/php-java/save-pdf-document/
description: Aspose.PDF for PHP via Javaライブラリを使用してPDFファイルを保存する方法を学びます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントをファイルシステムに保存する

作成または操作したPDFドキュメントをファイルシステムに保存するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのsaveメソッドを使用します。

```php

    $document = new Document($inputFile);        
    $document->save($outputFile);
```