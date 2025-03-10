---
title: استخدام التعليق النصي لملف PDF
linktitle: التعليق النصي
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/text-annotation/
description: Aspose.PDF for .NET يتيح لك إضافة، الحصول على، وحذف التعليق النصي من مستند PDF الخاص بك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Text Annotation for PDF",
    "alternativeHeadline": "Enhance PDFs with Dynamic Text Annotations",
    "abstract": "Aspose.PDF for .NET يقدم قدرات متقدمة للتعليق النصي، مما يسمح للمستخدمين بإضافة، استرجاع، أو إزالة التعليقات النصية بسهولة داخل مستندات PDF. تعزز هذه الميزة عملية تحرير PDF من خلال تمكين وضع وتخصيص دقيق للتعليقات، مما يحسن من تفاعل المستند وسهولة استخدامه.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Text Annotation, PDF document generation, Aspose.PDF for .NET, Add Annotation, Delete Annotation, Free Text Annotation, Popup Annotation, StrikeOutAnnotation, AnnotationCollection, Aspose.PDF library",
    "wordcount": "2636",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET يتيح لك إضافة، الحصول على، وحذف التعليق النصي من مستند PDF الخاص بك."
}
</script>

## كيفية إضافة تعليق نصي إلى ملف PDF موجود

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

التعليق النصي هو تعليق مرتبط بموقع معين في مستند PDF. عند إغلاقه، يتم عرض التعليق كأيقونة؛ عند فتحه، يجب أن يظهر نافذة منبثقة تحتوي على نص الملاحظة بالخط والحجم الذي اختاره القارئ.

تحتوي التعليقات على مجموعة [التعليقات](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) لصفحة معينة. تحتوي هذه المجموعة على التعليقات لتلك الصفحة الفردية فقط؛ كل صفحة لديها مجموعة التعليقات الخاصة بها.

لإضافة تعليق إلى صفحة معينة، أضفه إلى مجموعة التعليقات الخاصة بتلك الصفحة باستخدام طريقة [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add).

1. أولاً، أنشئ تعليقًا تريد إضافته إلى ملف PDF.
1. ثم افتح ملف PDF المدخل.
1. أضف التعليق إلى مجموعة التعليقات الخاصة بكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

تظهر مقتطفات الشيفرة التالية كيفية إضافة تعليق في صفحة PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotationToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
        textAnnotation.Title = "Sample Annotation Title";
        textAnnotation.Subject = "Sample Subject";
        textAnnotation.SetReviewState(Aspose.Pdf.Annotations.AnnotationState.Accepted);
        textAnnotation.Contents = "Sample contents for the annotation";
        textAnnotation.Open = true;
        textAnnotation.Icon = Aspose.Pdf.Annotations.TextIcon.Key;

        // Set border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(textAnnotation);
        border.Width = 5;
        border.Dash = new Aspose.Pdf.Annotations.Dash(1, 1);
        textAnnotation.Border = border;
        textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Add annotation to the annotations collection of the page
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddAnnotation_out.pdf");
    }
}
```

## كيفية إضافة تعليق منبثق

يعرض التعليق المنبثق النص في نافذة منبثقة للإدخال والتحرير. يجب ألا يظهر بمفرده ولكنه مرتبط بتعليق توضيحي، وهو التعليق الأب، ويجب استخدامه لتحرير نص الأب.

يجب ألا يحتوي على تدفق مظهر أو إجراءات مرتبطة به ويجب التعرف عليه من خلال إدخال Popup في قاموس تعليق الأب.

تظهر مقتطفات الشيفرة التالية كيفية إضافة [تعليق منبثق](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) في صفحة PDF باستخدام مثال لإضافة [تعليق خط](/pdf/ar/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file) للأب.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## كيفية إضافة (أو إنشاء) تعليق نصي مجاني جديد

يعرض التعليق النصي المجاني النص مباشرة على الصفحة. تتيح طريقة [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) إنشاء هذا النوع من التعليقات. في المقتطف التالي، نضيف تعليق نصي مجاني فوق أول ظهور للسلسلة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotationDemo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Assuming tfa is an instance of TextFragmentAbsorber or similar
        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber();
        tfa.Visit(document.Pages[1]);

        if (tfa.TextFragments.Count <= 0)
        {
            return;
        }

        // Define the rectangle for the free text annotation
        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Create free text annotation
        pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // Last param is the page number

        // Save PDF document
        pdfContentEditor.Save(dataDir + "pdf-sample-0.pdf");
    }
}
```

### تعيين خاصية Callout لتعليق FreeTextAnnotation

لإعداد تكوين أكثر مرونة للتعليق في مستند PDF، يوفر Aspose.PDF for .NET خاصية [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) لفئة [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) التي تسمح بتحديد مصفوفة من نقاط خط الاستدعاء. تظهر مقتطفات الشيفرة التالية كيفية استخدام هذه الوظيفة:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextCalloutAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create default appearance for the annotation
        var da = new Aspose.Pdf.Annotations.DefaultAppearance();
        da.TextColor = System.Drawing.Color.Red;
        da.FontSize = 10;

        // Create free text annotation with callout
        var fta = new Aspose.Pdf.Annotations.FreeTextAnnotation(page, new Aspose.Pdf.Rectangle(422.25, 645.75, 583.5, 702.75), da);
        fta.Intent = Aspose.Pdf.Annotations.FreeTextIntent.FreeTextCallout;
        fta.EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow;
        fta.Callout = new Aspose.Pdf.Point[]
        {
            new Aspose.Pdf.Point(428.25, 651.75),
            new Aspose.Pdf.Point(462.75, 681.375),
            new Aspose.Pdf.Point(474, 681.375)
        };

        // Add the annotation to the page
        page.Annotations.Add(fta);

        // Set rich text for the annotation
        fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";

        // Save PDF document
        document.Save(dataDir + "SetCalloutProperty_out.pdf");
    }
}
```

### تعيين خاصية Callout لملف XFDF

إذا كنت تستخدم الاستيراد من ملف XFDF، يرجى استخدام اسم خط الاستدعاء بدلاً من مجرد Callout. تظهر مقتطفات الشيفرة التالية كيفية استخدام هذه الوظيفة:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationsFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create an XFDF string builder
        var xfdf = new StringBuilder();
        xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");

        // Call the method to create XFDF content
        CreateXfdf(ref xfdf);

        xfdf.AppendLine("</annots></xfdf>");

        // Import annotations from the XFDF string
        document.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(xfdf.ToString())));

        // Save PDF document
        document.Save(dataDir + "SetCalloutPropertyXfdf_out.pdf");
    }
}
```

تستخدم الطريقة التالية لإنشاء Xfdf:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```

### جعل تعليق النص المجاني غير مرئي

في بعض الأحيان، من الضروري إنشاء علامة مائية غير مرئية في المستند عند مشاهدته ولكن يجب أن تكون مرئية عند طباعة المستند. استخدم علامات التعليق لهذا الغرض. تظهر مقتطفات الشيفرة التالية كيفية القيام بذلك.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInvisibleAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create a free text annotation
        var annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(50, 600, 250, 650),
            new Aspose.Pdf.Annotations.DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red)
        );

        annotation.Contents = "ABCDEFG";
        annotation.Characteristics.Border = System.Drawing.Color.Red;
        annotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print | Aspose.Pdf.Annotations.AnnotationFlags.NoView;

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(annotation);

        // Save PDF document
        document.Save(dataDir + "InvisibleAnnotation_out.pdf");
    }
}
```

### تعيين تنسيق FreeTextAnnotation

تتناول هذه الجزء كيفية تنسيق النص في تعليق نصي مجاني.

تحتوي التعليقات على مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). عند إضافة [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) إلى مستند PDF، يمكنك تحديد معلومات التنسيق مثل الخط، الحجم، اللون، وما إلى ذلك باستخدام فئة [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index). من الممكن أيضًا تحديد معلومات التنسيق باستخدام خاصية TextStyle. علاوة على ذلك، يمكنك تحديث تنسيق أي FreeTextAnnotation موجود بالفعل في مستند PDF.

تدعم فئة [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) العمل مع إدخال النمط الافتراضي. تتيح لك هذه الفئة تعيين اللون، حجم الخط واسم الخط:

- خاصية FontName تحصل أو تعين اسم الخط (سلسلة).
- خاصية FontSize تحصل وتعين حجم النص الافتراضي (مزدوج).
- خاصية System.Drawing.Color تحصل وتعين لون النص (لون).
- خاصية TextAlignment تحصل وتعين محاذاة نص التعليق (محاذاة).

تظهر مقتطفات الشيفرة التالية كيفية إضافة FreeTextAnnotation مع تنسيق نص محدد.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Instantiate DefaultAppearance object
        var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Arial", 28, System.Drawing.Color.Red);

        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600), defaultAppearance);

        // Specify the contents of annotation
        freetext.Contents = "Free Text";

        // Add annotation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation(string fontName = "Arial", float fontSize = 28)
{
     // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Set default values
        var textColor = System.Drawing.Color.Red;
        var position = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Instantiate DefaultAppearance object
        Aspose.Pdf.Annotations.DefaultAppearance defaultAppearance = new(fontName, fontSize, textColor);
        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], position, defaultAppearance)
        {
            // Specify the contents of annotation
            Contents = "Free Text"
        };
        // Add anootation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

{{% alert color="primary" %}}

عند تغيير محتويات أو نمط نص التعليق النصي المجاني، يتم إعادة توليد مظهر التعليق لتعكس التغييرات.

{{% /alert %}}

### شطب الكلمات باستخدام StrikeOutAnnotation

Aspose.PDF for .NET يتيح لك إضافة، حذف وتحديث التعليقات في مستندات PDF. واحدة من الفئات تتيح لك أيضًا شطب التعليقات. هذا مفيد عندما تريد شطب جزء أو أكثر من النص في مستند. يتم الاحتفاظ بالتعليقات في مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). يمكن استخدام فئة تسمى [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) لإضافة تعليقات شطب إلى مستند PDF.

لشطب جزء معين من TextFragment:

1. ابحث عن TextFragment في ملف PDF.
1. احصل على إحداثيات كائن TextFragment.
1. استخدم الإحداثيات لإنشاء كائن StrikeOutAnnotation.

تظهر مقتطفات الشيفرة التالية كيفية البحث عن TextFragment معين وإضافة StrikeOutAnnotation إلى ذلك الكائن.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void StrikeOutTextInDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        // Create TextFragment Absorber instance to search for a particular text fragment
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Estoque");

        // Iterate through pages of PDF document
        foreach (var page in document.Pages)
        {
            // Accept the absorber for the current page
            page.Accept(textFragmentAbsorber);
        }

        // Get the collection of absorbed text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Iterate through the collection of text fragments
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Get rectangular dimensions of the TextFragment object
            var rect = new Aspose.Pdf.Rectangle(
                (float)textFragment.Position.XIndent,
                (float)textFragment.Position.YIndent,
                (float)textFragment.Position.XIndent + (float)textFragment.Rectangle.Width,
                (float)textFragment.Position.YIndent + (float)textFragment.Rectangle.Height);

            // Instantiate StrikeOut Annotation instance
            var strikeOut = new Aspose.Pdf.Annotations.StrikeOutAnnotation(textFragment.Page, rect)
            {
                // Set opacity for annotation
                Opacity = 0.80f,

                // Set the color of annotation
                Color = Aspose.Pdf.Color.Red
            };

            // Set the border for annotation instance
            strikeOut.Border = new Aspose.Pdf.Annotations.Border(strikeOut);

            // Add annotation to the annotations collection of the TextFragment's page
            textFragment.Page.Annotations.Add(strikeOut);
        }

        // Save PDF document
        document.Save(dataDir + "StrikeOutWords_out.pdf");
    }
}
```

## حذف جميع التعليقات من صفحة ملف PDF

تحتوي مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) على جميع التعليقات لتلك الصفحة المعينة. لحذف جميع التعليقات من صفحة، استدعِ طريقة *Delete* لمجموعة AnnotationCollectoin.

تظهر مقتطفات الشيفرة التالية كيفية حذف جميع التعليقات من صفحة معينة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotationsFromPage.pdf"))
    {
        // Delete all annotations from the first page
        document.Pages[1].Annotations.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
    }
}
```

## حذف تعليق معين من ملف PDF

{{% alert color="primary" %}}

يمكنك التحقق من جودة Aspose.PDF والحصول على النتائج عبر الإنترنت من خلال هذا الرابط:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF يتيح لك إزالة تعليق معين من ملف PDF. يشرح هذا الموضوع كيفية القيام بذلك.

لحذف تعليق معين من PDF، استدعِ [طريقة Delete لمجموعة AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). تنتمي هذه المجموعة إلى كائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). تتطلب طريقة Delete فهرس التعليق الذي تريد حذفه. ثم، احفظ ملف PDF المحدث. تظهر مقتطفات الشيفرة التالية كيفية حذف تعليق معين.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularAnnotation.pdf"))
    {
        // Delete a particular annotation by index (e.g., the first annotation on the first page)
        document.Pages[1].Annotations.Delete(1);

        // Save PDF document
        document.Save(dataDir + "DeleteParticularAnnotation_out.pdf");
    }
}
```

## الحصول على جميع التعليقات من صفحة مستند PDF

Aspose.PDF يتيح لك الحصول على التعليقات من مستند كامل، أو من صفحة معينة. للحصول على جميع التعليقات من الصفحة في مستند PDF، قم بالتكرار عبر مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لموارد الصفحة المطلوبة. تظهر مقتطفات الشيفرة التالية كيفية الحصول على جميع التعليقات من صفحة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAllAnnotationsFromPage.pdf"))
    {
        // Loop through all the annotations on the first page
        foreach (Aspose.Pdf.Annotations.MarkupAnnotation annotation in document.Pages[1].Annotations)
        {
            // Get annotation properties
            Console.WriteLine("Title : {0} ", annotation.Title);
            Console.WriteLine("Subject : {0} ", annotation.Subject);
            Console.WriteLine("Contents : {0} ", annotation.Contents);
        }
    }
}
```

يرجى ملاحظة أنه للحصول على جميع التعليقات من ملف PDF بالكامل، يجب عليك التكرار عبر مجموعة فئة PageCollection الخاصة بالمستند قبل التنقل عبر مجموعة فئة AnnotationCollection. يمكنك الحصول على كل تعليق من المجموعة في نوع تعليق أساسي يسمى فئة MarkupAnnotation ثم عرض خصائصه.

## الحصول على تعليق معين من ملف PDF

التعليقات مرتبطة بالصفحات الفردية ومخزنة في مجموعة [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). للحصول على تعليق معين، حدد فهرسه. هذا يعيد كائن [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) الذي يحتاج إلى تحويله إلى نوع تعليق معين، على سبيل المثال [TextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textannotation). تظهر مقتطفات الشيفرة التالية كيفية الحصول على تعليق معين وخصائصه.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetParticularAnnotation.pdf"))
    {
        // Get a particular annotation by index (e.g., the first annotation on the first page)
        var textAnnotation = (Aspose.Pdf.Annotations.TextAnnotation)document.Pages[1].Annotations[1];

        // Get annotation properties
        Console.WriteLine("Title : {0} ", textAnnotation.Title);
        Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
        Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
    }
}
```

## الحصول على مورد التعليق

Aspose.PDF يتيح لك الحصول على مورد التعليق من مستند كامل، أو من صفحة معينة. تظهر مقتطفات الشيفرة التالية كيفية الحصول على مورد التعليق ككائن [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) من ملف PDF المدخل.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAndGetResourceOfAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create a screen annotation with a SWF file
        var sa = new Aspose.Pdf.Annotations.ScreenAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
        document.Pages[1].Annotations.Add(sa);

        // Save PDF document with the new annotation
        document.Save(dataDir + "GetResourceOfAnnotation_out.pdf");

        // Open the updated document
        var document1 = new Aspose.Pdf.Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

        // Get the action of the annotation
        var action = (document1.Pages[1].Annotations[1] as Aspose.Pdf.Annotations.ScreenAnnotation).Action as Aspose.Pdf.Annotations.RenditionAction;

        // Get the rendition of the rendition action
        var rendition = action.Rendition;

        // Get the media clip
        var clip = (rendition as Aspose.Pdf.Annotations.MediaRendition).MediaClip;
        var data = (clip as Aspose.Pdf.Annotations.MediaClipData).Data;

        // Read the media data
        using (var ms = new MemoryStream())
        {
            byte[] buffer = new byte[1024];
            int read = 0;

            // Data of media are accessible in FileSpecification.Contents
            using (var source = data.Contents)
            {
                while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
                {
                    ms.Write(buffer, 0, read);
                }
            }

            Console.WriteLine(rendition.Name);
            Console.WriteLine(action.RenditionOperation);
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>