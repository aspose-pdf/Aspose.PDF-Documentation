---
title: إنشاء إشارات مرجعية
type: docs
weight: 10
url: /net/create-bookmarks/
description: يشرح هذا القسم كيفية إنشاء إشارات مرجعية لملف PDF الخاص بك باستخدام Aspose.PDF Facades باستخدام فئة PdfBookmarkEditor.
lastmod: "2021-06-05"
draft: false
---

## إنشاء إشارات مرجعية لجميع الصفحات

من أجل إنشاء إشارات مرجعية لجميع الصفحات، تحتاج إلى استخدام طريقة [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) بدون أي معلمات. تتيح لك فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) إنشاء إشارات مرجعية لجميع صفحات ملف PDF. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثم، يجب عليك استدعاء طريقة [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) وحفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يوضح لك المقطع البرمجي التالي كيفية إنشاء إشارات مرجعية.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## إنشاء إشارات مرجعية لجميع الصفحات مع الخصائص

فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) تتيح لك إنشاء إشارات مرجعية لجميع صفحات ملف PDF وتحديد الخصائص (اللون، الغامق، المائل). يمكنك القيام بذلك بمساعدة طريقة [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). أولاً، تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثم، يجب عليك استدعاء طريقة [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) وحفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يُظهر لك جزء الشيفرة التالي كيفية إنشاء إشارات مرجعية لجميع الصفحات مع الخصائص.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## إنشاء إشارة مرجعية لصفحة معينة

يمكنك إنشاء إشارة مرجعية لصفحة معينة في ملف PDF موجود باستخدام طريقة [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). هذه الطريقة تأخذ وسيطين: عنوان العلامة المرجعية ورقم الصفحة. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثم، عليك استدعاء طريقة [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) وحفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يُظهر لك المقتطف البرمجي التالي كيفية إنشاء علامة مرجعية لصفحة معينة.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## إنشاء علامات مرجعية لنطاق من الصفحات

تسمح لك فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) بإنشاء علامات مرجعية لنطاق من الصفحات. يمكنك استخدام [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) مع طريقتين: قائمة العلامات المرجعية (قائمة عناوين العلامات المرجعية) وقائمة الصفحات (قائمة الصفحات المراد وضع علامات مرجعية لها). أولاً، تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، عليك استدعاء طريقة [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) وحفظ ملف PDF المُخرج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يُظهر لك المقتطف البرمجي التالي كيفية إنشاء علامات مرجعية لنطاق من الصفحات. 

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}
## إضافة إشارة مرجعية في ملف PDF موجود

يمكنك إضافة إشارة مرجعية في ملف PDF موجود باستخدام فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). لإنشاء الإشارة المرجعية، تحتاج إلى إنشاء كائن [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) وتعيين السمات المطلوبة للإشارة المرجعية. بعد ذلك، تحتاج إلى تمرير كائن [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) إلى طريقة [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يوضح لك مقتطف الشفرة التالي كيفية إضافة الإشارة المرجعية في ملف PDF موجود.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## إضافة إشارة مرجعية فرعية في ملف PDF موجود

يمكنك إضافة إشارات مرجعية فرعية في ملف PDF موجود باستخدام فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). In order to add child bookmarks, you need to create [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects.  
من أجل إضافة إشارات مرجعية فرعية، تحتاج إلى إنشاء كائنات [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark). You can add individual [إشارة مرجعية](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects into [إشارات مرجعية](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object. 
أنت بحاجة أيضًا إلى إنشاء كائن [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) وتعيين خاصية [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) إلى كائن [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks). تحتاج بعد ذلك إلى تمرير هذا الكائن [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) مع [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) إلى الطريقة [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). يوضح لك مقتطف الشيفرة التالي كيفية إضافة إشارات مرجعية فرعية في ملف PDF موجود.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddChildBookmark-AddChildBookmark.cs" >}}
```
## انظر أيضًا

حاول المقارنة والعثور على طريقة للعمل مع الإشارات المرجعية التي تناسبك. دعونا نتعلم قسم [العمل مع الإشارات المرجعية في PDF](/pdf/net/bookmarks/).