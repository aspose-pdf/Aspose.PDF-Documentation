---
title: استيراد وتصدير العلامات المرجعية
type: docs
weight: 20
url: /net/import-and-export-bookmarks/
description: يوضح هذا القسم كيفية استيراد وتصدير العلامات المرجعية باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## استيراد العلامات المرجعية من XML إلى ملف PDF موجود

تسمح لك طريقة [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) باستيراد العلامات المرجعية إلى ملف PDF من ملف XML. من أجل استيراد العلامات المرجعية، تحتاج إلى إنشاء كائن [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). بعد ذلك، تحتاج إلى استدعاء طريقة [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1). وأخيراً، احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يوضح لك المقتطف البرمجي التالي كيفية استيراد العلامات المرجعية من ملف XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ImportFromXML-ImportFromXML.cs" >}}

## تصدير العلامات المرجعية إلى XML من ملف PDF موجود

تسمح لك طريقة ExportBookmarksToXml بتصدير العلامات المرجعية من ملف PDF إلى ملف XML.

لتصدير العلامات المرجعية:

1. أنشئ كائن PdfBookmarkEditor واربط ملف PDF باستخدام طريقة BindPdf.
1. استدع طريقة ExportBookmarksToXml.
1. احفظ ملف PDF المحدث باستخدام طريقة Save.

يُظهر لك مقطع الشيفرة التالي كيفية تصدير العلامات المرجعية إلى ملف XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}