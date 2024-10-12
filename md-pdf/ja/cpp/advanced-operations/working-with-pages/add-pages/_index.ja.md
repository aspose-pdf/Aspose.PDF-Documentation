```
---
title: C++でPDFにページを追加
linktitle: ページを追加
type: docs
weight: 10
url: /cpp/add-pages/
description: この記事では、PDFファイルの任意の場所にページを挿入（追加）する方法を説明します。C++を使用してPDFファイルからページを移動、削除（削除）する方法を学びます。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

このセクションでは、**Aspose.PDF for C++**ライブラリを使用してPDFにページを追加する方法を示します。

Aspose.PDF for C++ APIは、C++を使用してPDFドキュメントのページを操作するための完全な柔軟性を提供します。

PDFドキュメントのすべてのページを[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)で管理し、PDFページを操作するために使用できます。Aspose.PDF for C++を使用すると、PDFドキュメントにファイル内の任意の場所にページを挿入したり、PDFファイルの末尾にページを追加したりできます。

## PDFファイルにページを追加または挿入

Aspose.PDF for C++を使用すると、PDFドキュメントにファイル内の任意の場所にページを挿入したり、PDFファイルの末尾にページを追加したりできます。

### 任意の場所に空のページをPDFファイルに挿入
```

以下のコードサンプルは、PDFドキュメントにページを追加する方法を説明します。

1. 入力PDFファイルを使用して[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスオブジェクトを作成します。
2. 指定されたインデックスで[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)コレクションの[Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2)メソッドを呼び出します。
3. 出力PDFを保存します。

以下のコードスニペットは、PDFファイルにページを挿入する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void InsertEmptyPageAtDesiredLocation() {
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // PDFに空のページを挿入する
    document->get_Pages()->Insert(2);

    // 出力ファイルを保存する
    document->Save(_dataDir + outputFileName);
}
```

以下のコード例では、指定されたページのパラメーターをコピーすることで、目的の場所に空のページを挿入できます。

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // PDFに空のページを挿入する
    auto pageNew = document->get_Pages()->Insert(2);

    // ページ1からページパラメーターをコピーする
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // 出力ファイルを保存する
    document->Save(_dataDir + outputFileName);
}
```

### PDFファイルの最後に空のページを追加

時々、ドキュメントが空のページで終わることを確認したいことがあります。 このトピックでは、PDF ドキュメントの最後に空白ページを挿入する方法を説明します。

PDF ファイルの最後に空白ページを挿入するには:

1. 入力 PDF ファイルを使用して [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラス オブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) コレクションの [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) メソッドを、パラメーターなしで呼び出します。
1. Save メソッドを使用して出力 PDF を保存します。

次のコード スニペットは、PDF ファイルの最後に空白ページを挿入する方法を示しています。

```cpp
void AddEmptyPageEnd() {
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // PDF ファイルの最後に空白ページを挿入
    document->get_Pages()->Add();

    // 出力ファイルを保存
    document->Save(_dataDir + outputFileName);
}
```