---
title: C++を使用してPDFをマージする
linktitle: PDFファイルをマージする
type: docs
weight: 50
url: /cpp/merge-pdf-documents/
description: このページでは、C++を使用してPDFドキュメントを1つのPDFファイルにマージする方法を説明します。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDFファイルをマージすることは簡単ではありませんが、非常に人気があります。Aspose.PDF for C++ライブラリを使用すると、PDFファイルをすばやく簡単に1つのドキュメントに結合できます。

## C++を使用してPDFファイルをマージする

2つのPDFファイルを連結するには：

1. 各入力PDFファイルを含む2つの[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトを作成します。
1. 次に、他のPDFファイルを追加したいDocumentオブジェクトに対して[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)コレクションのAddメソッドを呼び出します。
1. 2番目のドキュメントの[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)を最初のファイルに追加します。
1. 最後に、Saveメソッドを使用して出力PDFファイルを保存します。

次のコードスニペットは、PDFファイルを連結する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名のための文字列
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // ドキュメントを開く
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // 2番目のドキュメントのページを最初のドキュメントに追加する
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // 連結された出力ファイルを保存する
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## ライブ例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) は、プレゼンテーションのマージ機能がどのように機能するかを調査することができる無料のオンラインウェブアプリケーションです。

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)