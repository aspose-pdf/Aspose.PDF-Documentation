---
title: إضافة طابع نص وصورة
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/add-text-and-image-stamp/
description: يشرح هذا القسم كيفية إضافة طابع نص وصورة باستخدام Aspose.PDF Facades من خلال فئة PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "تتيح ميزات إضافة طابع نص وصورة في Aspose.PDF for .NET للمستخدمين تطبيق طوابع نص وصورة مخصصة بسلاسة عبر جميع صفحات أو صفحات محددة من مستندات PDF. تعزز هذه الوظيفة تخصيص المستندات، مما يسمح بالتحكم التفصيلي في خصائص الطابع مثل الموضع، والدوران، والجودة، مما يحسن في النهاية عرض وسمعة ملفات PDF الخاصة بك.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إضافة طابع نص على جميع الصفحات في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) إضافة طابع نص على جميع صفحات ملف PDF. لإضافة طابع نص، تحتاج أولاً إلى إنشاء كائنات من فئتي [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تحتاج أيضًا إلى إنشاء طابع النص باستخدام طريقة [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). يمكنك تعيين خصائص أخرى مثل الأصل، والدوران، والخلفية، إلخ. باستخدام كائن [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) أيضًا. ثم يمكنك إضافة الطابع في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يوضح مقتطف الكود التالي كيفية إضافة طابع نص على جميع الصفحات في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## إضافة طابع نص على صفحات معينة في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) إضافة طابع نص على صفحات معينة من ملف PDF. لإضافة طابع نص، تحتاج أولاً إلى إنشاء كائنات من فئتي [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تحتاج أيضًا إلى إنشاء طابع النص باستخدام طريقة [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). يمكنك تعيين خصائص أخرى مثل الأصل، والدوران، والخلفية، إلخ. باستخدام كائن [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) أيضًا. نظرًا لأنك تريد إضافة طابع نص على صفحات معينة من ملف PDF، تحتاج أيضًا إلى تعيين خاصية [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تتطلب هذه الخاصية مصفوفة صحيحة تحتوي على أرقام الصفحات التي تريد إضافة الطابع عليها. ثم يمكنك إضافة الطابع في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يوضح مقتطف الكود التالي كيفية إضافة طابع نص على صفحات معينة في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## إضافة طابع صورة على جميع الصفحات في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) إضافة طابع صورة على جميع صفحات ملف PDF. لإضافة طابع صورة، تحتاج أولاً إلى إنشاء كائنات من فئتي [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تحتاج أيضًا إلى إنشاء طابع الصورة باستخدام طريقة [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). يمكنك تعيين خصائص أخرى مثل الأصل، والدوران، والخلفية، إلخ. باستخدام كائن [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) أيضًا. ثم يمكنك إضافة الطابع في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يوضح مقتطف الكود التالي كيفية إضافة طابع صورة على جميع الصفحات في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### التحكم في جودة الصورة عند الإضافة كطابع

عند إضافة صورة ككائن طابع، يمكنك أيضًا التحكم في جودة الصورة. لتحقيق هذا المتطلب، تمت إضافة خاصية الجودة لفئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تشير إلى جودة الصورة بالنسبة المئوية (القيم الصالحة هي 0..100).

## إضافة طابع صورة على صفحات معينة في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) إضافة طابع صورة على صفحات معينة من ملف PDF. لإضافة طابع صورة، تحتاج أولاً إلى إنشاء كائنات من فئتي [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تحتاج أيضًا إلى إنشاء طابع الصورة باستخدام طريقة [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). يمكنك تعيين خصائص أخرى مثل الأصل، والدوران، والخلفية، إلخ. باستخدام كائن [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) أيضًا. نظرًا لأنك تريد إضافة طابع صورة على صفحات معينة من ملف PDF، تحتاج أيضًا إلى تعيين خاصية [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تتطلب هذه الخاصية مصفوفة صحيحة تحتوي على أرقام الصفحات التي تريد إضافة الطابع عليها. ثم يمكنك إضافة الطابع في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يوضح مقتطف الكود التالي كيفية إضافة طابع صورة على صفحات معينة في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```