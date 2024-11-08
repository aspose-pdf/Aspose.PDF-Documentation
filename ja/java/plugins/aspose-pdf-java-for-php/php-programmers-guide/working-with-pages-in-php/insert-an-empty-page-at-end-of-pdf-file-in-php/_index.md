---
title: PDFファイルの末尾に空白ページを挿入する方法（PHP）
type: docs
weight: 60
url: /ja/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFファイルの末尾に空白ページを挿入

**Aspose.PDF Java for PHP**を使用してPDFドキュメントの末尾に空白ページを挿入するには、**InsertEmptyPageAtEndOfFile**クラスを呼び出すだけです。

PHPコード

```php

# 対象のドキュメントを開く
$pdf = new Document($dataDir . 'input1.pdf');

# PDFに空白ページを挿入する
$pdf->getPages()->add();

# 結合された出力ファイル（対象のドキュメント）を保存
$pdf->save($dataDir . "output.pdf");

print "空白ページが正常に追加されました！" . PHP_EOL;

```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから、**PDFファイルの末尾に空白ページを挿入する (Aspose.PDF)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)