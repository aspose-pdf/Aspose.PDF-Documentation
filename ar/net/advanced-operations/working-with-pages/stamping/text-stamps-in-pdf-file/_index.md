---
title: إضافة طوابع نصية في PDF C#
linktitle: الطوابع النصية في ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/text-stamps-in-the-pdf-file/
description: إضافة طابع نصي إلى مستند PDF باستخدام فئة TextStamp مع مكتبة Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text stamps in PDF C#",
    "alternativeHeadline": "Effortlessly Add Text Stamps in PDF Documents with C#",
    "abstract": "تتيح ميزة TextStamp الجديدة في Aspose.PDF for .NET للمستخدمين إضافة طوابع نصية قابلة للتخصيص إلى مستندات PDF بسهولة. مع خصائص لحجم الخط، النمط، واللون، بالإضافة إلى خيارات المحاذاة، تعزز هذه الوظيفة توضيح المستند من خلال السماح بوضع دقيق ومظهر للنص داخل ملفات PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "765",
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "إضافة طابع نصي إلى مستند PDF باستخدام فئة TextStamp مع مكتبة Aspose.PDF for .NET."
}
</script>

## إضافة طابع نصي

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) لإضافة طابع نصي في ملف PDF. توفر فئة TextStamp الخصائص اللازمة لإنشاء طابع نصي مثل حجم الخط، نمط الخط، ولون الخط، إلخ. لإضافة طابع نصي، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp من Page لإضافة الطابع في PDF.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

تظهر مقتطفات الكود التالية كيفية إضافة طابع نصي في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Create text stamp
        var textStamp = new Aspose.Pdf.TextStamp("Sample Stamp");
        // Set whether stamp is background
        textStamp.Background = true;
        // Set origin
        textStamp.XIndent = 100;
        textStamp.YIndent = 100;
        // Rotate stamp
        textStamp.Rotate = Rotation.on90;
        // Set text properties
        textStamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        textStamp.TextState.FontSize = 14.0F;
        textStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        textStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.Aqua;
        // Add stamp to particular page
        document.Pages[1].AddStamp(textStamp);
        // Save PDF document
        document.Save(dataDir + "AddTextStamp_out.pdf");  
    }
}
```

## تحديد المحاذاة لكائن TextStamp

إضافة علامات مائية إلى مستندات PDF هي واحدة من الميزات المطلوبة بشكل متكرر و Aspose.PDF for .NET قادر تمامًا على إضافة علامات مائية نصية وصورية. لدينا فئة تُسمى [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) التي توفر ميزة إضافة طوابع نصية فوق ملف PDF. مؤخرًا، كانت هناك حاجة لدعم ميزة تحديد محاذاة النص عند استخدام كائن TextStamp. لذلك، لتلبية هذه الحاجة، قدمنا خاصية TextAlignment في فئة TextStamp. باستخدام هذه الخاصية، يمكننا تحديد محاذاة النص الأفقية.

تظهر مقتطفات الكود التالية مثالًا على كيفية تحميل مستند PDF موجود وإضافة TextStamp فوقه.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DefineAlignmentForTextStampObject()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Instantiate FormattedText object with sample string
        var text = new Aspose.Pdf.Facades.FormattedText("This");
        // Add new text line to FormattedText
        text.AddNewLineText("is sample");
        text.AddNewLineText("Center Aligned");
        text.AddNewLineText("TextStamp");
        text.AddNewLineText("Object");
        // Create TextStamp object using FormattedText
        var stamp = new Aspose.Pdf.TextStamp(text);
        // Specify the Horizontal Alignment of text stamp as Center aligned
        stamp.HorizontalAlignment = HorizontalAlignment.Center;
        // Specify the Vertical Alignment of text stamp as Center aligned
        stamp.VerticalAlignment = VerticalAlignment.Center;
        // Specify the Text Horizontal Alignment of TextStamp as Center aligned
        stamp.TextAlignment = HorizontalAlignment.Center;
        // Set top margin for stamp object
        stamp.TopMargin = 20;
        // Add the stamp object over first page of document
        document.Pages[1].AddStamp(stamp);
        // Save PDF document
        document.Save(dataDir + "StampedPDF_out.pdf");
    }
}
```

## ملء نص السكتة الدماغية كطابع في ملف PDF

لقد قمنا بتنفيذ إعداد وضع العرض لإضافة النص وتحريره. لرسم نص السكتة الدماغية، يرجى إنشاء كائن TextState وتعيين RenderingMode إلى TextRenderingMode.StrokeText واختيار اللون لخاصية StrokingColor. بعد ذلك، اربط TextState بالطابع باستخدام طريقة BindTextState().

توضح مقتطفات الكود التالية كيفية إضافة نص السكتة الدماغية:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillStrokeTextAsStampInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    // Create TextState object to transfer advanced properties
    var textState = new Aspose.Pdf.Text.TextState();
    // Set color for stroke
    textState.StrokingColor = Color.Gray;
    // Set text rendering mode
    textState.RenderingMode = Aspose.Pdf.Text.TextRenderingMode.StrokeText;
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Create PdfFileStamp
        var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp(document);
        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("PAID IN FULL", System.Drawing.Color.Gray, "Arial", Aspose.Pdf.Facades.EncodingType.Winansi, true, 78));
        // Bind TextState
        stamp.BindTextState(textState);
        // Set X,Y origin
        stamp.SetOrigin(100, 100);
        stamp.Opacity = 5;
        stamp.BlendingSpace = Aspose.Pdf.Facades.BlendingColorSpace.DeviceRGB;
        stamp.Rotation = 45.0F;
        stamp.IsBackground = false;
        // Add Stamp
        fileStamp.AddStamp(stamp);
        // Save PDF document
        fileStamp.Save(dataDir + "FillStrokeTextAsStampInPdfFile_out.pdf");
        fileStamp.Close();
    }
}
```

## إضافة طابع نصي وضبط حجم الخط تلقائيًا

توضح مقتطفات الكود التالية كيفية إضافة طابع نصي إلى ملف PDF وضبط حجم الخط تلقائيًا ليتناسب مع مستطيل الطابع.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        stamp.Width = 400;
        stamp.Height = 200;
        //Add stamp
        document.Pages[1].AddStamp(stamp);
        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStamp_out.pdf");
    }
}
```
توضح مقتطفات الكود التالية كيفية إضافة طابع نصي إلى ملف PDF وضبط حجم الخط تلقائيًا ليتناسب مع مستطيل الطابع. يكون مستطيل الطابع افتراضيًا بحجم الصفحة.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStampToFitPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        //Add stamp
        document.Pages[1].AddStamp(stamp);
        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStampToFItPage_out.pdf");
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