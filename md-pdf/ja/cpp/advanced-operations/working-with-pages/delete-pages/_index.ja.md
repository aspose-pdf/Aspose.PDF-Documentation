---
title: プログラムでPDFページを削除する
linktitle: PDFページを削除する
type: docs
weight: 30
url: /cpp/delete-pages/
description: C++ライブラリを使用してPDFファイルからページを削除できます。
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for C++を使用してPDFファイルからページを削除できます。[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)コレクションから特定のページを削除するには、以下の手順に従います。

## PDFファイルからページを削除する

1. [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7)メソッドを呼び出してページのインデックスを指定します
1. Saveメソッドを呼び出して更新されたPDFファイルを保存します
以下のコードスニペットは、C++を使用してPDFファイルから特定のページを削除する方法を示しています。

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 特定のページを削除する
    document->get_Pages()->Delete(2);

    // 更新されたPDFを保存する
    document->Save(_dataDir + inputFileName);
}
```