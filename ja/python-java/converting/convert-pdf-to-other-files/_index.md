---
title: PDFをEPUB、LaTeX、Text、XPSに変換する方法（Python）
linktitle: PDFを他の形式に変換
type: docs
weight: 90
url: /ja/python-java/convert-pdf-to-other-files/
lastmod: "2023-04-06"
description: このトピックでは、Pythonを使用してPDFファイルをEPUB、LaTeX、テキスト、XPSなどの他のファイル形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDFをEPUBに変換

{{% alert color="success" %}}
**オンラインでPDFをEPUBに変換してみてください**

Aspose.PDF for Pythonは、オンライン無料アプリケーション["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)を提供しており、機能と品質を試して調査することができます。

[![無料アプリでのAspose.PDF変換PDFをEPUBに](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="電子出版物">EPUB</abbr>**は、国際デジタル出版フォーラム（IDPF）による無料のオープンな電子書籍標準です。
 ファイルには拡張子 .epub が付いています。  
EPUB はリフロー可能なコンテンツ用に設計されており、EPUB リーダーは特定の表示デバイスに最適化されたテキストを表示できます。EPUB は固定レイアウトのコンテンツもサポートしています。この形式は、出版社や変換ハウスが社内で使用するため、および配布や販売のための単一の形式として意図されています。これは Open eBook 標準の後継です。

Aspose.PDF for Python も PDF ドキュメントを EPUB 形式に変換する機能をサポートしています。Aspose.PDF for Python には 'EpubSaveOptions' という名前のクラスがあり、EPUB ファイルを生成するために [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) メソッドの第二引数として使用できます。  
以下のコードスニペットを使用して、この要件を Python で達成してみてください。

```python

from asposepdf import Api

# ライセンスを初期化
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Epub に変換
documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.epub"
doc.save(documentOutName, Api.SaveFormat.Epub)
```

## PDFをLaTeX/TeXに変換

**Aspose.PDF for Python via Java**は、PDFをLaTeX/TeXに変換することをサポートしています。LaTeXファイル形式は特別なマークアップのあるテキストファイル形式で、高品質な組版のためのTeXベースのドキュメント準備システムで使用されます。

{{% alert color="success" %}}
**PDFをLaTeX/TeXにオンラインで変換してみてください**

Aspose.PDF for Pythonは、オンラインで無料のアプリケーション["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDFファイルをTeXに変換するには、Aspose.PDFは[LaTeXSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/latexsaveoptions/)クラスを提供しており、変換プロセス中に一時的な画像を保存するためのOutDirectoryPathプロパティを提供しています。

以下のコードスニペットは、PDFファイルをPythonでTEX形式に変換するプロセスを示しています。

```python
from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.tex"
doc.save(documentOutName, Api.SaveFormat.TeX)
```

## PDFをテキストに変換

**Aspose.PDF for Python**は、PDFドキュメント全体および単一ページをテキストファイルに変換することをサポートしています。

### PDFドキュメントをテキストファイルに変換

'TextDevice'クラスを使用してPDFドキュメントをTXTファイルに変換できます。

以下のコードスニペットは、すべてのページからテキストを抽出する方法を説明しています。

```python

from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_text"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

device = Device.TextDevice()

for i in range(0, document.getPages.size):
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.txt"
    # 特定のページを変換し、テキストファイルとして保存
    device.process(document.getPages.getPage(i + 1), imageFileName)
```


{{% alert color="success" %}}
**オンラインでPDFをテキストに変換してみてください**

Aspose.PDF for Pythonは、オンラインで無料で利用できるアプリケーション「[PDF to Text](https://products.aspose.app/pdf/conversion/pdf-to-txt)」を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF 無料アプリでPDFをテキストに変換](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDFをXPSに変換

**Aspose.PDF for Python** は、PDFファイルを<abbr title="XML Paper Specification">XPS</abbr>形式に変換する機能を提供します。PythonでPDFファイルをXPS形式に変換するために、提示されたコードスニペットを試してみましょう。

{{% alert color="success" %}}
**オンラインでPDFをXPSに変換してみてください**

Aspose.PDF for Pythonは、オンラインで無料で利用できるアプリケーション「[PDF to XPS](https://products.aspose.app/pdf/conversion/pdf-to-xps)」を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF 無料アプリでPDFをXPSに変換](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPSファイルタイプは、主にMicrosoft CorporationによるXML Paper Specificationに関連付けられています。XML Paper Specification（XPS）は、以前はMetroというコードネームで、Next Generation Print Path（NGPP）マーケティングコンセプトを包含しており、Windowsオペレーティングシステムに文書の作成と表示を統合するためのMicrosoftの取り組みです。

PDFファイルをXPSに変換するには、Aspose.PDFには[XpsSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/xpssaveoptions/)クラスがあり、これはXPSファイルを生成するために[Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods)メソッドの2番目の引数として使用されます。

次のコードスニペットは、PDFファイルをXPS形式に変換するプロセスを示しています。

```python

from asposepdf import Api

documentName = "../../testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "../../testout/out.xps"
doc.save(documentOutName, Api.SaveFormat.Xps)

```