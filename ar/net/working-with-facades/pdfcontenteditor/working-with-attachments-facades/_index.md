---
title: العمل مع المرفقات - الواجهات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/working-with-attachments-facades/
description: يشرح هذا القسم كيفية العمل مع المرفقات - الواجهات باستخدام فئة PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments - Facades",
    "alternativeHeadline": "Enhanced PDF Attachment Management",
    "abstract": "تتيح ميزة العمل مع المرفقات - الواجهات في Aspose.PDF for .NET للمستخدمين إدارة مرفقات الملفات بسهولة داخل مستندات PDF. مع وظائف لإضافة واسترجاع وإزالة أنواع ملفات مختلفة برمجيًا باستخدام فئة PdfContentEditor، تعمل هذه الميزة على تبسيط عملية تعزيز تفاعلية PDF من خلال السماح بدمج المرفقات بسلاسة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "589",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/working-with-attachments-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-attachments-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء مهام بسيطة وسهلة، ولكن أيضًا التعامل مع أهداف أكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

في هذا القسم، سنشرح كيفية العمل مع المرفقات في PDF باستخدام Aspose.PDF for .NET الواجهات. المرفق هو ملف إضافي مرتبط بمستند رئيسي، ويمكن أن يكون مجموعة متنوعة من أنواع الملفات، مثل pdf، word، صورة، أو ملفات أخرى. ستتعلم كيفية إضافة مرفقات إلى pdf، والحصول على معلومات المرفق، وحفظه في ملف، وحذف المرفق من PDF برمجيًا باستخدام C#.

## إضافة مرفق من ملف في PDF موجود

يمكنك إضافة مرفق في ملف PDF موجود باستخدام فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor). يمكن إضافة المرفق من ملف على القرص باستخدام مسار الملف. يمكنك إضافة المرفق باستخدام طريقة [AddDocumentAttachment](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). تأخذ هذه الطريقة وسيطين: مسار الملف ووصف المرفق. أولاً، تحتاج إلى فتح ملف PDF الموجود وإضافة المرفق إليه. ثم يمكنك حفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save/index) من فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor).

تظهر الشيفرة التالية كيفية إضافة مرفق من ملف. على سبيل المثال، دعنا نضيف ملف MP3.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor =  new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));
    editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## إضافة مرفق من دفق في PDF موجود

يمكن إضافة مرفق في ملف PDF من دفق - FileStream - باستخدام طريقة [AddDocumentAttachment](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). تأخذ هذه الطريقة ثلاثة وسائط: الدفق، اسم المرفق، ووصف المرفق. لإضافة المرفق، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/facade/methods/bindpdf/index). بعد ذلك، يمكنك استدعاء طريقة [AddDocumentAttachment](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) لإضافة المرفق. أخيرًا، يمكنك استدعاء طريقة Save لحفظ ملف PDF المحدث. تظهر الشيفرة التالية كيفية إضافة مرفق من دفق.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
        editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));

    var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
    editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## حذف جميع المرفقات من ملف PDF موجود

تتيح لك طريقة [DeleteAttachments](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) من فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) حذف جميع المرفقات من ملف PDF موجود. استدعِ طريقة [DeleteAttachments](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). أخيرًا، يجب عليك استدعاء طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save/index) لحفظ ملف PDF المحدث. تظهر الشيفرة التالية كيفية حذف جميع المرفقات من ملف PDF موجود.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf")))
    {
        editor.DeleteAttachments();

        // Save PDF document
        editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf"));
    editor.DeleteAttachments();

    // Save PDF document
    editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}