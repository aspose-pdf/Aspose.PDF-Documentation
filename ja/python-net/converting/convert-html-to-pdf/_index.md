---
title: PythonでHTMLをPDFに変換
linktitle: HTMLをPDFファイルに変換
type: docs
weight: 40
url: ja/python-net/convert-html-to-pdf/
lastmod: "2022-12-22"
description: このトピックでは、Aspose.PDFを使用してHTMLをPDFに、MHTMLをPDFに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概要

Aspose.PDF for Python via .NETは、アプリケーション内でウェブページや生のHTMLコードからPDFファイルを作成できるプロフェッショナルなソリューションです。

この記事では、Pythonを使用して**HTMLをPDFに変換する方法**を説明します。以下のトピックをカバーしています。

_フォーマット_: **HTML**
- [Python HTMLをPDFに](#python-html-to-pdf)
- [Python HTMLをPDFに変換](#python-html-to-pdf)
- [Python HTMLをPDFに変換する方法](#python-html-to-pdf)

## Python HTMLからPDFへの変換

**Aspose.PDF for Python**は、既存のHTMLドキュメントをシームレスにPDFに変換できるPDF操作APIです。HTMLからPDFへの変換プロセスは柔軟にカスタマイズ可能です。

## HTMLをPDFに変換

以下のPythonコードサンプルは、HTMLドキュメントをPDFに変換する方法を示しています。

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) クラスのインスタンスを作成します。
2. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトを初期化します。
3. **Document.Save()** メソッドを呼び出して、出力PDFドキュメントを保存します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "little_html.html"
    output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
    options = ap.HtmlLoadOptions()
    document = ap.Document(input_pdf, options)
    document.save(output_pdf)
```

{{% alert color="success" %}}
**HTMLをPDFにオンラインで変換してみてください**

Asposeはオンラインで無料のアプリケーション「[HTML to PDF](https://products.aspose.app/html/en/conversion/html-to-pdf)」を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}