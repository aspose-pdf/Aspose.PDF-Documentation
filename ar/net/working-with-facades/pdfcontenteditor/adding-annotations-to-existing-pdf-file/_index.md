---
title: إضافة تعليقات على ملف PDF موجود
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ar/net/adding-annotations-to-existing-pdf-file/
description: استكشف كيفية إضافة تعليقات مثل التعليقات أو التمييز إلى مستندات PDF الموجودة في .NET باستخدام Aspose.PDF.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Annotations to existing PDF file",
    "alternativeHeadline": "Enhance PDF with Dynamic Annotation Capabilities",
    "abstract": "قم بتحسين مستندات PDF الخاصة بك مع ميزة التعليق الجديدة لدينا، مما يسمح للمستخدمين بإضافة أنواع مختلفة من التعليقات بما في ذلك النص الحر، والنص، وتعليقات الخط بشكل سلس. من خلال استخدام PdfContentEditor، يمكنك بسهولة ربط ملفات PDF الموجودة وتحديد مناطق التعليق، مما يحسن تفاعل الوثائق ووضوحها مع بضع سطور من التعليمات البرمجية. قم بتحسين سير العمل الخاص بك من خلال دمج التعليقات الغنية مباشرة في ملفات PDF الخاصة بك، مما يعزز تفاعل المستخدم وفهمه.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "621",
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
    "url": "/net/adding-annotations-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-annotations-to-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إضافة تعليق نصي حر في ملف PDF موجود (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) يتيح لك إضافة تعليقات من أنواع مختلفة في ملف PDF موجود. يمكنك استخدام الطريقة المناسبة لإضافة تعليق معين. على سبيل المثال، في مقتطف التعليمات البرمجية التالي، استخدمنا [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) لإضافة تعليق من نوع [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation).

يمكن إضافة أي نوع من التعليقات إلى ملف PDF بنفس الطريقة. أولاً، تحتاج إلى إنشاء كائن من نوع [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثانيًا، يجب عليك إنشاء كائن Rectangle لتحديد منطقة التعليق.

بعد ذلك، يمكنك استدعاء [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) لإضافة تعليق [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)، ثم استخدم [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لحفظ ملف PDF المحدث.

مقتطف التعليمات البرمجية التالي يوضح لك كيفية إضافة تعليق نصي حر في ملف PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Add annotation
        editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number

        // Save PDF document
        editor.Save(dataDir + "AddFreeTextAnnotation_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
    tfa.Visit(document.Pages[1]);

    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    // Add annotation
    editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number

    // Save PDF document
    editor.Save(dataDir + "AddFreeTextAnnotation_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## إضافة تعليق نصي في ملف PDF موجود (facades)

في هذا المثال أيضًا، تحتاج إلى إنشاء كائن من نوع [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثانيًا، يجب عليك إنشاء كائن Rectangle لتحديد منطقة التعليق. بعد ذلك، يمكنك استدعاء [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) لإضافة تعليق FreeText، وإنشاء عنوان لتعليقاتك، ورقم الصفحة التي يقع عليها التعليق.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Add annotation
        editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);

        // Save PDF document
        editor.Save(dataDir + "AddTextAnnotation_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
    tfa.Visit(document.Pages[1]);

    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    // Add annotation
    editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);

    // Save PDF document
    editor.Save(dataDir + "AddTextAnnotation_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## إضافة تعليق خط في ملف PDF موجود (facades)

نحدد أيضًا المستطيل، وإحداثيات بداية ونهاية الخط، ورقم الصفحة، والسماكة، والأسلوب ولون إطار التعليق، ونوع خط التقطيع، ونوع بداية ونهاية الخط.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Create Line Annotation
        editor.CreateLine(
            new System.Drawing.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 2,
            System.Drawing.Color.Red,
            "dash",
            new int[] { 1, 0, 3 },
            new[] { "Open", "Open" });

        // Save PDF document
        editor.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    // Create Line Annotation
    editor.CreateLine(
        new System.Drawing.Rectangle(550, 93, 562, 439),
        "Test",
        556, 99, 556, 443, 1, 2,
        System.Drawing.Color.Red,
        "dash",
        new int[] { 1, 0, 3 },
        new[] { "Open", "Open" });

    // Save PDF document
    editor.Save(dataDir + "AddLineAnnotation_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}