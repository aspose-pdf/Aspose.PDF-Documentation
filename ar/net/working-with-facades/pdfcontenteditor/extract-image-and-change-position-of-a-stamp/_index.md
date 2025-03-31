---
title: استخراج الصورة وتغيير موضع الختم
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/extract-image-and-change-position-of-a-stamp/
description: يشرح هذا القسم كيفية استخراج الصورة وتغيير موضع الختم باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract image and change stamp position",
    "alternativeHeadline": "Extract Images and Adjust Stamp Positions in PDF",
    "abstract": "تتيح الميزة في Aspose.PDF for .NET للمستخدمين استخراج الصور بكفاءة من أختام PDF وإعادة وضعها بدقة. من خلال استخدام فئة PdfContentEditor، يمكن للمطورين إدارة وتعديل صور الأختام بسهولة، مما يعزز قدراتهم في تحرير PDF ويحسن العرض العام للوثيقة",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "393",
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
    "url": "/net/extract-image-and-change-position-of-a-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-change-position-of-a-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## استخراج الصورة من ختم الصورة

تتيح لك فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) استخراج الصور من ختم في ملف PDF. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، استدعِ طريقة [GetStamps](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) للحصول على مصفوفة من كائنات StampInfo من صفحة معينة من ملف PDF. ثم يمكنك الحصول على الصورة من StampInfo باستخدام خاصية StampInfo.Image. بمجرد الحصول على الصورة، يمكنك حفظ الصورة أو العمل مع خصائص مختلفة للصورة. يوضح لك مقتطف الكود التالي كيفية استخراج الصورة من ختم الصورة.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ExtractImage-ImageStamp.pdf");

        // Get Stamp info for the first stamp
        var infos = pdfContentEditor.GetStamps(1);

        // Get the image from Stamp Info
        var image = infos[0].Image;

        // Save the extracted image
        image.Save(dataDir + "image_out.jpg");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ExtractImage-ImageStamp.pdf");

    // Get Stamp info for the first stamp
    var infos = pdfContentEditor.GetStamps(1);

    // Get the image from Stamp Info
    var image = infos[0].Image;

    // Save the extracted image
    image.Save(dataDir + "image_out.jpg");
}
```
{{< /tab >}}
{{< /tabs >}}

## تغيير موضع ختم في ملف PDF

تتيح لك فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) تغيير موضع ختم في ملف PDF. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، استدعِ طريقة [MoveStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) مع فهرس الختم والموقع الجديد على صفحة معينة من ملف PDF. ثم، يمكنك حفظ الملف المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save). يوضح لك مقتطف الكود التالي كيفية نقل ختم في صفحة معينة.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeStampPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

        int pageId = 1;
        int stampIndex = 1;
        double x = 200;
        double y = 200;

        // Change the position of the stamp to new x and y position
        pdfContentEditor.MoveStamp(pageId, stampIndex, x, y);

        // Save PDF document
        pdfContentEditor.Save(dataDir + "ChangeStampPosition_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeStampPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

    int pageId = 1;
    int stampIndex = 1;
    double x = 200;
    double y = 200;

    // Change the position of the stamp to new x and y position
    pdfContentEditor.MoveStamp(pageId, stampIndex, x, y);

    // Save PDF document
    pdfContentEditor.Save(dataDir + "ChangeStampPosition_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

أيضًا، يمكنك استخدام طريقة [MoveStampById](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) لنقل ختم معين باستخدام StampId.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveStampById()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor Object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

        int pageId = 1;
        int stampId = 1;
        double x = 200;
        double y = 200;

        // Change the position of the stamp to new x and y position
        pdfContentEditor.MoveStamp(pageId, stampId, x, y);

        // Save PDF document
        pdfContentEditor.Save(dataDir + "ChangeStampPositionByID_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveStampById()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor Object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

    int pageId = 1;
    int stampId = 1;
    double x = 200;
    double y = 200;

    // Change the position of the stamp to new x and y position
    pdfContentEditor.MoveStamp(pageId, stampId, x, y);

    // Save PDF document
    pdfContentEditor.Save(dataDir + "ChangeStampPositionByID_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}