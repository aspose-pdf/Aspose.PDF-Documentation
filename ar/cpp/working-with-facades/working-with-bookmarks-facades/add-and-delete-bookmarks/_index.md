---
title: إضافة وحذف العلامات المرجعية
type: docs
weight: 10
url: /ar/cpp/add-and-delete-bookmarks/
---

## <ins>**إضافة علامة مرجعية**
تسمح لك فئة PdfBookmarkEditor بإضافة علامات مرجعية داخل مستند PDF. تتيح لك طريقة CreateBookmarkOfPage المقدمة من هذه الفئة إنشاء علامة مرجعية، تستهدف رقم الصفحة المحدد. يوضح مقتطف الشيفرة التالي هذه الميزة في Aspose.PDF لواجهة برمجة التطبيقات C++:



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
## <ins>**إضافة علامة مرجعية فرعية في المستند الحالي**
يمكنك إضافة علامات مرجعية فرعية في ملف PDF موجود باستخدام فئة **PdfBookmarkEditor**. من أجل إضافة إشارات مرجعية فرعية، تحتاج إلى إنشاء كائنات **Bookmarks** و*Bookmark*. يمكنك إضافة كائنات **Bookmark** الفردية إلى كائن **Bookmarks**. تحتاج أيضًا إلى إنشاء كائن **Bookmark** وتعيين خاصية **ChildItem** إلى كائن **Bookmarks**. ثم تحتاج إلى تمرير هذا الكائن **Bookmark** مع **ChildItem** إلى طريقة **CreateBookmarks**. أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة **Save** من فئة **PdfBookmarkEditor**. يوضح لك مقتطف الشيفرة التالي كيفية إضافة إشارات مرجعية فرعية في ملف PDF موجود.

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
## <ins>**حذف جميع الإشارات المرجعية من ملف PDF**
يمكنك حذف جميع الإشارات المرجعية من ملف PDF باستخدام طريقة **DeleteBookmarks** بدون أي معلمات. أولاً، تحتاج إلى إنشاء كائن من فئة **PdfBookmarkEditor** وربط ملف PDF المدخل باستخدام طريقة **BindPdf**. بعد ذلك، تحتاج إلى استدعاء طريقة **DeleteBookmarks** ثم حفظ ملف PDF المحدث باستخدام طريقة **Save**. يوضح لك مقتطف الشيفرة التالي كيفية حذف جميع العلامات المرجعية من ملف PDF.

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

## <ins>**حذف علامة مرجعية معينة من ملف PDF**

لحذف علامة مرجعية معينة، تحتاج إلى استدعاء طريقة **DeleteBookmarks** مع معلمة سلسلة (العنوان). يمثل **العنوان** هنا العلامة المرجعية المراد حذفها من ملف PDF. قم بإنشاء كائن من فئة **PdfBookmarkEditor** واربط ملف PDF المدخل باستخدام طريقة **BindPdf**. بعد ذلك، استدع طريقة **DeleteBookmarks** ثم احفظ ملف PDF المحدث باستخدام طريقة **Save**. يوضح لك مقتطف الشيفرة التالي كيفية حذف علامة مرجعية معينة من ملف PDF.

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