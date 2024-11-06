```
title: ブックマークの追加と削除
linktitle: ブックマークの追加と削除
type: docs
weight: 10
url: ja/cpp/add-and-delete-bookmark/
description: このトピックでは、C++ライブラリを使用してPDFドキュメントにブックマークを追加する方法を説明します。また、PDFドキュメントからすべてまたは特定のブックマークを削除することもできます。
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントにブックマークを追加する

ブックマークは、[OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) コレクションの Document オブジェクト内に保持され、[OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) コレクション内にあります。

PDFにブックマークを追加するには:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) オブジェクトを使用してPDFドキュメントを開きます。
1. ブックマークを作成し、そのプロパティを定義します。
1.
``` [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) コレクションを Outlines コレクションに追加します。

次のコードスニペットは、PDF ドキュメントにブックマークを追加する方法を示しています。

```cpp
void AddBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");


// ブックマークオブジェクトを作成する

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Test Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// 目的のページ番号を設定する

pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// ドキュメントのアウトラインコレクションにブックマークを追加する

pdfDocument->get_Outlines()->Add(pdfOutline);


// 更新されたドキュメントを保存する

pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## PDF ドキュメントに子ブックマークを追加する

ブックマークはネスト可能で、親ブックマークと子ブックマークの階層関係を示します。 この記事では、PDFに子ブックマーク、つまり第2レベルのブックマークを追加する方法を説明します。

PDFファイルに子ブックマークを追加するには、まず親ブックマークを追加します。

1. ドキュメントを開きます。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/)にブックマークを追加し、そのプロパティを定義します。
1. OutlineItemCollectionをDocumentオブジェクトの[OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/)コレクションに追加します。

子ブックマークは、上記で説明した親ブックマークと同様に作成されますが、親ブックマークのOutlinesコレクションに追加されます。

以下のコードスニペットは、PDFドキュメントに子ブックマークを追加する方法を示しています。

```cpp
void AddChildBookmark() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// ドキュメントを開く

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");

// 親ブックマークオブジェクトを作成

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Parent Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// 子ブックマークオブジェクトを作成

auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfChildOutline->set_Title(u"Child Outline");

pdfChildOutline->set_Italic(true);

pdfChildOutline->set_Bold(true);

// 親ブックマークのコレクションに子ブックマークを追加

pdfOutline->Add(pdfChildOutline);

// ドキュメントのアウトラインコレクションに親ブックマークを追加

pdfDocument->get_Outlines()->Add(pdfOutline);

// 出力を保存

pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```
## PDFドキュメントからすべてのブックマークを削除する

PDF内のすべてのブックマークは、[OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) コレクションに保持されています。この記事では、PDFファイルからすべてのブックマークを削除する方法を説明します。

PDFファイルからすべてのブックマークを削除するには：

1. [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) コレクションのDeleteメソッドを呼び出します。
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) オブジェクトのSaveメソッドを使用して、変更されたファイルを保存します。

次のコードスニペットは、PDFドキュメントからすべてのブックマークを削除する方法を示しています。

```cpp
void DeleteAllBookmarksFromPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// ドキュメントを開く

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");


// すべてのブックマークを削除

pdfDocument->get_Outlines()->Delete();


// 更新されたファイルを保存

pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```


## PDFドキュメントから特定のブックマークを削除する

[PDFドキュメントからすべての添付ファイルを削除する](https://docs.aspose.com/pdf/cpp/working-with-attachments/) は、PDFファイルからすべての添付ファイルを削除する方法を示しています。特定の添付ファイルのみを削除することも可能です。

PDFファイルから特定のブックマークを削除するには：

1. ブックマークのタイトルをパラメーターとして[OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/)コレクションのDeleteメソッドに渡します。
1. 次に、DocumentオブジェクトのSaveメソッドで更新されたファイルを保存します。

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)クラスは[OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/)コレクションを提供します。[Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b)メソッドは、メソッドに渡されたタイトルを持つブックマークを削除します。

以下のコードスニペットは、PDFドキュメントから特定のブックマークを削除する方法を示しています。

```cpp
void DeleteParticularBookmarkPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// ドキュメントを開く

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");


// タイトルで特定のアウトラインを削除

pdfDocument->get_Outlines()->Delete(u"Child Outline");


// 更新されたファイルを保存

pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```