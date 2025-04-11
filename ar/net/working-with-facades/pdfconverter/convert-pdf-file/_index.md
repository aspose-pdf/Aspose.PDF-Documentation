---
title: تحويل ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/convert-pdf-file/
description: تعلم كيفية تحويل ملف PDF إلى تنسيقات مختلفة في .NET باستخدام Aspose.PDF لمعالجة المستندات بشكل مرن.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF File",
    "alternativeHeadline": "Convert PDF Pages to Image Formats Efficiently",
    "abstract": "افتح قوة Aspose.PDF for .NET Facades لتحويل صفحات PDF بسهولة إلى تنسيقات صور متنوعة مثل JPEG و GIF و PNG باستخدام فئة PdfConverter. تتيح لك هذه الميزة التحكم التفصيلي في عملية التحويل، مما يسمح لك بتحديد معلمات مثل الدقة ونوع الإحداثيات ونطاق الصفحات للإخراج المخصص. عزز قدرات معالجة المستندات الخاصة بك من خلال دمج تحويلات PDF إلى صورة بسلاسة في تطبيقاتك",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "561",
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
    "url": "/net/convert-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## تحويل صفحات PDF إلى تنسيقات صور مختلفة (Facades)

لتحويل صفحات PDF إلى تنسيقات صور مختلفة، تحتاج إلى إنشاء كائن [PdfConverter](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfconverter) وفتح ملف PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، تحتاج إلى استدعاء طريقة [DoConvert](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfconverter/methods/doconvert) للمهام الأولية. ثم يمكنك التكرار عبر جميع الصفحات باستخدام طريقتي [HasNextImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) و [GetNextImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). تتيح لك طريقة [GetNextImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) إنشاء صورة لصفحة معينة. تحتاج أيضًا إلى تمرير ImageFormat إلى هذه الطريقة لإنشاء صورة من نوع محدد مثل JPEG أو GIF أو PNG وما إلى ذلك. أخيرًا، استدعِ طريقة [Close](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfconverter/methods/close) من فئة [PdfConverter](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfconverter). يوضح لك الكود التالي كيفية تحويل صفحات PDF إلى صور.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

في الكود التالي، سنوضح لك كيفية تغيير بعض المعلمات. باستخدام [CoordinateType](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) نحدد الإطار 'CropBox'. أيضًا، يمكننا تغيير [Resolution](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfconverter/properties/resolution) بتحديد عدد النقاط لكل بوصة. التالي هو [FormPresentationMode](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - وضع عرض النموذج. ثم نشير إلى [StartPage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfconverter/properties/startpage) الذي يتم من خلاله تعيين رقم الصفحة لبداية التحويل. يمكننا أيضًا تحديد الصفحة الأخيرة عن طريق تعيين نطاق.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Set additional conversion settings
        converter.CoordinateType = Aspose.Pdf.PageCoordinateType.CropBox;
        converter.Resolution = new Aspose.Pdf.Devices.Resolution(600);
        converter.FormPresentationMode = Aspose.Pdf.Devices.FormPresentationMode.Production;
        converter.StartPage = 2;

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

## تحويل صفحات PDF إلى تنسيقات صور مع استبدال خط مخصص

في مقتطف الكود التالي، نوضح كيفية تطبيق استبدال خط مخصص أثناء عملية تحويل PDF إلى صورة. نستخدم مجموعة FontRepository.Substitutions لتسجيل قاعدة استبدال مخصصة. في هذا المثال، عندما يتم العثور على الخط "Helvetica"، يتم استبداله بـ "Arial".

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertWithCustomFontSubstitution()
{
    // Add custom font substitution
    Aspose.Pdf.Text.FontRepository.Substitutions.Add(new CustomPdfFontSubstitution());

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertWithSubstitution.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}

private class CustomPdfFontSubstitution : Aspose.Pdf.Text.CustomFontSubstitutionBase
{
    public override bool TrySubstitute(
        Aspose.Pdf.Text.CustomFontSubstitutionBase.OriginalFontSpecification originalFontSpecification,
        out Aspose.Pdf.Text.Font substitutionFont)
    {
        if (originalFontSpecification.OriginalFontName == "Helvetica")
        {
            substitutionFont = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            return true;
        }
        // Default substitution logic
        return base.TrySubstitute(originalFontSpecification, out substitutionFont);
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertWithCustomFontSubstitution()
{
    // Add custom font substitution
    Aspose.Pdf.Text.FontRepository.Substitutions.Add(new CustomPdfFontSubstitution());

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    using var converter = new Aspose.Pdf.Facades.PdfConverter();
    
     // Bind PDF document
     converter.BindPdf(dataDir + "ConvertWithSubstitution.pdf");

     // Initialize the converting process
     converter.DoConvert();

     // Check if pages exist and then convert to image one by one
     while (converter.HasNextImage())
     {
         // Generate output file name with '_out' suffix
         var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
         // Convert the page to image and save it
         converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
     }
}

private class CustomPdfFontSubstitution : Aspose.Pdf.Text.CustomFontSubstitutionBase
{
    public override bool TrySubstitute(
        Aspose.Pdf.Text.CustomFontSubstitutionBase.OriginalFontSpecification originalFontSpecification,
        out Aspose.Pdf.Text.Font substitutionFont)
    {
        if (originalFontSpecification.OriginalFontName == "Helvetica")
        {
            substitutionFont = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            return true;
        }
        // Default substitution logic
        return base.TrySubstitute(originalFontSpecification, out substitutionFont);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## انظر أيضًا

Aspose.PDF for .NET يسمح بتحويل مستندات PDF إلى تنسيقات مختلفة وأيضًا التحويل من تنسيقات أخرى إلى PDF. أيضًا، يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت باستخدام تطبيق محول Aspose.PDF. تعلم قسم [التحويل](/pdf/ar/net/converting/) لحل مهامك.