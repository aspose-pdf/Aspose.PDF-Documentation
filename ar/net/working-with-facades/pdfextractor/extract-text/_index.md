---
title: استخراج النص من ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/extract-text/
description: يشرح هذا القسم كيفية استخراج النص من PDF باستخدام فئة PdfExtractor.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF File",
    "alternativeHeadline": "Effortless Text Extraction from PDF Files",
    "abstract": "تمكن فئة PdfExtractor من استخراج النص بكفاءة من ملفات PDF من خلال طرق متعددة، مما يسمح للمستخدمين باسترجاع النصوص والصور والمرفقات بسهولة. من خلال استخدام طرق مثل ExtractText و GetText و GetNextPageText، يمكن للمطورين استخراج وحفظ المحتوى النصي من صفحات فردية أو مستندات كاملة، مما يسهل مهام معالجة PDF. مع توفر أوضاع استخراج مرنة، تعزز هذه الميزة التحكم في تنسيق الإخراج، مما يجعلها أداة أساسية لأي شخص يعمل مع بيانات PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "441",
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
    "url": "/net/extract-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

في هذه المقالة، سنستعرض تفاصيل استخراج النص من ملف PDF. جميع ميزات الاستخراج هذه متاحة في مكان واحد، في فئة [PdfExtractor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfextractor). سنرى كيف نستخدم هذه الميزات في كودنا.

توفر فئة [PdfExtractor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfextractor) ثلاثة أنواع من قدرات الاستخراج. هذه الفئات الثلاث هي النصوص والصور والمرفقات. من أجل إجراء الاستخراج تحت كل من هذه الفئات الثلاث، توفر PdfExtractor طرقًا متنوعة تعمل معًا لتقديم الناتج النهائي.

على سبيل المثال، لاستخراج النص يمكنك استخدام ثلاث طرق وهي [ExtractText و GetText و HasNextPageText و GetNextPageText](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfextractor/methods/index). الآن، من أجل البدء في استخراج النص، تحتاج أولاً إلى استدعاء طريقة [ExtractText](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index)؛ ستقوم هذه الطريقة باستخراج النص من ملف PDF وتخزينه في الذاكرة. بعد ذلك، ستقوم طريقة [GetText](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) بأخذ هذا النص المستخرج وحفظه على القرص في موقع محدد في ملف. تساعدك [HasNextPageText](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) في التكرار عبر كل صفحة والتحقق مما إذا كانت الصفحة التالية تحتوي على أي نص أم لا. إذا كانت تحتوي على نص، فإن [GetNextPageText](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) ستساعدك في حفظ نص صفحة فردية في الملف.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "sample.pdf");

        // ExtractText
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "sample.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```

لاستخراج وضع استخراج النص، استخدم الكود التالي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextExtractonMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "ExtractTextExtractonMode.pdf");

        // ExtractText
        // pdfExtractor.ExtractTextMode = 0; // pure mode
        pdfExtractor.ExtractTextMode = 1; // raw mode
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "ExtractTextExtractonMode_out.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```