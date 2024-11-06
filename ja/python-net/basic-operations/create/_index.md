---
title: プログラムでPDFドキュメントを作成する
linktitle: PDFを作成
type: docs
weight: 10
url: ja/python-net/create-document/
description: このページでは、Aspose.PDF for Python via .NETライブラリを使用して、PDFドキュメントをゼロから作成する方法を説明します。
---

開発者にとって、プログラムでPDFファイルを生成する必要があるシナリオは多く存在します。あなたのソフトウェアでPDFレポートやその他のPDFファイルをプログラムで生成する必要があるかもしれません。一から自分のコードや関数を書くのは非常に長く非効率的です。PythonでPDFファイルを作成するには、より良い解決策があります - **Aspose.PDF for Python via .NET**です。

## Pythonを使用してPDFファイルを作成する方法

Pythonを使用してPDFファイルを作成するには、次の手順を使用できます。

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスのオブジェクトを作成します。

1. [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトを Document オブジェクトの [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) コレクションに追加します
1. [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) をページの [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) コレクションに追加します
1. 結果として得られる PDF ドキュメントを保存します

```python

    import aspose.pdf as ap

    # ドキュメントオブジェクトを初期化
    document = ap.Document()
    # ページを追加
    page = document.pages.add()
    # テキストフラグメントオブジェクトを初期化
    text_fragment = ap.text.TextFragment("Hello,world!")
    # 新しいページにテキストフラグメントを追加
    page.paragraphs.add(text_fragment)
    # 更新されたPDFを保存
    document.save("output.pdf")
```