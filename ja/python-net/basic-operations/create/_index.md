---
title: プログラムで PDF ドキュメントを作成
linktitle: PDF ファイルを作成
type: docs
weight: 10
url: /ja/python-net/create-document/
description: このページでは、.NET ライブラリ経由で Aspose.PDF for Python を使用してゼロから PDF ドキュメントを作成する方法について説明します。
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使って PDF ファイルを生成する
Abstract: ソフトウェア開発では、特にレポートやその他の文書を作成する場合には、プログラムで PDF ファイルを生成することが一般的な要件です。このタスク用のカスタムコードを書くのは非効率的で時間がかかることがあります。その代わり、開発者は Python を使用して PDF ファイルを作成するための堅牢なソリューションである **Aspose.PDF for Python via .NET ** を利用することができます。このプロセスでは、「Document」オブジェクトを作成し、そのドキュメントの「Pages」コレクションに「Page」オブジェクトを追加し、ページの「Paragraphs」コレクションに「TextFragment」を挿入して、ドキュメントを保存します。Python のサンプルコードスニペットではこれらの手順を示し、Aspose.PDF を使用して PDF ファイルを簡単に生成できることを紹介しています。
---

開発者にとって、プログラムで PDF ファイルを生成する必要が生じるシナリオは多数あります。ソフトウェアで PDF レポートやその他の PDF ファイルをプログラム的に生成しなければならない場合があります。独自のコードや関数を一から作成するのはかなり時間がかかり、非効率的です。Python で PDF ファイルを作成するには、**.NET 経由の Python 用の Aspose.PDF というよりよい解決策があります。

## パイソンを使用してPDFファイルを作成する方法

Python を使用して PDF ファイルを作成するには、次の手順を使用できます。

1. のオブジェクトを作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス
1. を追加 [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) への対象 [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) ドキュメントオブジェクトのコレクション
1. 追加 [テキストフラグメント](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) に [段落](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) ページのコレクション
1. 結果の PDF ドキュメントを保存する

```python
import aspose.pdf as ap

# Initialize document object
document = ap.Document()
# Add page
page = document.pages.add()
# Add text to new page
page.paragraphs.add(ap.text.TextFragment("Hello World!"))
# Define output file path
output_pdf = "output.pdf"
# Save updated PDF
output_pdf = "output.pdf"
document.save(output_pdf)
```
