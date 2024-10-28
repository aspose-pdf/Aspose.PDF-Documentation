---
title: PHPでPDFドキュメントをWeb用に最適化する
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Web用にPDFを最適化

**Aspose.PDF Java for PHP**を使用してPDFドキュメントをWeb用に最適化するには、**Optimize**クラスの**optimize_web**メソッドを呼び出すだけです。

PHPコード

```php

 public static function optimize_web($dataDir=null)

{

    # PDFドキュメントを開く。

    $doc = new Document($dataDir . "input1.pdf");

    # Web用に最適化

    $doc->optimize();

    # 出力ドキュメントを保存

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Web用にPDFを最適化しました。出力ファイルを確認してください。" . PHP_EOL;

}    
```

**実行コードのダウンロード**

以下に挙げるソーシャルコーディングサイトのいずれかから**Optimize PDF for Web (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)