---
title: تحويل PDF إلى مستندات Microsoft Word في .NET
linktitle: تحويل PDF إلى Word
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: تعلم كيفية كتابة كود C# لتحويل PDF إلى تنسيقات Microsoft Word مع Aspose.PDF for .NET. وضبط تحويل PDF إلى DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Microsoft Word Documents in .NET",
    "alternativeHeadline": "Seamlessly Convert PDFs to Word Documents with C#",
    "abstract": "Aspose.PDF for .NET يقدم ميزة قوية لتحويل ملفات PDF إلى تنسيقات Microsoft Word (DOC و DOCX) باستخدام C#. هذه الوظيفة لا تعزز فقط تحرير المستندات ولكنها توفر أيضًا خيارات مرنة للتعرف على النص والتنسيق، مما يضمن دقة عالية بين ملف PDF المصدر والمستند الناتج.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1179",
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
    "url": "/net/convert-pdf-to-word/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-word/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF يمكنه أداء المهام البسيطة والسلسة ولكنه أيضًا قادر على التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## نظرة عامة

تشرح هذه المقالة كيفية **تحويل PDF إلى مستندات Microsoft Word باستخدام C#**. تغطي هذه المواضيع.

- [تحويل PDF إلى DOC](#csharp-pdf-to-doc)
- [تحويل PDF إلى DOCX](#csharp-pdf-to-docx)

يعمل مقتطف الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## تحويل PDF إلى DOC و DOCX

تعتبر ميزة تحويل PDF إلى Microsoft Word DOC واحدة من أكثر الميزات شعبية، مما يجعل إدارة المحتوى أكثر سهولة. **Aspose.PDF for .NET** يتيح لك تحويل ملفات PDF إلى تنسيق DOC و DOCX بسرعة وكفاءة.

## تحويل PDF إلى ملف DOC (Microsoft Word 97-2003)

قم بتحويل ملفات PDF إلى تنسيق DOC بسهولة وبتحكم كامل. Aspose.PDF for .NET مرن ويدعم مجموعة واسعة من التحويلات. على سبيل المثال، تحويل الصفحات من مستندات PDF إلى صور هو ميزة شائعة جدًا.

طلب العديد من عملائنا تحويل PDF إلى DOC: تحويل ملف PDF إلى مستند Microsoft Word. يريد العملاء ذلك لأن ملفات PDF لا يمكن تعديلها بسهولة، بينما يمكن تعديل مستندات Word. ترغب بعض الشركات في أن يتمكن مستخدموها من التلاعب بالنصوص والجداول والصور في الملفات التي بدأت كملفات PDF.

استمرارًا للتقليد المتمثل في جعل الأمور بسيطة ومفهومة، يتيح لك Aspose.PDF for .NET تحويل ملف PDF المصدر إلى ملف DOC باستخدام سطرين من الكود. لتحقيق هذه الميزة، قدمنا تعدادًا يسمى SaveFormat وقيمته .Doc تتيح لك حفظ الملف المصدر بتنسيق Microsoft Word.

يظهر مقتطف كود C# التالي كيفية تحويل ملف PDF إلى تنسيق DOC.

<a name="csharp-pdf-to-doc" id="csharp-pdf-to-doc"><strong>تحويل PDF إلى DOC</strong></a>

1. أنشئ مثيلًا من كائن [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/) مع مستند PDF المصدر.
2. احفظه بتنسيق **SaveFormat.Doc** عن طريق استدعاء طريقة **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    usnig (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
    }
}
```

### استخدام فئة DocSaveOptions

توفر فئة [`DocSaveOptions`](https://reference.aspose.com/pdf/ar/net/aspose.pdf/docsaveoptions) العديد من الخصائص التي تحسن تحويل ملفات PDF إلى تنسيق DOC. من بين هذه الخصائص، يتيح لك Mode تحديد وضع التعرف على محتوى PDF. يمكنك اختيار أي قيمة من تعداد RecognitionMode لهذه الخاصية. كل من هذه القيم لها فوائد وقيود محددة:

- وضع [`Textbox`](https://reference.aspose.com/pdf/ar/net/aspose.pdf.docsaveoptions/recognitionmode) سريع وجيد للحفاظ على المظهر الأصلي لملف PDF، ولكن قابلية تعديل المستند الناتج قد تكون محدودة. يتم تحويل كل كتلة نصية مرئية في ملف PDF الأصلي إلى مربع نص في المستند الناتج. وهذا يحقق أقصى تشابه مع الأصل، لذا يبدو المستند الناتج جيدًا، ولكنه يتكون بالكامل من مربعات نصية، والتي يمكن تعديلها في Microsoft Word، وهو أمر صعب للغاية.
- [`Flow`](https://reference.aspose.com/pdf/ar/net/aspose.pdf.docsaveoptions/recognitionmode) هو وضع التعرف الكامل، حيث يقوم المحرك بأداء التجميع والتحليل متعدد المستويات لاستعادة المستند الأصلي وفقًا لنية المؤلف مع إنتاج مستند سهل التعديل. القيود هي أن المستند الناتج قد يبدو مختلفًا عن الأصل.

يمكن استخدام خاصية [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/ar/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) للتحكم في القرب النسبي بين العناصر النصية. يعني ذلك أن المسافة يتم قياسها حسب حجم الخط. قد تحتوي الخطوط الأكبر على مسافات أكبر بين المقاطع ولا تزال تعتبر ككل واحد. يتم تحديدها كنسبة مئوية من حجم الخط؛ على سبيل المثال، 1 = 100%. وهذا يعني أن حرفين بحجم 12pt موضوعين على بعد 12 pt يعتبران قريبين.
- تستخدم خاصية [`RecognitionBullets`](https://reference.aspose.com/pdf/ar/net/aspose.pdf/docsaveoptions/properties/recognizebullets) لتفعيل التعرف على النقاط أثناء التحويل.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWordDocAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDF-to-DOC.pdf"))
    {
        var saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.Doc,
            // Set the recognition mode as Flow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.Flow,
            // Set the Horizontal proximity as 2.5
            RelativeHorizontalProximity = 2.5f,
            // Enable the value to recognize bullets during the conversion process
            RecognizeBullets = true
        };
        // Save the file into MS document with save options
        document.Save(dataDir + "PDFtoDOC_out.doc", saveOptions);
    }
}
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

يقدم لك Aspose.PDF for .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك تجربة الوظائف وجودة العمل.

[![تحويل PDF إلى DOC](/pdf/ar/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى ملف DOCX (Microsoft Word 2007-2024)

تتيح لك واجهة برمجة التطبيقات Aspose.PDF for .NET قراءة وتحويل مستندات PDF إلى DOCX باستخدام C# وأي لغة .NET. DOCX هو تنسيق معروف لمستندات Microsoft Word الذي تم تغيير هيكله من ثنائي بسيط إلى مزيج من ملفات XML وملفات ثنائية. يمكن فتح ملفات Docx باستخدام Word 2007 والإصدارات الأحدث ولكن ليس مع الإصدارات السابقة من MS Word، التي تدعم امتدادات ملفات DOC.

يظهر مقتطف كود C# التالي كيفية تحويل ملف PDF إلى تنسيق DOCX.

<a name="csharp-pdf-to-docx" id="csharp-pdf-to-docx"><strong>تحويل PDF إلى DOCX</strong></a>

1. أنشئ مثيلًا من كائن [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/) مع مستند PDF المصدر.
2. احفظه بتنسيق **SaveFormat.DocX** عن طريق استدعاء طريقة **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFtoDOC_out.docx", SaveFormat.DocX);
    }
}
```

### تحويل PDF إلى DOCX في الوضع المحسن

للحصول على نتائج أفضل من تحويل PDF إلى DOCX، يمكنك استخدام وضع `EnhancedFlow`.
الفرق الرئيسي بين Flow و Enhanced Flow هو أن الجداول (سواء كانت ذات حدود أو بدون حدود) يتم التعرف عليها كجداول حقيقية، وليس كنص مع صورة في الخلفية.
هناك أيضًا التعرف على القوائم المرقمة والعديد من الأشياء الثانوية الأخرى.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.DocX,
            // Set the recognition mode as EnhancedFlow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.EnhancedFlow
        };

        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.docx", saveOptions);
    }
}
```

{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

يقدم لك Aspose.PDF for .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك تجربة الوظائف وجودة العمل.

[![Aspose.PDF تحويل PDF إلى Word تطبيق مجاني](/pdf/ar/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}