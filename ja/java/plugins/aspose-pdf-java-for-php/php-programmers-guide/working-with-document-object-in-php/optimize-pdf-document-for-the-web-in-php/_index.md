---
title: "PHP での Web 用 PDF ドキュメントの最適化"
linktitle: "PHP での Web 用 PDF ドキュメントの最適化"
type: docs
weight: 60
url: /ja/java/optimize-pdf-document-for-the-web-in-php/
description: "Aspose.PDF を使用して、PHP で PDF ドキュメントを最適化し、Web 上でのパフォーマンスを向上させ、ファイルサイズを削減する方法を学びます。"
lastmod: "2026-10-06"
---
## Aspose.PDF - Web 用に PDF の最適化

**Aspose.PDF Java for PHP** を使用して Web 用に PDF ドキュメントを最適化するには、**Optimize** クラスの **optimize_web** メソッドを呼び出すだけです。

PHP コード

```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```

**実行コードをダウンロード**

ダウンロード **Web 用に最適化された PDF (Aspose.PDF)** は、以下に記載されたソーシャルコーディングサイトのいずれかから行えます。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
