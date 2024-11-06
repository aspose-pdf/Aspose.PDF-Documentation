---
title: PHPでSVGファイルをPDF形式に変換する
type: docs
weight: 40
url: ja/java/convert-svg-file-to-pdf-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - SVGをPDFに変換する

**Aspose.PDF Java for PHP**を使用してSVGファイルをPDF形式に変換するには、単に**SvgToPdf**モジュールを呼び出します。

PHPコード

```php
# SVGロードオプションを使用してLoadOptionオブジェクトをインスタンス化する
$options = new SvgLoadOptions();

# ドキュメントオブジェクトを作成する
$pdf = new Document($dataDir . 'Example.svg', $options);

# 出力をXLS形式で保存する
$pdf->save($dataDir . "SVG.pdf");

print "ドキュメントが正常に変換されました";

```

**実行コードをダウンロードする**

以下に示すいずれかのソーシャルコーディングサイトから、**Convert SVG to PDF (Aspose.PDF)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)