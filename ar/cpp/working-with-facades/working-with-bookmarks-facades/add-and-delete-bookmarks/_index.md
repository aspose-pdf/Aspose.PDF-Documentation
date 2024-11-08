---
title: إضافة وحذف العلامات المرجعية
type: docs
weight: 10
url: /ar/cpp/add-and-delete-bookmarks/
---

## <ins>**إضافة علامة مرجعية**
تسمح لك فئة PdfBookmarkEditor بإضافة علامات مرجعية داخل مستند PDF. تتيح لك طريقة CreateBookmarkOfPage المقدمة من هذه الفئة إنشاء علامة مرجعية، تستهدف رقم الصفحة المحدد. يوضح مقتطف الشيفرة التالي هذه الميزة في Aspose.PDF لواجهة برمجة التطبيقات C++:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateBookmark-1.cpp" >}}
## <ins>**إضافة علامة مرجعية فرعية في المستند الحالي**
يمكنك إضافة علامات مرجعية فرعية في ملف PDF موجود باستخدام فئة **PdfBookmarkEditor**. من أجل إضافة إشارات مرجعية فرعية، تحتاج إلى إنشاء كائنات **Bookmarks** و*Bookmark*. يمكنك إضافة كائنات **Bookmark** الفردية إلى كائن **Bookmarks**. تحتاج أيضًا إلى إنشاء كائن **Bookmark** وتعيين خاصية **ChildItem** إلى كائن **Bookmarks**. ثم تحتاج إلى تمرير هذا الكائن **Bookmark** مع **ChildItem** إلى طريقة **CreateBookmarks**. أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة **Save** من فئة **PdfBookmarkEditor**. يوضح لك مقتطف الشيفرة التالي كيفية إضافة إشارات مرجعية فرعية في ملف PDF موجود.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateChildBookmark-1.cpp" >}}
## <ins>**حذف جميع الإشارات المرجعية من ملف PDF**
يمكنك حذف جميع الإشارات المرجعية من ملف PDF باستخدام طريقة **DeleteBookmarks** بدون أي معلمات. أولاً، تحتاج إلى إنشاء كائن من فئة **PdfBookmarkEditor** وربط ملف PDF المدخل باستخدام طريقة **BindPdf**. بعد ذلك، تحتاج إلى استدعاء طريقة **DeleteBookmarks** ثم حفظ ملف PDF المحدث باستخدام طريقة **Save**. يوضح لك مقتطف الشيفرة التالي كيفية حذف جميع العلامات المرجعية من ملف PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteAllBookmarks-1.cpp" >}}

## <ins>**حذف علامة مرجعية معينة من ملف PDF**

لحذف علامة مرجعية معينة، تحتاج إلى استدعاء طريقة **DeleteBookmarks** مع معلمة سلسلة (العنوان). يمثل **العنوان** هنا العلامة المرجعية المراد حذفها من ملف PDF. قم بإنشاء كائن من فئة **PdfBookmarkEditor** واربط ملف PDF المدخل باستخدام طريقة **BindPdf**. بعد ذلك، استدع طريقة **DeleteBookmarks** ثم احفظ ملف PDF المحدث باستخدام طريقة **Save**. يوضح لك مقتطف الشيفرة التالي كيفية حذف علامة مرجعية معينة من ملف PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteBookmark-1.cpp" >}}