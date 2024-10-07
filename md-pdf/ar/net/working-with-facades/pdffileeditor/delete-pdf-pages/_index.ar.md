---
title: حذف صفحات PDF
type: docs
weight: 70
url: /net/delete-pdf-pages/
description: يوضح هذا القسم كيفية حذف صفحات PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

إذا كنت ترغب في حذف عدد من الصفحات من ملف PDF الموجود على القرص، يمكنك استخدام التحميل الزائد لطريقة [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) التي تأخذ المعلمات الثلاثة التالية: مسار الملف المدخل، ومصفوفة أرقام الصفحات المراد حذفها، ومسار ملف PDF الناتج. المعلمة الثانية هي مصفوفة من الأعداد الصحيحة تمثل جميع الصفحات التي تحتاج إلى حذفها. يتم إزالة الصفحات المحددة من الملف المدخل ويتم حفظ النتيجة كملف ناتج. يظهر لك مقتطف الشفرة التالي كيفية حذف صفحات PDF باستخدام مسارات الملفات.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}


## حذف صفحات PDF باستخدام التدفقات

The [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class also provides an overload which allows you to delete the pages from the input PDF file, while both the input and output files are in the streams. This overload takes following three parameters: intput stream, integer array of PDF pages to be deleted, and output stream.The following code snippet shows you how to delete PDF pages using streams.

طريقة [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) لفئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) توفر أيضًا تحميلًا زائدًا يتيح لك حذف الصفحات من ملف PDF المدخل، بينما تكون كل من الملفات المدخلة والمخرجة في التدفقات. يأخذ هذا التحميل الزائد المعلمات الثلاثة التالية: تدفق المدخل، مصفوفة أعداد صحيحة لصفحات PDF المراد حذفها، وتدفق المخرج. يوضح لك المقتطف البرمجي التالي كيفية حذف صفحات PDF باستخدام التدفقات.