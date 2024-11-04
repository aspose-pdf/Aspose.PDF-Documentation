---
title: PDFドキュメントを作成する
linktitle: PDFを作成
type: docs
weight: 10
url: /python-cpp/create-document/
description: このページでは、Aspose.PDF for Python via C++ライブラリを使用してゼロからPDFドキュメントを作成する方法について説明します。
---

開発者にとって、PDFファイルをプログラムで生成する必要があるシナリオは数多くあります。 ソフトウェア内でPDFレポートやその他のPDFファイルをプログラムで生成する必要があるかもしれません。 独自のコードや関数をゼロから書くのは非常に長く非効率的です。 PythonでPDFファイルを作成するには、より良い解決策があります - **Aspose.PDF for Python via C++**です。

## Pythonを使用してPDFファイルを作成する

Pythonを使用してPDFファイルを作成するには、次の手順を使用できます。

* Aspose.PDF for Python via C++ライブラリからすべてのクラスとメソッドをインポートします。
* [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/)を使用して、空のPDFドキュメントを表す新しいDocumentオブジェクトを作成します。

* ドキュメント内のすべてのページを含む[document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)オブジェクトを取得します。
 * ページコレクションの最後に新しいページを追加し、追加されたページを表すPageオブジェクトを返します。[page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/)
* 現在の作業ディレクトリに指定された名前でドキュメントをファイルに保存します。
* ドキュメントへのハンドルを閉じ、それに関連するリソースを解放します。

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```


## DOMに基づいてPDFファイルを作成

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```