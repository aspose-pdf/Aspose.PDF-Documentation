---
title: PHPでPDFをDOCまたはDOCX形式に変換
type: docs
weight: 10
url: ja/java/convert-pdf-to-doc-or-docx-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFをDOCまたはDOCXに変換

**Aspose.PDF Java for PHP**を使用してPDFドキュメントをDOCまたはDOCX形式に変換するには、**PdfToDoc**モジュールを呼び出すだけです。

PHPコード

```php

# 対象ドキュメントを開く
$pdf = new Document($dataDir . 'input1.pdf');

# 連結された出力ファイル（対象ドキュメント）を保存
$pdf->save($dataDir . "output.doc");

print "ドキュメントが正常に変換されました";

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Convert PDF to DOC or DOCX (Aspose.PDF)**をダウンロードできます：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)