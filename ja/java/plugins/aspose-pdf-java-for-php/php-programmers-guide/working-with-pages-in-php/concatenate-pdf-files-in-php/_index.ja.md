---
title: PHPでPDFファイルを連結する
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFファイルを連結する

**Aspose.PDF Java for PHP**を使用してPDFファイルを連結するには、**ConcatenatePdfFiles**クラスを呼び出します。

PHPコード

```php

# 対象のドキュメントを開く
$pdf1 = new Document($dataDir . 'input1.pdf');

# ソースドキュメントを開く
$pdf2 = new Document($dataDir . 'input2.pdf');

# ソースドキュメントのページを対象のドキュメントに追加する
$pdf1->getPages()->add($pdf2->getPages());

# 連結された出力ファイル（対象のドキュメント）を保存する
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "新しいドキュメントが保存されました。出力ファイルを確認してください。" . PHP_EOL;

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから **Concatenate PDF Files (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)