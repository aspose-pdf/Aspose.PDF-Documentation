---
title: استخراج النص من PDF C#
linktitle: استخراج النص من PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/extract-text-from-all-pdf/
description: تصف هذه المقالة طرقًا مختلفة لاستخراج النص من مستندات PDF باستخدام Aspose.PDF في C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Text from PDFs in C#",
    "abstract": "اكتشف الوظيفة الجديدة القوية في Aspose.PDF for .NET التي تتيح للمطورين استخراج النص من مستندات PDF بسهولة. تدعم هذه الميزة الاستخراج من جميع الصفحات أو مناطق معينة، وتتناسب مع تخطيطات متعددة الأعمدة، وتتيح حتى استرجاع النص المميز ببضع سطور من التعليمات البرمجية. عزز قدرات معالجة المستندات الخاصة بك وسهل استخراج المحتوى باستخدام هذه الأداة متعددة الاستخدامات.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2005",
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
    "url": "/net/extract-text-from-all-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-all-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## استخراج النص من جميع صفحات مستند PDF

استخراج النص من مستند PDF هو متطلب شائع. في هذا المثال، سترى كيف يسمح Aspose.PDF for .NET باستخراج النص من جميع صفحات مستند PDF. تحتاج إلى إنشاء كائن من فئة **TextAbsorber**. بعد ذلك، افتح PDF باستخدام فئة **Document** واستدعِ طريقة **Accept** لمجموعة **Pages**. تقوم فئة **TextAbsorber** بامتصاص النص من المستند وتعيده في خاصية **Text**. يوضح مقتطف التعليمات البرمجية التالي كيفية استخراج النص من جميع صفحات مستند PDF.

يعمل مقتطف التعليمات البرمجية التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

استدعِ طريقة **Accept** على صفحة معينة من كائن Document. الفهرس هو رقم الصفحة المحددة التي يحتاج النص إلى استخراجها.

يعمل مقتطف التعليمات البرمجية التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for a particular page
        document.Pages[1].Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text_out.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## استخراج النص من الصفحات باستخدام جهاز النص

يمكنك استخدام فئة **TextDevice** لاستخراج النص من ملف PDF. تستخدم TextDevice فئة TextAbsorber في تنفيذها، وبالتالي، في الواقع، يقومان بنفس الشيء ولكن تم تنفيذ TextDevice لتوحيد نهج "الجهاز" لاستخراج أي شيء من الصفحة مثل ImageDevice وPageDevice، إلخ. يمكن لـ TextAbsorber استخراج النص من الصفحة، أو PDF بالكامل أو XForm، هذه TextAbsorber أكثر عمومية.

### استخراج النص من جميع الصفحات

توضح الخطوات ومقتطف التعليمات البرمجية التالية كيفية استخراج النص من PDF باستخدام جهاز النص.

1. إنشاء كائن من فئة Document مع تحديد ملف PDF المدخل.
1. إنشاء كائن من فئة TextDevice.
1. استخدام كائن من فئة TextExtractOptions لتحديد خيارات الاستخراج.
1. استخدام طريقة Process من فئة TextDevice لتحويل المحتويات إلى نص.
1. حفظ النص في ملف الإخراج.

يعمل مقتطف التعليمات البرمجية التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPagesWithTextDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var builder = new System.Text.StringBuilder();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // String to hold extracted text
        string extractedText = "";

        foreach (var page in document.Pages)
        {
            using (MemoryStream textStream = new MemoryStream())
            {
                // Create text device
                var textDevice = new Aspose.Pdf.Devices.TextDevice();

                // Set text extraction options - set text extraction mode (Raw or Pure)
                var textExtOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
                textDevice.ExtractionOptions = textExtOptions;

                // Convert a particular page and save text to the stream
                textDevice.Process(page, textStream);
                // Convert a particular page and save text to the stream
                textDevice.Process(document.Pages[1], textStream);

                // Get text from memory stream
                extractedText = System.Text.Encoding.Unicode.GetString(textStream.ToArray());
            }
            builder.Append(extractedText);
        }
    }

    // Save the extracted text in text file
    File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", builder.ToString());
}
```

## استخراج النص من منطقة صفحة معينة

توفر فئة **TextAbsorber** القدرة على استخراج النص من صفحة معينة أو جميع صفحات مستند PDF. تعيد هذه الفئة النص المستخرج في خاصية **Text**. ومع ذلك، إذا كانت لدينا متطلبات لاستخراج النص من منطقة صفحة معينة، يمكننا استخدام خاصية **Rectangle** من **TextSearchOptions**. تأخذ خاصية Rectangle كائن Rectangle كقيمة ومن خلال استخدام هذه الخاصية، يمكننا تحديد منطقة الصفحة التي نحتاج لاستخراج النص منها.

يتم استدعاء طريقة **Accept** لصفحة لاستخراج النص. قم بإنشاء كائنات من فئات **Document** و**TextAbsorber**. استدعِ طريقة **Accept** على الصفحة الفردية، كفهرس **Page**، من كائن **Document**. الفهرس هو رقم الصفحة المحددة التي يحتاج النص إلى استخراجها. يمكنك الحصول على النص من خاصية **Text** من فئة **TextAbsorber**. يوضح مقتطف التعليمات البرمجية التالي كيفية استخراج النص من صفحة فردية.

يعمل مقتطف التعليمات البرمجية التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var absorber = new Aspose.Pdf.Text.TextAbsorber();
        absorber.TextSearchOptions.LimitToPageBounds = true;
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

        // Accept the absorber for first page
        document.Pages[1].Accept(absorber);

        // Get the extracted text
        string extractedText = absorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## استخراج النص بناءً على الأعمدة

قد يتكون ملف PDF من نصوص وصور وتعليقات ومرفقات ورسوم بيانية، وما إلى ذلك، وتقدم Aspose.PDF for .NET ميزة الإضافة والتلاعب بجميع هذه العناصر. هذه واجهة برمجة التطبيقات رائعة عندما يتعلق الأمر بإضافة النص واستخراجه من مستند PDF وقد نواجه سيناريو حيث يتكون مستند PDF من أكثر من عمود واحد (مستند متعدد الأعمدة) ونحتاج لاستخراج محتويات الصفحة مع احترام نفس التخطيط، فإن Aspose.PDF for .NET هو الخيار الصحيح لتحقيق هذا المتطلب. إحدى الطرق هي تقليل حجم الخط للمحتويات داخل مستند PDF ثم إجراء استخراج النص. يوضح مقتطف التعليمات البرمجية التالي الخطوات لتقليل حجم النص ثم محاولة استخراج النص من مستند PDF.

يعمل مقتطف التعليمات البرمجية التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextBasedOnColumns()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var extractedText = string.Empty;
    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        sourceDocument.Pages.Accept(textFragmentAbsorber);
        Aspose.Pdf.Text.TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Need to reduce font size at least for 70%
            textFragment.TextState.FontSize = textFragment.TextState.FontSize * 0.7f;
        }
        using (Stream sourceStream = new MemoryStream())
        {
            sourceDocument.Save(sourceStream);
            using (var destDocument = new Aspose.Pdf.Document(sourceStream))
            {
                var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
                destDocument.Pages.Accept(textAbsorber);
                extractedText = textAbsorber.Text;
                textAbsorber.Visit(destDocument);
            }
        }

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractColumnsText_out.txt", extractedText);
    }
}
```

### النهج الثاني - باستخدام ScaleFactor

في هذا الإصدار الجديد، قدمنا أيضًا العديد من التحسينات في TextAbsorber وآلية تنسيق النص الداخلية. لذا الآن أثناء استخراج النص باستخدام وضع "نقي"، يمكنك تحديد خيار ScaleFactor ويمكن أن يكون نهجًا آخر لاستخراج النص من مستند PDF متعدد الأعمدة بجانب النهج المذكور أعلاه. يمكن تعيين هذا العامل المقياسي لضبط الشبكة المستخدمة في آلية تنسيق النص الداخلية أثناء استخراج النص. إن تحديد قيم ScaleFactor بين 1 و0.1 (بما في ذلك 0.1) له نفس تأثير تقليل الخط.

تُعتبر قيم ScaleFactor بين 0.1 و-0.1 كقيمة صفرية، لكنها تجعل الخوارزمية تحسب العامل المقياسي المطلوب أثناء استخراج النص تلقائيًا. يعتمد الحساب على متوسط عرض الرموز الأكثر شيوعًا على الصفحة، لكن لا يمكننا ضمان أن النص المستخرج لا يصل أي سلسلة من العمود إلى بداية العمود التالي. يرجى ملاحظة أنه إذا لم يتم تحديد قيمة ScaleFactor، فسيتم استخدام القيمة الافتراضية 1.0. وهذا يعني أنه لن يتم إجراء أي تغيير في الحجم. إذا كانت قيمة ScaleFactor المحددة أكبر من 10 أو أقل من -0.1، فسيتم استخدام القيمة الافتراضية 1.0.

نقترح استخدام التغيير التلقائي (ScaleFactor = 0) عند معالجة عدد كبير من ملفات PDF لاستخراج محتوى النص. أو تعيين تقليل عرض الشبكة بشكل يدوي (حوالي ScaleFactor = 0.5). ومع ذلك، يجب عليك عدم تحديد ما إذا كان التغيير ضروريًا للمستندات المحددة أم لا. إذا قمت بتعيين تقليل عرض الشبكة بشكل زائد للمستند (الذي لا يحتاج إليه)، سيبقى محتوى النص المستخرج كافيًا تمامًا. يرجى إلقاء نظرة على مقتطف التعليمات البرمجية التالي.

يعمل مقتطف التعليمات البرمجية التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExctractTextWithScaleFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
        textAbsorber.ExtractionOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
        // Setting scale factor to 0.5 is enough to split columns in the majority of documents
        // Setting of zero allows to algorithm choose scale factor automatically
        textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
        document.Pages.Accept(textAbsorber);
        var extractedText = textAbsorber.Text;

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
    }
}
```

{{% alert color="primary" %}}

يرجى ملاحظة أنه لا يوجد تطابق مباشر بين ScaleFactor الجديد ومعامل تقليل الخط القديم يدويًا. ومع ذلك، تأخذ الخوارزمية الافتراضية في الاعتبار قيمة حجم الخط التي تم تقليلها بالفعل لأسباب داخلية معينة. على سبيل المثال، تقليل حجم الخط من 10 إلى 7 له نفس تأثير تعيين عامل مقياس إلى 5/8 (= 0.625).

{{% /alert %}}

## استخراج النص المميز من مستند PDF

في سيناريوهات مختلفة لاستخراج النص من مستند PDF، قد تواجه متطلبًا لاستخراج النص المميز فقط من مستند PDF. لتنفيذ هذه الوظيفة، أضفنا طرق TextMarkupAnnotation.GetMarkedText() وTextMarkupAnnotation.GetMarkedTextFragments() في واجهة برمجة التطبيقات. يمكنك استخراج النص المميز من مستند PDF عن طريق تصفية TextMarkupAnnotation واستخدام الطرق المذكورة. يوضح مقتطف التعليمات البرمجية التالي كيفية استخراج النص المميز من مستند PDF.

يعمل مقتطف التعليمات البرمجية التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractHighlightedTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractHighlightedText.pdf"))
    {
        // Loop through all the annotations
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            // Filter TextMarkupAnnotation
            if (annotation is Aspose.Pdf.Annotations.TextMarkupAnnotation)
            {
                var highlightedAnnotation = annotation as Aspose.Pdf.Annotations.TextMarkupAnnotation;
                // Retrieve highlighted text fragments
                Aspose.Pdf.Text.TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
                foreach (Aspose.Pdf.Text.TextFragment textFragment in collection)
                {
                    // Display highlighted text
                    Console.WriteLine(textFragment.Text);
                }
            }
        }
    }
}
```

## الوصول إلى عناصر Fragment النص وSegment من XML

أحيانًا نحتاج إلى الوصول إلى عناصر TextFragment أو TextSegment عند معالجة مستندات PDF التي تم إنشاؤها من XML. توفر Aspose.PDF for .NET الوصول إلى مثل هذه العناصر بالاسم. يوضح مقتطف التعليمات البرمجية أدناه كيفية استخدام هذه الوظيفة.

يعمل مقتطف التعليمات البرمجية التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessTextFragmentAndSegmentElementsFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.BindXml(dataDir + "40014.xml");

        // Get page
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get elements by Id
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "DocumentFromXML_out.pdf");
    }
}
```