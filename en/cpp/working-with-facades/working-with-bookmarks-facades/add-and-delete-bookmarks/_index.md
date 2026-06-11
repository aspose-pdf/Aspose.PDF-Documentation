---

title: Add and Delete Bookmarks

linktitle: Add and Delete Bookmarks

type: docs

weight: 10

url: /cpp/add-and-delete-bookmarks/

description: Learn how to manage bookmarks in PDF files, including adding and deleting, using C++ and Aspose.PDF for better document navigation.

---



## <ins>**Add Bookmark**

PdfBookmarkEditor class allows you to add bookmarks inside PDF document. CreateBookmarkOfPage method offered by this class, enables you to create bookmark, which will target to the specified page number. Following code snippet demonstrates this feature of the Aspose.PDF for C++ API:

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

## <ins>**Add Child Bookmark in existing document**

You can add child bookmarks in an existing PDF file using **PdfBookmarkEditor** class. In order to add child bookmarks, you need to create **Bookmarks** and*Bookmark* objects. You can add individual **Bookmark** objects into **Bookmarks** object. You also need to create a **Bookmark** object and set its **ChildItem** property to **Bookmarks** object. You then need to pass this **Bookmark** object with **ChildItem** to the **CreateBookmarks** method. Finally, you need to save the updated PDF using **Save**method of the **PdfBookmarkEditor** class. The following code snippet shows you how to add child bookmarks in an existing PDF file.

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

## <ins>**Delete All Bookmarks from PDF file**

You can delete all the bookmarks from the PDF file using **DeleteBookmarks** method without any parameters. First of all, you need to create an object of **PdfBookmarkEditor** class and bind the input PDF file using **BindPdf** method. After that, you need to call the **DeleteBookmarks** method and then save the updated PDF file using **Save** method. The following code snippet shows you how to delete all the bookmarks from the PDF file.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfBookmarkEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Bookmarks\\DeleteAllBookmarks.pdf");
// Delete All Bookmarks
editor->DeleteBookmarks();
// Save the document
editor->Save(L"..\\Data\\Bookmarks\\DeleteAllBookmarks_out.pdf");
```

## <ins>**Delete a Particular Bookmark from a PDF File**

In order to delete a particular bookmark, you need to call **DeleteBookmarks** method with string (title) parameter. The **title** here represents the bookmark to be deleted from the PDF. Create an object of **PdfBookmarkEditor** class and bind input PDF file using **BindPdf** method. After that, call **DeleteBookmarks** method and then save the updated PDF file using **Save** method. The following code snippet shows you how to delete a particular bookmark from a PDF file.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfBookmarkEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Bookmarks\\DeleteParticularBookmark.pdf");
// Delete Particular Bookmarks
editor->DeleteBookmarks(L"Parent Outline");
// Save the document
editor->Save(L"..\\Data\\Bookmarks\\DeleteParticularBookmark_out.pdf");
```
