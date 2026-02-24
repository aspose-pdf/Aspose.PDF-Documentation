---
title: PDF文書をプログラムで作成する
linktitle: PDFを作成
type: docs
weight: 10
url: /ja/python-net/create-document/
description: このページでは、Aspose.PDF for Python via .NET ライブラリを使用して、最初から PDF 文書を作成する方法について説明します。
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python を使用した PDF ファイルの生成
Abstract: ソフトウェア開発において、PDF ファイルをプログラムで生成することは一般的な要件であり、特にレポートやその他の文書を作成する際に必要となります。このタスクのためにカスタムコードを書くことは、非効率で時間がかかります。代わりに、開発者は **Aspose.PDF for Python via .NET** を利用でき、Python で PDF ファイルを作成するための堅牢なソリューションです。プロセスは、`Document` オブジェクトを作成し、`Pages` コレクションに `Page` オブジェクトを追加し、ページの `paragraphs` コレクションに `TextFragment` を挿入し、最後に文書を保存することです。サンプルの Python コードスニペットはこれらの手順を示し、Aspose.PDF を使用して PDF ファイルを容易に生成できることを実証します。
---

開発者にとって、プログラムで PDF ファイルを生成する必要が生じるシナリオは多数あります。ソフトウェア内で PDF レポートやその他の PDF ファイルをプログラムで生成する必要があるかもしれません。最初から自分でコードや関数を作成するのは非常に手間がかかり、非効率です。Python で PDF ファイルを作成するには、より優れたソリューションがあります - **Aspose.PDF for Python via .NET**。

## Python を使用して PDF ファイルを作成する方法

Python を使用して PDF ファイルを作成するには、以下の手順を使用できます。

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスのオブジェクトを作成する
1. Document オブジェクトの [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) コレクションに [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトを追加する
1. ページの [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) コレクションに [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) を追加する
1. 結果の PDF 文書を保存する

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```



