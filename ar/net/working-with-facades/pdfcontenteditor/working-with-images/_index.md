---
title: العمل مع الصور باستخدام PdfContentEditor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/working-with-images-in-pdf
description: يشرح هذا القسم كيفية إضافة وحذف الصور باستخدام Aspose.PDF Facades من خلال فئة PdfContentEditor.
lastmod: "2021-06-24"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with Images using PdfContentEditor",
    "alternativeHeadline": "Enhance PDF Images with PdfContentEditor Features",
    "abstract": "تقدم Aspose.PDF for .NET الآن قدرات إدارة الصور المحسّنة من خلال فئة PdfContentEditor، مما يمكّن المستخدمين من حذف صور معينة بسهولة من صفحات محددة أو إزالة جميع الصور تمامًا من ملفات PDF. بالإضافة إلى ذلك، تتيح الميزة استبدال الصور بسلاسة، مما يبسط عملية التحرير ويحسن تخصيص الوثائق",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "415",
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
    "url": "/net/working-with-images-in-pdf",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-images-in-pdf"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## حذف الصور من صفحة معينة من PDF (Facades)

لحذف الصور من صفحة معينة، تحتاج إلى استدعاء [DeleteImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) مع معلمات pageNumber و index. تمثل معلمة index مصفوفة من الأعداد الصحيحة - مؤشرات الصور التي سيتم حذفها. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) ثم استدعاء طريقة [DeleteImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1). بعد ذلك، يمكنك حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save/index).

تظهر لك الشيفرة التالية كيفية حذف الصور من صفحة معينة من PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage(2, new[] { 2 });

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor Object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage(2, new[] { 2 });

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## حذف جميع الصور من ملف PDF (Facades)

يمكن حذف جميع الصور من ملف PDF باستخدام طريقة [DeleteImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) من فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor). استدعِ طريقة [DeleteImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) - النسخة التي لا تحتوي على أي معلمات - لحذف جميع الصور، ثم احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save/index).

تظهر لك الشيفرة التالية كيفية حذف جميع الصور من ملف PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage();

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage();

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## استبدال صورة في ملف PDF (Facades)

تتيح لك [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) استبدال صورتك في ملف PDF، استدعِ لذلك طريقة [ReplaceImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) واحفظ النتيجة.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf")))
    {
        editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}