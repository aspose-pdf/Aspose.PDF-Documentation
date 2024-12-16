---
title: PythonでHTMLをPDFに変換する
linktitle: HTMLをPDFファイルに変換
type: docs
weight: 40
url: /ja/python-java/convert-html-to-pdf/
lastmod: "2023-04-06"
description: このトピックでは、Aspose.PDFを使用してHTMLをPDFおよびMHTMLをPDFに変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概要

Aspose.PDF for Python via Javaは、アプリケーション内でウェブページや生のHTMLコードからPDFファイルを作成できるプロフェッショナルなソリューションです。

この記事では、Pythonを使用して**HTMLをPDFに変換する方法**を説明します。以下のトピックをカバーしています。

_フォーマット_: **HTML**
- [Python HTMLをPDFに](#python-html-to-pdf)
- [Python HTMLをPDFに変換](#python-html-to-pdf)
- [Python HTMLをPDFに変換する方法](#python-html-to-pdf)

## Python HTMLをPDFに変換

**Aspose.PDF for Python**は、既存のHTMLドキュメントをシームレスにPDFに変換できるPDF操作APIです。HTMLをPDFに変換するプロセスは柔軟にカスタマイズできます。

## HTMLをPDFに変換

以下のPythonコードサンプルは、HTMLドキュメントをPDFに変換する方法を示しています。

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) クラスのインスタンスを作成します。
2. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトを初期化します。
3. **Document.Save()** メソッドを呼び出して出力PDFドキュメントを保存します。

```python

from asposepdf import Api


# ライセンスを初期化します
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# バイト配列からの変換
documentName = "input.html"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array, Api.LoadFormat.HTML)
documentOutName = "result_fromHtml.pdf"
doc.save(documentOutName)

# ファイルからの変換
documentName = "input.html"
doc = Api.Document(documentName, Api.LoadFormat.HTML)
documentOutName = "result2_fromHtml.pdf"
doc.save(documentOutName)
```

{{% alert color="success" %}}
**HTMLをPDFにオンラインで変換してみる**


Asposeは、機能と品質を調査するために試すことができるオンライン無料アプリケーション ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf) を提供しています。

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}