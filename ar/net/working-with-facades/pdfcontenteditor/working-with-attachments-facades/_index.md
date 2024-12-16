---
title: العمل مع المرفقات - الواجهات
type: docs
weight: 50
url: /ar/net/working-with-attachments-facades/
description: يشرح هذا القسم كيفية العمل مع المرفقات - الواجهات باستخدام فئة PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

في هذا القسم، سنشرح كيفية العمل مع المرفقات في PDF باستخدام Aspose.PDF لـ .NET Facades. المرفق هو ملف إضافي يتم إرفاقه بوثيقة رئيسية، ويمكن أن يكون من أنواع ملفات متنوعة، مثل pdf، word، صورة، أو ملفات أخرى. ستتعلم كيفية إضافة مرفقات إلى pdf، والحصول على معلومات المرفق، وحفظه إلى ملف، وحذف المرفق من PDF برمجياً باستخدام C#.

## إضافة مرفق من ملف في PDF موجود

يمكنك إضافة مرفق في ملف PDF موجود باستخدام فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). الملحق يمكن إضافته من ملف على القرص باستخدام مسار الملف. يمكنك إضافة الملحق باستخدام [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) الطريقة. تأخذ هذه الطريقة وسيطين: مسار الملف ووصف الملحق. أولاً، تحتاج إلى فتح ملف PDF الحالي وإضافة الملحق إليه. ثم يمكنك حفظ ملف PDF الناتج باستخدام [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) طريقة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

يوضح لك الجزء التالي من الشيفرة كيفية إضافة ملحق من ملف. على سبيل المثال، لنقم بإضافة ملف MP3.

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```
## إضافة مرفق من تدفق في ملف PDF موجود

يمكن إضافة مرفق في ملف PDF من تدفق - FileStream - باستخدام طريقة [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). تأخذ هذه الطريقة ثلاثة معايير: التدفق، اسم المرفق، ووصف المرفق. من أجل إضافة المرفق، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). بعد ذلك، يمكنك استدعاء طريقة [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) لإضافة المرفق. أخيراً، يمكنك استدعاء طريقة Save لحفظ ملف PDF المحدث. يوضح لك مقطع الشيفرة التالي كيفية إضافة مرفق من تدفق.

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## حذف جميع المرفقات من ملف PDF موجود

طريقة [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) لفئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) تتيح لك حذف جميع المرفقات من ملف PDF موجود. استدع طريقة [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). وأخيرًا، يجب عليك استدعاء طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) لحفظ ملف PDF المحدث. يوضح لك مقطع الشيفرة التالي كيفية حذف جميع المرفقات من ملف PDF موجود.

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
```