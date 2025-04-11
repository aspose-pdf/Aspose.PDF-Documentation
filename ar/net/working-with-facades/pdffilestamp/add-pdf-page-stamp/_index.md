---
title: إضافة ختم صفحة PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/add-pdf-page-stamp/
description: اكتشف كيفية إضافة الأختام إلى صفحات PDF في .NET، بما في ذلك النصوص والصور، لأغراض العلامة المائية أو العلامة التجارية باستخدام Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamp",
    "alternativeHeadline": "Enhance PDFs with Custom Stamps and Page Numbers",
    "abstract": "تقديم ميزة ختم صفحة PDF التي تتيح للمستخدمين إضافة أختام مخصصة بسهولة على جميع أو صفحات معينة من مستند PDF باستخدام فئة PdfFileStamp. تعزز هذه الوظيفة تخصيص المستند من خلال تمكين سمات مختلفة مثل الدوران والخلفية وأنماط الترقيم المخصصة لختم الصفحات، مما يجعل ملفات PDF الخاصة بك فريدة من نوعها واحترافية.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1309",
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
    "url": "/net/add-pdf-page-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pdf-page-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إضافة ختم صفحة PDF على جميع الصفحات في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp) إضافة ختم صفحة PDF على جميع صفحات ملف PDF. لإضافة ختم صفحة PDF، تحتاج أولاً إلى إنشاء كائنات من فئتي [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp) و [Stamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp). تحتاج أيضًا إلى إنشاء ختم صفحة PDF باستخدام طريقة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp) من فئة [Stamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp). يمكنك أيضًا تعيين سمات أخرى مثل الأصل والدوران والخلفية وما إلى ذلك باستخدام كائن [Stamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp). ثم يمكنك إضافة الختم في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp). يوضح لك مقتطف الكود التالي كيفية إضافة ختم صفحة PDF على جميع الصفحات في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "AddPageStampOnAllPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnAllPages_out.pdf");
    }
}
```

## إضافة ختم صفحة PDF على صفحات معينة في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp) إضافة ختم صفحة PDF على صفحات معينة من ملف PDF. لإضافة ختم صفحة PDF، تحتاج أولاً إلى إنشاء كائنات من فئتي [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp) و [Stamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp). تحتاج أيضًا إلى إنشاء ختم صفحة PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3) من فئة [Stamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp). يمكنك أيضًا تعيين سمات أخرى مثل الأصل والدوران والخلفية وما إلى ذلك باستخدام كائن [Stamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp). كما تريد إضافة ختم صفحة PDF على صفحات معينة من ملف PDF، تحتاج أيضًا إلى تعيين خاصية [Pages](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/stamp/properties/pages) من فئة [Stamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp). تتطلب هذه الخاصية مصفوفة صحيحة تحتوي على أرقام الصفحات التي تريد إضافة الختم عليها. ثم يمكنك إضافة الختم في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp). يوضح لك مقتطف الكود التالي كيفية إضافة ختم صفحة PDF على صفحات معينة في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnCertainPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "PageStampOnCertainPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;
        stamp.Pages = new[] { 1, 3 };  // Apply stamp to specific pages (1 and 3)

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnCertainPages_out.pdf");
    }
}
```

## إضافة رقم الصفحة في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp) إضافة أرقام الصفحات في ملف PDF. لإضافة أرقام الصفحات، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp). إذا كنت ترغب في عرض رقم الصفحة مثل "الصفحة X من N" حيث X هو رقم الصفحة الحالي وN هو العدد الإجمالي للصفحات في ملف PDF، تحتاج أولاً إلى الحصول على عدد الصفحات باستخدام خاصية [NumberOfpages](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) من فئة [PdfFileInfo](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileinfo). للحصول على رقم الصفحة الحالي، يمكنك استخدام علامة **#** في نصك في أي مكان تريده. يمكنك تنسيق نص رقم الصفحة باستخدام فئة [FormattedText](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formattedtext). إذا كنت ترغب في بدء ترقيم الصفحات من رقم معين، يمكنك تعيين خاصية [StartingNumber](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). بمجرد أن تكون جاهزًا لإضافة رقم الصفحة في الملف، تحتاج إلى استدعاء طريقة [AddPageNumber](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilestamp). يوضح لك مقتطف الكود التالي كيفية إضافة رقم الصفحة في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;
        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```

### نمط الترقيم المخصص

تقدم فئة PdfFileStamp ميزة إضافة معلومات رقم الصفحة ككائن ختم داخل مستند PDF. قبل هذا الإصدار، كانت الفئة تدعم فقط نمط ترقيم الصفحات 1،2،3،4. ومع ذلك، كان هناك طلب من بعض العملاء لاستخدام نمط ترقيم مخصص عند وضع ختم رقم الصفحة داخل مستند PDF. لتحقيق هذا الطلب، تم تقديم خاصية [NumberingStyle](https://reference.aspose.com/pdf/ar/net/aspose.pdf/numberingstyle) التي تقبل القيم من تعداد [NumberingStyle](https://reference.aspose.com/pdf/ar/net/aspose.pdf/numberingstyle). القيم المحددة أدناه هي القيم المقدمة في هذا التعداد.

- حروف صغيرة.
- حروف كبيرة.
- أرقام عربية.
- أرقام رومانية صغيرة.
- أرقام رومانية كبيرة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCustomPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Specify numbering style as Numerals Roman UpperCase
        fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;

        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddCustomPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```