---
title: PHPでPDFをSVG形式に変換
type: docs
weight: 30
url: /ja/java/convert-pdf-to-svg-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFをSVGに変換

**Aspose.PDF Java for PHP**を使用してPDFをSVG形式に変換するには、単に**PdfToSvg**モジュールを呼び出します。

PHPコード

```php

# 対象のドキュメントを開く
$pdf = new Document($dataDir . 'input1.pdf');

# SvgSaveOptionsのオブジェクトをインスタンス化する
$save_options = new SvgSaveOptions();

# SVG画像をZipアーカイブに圧縮しない
$save_options->CompressOutputToZipArchive = false;

# 出力をXLS形式で保存
$pdf->save($dataDir . "Output.svg", $save_options);

print "ドキュメントが正常に変換されました" . PHP_EOL;

```

**実行可能なコードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Convert PDF to SVG Format (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)