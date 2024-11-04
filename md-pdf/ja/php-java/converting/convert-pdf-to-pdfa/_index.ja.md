---
title: PDFをPDF/A形式に変換する
linktitle: PDFをPDF/A形式に変換する
type: docs
weight: 100
url: /php-java/convert-pdf-to-pdfa/
lastmod: "2024-05-20"
description: このトピックでは、Aspose.PDFがPDFファイルをPDF/A準拠のPDFファイルに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for PHP**を使用すると、PDFファイルをPDF/A準拠のPDFファイルに変換することができます。その前に、ファイルを検証する必要があります。この記事では、その方法を説明します。

PDF/A準拠の検証にはAdobeのPreflightを使用しています。市場に出回っているすべてのツールは、それぞれ独自のPDF/A準拠の「表現」を持っています。参考として、[PDF/A検証ツール](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results)に関する記事を確認してください。Aspose.PDFが生成するPDFファイルを検証するためにAdobe製品を選んだのは、AdobeがPDFに関連するすべての中心にあるからです。

PDFをPDF/A準拠のファイルに変換する前に、validateメソッドを使用してPDFを検証してください。
 検証結果はXMLファイルに保存され、この結果はconvertメソッドにも渡されます。変換できない要素に対するアクションを[ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction)列挙で指定することもできます。

## PDFからPDF/Aへの変換

次のコードスニペットは、PDFファイルをPDF/A-1b準拠のPDFに変換する方法を示しています。

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルを読み込みます。
$document = new Document($inputFile);

// ドキュメントをPDF/A-1a形式に変換し、ログファイルとエラーアクションを指定します。
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// 変換されたドキュメントを出力ファイルに保存します。
$document->save($outputFile);
```

検証のみを行うには、次のコード行を使用します：

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルを読み込みます。
$document = new Document($inputFile);

// ドキュメントをPDF/A-1a形式に変換し、ログファイルとエラーアクションを指定します。
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// PDFをPDF/A-1aとして検証します。
if ($document->validate("validation-result-A1A.xml", PdfFormat.PDF_A_1A))
{
    echo "Valid";
}
else
{
    echo "Not valid";
}
```

{{% alert color="primary" %}}
**PDFをPDF/Aにオンラインで変換してみてください**

Aspose.PDF for PHPは、オンラインで無料のアプリケーション["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)を提供しており、その機能性と品質を調査することができます。

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}