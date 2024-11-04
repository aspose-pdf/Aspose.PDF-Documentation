---
title: PDFをPDF/A形式に変換する方法（Python）
linktitle: PDFをPDF/A形式に変換
type: docs
weight: 100
url: /python-java/convert-pdf-to-pdfa/
lastmod: "2023-04-06"
description: このトピックでは、Aspose.PDF for Pythonを使用してPDFファイルをPDF/A準拠のPDFファイルに変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Python**を使用すると、PDFファイルを<abbr title="Portable Document Format / A">PDF/A</abbr>準拠のPDFファイルに変換できます。これを行う前に、ファイルを検証する必要があります。このトピックではその方法を説明します。

{{% alert color="primary" %}}

PDF/Aの準拠を検証するために、Adobe Preflightを使用しています。市場に出回っているすべてのツールには、PDF/A準拠の「表現」がそれぞれあります。参考としてPDF/A検証ツールに関するこの記事をご確認ください。Aspose.PDFがPDFファイルを生成する際の検証には、PDFに関連するすべての中心にあるAdobe製品を選びました。

{{% /alert %}}

ファイルはDocumentクラスのConvertメソッドを使用して変換します。
 PDFをPDF/A準拠ファイルに変換する前に、Validateメソッドを使用してPDFを検証してください。検証結果はXMLファイルに保存され、この結果はConvertメソッドにも渡されます。また、ConvertErrorAction列挙を使用して変換できない要素に対するアクションを指定することもできます。

{{% alert color="success" %}}
**PDFをPDF/Aにオンラインで変換してみましょう**

Aspose.PDF for Pythonは、オンラインで無料のアプリケーション["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)を提供しており、そこで機能と品質を確認することができます。

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## PDFファイルをPDF/A-1bに変換する

以下のコードスニペットは、PDFファイルをPDF/A-1b準拠のPDFに変換する方法を示しています。

```python
from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
# PDFドキュメントを開く
document = Api.Document(input_pdf)
# PDF/A準拠ドキュメントに変換する
document.convert(output_log, Api.PdfFormat.PDF_A_1B, Api.ConvertErrorAction.Delete)
# 出力ドキュメントを保存する
document.save(output_pdf)
```