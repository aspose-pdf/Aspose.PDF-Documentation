---
title: ブックマークの追加と削除
type: docs
weight: 10
url: /ja/cpp/add-and-delete-bookmarks/
---

## <ins>**ブックマークを追加する**
PdfBookmarkEditor クラスを使用すると、PDF ドキュメント内にブックマークを追加できます。このクラスが提供する CreateBookmarkOfPage メソッドを使用することで、指定されたページ番号をターゲットとするブックマークを作成できます。次のコードスニペットは、Aspose.PDF for C++ API のこの機能を示しています:



```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfBookmarkEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Bookmarks\\AddBookmark.pdf");
// Create Bookmark
editor->CreateBookmarkOfPage(L"bookmark for page 1", 1);
// Save the document
editor->Save(L"..\\Data\\Bookmarks\\AddBookmark_out.pdf");
```
## <ins>**既存のドキュメントに子ブックマークを追加する**
**PdfBookmarkEditor** クラスを使用して、既存の PDF ファイルに子ブックマークを追加することができます。
``` ドキュメントに子ブックマークを追加するには、**Bookmarks** と *Bookmark* オブジェクトを作成する必要があります。個々の **Bookmark** オブジェクトを **Bookmarks** オブジェクトに追加できます。また、**Bookmarks** オブジェクトを **ChildItem** プロパティに設定した **Bookmark** オブジェクトを作成する必要があります。その後、この **ChildItem** を持つ **Bookmark** オブジェクトを **CreateBookmarks** メソッドに渡す必要があります。最後に、更新された PDF を **PdfBookmarkEditor** クラスの **Save** メソッドを使用して保存する必要があります。次のコードスニペットは、既存の PDF ファイルに子ブックマークを追加する方法を示しています。

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfBookmarkEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Bookmarks\\AddChildBookmark.pdf");
System::SharedPtr<Aspose::Pdf::Facades::Bookmark> bm1 = System::MakeObject<Aspose::Pdf::Facades::Bookmark>();
bm1->set_PageNumber(1);
bm1->set_Title(L"First child");
System::SharedPtr<Aspose::Pdf::Facades::Bookmark> bm2 = System::MakeObject<Aspose::Pdf::Facades::Bookmark>();
bm2->set_PageNumber(2);
bm2->set_Title(L"Second child");
System::SharedPtr<Aspose::Pdf::Facades::Bookmark> bm = System::MakeObject<Aspose::Pdf::Facades::Bookmark>();
bm->set_Action(L"GoTo");
bm->set_PageNumber(1);
bm->set_Title(L"Parent");
System::SharedPtr<Aspose::Pdf::Facades::Bookmarks> bms = System::MakeObject<Aspose::Pdf::Facades::Bookmarks>();
bms->Add(bm1);
bms->Add(bm2);
bm->set_ChildItem(bms);
editor->CreateBookmarks(bm);
// Save the document
editor->Save(L"..\\Data\\Bookmarks\\AddChildBookmark_out.pdf");
```
## <ins>**PDFファイルからすべてのブックマークを削除する**
**DeleteBookmarks** メソッドを使用して、パラメータなしで PDF ファイルからすべてのブックマークを削除できます。 最初に、**PdfBookmarkEditor** クラスのオブジェクトを作成し、**BindPdf** メソッドを使用して入力 PDF ファイルをバインドする必要があります。その後、**DeleteBookmarks** メソッドを呼び出し、**Save** メソッドを使用して更新された PDF ファイルを保存します。次のコードスニペットは、PDF ファイルからすべてのブックマークを削除する方法を示しています。

## <ins>**PDF ファイルから特定のブックマークを削除する**
特定のブックマークを削除するには、文字列 (タイトル) パラメーターを使用して **DeleteBookmarks** メソッドを呼び出す必要があります。ここでの **title** は、PDF から削除されるブックマークを表します。**PdfBookmarkEditor** クラスのオブジェクトを作成し、**BindPdf** メソッドを使用して入力 PDF ファイルをバインドします。その後、**DeleteBookmarks** メソッドを呼び出し、**Save** メソッドを使用して更新された PDF ファイルを保存します。次のコードスニペットは、PDF ファイルから特定のブックマークを削除する方法を示しています。