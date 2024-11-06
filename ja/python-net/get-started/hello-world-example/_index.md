title: Hello WorldをPythonで使用する例
linktitle: Hello Worldの例
type: docs
weight: 20
url: ja/python-net/hello-world-example/
description: このサンプルは、Aspose.PDF for Python via .NETを使用して、Hello Worldというテキストを含むシンプルなPDFドキュメントを作成する方法を示しています。
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

「Hello World」の例は、特定のプログラミング言語において最も簡単な構文とプログラムを示します。開発者は、デバイスの画面に「Hello World」と表示する方法を学ぶことで、基本的なプログラミング言語の構文を紹介されます。したがって、伝統的に私たちのライブラリとの出会いをこれから始めます。

この記事では、「Hello World!」というテキストを含むPDFドキュメントを作成します。環境に**Aspose.PDF for Python via .NET**をインストールした後、以下のコードサンプルを実行して、Aspose.PDF APIの動作を確認できます。

以下のコードスニペットはこれらのステップに従います：

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトをインスタンス化する  
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)を追加する  
1. [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) オブジェクトを作成する  
1. ページの[paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) コレクションにTextFragmentを追加する  
1. 結果のPDFドキュメントを[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)する  

以下のコードスニペットは、.NET API経由でPython用Aspose.PDFの動作を示す「Hello World」プログラムです。

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