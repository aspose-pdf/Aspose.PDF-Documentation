---
title: ブックマークの取得、更新、展開 
linktitle: ブックマークの取得、更新、展開
type: docs
weight: 20
url: ja/cpp/get-update-and-expand-bookmark/
description: Aspose.PDF for C++ ライブラリを使用して PDF ファイル内のブックマークを取得、更新できます。
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ブックマークの取得

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトの [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) コレクションには、PDF ファイルのすべてのブックマークが含まれています。この記事では、PDF ファイルからブックマークを取得する方法と、特定のブックマークがどのページにあるかを取得する方法について説明します。

ブックマークを取得するには、[OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) コレクションをループして、OutlineItemCollection 内の各ブックマークを取得します。 The OutlineItemCollectionは、すべてのブックマークの属性へのアクセスを提供します。次のコードスニペットは、PDFファイルからブックマークを取得する方法を示しています。

```cpp
void GettingBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// ドキュメントを開く

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// すべてのブックマークをループする

for (auto outlineItem : pdfDocument->get_Outlines()) {

Console::WriteLine(u"タイトル :- " + outlineItem->get_Title());

Console::WriteLine(u"イタリックですか :- " + outlineItem->get_Italic());

Console::WriteLine(u"太字ですか :- " + outlineItem->get_Bold());

Console::WriteLine(u"色 :- {0}", outlineItem->get_Color());

}
}
```

## ブックマークのページ番号を取得する

ブックマークを追加したら、Bookmarkオブジェクトに関連付けられたdestination PageNumberを取得することで、それがどのページにあるかを確認できます。

```cpp
void GettingBookmarksPageNumber() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// PdfBookmarkEditorを作成する

auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();

// PDFファイルを開く

bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");

// ブックマークを抽出する

auto bookmarks = bookmarkEditor->ExtractBookmarks();

for (auto bookmark : bookmarks) {

String strLevelSeprator("");

for (int i = 1; i < bookmark->get_Level(); i++) {

strLevelSeprator += u"---- ";

}

Console::WriteLine(u"タイトル :- " + strLevelSeprator + bookmark->get_Title());

Console::WriteLine(u"ページ番号 :- " + strLevelSeprator + bookmark->get_PageNumber());

Console::WriteLine(u"ページアクション :- " + strLevelSeprator + bookmark->get_Action());

}
}
```
## PDFドキュメントのブックマークを更新する

PDFファイル内のブックマークを更新するには、まず、ブックマークのインデックスを指定して、DocumentオブジェクトのOutlineColletionコレクションから特定のブックマークを取得します。ブックマークを[OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection)オブジェクトに取得したら、そのプロパティを更新し、Saveメソッドを使用して更新されたPDFファイルを保存することができます。次のコードスニペットは、PDFドキュメント内のブックマークを更新する方法を示しています。

```cpp
void UpdateBookmarksInPDFDocument() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// ドキュメントを開く

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// ブックマークオブジェクトを取得

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);


// ブックマークオブジェクトを更新

pdfOutline->set_Title(u"Updated Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// ターゲットページを2に設定

pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// 出力を保存

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## PDFドキュメントで子ブックマークを更新する

子ブックマークを更新するには：

1. 親ブックマークを取得してから適切なインデックス値を使用して子ブックマークを取得することにより、PDFファイルから更新したい子ブックマークを取得します。
1. Saveメソッドを使用して更新されたPDFファイルを保存します。

{{% alert color="primary" %}}

DocumentオブジェクトのOutlineCollectionコレクションからブックマークのインデックスを指定してブックマークを取得し、親ブックマークのインデックスを指定して子ブックマークを取得します。

{{% /alert %}}

次のコードスニペットは、PDFドキュメントで子ブックマークを更新する方法を示しています。

```cpp
void UpdateChildBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// ドキュメントを開く

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// ブックマークオブジェクトを取得

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// 子ブックマークオブジェクトを取得

auto childOutline = pdfOutline->idx_get(1);


// ブックマークオブジェクトを更新

childOutline->set_Title(u"Updated Outline");

childOutline->set_Italic(true);

childOutline->set_Bold(true);

// ターゲットページを2に設定

childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// 出力を保存

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## ドキュメント閲覧時にブックマークを展開する

ブックマークは、[OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) コレクションに保持され、そのコレクション自体は [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) コレクションに含まれています。ただし、PDF ファイルを閲覧する際にすべてのブックマークが展開されている必要がある場合があります。

この要件を満たすためには、各アウトライン/ブックマーク項目のオープン状態を「開いている」と設定することができます。以下のコードスニペットは、PDF ドキュメント内の各ブックマークのオープン状態を展開として設定する方法を示しています。

```cpp
void ExpandedBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// ページ表示モードを設定、例えばサムネイル表示、全画面表示、添付ファイルパネル表示

doc->set_PageMode(PageMode::UseOutlines);

// PDF ファイル内のブックマークの総数を出力

Console::WriteLine(doc->get_Outlines()->get_Count());

// PDF ファイルのアウトラインコレクション内の各アウトラインアイテムを巡回

for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {

// アウトラインアイテムのオープン状態を設定

doc->get_Outlines()->idx_get(counter)->set_Open(true);

}

// PDF ファイルを保存

doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```