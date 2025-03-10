---
title: استخدام تعليقات الارتباط في PDF
linktitle: تعليقات الارتباط
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ar/net/link-annotations/
description: Aspose.PDF for .NET يتيح لك إضافة واسترجاع وحذف تعليق ارتباط من مستند PDF الخاص بك.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Link Annotation for PDF",
    "alternativeHeadline": "How to add Link Annotation in PDF",
    "abstract": "Aspose.PDF for .NET يقدم قدرات قوية لإدارة تعليقات الارتباط داخل مستندات PDF، مما يمكّن المستخدمين من إضافة واسترجاع وإزالة الروابط بسلاسة. تعزز هذه الميزة تفاعل المستند من خلال السماح للروابط بفتح صفحات معينة أو ملفات خارجية أو عناوين URL على الويب، جميعها قابلة للتخصيص بأنماط وإجراءات متنوعة. افتح إمكانيات جديدة للتنقل في PDF وتفاعل المستخدم مع هذه الوظيفة القوية للتعليقات.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, text annotation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET يتيح لك إضافة واسترجاع وحذف تعليق نصي من مستند PDF الخاص بك."
}
</script>

## إضافة تعليق ارتباط إلى ملف PDF موجود

> تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

يمثل [تعليق الارتباط](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) ارتباطًا تشعبيًا، وجهة في مكان آخر، ومستندًا. وفقًا لمعيار PDF، يمكن استخدام تعليق الارتباط في ثلاث حالات: فتح عرض الصفحة، فتح ملف، وفتح صفحة ويب.

### استخدام تعليق الارتباط لفتح عرض الصفحة

تم تنفيذ عدة خطوات إضافية لإنشاء التعليق. استخدمنا 2 TextFragmentAbsorbers للعثور على أجزاء للتجربة. الأول هو لتحديد نص تعليق الارتباط، والثاني يشير إلى بعض الأماكن في المستند.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Link Annotation Demo.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define regular expressions for text fragments
        var regEx1 = new Regex(@"Link Annotation Demo \d");
        var regEx2 = new Regex(@"Sample text \d");

        // Create TextFragmentAbsorber for the first regular expression
        var textFragmentAbsorber1 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx1);
        textFragmentAbsorber1.Visit(document);

        // Create TextFragmentAbsorber for the second regular expression
        var textFragmentAbsorber2 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx2);
        textFragmentAbsorber2.Visit(document);

        // Get the text fragments for both absorbers
        var linkFragments = textFragmentAbsorber1.TextFragments;
        var sampleTextFragments = textFragmentAbsorber2.TextFragments;

        // Create a LinkAnnotation
        var linkAnnotation1 = new Aspose.Pdf.Annotations.LinkAnnotation(page, linkFragments[1].Rectangle)
        {
            Action = new Aspose.Pdf.Annotations.GoToAction(
                new Aspose.Pdf.Annotations.XYZExplicitDestination(
                    sampleTextFragments[1].Page,
                    sampleTextFragments[1].Rectangle.LLX,
                    sampleTextFragments[1].Rectangle.URX, 1.5))
        };

        // Add the link annotation to the page
        page.Annotations.Add(linkAnnotation1);

        // Save PDF document
        document.Save(dataDir + "AddLinkAnnotation_out.pdf");
    }
}
```

لإنشاء التعليق، اتبعنا خطوات معينة:

1. إنشاء `LinkAnnotation` وتمرير كائن الصفحة ومستطيل جزء النص الذي يتوافق مع التعليق.
1. تعيين `Action` كـ `GoToAction` وتمرير `XYZExplicitDestination` كوجهة مرغوبة. أنشأنا `XYZExplicitDestination` بناءً على الصفحة، والإحداثيات اليسرى والعلوية، والتكبير.
1. إضافة التعليق إلى مجموعة تعليقات الصفحة.
1. حفظ المستند.

### استخدام تعليق الارتباط مع وجهة مسماة

عند معالجة مستندات متنوعة، تظهر حالة عندما تكون تكتب ولا تعرف إلى أين ستشير التعليق.
في هذه الحالة، يمكنك استخدام وجهة خاصة (مسمى) وستبدو الشيفرة هنا:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

في مكان آخر، يمكنك إنشاء وجهة مسماة.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```

### استخدام تعليق الارتباط لفتح ملف

نفس النهج مستخدم عند إنشاء تعليق لفتح ملف، كما في الأمثلة أعلاه.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

الفرق هو أننا سنستخدم `GoToRemoteAction` بدلاً من `GoToAction`. يأخذ مُنشئ GoToRemoteAction معاملين: اسم الملف ورقم الصفحة.
يمكنك أيضًا استخدام شكل آخر وتمرير اسم الملف وبعض الوجهة. من الواضح أنك بحاجة إلى إنشاء مثل هذه الوجهة قبل استخدامها.

### استخدام تعليق الارتباط لفتح صفحة ويب

لفتح صفحة ويب، فقط قم بتعيين `Action` مع كائن `GoToURIAction`.
يمكنك تمرير ارتباط تشعبي كمعامل مُنشئ أو أي نوع آخر من URI. على سبيل المثال، يمكنك استخدام `callto` لتنفيذ إجراء مع رقم هاتف.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Create Link Annotation and set the action to call a phone number
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```

## إضافة تعليق ارتباط مزخرف

يمكنك تخصيص تعليق الارتباط باستخدام الحدود. في المثال أدناه، سنقوم بإنشاء حد متقطع أزرق بعرض 3pt.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

مثال آخر يظهر كيفية محاكاة نمط المتصفح واستخدام الخط السفلي للروابط.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### الحصول على تعليقات الارتباط

يرجى محاولة استخدام مقتطف الشيفرة التالية للحصول على LinkAnnotation من مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Get all Link annotations from the first page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        // Iterate through each Link annotation
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);

            // Create a TextAbsorber to extract text within the annotation's rectangle
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;

            // Accept the absorber for the first page
            document.Pages[1].Accept(absorber);

            // Extract and print the text associated with the hyperlink
            string extractedText = absorber.Text;
            Console.WriteLine(extractedText);
        }
    }
}
```

### حذف تعليقات الارتباط

تظهر مقتطف الشيفرة التالية كيفية حذف تعليق ارتباط من ملف PDF. لهذا، نحتاج إلى العثور على جميع تعليقات الارتباط وإزالتها في الصفحة الأولى. بعد ذلك، سنقوم بحفظ المستند مع التعليق المحذوف.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Find and delete all link annotations on the 1st page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        foreach (var la in linkAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLinkAnnotations_out.pdf");
    }
}
```