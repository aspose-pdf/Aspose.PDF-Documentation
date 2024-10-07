---
title: التلاعب بخصائص الصفحة
type: docs
weight: 80
url: /net/manipulate-page-properties/
description: يشرح هذا القسم كيفية التلاعب بخصائص الصفحة باستخدام Aspose.PDF Facades باستخدام فئة PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

## الحصول على خصائص صفحة PDF من ملف PDF موجود

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) يتيح لك العمل مع صفحات فردية من ملف PDF. يساعدك في الحصول على خصائص الصفحة الفردية مثل أحجام صناديق الصفحة المختلفة، تدوير الصفحة، تكبير الصفحة، إلخ. للحصول على تلك الخصائص، تحتاج إلى إنشاء كائن [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، يمكنك استخدام طرق مختلفة للحصول على خصائص الصفحة مثل [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation)، [GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages)، [GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) إلخ.

يظهر لك مقطع الشيفرة التالي كيفية الحصول على خصائص صفحة PDF من ملف PDF موجود.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-GetPageProperties-GetPageProperties.cs" >}}
## تعيين خصائص صفحة PDF في ملف PDF موجود

من أجل تعيين خصائص الصفحة مثل دوران الصفحة أو التكبير أو نقطة الأصل، تحتاج إلى استخدام فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). توفر هذه الفئة طرقًا وخصائص مختلفة لتعيين خصائص هذه الصفحة. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، يمكنك استخدام هذه الطرق والخصائص لتعيين خصائص الصفحة. وأخيرًا، قم بحفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

يعرض لك مقتطف الشيفرة التالي كيفية تعيين خصائص صفحة PDF في ملف PDF موجود.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-SetPageProperties-SetPageProperties.cs" >}}

## تغيير حجم محتويات صفحات محددة في ملف PDF

تسمح لك طريقة ResizeContents في فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) بتغيير حجم محتويات الصفحة في ملف PDF. تُستخدم فئة [ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) لتحديد المعلمات المستخدمة لتغيير حجم الصفحة أو الصفحات، على سبيل المثال الهوامش كنسبة مئوية أو وحدات أخرى. يمكنك تغيير حجم جميع الصفحات أو تحديد مصفوفة من الصفحات لتغيير حجمها باستخدام طريقة ResizeContents.

يوضح مقتطف الكود التالي كيفية تغيير حجم محتويات بعض الصفحات المحددة في ملف PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-ResizePageContents-ResizePageContents.cs" >}}