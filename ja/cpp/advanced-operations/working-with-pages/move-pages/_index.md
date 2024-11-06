---
title: PDFページをプログラムで移動 C++
linktitle: PDFページを移動
type: docs
weight: 20
url: ja/cpp/move-pages/
description: Aspose.PDF for C++を使用して、PDFファイル内の希望する場所または最後にページを移動してみてください。
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## あるPDFドキュメントから別のPDFドキュメントへのページ移動

ドキュメント内でPDFページを移動することは非常に興味深く、人気のあるタスクです。
このトピックでは、C++を使用して1つのPDFドキュメントから別のドキュメントの最後にページを移動する方法を説明します。
ページを移動するには、次の手順を実行します：

1. ソースPDFファイルを使用して[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)コレクションからページを取得します。
1. ページを移動先ドキュメントに[追加](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1)します。
1. Saveメソッドを使用して出力PDFを保存します。
1. [削除](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) ソースドキュメント内のページ。  
1. 保存メソッドを使用して、ソースPDFを保存します。

次のコードスニペットは、1ページを移動する方法を示しています。

```cpp
void MovePage()
{
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    dstDocument->get_Pages()->Add(page);
    // 出力ファイルを保存
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(dstFileName);
}
```

## 複数のページを1つのPDFドキュメントから別のPDFドキュメントに移動する

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスオブジェクトを作成します。  
1. 移動するページ番号を指定した配列を定義します。  
1. 配列をループして実行します:
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) コレクションからページを取得します。
1. ページを宛先ドキュメントに[追加](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1)します。
1. Save メソッドを使用して出力 PDF を保存します。
1. ソースドキュメントのページを[削除](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15)します。
1. Save メソッドを使用してソース PDF を保存します。

次のコードスニペットは、PDF ファイルの末尾に空のページを挿入する方法を示しています。

```cpp
void MoveBunchPages()
{
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();


    auto pages = MakeArray<int>({ 1,3 });

    for (auto pageIndex : pages)
    {
        auto page = srcDocument->get_Pages()->idx_get(pageIndex);
        dstDocument->get_Pages()->Add(page);
    }
    // 出力ファイルを保存
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete();
    srcDocument->Save(dstFileName);
}
```
## 現在のPDFドキュメント内でページを新しい位置に移動する

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)コレクションからページを取得します。
1. ページを新しい位置（例えば最後）に[追加](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1)します。
1. 前の位置のページを[削除](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15)します。
1. Saveメソッドを使用して出力PDFを保存します。

```cpp
void MovePagesInOnePDF()
{
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    srcDocument->get_Pages()->Add(page);
    srcDocument->get_Pages()->Delete(2);

    // 出力ファイルを保存
    srcDocument->Save(dstFileName);
}
```