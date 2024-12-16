---
title: Split PDFをプログラムで行う
linktitle: PDFファイルを分割する
type: docs
weight: 60
url: /ja/cpp/split-pdf-document/
description: このトピックでは、C++でPDFページを個別のPDFファイルに分割する方法を示します。
lastmod: "2022-09-01"
sitemap:
    changefreq: "monthy"
    priority: 0.7
---

## ライブ例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) は、プレゼンテーション分割機能がどのように機能するかを調査できる無料のオンラインWebアプリケーションです。

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

このトピックでは、C++アプリケーションでPDFページを個別のPDFファイルに分割する方法を示します。C++を使用してPDFページを単一ページのPDFファイルに分割するには、次の手順に従います：

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトの [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) コレクションを通じてPDFドキュメントのページをループする
1. 各反復で、新しいDocumentオブジェクトを作成し、個別の[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)オブジェクトを空のドキュメントにコピーします。
1. Saveメソッドを使用して新しいPDFを保存します。

以下のC++コードスニペットは、PDFページを個別のPDFファイルに分割する方法を示しています。

```cpp
void SplittingDocuments() {
    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名のための文字列
    String documentFileName("sample.pdf");
    
    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // すべてのページをループする
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->CopyPage(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```