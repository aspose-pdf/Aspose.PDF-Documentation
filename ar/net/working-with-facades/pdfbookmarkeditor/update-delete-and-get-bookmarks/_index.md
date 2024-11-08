---
title: تحديث، حذف والحصول على العلامات المرجعية
type: docs
weight: 30
url: /ar/net/update-delete-and-get-bookmarks/
description: تشرح هذه القسم كيفية تحديث، حذف والحصول على العلامات المرجعية باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## تحديث علامة مرجعية موجودة في ملف PDF

لتحديث علامة مرجعية موجودة في ملف PDF، تحتاج إلى استخدام طريقة [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks).
``` هذه الطريقة تأخذ وسيطين: عنوان المصدر (عنوان الإشارة المرجعية المراد تعديلها)، عنوان الوجهة (العنوان الذي سيتم استبداله). تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، تحتاج إلى استدعاء طريقة [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks)، ثم حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يوضح لك مقطع الشيفرة التالي كيفية تعديل إشارة مرجعية موجودة في ملف PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-UpdateBookmark-UpdateBookmark.cs" >}}

## حذف جميع الإشارات المرجعية من ملف PDF

يمكنك حذف جميع الإشارات المرجعية من ملف PDF باستخدام طريقة [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) دون أي معلمات. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، تحتاج إلى استدعاء طريقة [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) ثم حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يُظهر لك الجزء التالي من الكود كيفية حذف جميع الإشارات المرجعية من ملف PDF.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteAllBookmarks-DeleteAllBookmarks.cs" >}}

## حذف إشارة مرجعية معينة من ملف PDF

لحذف إشارة مرجعية معينة، تحتاج إلى استدعاء طريقة [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) مع معلمة نصية (العنوان). The *title* هنا يمثل الإشارة المرجعية التي سيتم حذفها من ملف PDF. قم بإنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) واربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، قم باستدعاء طريقة [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) ثم احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يوضح لك مقتطف الشيفرة التالي كيفية حذف إشارة مرجعية معينة من ملف PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteABookmark-DeleteABookmark.cs" >}}

## الحصول على الإشارات المرجعية من واجهات وثيقة PDF

توفر فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) ميزة التلاعب بالإشارات المرجعية في ملف PDF الموجود. يوفر خصائص متعددة للحصول على/تعيين معلومات تتعلق بالإشارات المرجعية. يوضح المقتطف التالي من الكود كيفية الحصول على معلومات متعلقة بكل إشارة مرجعية في ملف PDF.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-GetFromPDF-GetFromPDF.cs" >}}

## استخراج الإشارات المرجعية من ملف PDF موجود

تسمح لك طريقة [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) باستخراج الإشارات المرجعية من ملف PDF. In order to extract the bookmarks, you need to create [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) object and bind the PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method.

من أجل استخراج الإشارات المرجعية، تحتاج إلى إنشاء كائن [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، تحتاج إلى استدعاء طريقة [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). تعيد طريقة [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) كائن [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index). يمكنك بعد ذلك التكرار من خلال هذه العلامات المرجعية والحصول على كائنات [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) فردية. أخيراً، احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يُظهر لك مقتطف الشيفرة التالي كيفية تصدير العلامات المرجعية إلى ملف XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExtractBookmarks-ExtractBookmarks.cs" >}}