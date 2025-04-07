---
title: مقارنة مستندات PDF
linktitle: مقارنة PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /ar/net/compare-pdf-documents/
description: منذ إصدار 24.7، أصبح من الممكن مقارنة محتوى مستندات PDF مع علامات التوضيح وإخراج جنبًا إلى جنب
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "تتيح ميزة مقارنة PDF الجديدة في Aspose.PDF for .NET للمستخدمين تحديد الاختلافات بين مستندين PDF بكفاءة، سواء من خلال صفحات محددة أو المحتوى بالكامل. مع إخراج جنبًا إلى جنب وخيارات قابلة للتخصيص مثل علامات التغيير الإضافية وأنماط المقارنة المختلفة، تعزز هذه الأداة القوية التعاون من خلال جعل المراجعات سهلة التتبع والمراجعة",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "1091",
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
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2025-04-04",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

يرجى ملاحظة أن جميع أدوات المقارنة متاحة في مكتبة [Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/).

## طرق مقارنة مستندات PDF

عند العمل مع مستندات PDF، هناك أوقات تحتاج فيها إلى مقارنة محتوى مستندين لتحديد الاختلافات. توفر مكتبة Aspose.PDF for .NET مجموعة أدوات قوية لهذا الغرض. في هذه المقالة، سنستكشف كيفية مقارنة مستندات PDF باستخدام بعض مقتطفات الشيفرة البسيطة.

تتيح وظيفة المقارنة في Aspose.PDF لك مقارنة مستندين PDF صفحة بصفحة. يمكنك اختيار مقارنة صفحات محددة أو مستندات كاملة. تسلط وثيقة المقارنة الناتجة الضوء على الاختلافات، مما يسهل تحديد التغييرات بين الملفين.

إليك قائمة بالطرق الممكنة لمقارنة مستندات PDF باستخدام Aspose.PDF لمكتبة .NET:

1. **مقارنة صفحات محددة** - مقارنة الصفحات الأولى من مستندين PDF.

1. **مقارنة مستندات كاملة** - مقارنة المحتوى الكامل لمستندين PDF.

1. **مقارنة مستندات PDF رسوميًا**:

- مقارنة PDF باستخدام طريقة GetDifference - صور فردية حيث يتم وضع علامات على التغييرات.

- مقارنة PDF باستخدام طريقة CompareDocumentsToPdf - مستند PDF مع صور حيث يتم وضع علامات على التغييرات.

## مقارنة صفحات محددة

توضح مقتطف الشيفرة الأول كيفية مقارنة الصفحات الأولى من مستندين PDF.

1. تهيئة المستند.
تبدأ الشيفرة بتهيئة مستندين PDF باستخدام مسارات الملفات الخاصة بهما (documentPath1 و documentPath2). يتم تحديد المسارات كسلاسل فارغة في الوقت الحالي، ولكن في الممارسة العملية، ستستبدل هذه بالمسارات الفعلية للملفات.

2. عملية المقارنة.

- اختيار الصفحة - تقتصر المقارنة على الصفحة الأولى من كل مستند ('Pages[1]').
- خيارات المقارنة:

'AdditionalChangeMarks = true' - تضمن هذه الخيار عرض علامات التغيير الإضافية. تبرز هذه العلامات الاختلافات التي قد تكون موجودة في صفحات أخرى، حتى لو لم تكن على الصفحة الحالية التي تتم مقارنتها.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - تخبر هذه الوضعية المقارن بتجاهل الفراغات في النص، والتركيز فقط على التغييرات داخل الكلمات.

3. يتم حفظ وثيقة المقارنة الناتجة، التي تبرز الاختلافات بين الصفحتين، في مسار الملف المحدد في 'resultPdfPath'.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## مقارنة مستندات كاملة

يوسع مقتطف الشيفرة الثاني النطاق لمقارنة المحتوى الكامل لمستندين PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

تكون نتائج المقارنة التي تم إنشاؤها بواسطة هذه المقتطفات مستندات PDF يمكنك فتحها في عارض مثل Adobe Acrobat. إذا كنت تستخدم عرض الصفحتين في Adobe Acrobat، سترى التغييرات جنبًا إلى جنب:

- الحذف - يتم ملاحظتها على الصفحة اليسرى.
- الإضافات - يتم ملاحظتها على الصفحة اليمنى.

من خلال تعيين 'AdditionalChangeMarks' إلى 'true'، يمكنك أيضًا رؤية علامات للتغييرات التي قد تحدث في صفحات أخرى، حتى لو لم تكن تلك التغييرات على الصفحة الحالية المعروضة.

**Aspose.PDF for .NET** توفر أدوات قوية لمقارنة مستندات PDF، سواء كنت بحاجة إلى مقارنة صفحات محددة أو مستندات كاملة. من خلال استخدام خيارات مثل 'AdditionalChangeMarks' وإعدادات 'ComparisonMode' المختلفة، يمكنك تخصيص عملية المقارنة وفقًا لاحتياجاتك الخاصة. توفر الوثيقة الناتجة عرضًا واضحًا، جنبًا إلى جنب، للتغييرات، مما يسهل تتبع المراجعات وضمان دقة المستند.

## مقارنة مستندات PDF باستخدام GraphicalPdfComparer

عند التعاون في المستندات، خاصة في البيئات المهنية، غالبًا ما ينتهي بك الأمر مع إصدارات متعددة من نفس الملف.

يمكنك استخدام فئة [GraphicalPdfComparer](https://reference.aspose.com/pdf/ar/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/) لمقارنة مستندات PDF والصفحات. الفئة مناسبة لمقارنة التغييرات في محتوى الصفحة الرسومي.

مع Aspose.PDF for .NET، من الممكن مقارنة المستندات والصفحات وإخراج نتيجة المقارنة إلى مستند PDF أو ملف صورة.

يمكنك تعيين الخصائص التالية للفئة:

- الدقة - الدقة بوحدات DPI للصور الناتجة، وكذلك للصور التي تم إنشاؤها أثناء المقارنة.
- اللون - لون علامات التغيير.
- العتبة - عتبة التغيير بالنسبة المئوية. القيمة الافتراضية هي صفر. تعيين قيمة غير صفرية يسمح لك بتجاهل التغييرات الرسومية التي تعتبر غير مهمة بالنسبة لك.

تحتوي الفئة على طريقة تتيح لك الحصول على اختلافات صورة الصفحة في شكل مناسب لمزيد من المعالجة: **ImagesDifference GetDifference(Page page1, Page page2)**.

ترجع هذه الطريقة كائنًا من فئة [ImagesDifference](https://reference.aspose.com/pdf/ar/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/) التي تحتوي على صورة الصفحة الأولى التي تتم مقارنتها ومصفوفة من الاختلافات. تحتوي مصفوفة الاختلافات والصورة الأصلية على تنسيق بكسل **RGB24bpp**.

تتيح لك ImagesDifference إنشاء صورة مختلفة والحصول على صورة الصفحة الثانية التي تتم مقارنتها عن طريق إضافة مصفوفة الاختلافات إلى الصورة الأصلية. للقيام بذلك، استخدم طرق **ImagesDifference.GetDestinationImage و ImagesDifference.DifferenceToImage**.

### مقارنة PDF باستخدام طريقة GetDifference

تحدد الشيفرة المقدمة طريقة [GetDifference](https://reference.aspose.com/pdf/ar/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods) التي تقارن مستندين PDF وتولد تمثيلات بصرية للاختلافات بينهما.

تقارن هذه الطريقة الصفحات الأولى من ملفي PDF وتولد صورتين PNG:

- صورة واحدة (diffPngFilePath) تبرز الاختلافات بين الصفحتين باللون الأحمر.
- الصورة الأخرى (destPngFilePath) هي تمثيل بصري للصفحة الثانية من PDF.

يمكن أن تكون هذه العملية مفيدة للمقارنة البصرية للتغييرات أو الاختلافات بين إصدارين من مستند.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod2.pdf"))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
                }
            }
        }
    }
}
```

### مقارنة PDF باستخدام طريقة CompareDocumentsToPdf

يستخدم مقتطف الشيفرة المقدمة طريقة [CompareDocumentsToPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/) التي تقارن مستندين وتولد تقرير PDF بنتائج المقارنة.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```