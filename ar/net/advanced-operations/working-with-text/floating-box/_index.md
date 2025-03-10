---
title: استخدام FloatingBox لتوليد النص
linktitle: استخدام FloatingBox
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/floating-box/
description: تشرح هذه الصفحة كيفية تنسيق النص داخل صندوق عائم.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using FloatingBox for text generation",
    "alternativeHeadline": "FloatingBox Enhances PDF Text Layout Options",
    "abstract": "تعمل ميزة FloatingBox على تحسين تنسيق نص PDF من خلال السماح للمستخدمين بإدارة موضع النص بدقة، بما في ذلك تخطيطات متعددة الأعمدة وإزاحات قابلة للتعديل. تدعم قص النصوص، وألوان الخلفية، وخيارات لتكرار المحتوى عبر الصفحات، مما يجعلها أداة متعددة الاستخدامات لإنشاء مستندات منظمة وجذابة بصريًا.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "682",
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
    "url": "/net/floating-box/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/floating-box/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تعمل هذه الميزة أيضًا في مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

## أساسيات استخدام أداة FloatingBox

أداة Floating Box هي أداة خاصة لوضع النص والمحتوى الآخر على صفحة PDF. تتمثل ميزتها الرئيسية في قص النص عندما يتجاوز حجم FloatingBox.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAndAddFloatingBox()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        // Create and fill box
        var box = new Aspose.Pdf.FloatingBox(400, 30)
        {
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.5f, Aspose.Pdf.Color.DarkGreen),
            IsNeedRepeating = false,
        };
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example"));
        // Add box
        page.Paragraphs.Add(box);
    }
}
```  

في المثال أعلاه، نقوم بإنشاء FloatingBox بعرض 400 نقطة وارتفاع 30 نقطة.
أيضًا، في هذا المثال، تم إنشاء نص أكثر عمدًا مما يمكن أن يتناسب مع الحجم المحدد.
نتيجة لذلك، تم قطع النص.

![صورة 1](image01.png)

تحدد خاصية `IsNeedRepeating` بقيمة `false` النص بصفحة واحدة.

إذا قمنا بتعيين هذه الخاصية إلى `true`، سيتم إعادة تدفق النص إلى الصفحة التالية في نفس الموضع.

![صورة 2](image02.png)

## الميزات المتقدمة لـ FloatingBox

### دعم الأعمدة المتعددة

#### تخطيط متعدد الأعمدة (حالة بسيطة)

يدعم `FloatingBox` تخطيط الأعمدة المتعددة. لإنشاء مثل هذا التخطيط، يجب عليك تحديد قيم خصائص ColumnInfo.

* `ColumnWidths` هو سلسلة تحتوي على تعداد العرض بالنقاط.
* `ColumnSpacing` هو سلسلة تحتوي على عرض الفجوة بين الأعمدة.
* `ColumnCount` هو عدد الأعمدة.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MultiColumnLayout()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tooltip();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set margin settings
        page.PageInfo.Margin = new Aspose.Pdf.MarginInfo(36, 18, 36, 18);
        var columnCount = 3;
        var spacing = 10;
        var width = page.PageInfo.Width
            - page.PageInfo.Margin.Left
            - page.PageInfo.Margin.Right
            - (columnCount - 1) * spacing;
        var columnWidth = width / 3;
        // Create FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            IsNeedRepeating = true
        };
        box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
        box.ColumnInfo.ColumnSpacing = $"{spacing}";
        box.ColumnInfo.ColumnCount = 3;

        var phrase = "text example";
        var paragraphs = new string[10]
        {
            phrase, phrase, phrase, phrase, phrase,
            phrase, phrase, phrase, phrase, phrase,
        };
        foreach (var paragraph in paragraphs)
        {
            box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment(paragraph));
        }
        // Add a box to a page
        page.Paragraphs.Add(box);
        // Save PDF document
        document.Save(dataDir + "MultiColumnLayout_out.pdf");
    }
}
```

استخدمنا المكتبة الإضافية LoremNET في المثال أعلاه وأنشأنا 20 فقرة. تم تقسيم هذه الفقرات إلى ثلاثة أعمدة وملأت الصفحات التالية حتى نفاد النص.

#### تخطيط متعدد الأعمدة مع بدء عمود قسري

سنقوم بنفس الشيء مع المثال التالي كما في السابق. الفرق هو أننا أنشأنا 3 فقرات. يمكننا إجبار FloatingBox على عرض كل فقرة في عمود جديد. للقيام بذلك، نحتاج إلى تعيين `IsFirstParagraphInColumn` عند إضافة نص إلى كائن FloatingBox.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MultiColumnLayout2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tooltip();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set margin settings
        page.PageInfo.Margin = new Aspose.Pdf.MarginInfo(36, 18, 36, 18);
        var columnCount = 3;
        var spacing = 10;
        var width = page.PageInfo.Width
            - page.PageInfo.Margin.Left
            - page.PageInfo.Margin.Right
            - (columnCount - 1) * spacing;
        var columnWidth = width / 3;
        // Create the FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            IsNeedRepeating = true
        };
        box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
        box.ColumnInfo.ColumnSpacing = $"{spacing}";
        box.ColumnInfo.ColumnCount = 3;

        var phrase = "text example";
        var paragraphs = new string[10]
        {
            phrase, phrase, phrase, phrase, phrase,
            phrase, phrase, phrase, phrase, phrase,
        };
        foreach (var paragraph in paragraphs)
        {
            var text = new Aspose.Pdf.Text.TextFragment(paragraph)
            {
                IsFirstParagraphInColumn = true
            };
            box.Paragraphs.Add(text);
        }

        // Add a box to a page
        page.Paragraphs.Add(box);
        // Save PDF document
        document.Save(dataDir + "MultiColumnLayout2_out.pdf");
    }
}
```

### دعم الخلفية

يمكنك تعيين لون الخلفية المطلوب باستخدام خاصية `BackgroundColor`.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void BackgroundSupport()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var box = new Aspose.Pdf.FloatingBox(400, 60)
        {
            IsNeedRepeating = false,
            BackgroundColor = Aspose.Pdf.Color.LightGreen,
        };
        var text = "text example";
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment(text));
        page.Paragraphs.Add(box);
    }
}
```

### دعم التمركز

يتم تحديد موقع FloatingBox على الصفحة المولدة بواسطة خصائص `PositioningMode` و `Left` و `Top`.
عندما تكون قيمة `PositioningMode` هي
- `ParagraphPositioningMode.Default` (القيمة الافتراضية)
	يتم تحديد الموقع بواسطة العناصر الموضوعة مسبقًا.
	يتم أخذ إضافة عنصر في الاعتبار عند تحديد موقع العناصر اللاحقة.
	إذا كانت قيمة أي من خصائص Left أو Top ليست صفرًا، فسيتم أخذها أيضًا في الاعتبار، ولكن هذا يستخدم منطقًا ليس واضحًا تمامًا ومن الأفضل عدم استخدامه.

- `ParagraphPositioningMode.Absolute`
	يتم تحديد الموقع بواسطة قيم Left و Top، ولا يعتمد على العناصر السابقة ولا يؤثر على موقع العناصر اللاحقة.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OffsetSupport()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            Top = 45,
            Left = 15,
            PositioningMode = Aspose.Pdf.ParagraphPositioningMode.Absolute
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.5f, Aspose.Pdf.Color.DarkGreen)
        };
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 1"));

        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 2"));
        // Add the box to the page
        page.Paragraphs.Add(box);
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 3"));
    }
}
```