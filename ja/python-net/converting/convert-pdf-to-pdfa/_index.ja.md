---
title: PythonでPDFをPDF/A形式に変換
linktitle: PDFをPDF/A形式に変換
type: docs
weight: 100
url: /python-net/convert-pdf-to-pdfa/
lastmod: "2022-12-23"
description: このトピックでは、Aspose.PDF for Pythonを使用してPDFファイルをPDF/A準拠のPDFファイルに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Python**を使用すると、PDFファイルを<abbr title="Portable Document Format / A">PDF/A</abbr>準拠のPDFファイルに変換することができます。その前に、ファイルを検証する必要があります。このトピックではその方法を説明します。

{{% alert color="primary" %}}

PDF/A準拠の検証にはAdobe Preflightを使用しています。市場にあるすべてのツールには、それぞれ独自のPDF/A準拠の「表現」があります。参考のためにPDF/A検証ツールに関するこの記事を確認してください。Aspose.PDFが生成するPDFファイルを確認するためにAdobe製品を選んだのは、AdobeがPDFに関連するすべての中心に位置しているからです。

{{% /alert %}}

DocumentクラスのConvertメソッドを使用してファイルを変換します。
 PDFをPDF/A準拠のファイルに変換する前に、Validateメソッドを使用してPDFを検証します。検証結果はXMLファイルに保存され、その結果はConvertメソッドにも渡されます。ConvertErrorAction列挙を使用して変換できない要素のアクションを指定することもできます。

{{% alert color="success" %}}
**PDFをPDF/Aにオンラインで変換してみる**

Aspose.PDF for Pythonは、オンラインで無料のアプリケーション["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## PDFファイルをPDF/A-1bに変換する

次のコードスニペットは、PDFファイルをPDF/A-1b準拠のPDFに変換する方法を示しています。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
    output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)
    # PDF/A準拠のドキュメントに変換
    document.convert(output_log, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    # 出力ドキュメントを保存
    document.save(output_pdf)
```