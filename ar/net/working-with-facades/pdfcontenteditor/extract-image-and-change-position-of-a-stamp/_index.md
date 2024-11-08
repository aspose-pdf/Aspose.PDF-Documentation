---
title: استخراج الصورة وتغيير موضع الختم
type: docs
weight: 30
url: /ar/net/extract-image-and-change-position-of-a-stamp/
description: يشرح هذا القسم كيفية استخراج الصورة وتغيير موضع الختم باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## استخراج الصورة من ختم الصورة

تسمح لك فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) باستخراج الصور من ختم في ملف PDF. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، قم باستدعاء طريقة [GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) للحصول على مصفوفة من كائنات StampInfo من صفحة معينة من ملف PDF. ثم يمكنك الحصول على الصورة من StampInfo باستخدام الخاصية StampInfo.Image. بمجرد الحصول على الصورة، يمكنك حفظ الصورة أو العمل مع خصائص مختلفة للصورة. يوضح لك مقطع الشيفرة التالي كيفية استخراج الصورة من ختم الصورة.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ExtractImageImageStamp-ExtractImageImageStamp.cs" >}}

## تغيير موضع الختم في ملف PDF

تسمح لك فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) بتغيير موضع الختم في ملف PDF. 
أولاً، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، استدعِ طريقة [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) مع مؤشر الطابع والموقع الجديد في صفحة معينة من ملف PDF. ثم، يمكنك حفظ الملف المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). يوضح لك مقتطف الشيفرة التالي كيفية نقل طابع في صفحة معينة.


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPosition.cs" >}}


أيضاً، يمكنك استخدام طريقة [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) لنقل طابع معين باستخدام StampId.


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPositionByID.cs" >}}
```