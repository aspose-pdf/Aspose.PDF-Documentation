---
title: قص صفحات PDF برمجياً C#
linktitle: قص الصفحات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ar/net/crop-pages/
description: يمكنك الحصول على خصائص الصفحة، مثل العرض، الارتفاع، صندوق النزيف، صندوق القص وصندوق القطع باستخدام Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "يقدم Aspose.PDF for .NET ميزة جديدة قوية تتيح للمطورين الوصول برمجياً إلى خصائص الصفحة المختلفة في ملف PDF، بما في ذلك صندوق الوسائط، صندوق النزيف، صندوق القطع، صندوق الفن، وصندوق القص. تعمل هذه الوظيفة على تبسيط عملية تخصيص تخطيطات PDF، مما يضمن الدقة في تقديم الوثائق وتحسين جودة الطباعة مع تقليل الحواف البيضاء. مع مقتطفات الشيفرة السهلة الاستخدام، يمكن للمستخدمين دمج هذه القدرات بسلاسة في تطبيقاتهم، مما يحسن إدارة PDF والتلاعب به.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1118",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2025-04-10",
    "description": "يمكنك الحصول على خصائص الصفحة، مثل العرض، الارتفاع، صندوق النزيف، صندوق القص وصندوق القطع باستخدام Aspose.PDF for .NET."
}
</script>

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF لها عدد من الخصائص، مثل العرض، الارتفاع، صندوق النزيف، صندوق القص وصندوق القطع. يتيح لك Aspose.PDF الوصول إلى هذه الخصائص.

- **صندوق الوسائط**: صندوق الوسائط هو أكبر صندوق صفحة. يتوافق مع حجم الصفحة (مثل A4، A5، US Letter، إلخ) الذي تم اختياره عند طباعة الوثيقة إلى PostScript أو PDF. بعبارة أخرى، يحدد صندوق الوسائط الحجم الفعلي للوسائط التي يتم عرض مستند PDF عليها أو طباعته.
- **صندوق النزيف**: إذا كانت الوثيقة تحتوي على نزيف، فسيكون لدى PDF أيضاً صندوق نزيف. النزيف هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما وراء حافة الصفحة. يُستخدم لضمان أنه عند طباعة الوثيقة وقطعها إلى الحجم ("قصها")، سيصل الحبر إلى حافة الصفحة. حتى إذا تم قطع الصفحة بشكل غير دقيق - قطعها قليلاً بعيداً عن علامات القص - فلن تظهر حواف بيضاء على الصفحة.
- **صندوق القطع**: يشير صندوق القطع إلى الحجم النهائي للوثيقة بعد الطباعة والقص.
- **صندوق الفن**: صندوق الفن هو الصندوق المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يُستخدم هذا الصندوق عند استيراد مستندات PDF في تطبيقات أخرى.
- **صندوق القص**: صندوق القص هو حجم "الصفحة" الذي يتم عرض مستند PDF الخاص بك به في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق القص فقط في Adobe Acrobat. للحصول على أوصاف مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وخاصة 10.10.1 حدود الصفحة.
- **Page.Rect**: التقاطع (المستطيل المرئي عادةً) بين MediaBox وDropBox. توضح الصورة أدناه هذه الخصائص.
للحصول على مزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

يعمل مقتطف الشيفرة التالي أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

يوضح المقتطف أدناه كيفية قص الصفحة:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

في هذا المثال استخدمنا ملف عينة [هنا](crop_page.pdf). في البداية، تبدو صفحتنا كما هو موضح في الشكل 1.

بعد التغيير، ستبدو الصفحة كما في الشكل 2.

### قص المساحات البيضاء حول الصفحة

على سبيل المثال، يمكنك قص المساحات البيضاء حول الصفحة باستخدام أي مكتبة رسومات يمكنها تحميل الصور النقطية:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TrimWhiteSpaceAroundPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TrimWhiteSpaceAroundPage.pdf"))
    {
        var device = new Aspose.Pdf.Devices.PngDevice(new Resolution(300));

        using (var imageStr = new MemoryStream())
        {
            // Convert page to PNG image
            device.Process(document.Pages[1], imageStr);
            using (var pageBitmap = new Bitmap(imageStr))
            {
                document.Pages[1].CropBox = GetNewCropBox(pageBitmap, document.Pages[1].CropBox);
            }
        }
        // Save PDF document
        document.Save(dataDir + "TrimWhiteSpaceAroundPage_out.pdf");
    }
}

// Determine white areas with System.Drawing
private static Aspose.Pdf.Rectangle GetNewCropBox(Bitmap pageBitmap, Aspose.Pdf.Rectangle prevCropBox)
{
    var imageBitmapData = pageBitmap.LockBits(new Rectangle(0, 0, pageBitmap.Width, pageBitmap.Height),
                            ImageLockMode.ReadOnly, PixelFormat.Format32bppRgb);

    int toHeight = pageBitmap.Height;
    int toWidth = pageBitmap.Width;

    int? leftNonWhite = null;
    int? rightNonWhite = null;
    int? topNonWhite = null;
    int? bottomNonWhite = null;

    var imageRowBytes = new byte[imageBitmapData.Stride];
    for (int y = 0; y < toHeight; y++)
    {

        // Copy the row data to byte array
        if (IntPtr.Size == 4)
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt32() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }
        else
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt64() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }

        int? leftNonWhite_row = null;
        int? rightNonWhite_row = null;

        for (int x = 0; x < toWidth; x++)
        {
            if (imageRowBytes[x * 4] != 255
                || imageRowBytes[x * 4 + 1] != 255
                || imageRowBytes[x * 4 + 2] != 255)
            {
                if (leftNonWhite_row == null)
                {
                    leftNonWhite_row = x;
                }

                rightNonWhite_row = x;
            }
        }

        if (leftNonWhite_row != null || rightNonWhite_row != null)
        {
            if (topNonWhite == null)
            {
                topNonWhite = y;
            }

            bottomNonWhite = y;
        }

        if (leftNonWhite_row != null
            && (leftNonWhite == null || leftNonWhite > leftNonWhite_row))
        {
            leftNonWhite = leftNonWhite_row;
        }
        if (rightNonWhite_row != null
            && (rightNonWhite == null || rightNonWhite < rightNonWhite_row))
        {
            rightNonWhite = rightNonWhite_row;
        }
    }

    leftNonWhite = leftNonWhite ?? 0;
    rightNonWhite = rightNonWhite ?? toWidth;
    topNonWhite = topNonWhite ?? 0;
    bottomNonWhite = bottomNonWhite ?? toHeight;

    double xCoef = prevCropBox.Width / toWidth;
    double yCoef = prevCropBox.Height / toHeight;

    pageBitmap.UnlockBits(imageBitmapData);
    
    // Create crop box with correction to previous crop box
    return
        new Aspose.Pdf.Rectangle(
            leftNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - bottomNonWhite.Value * yCoef,
            rightNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - topNonWhite.Value * yCoef
        );
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TrimWhiteSpaceAroundPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "TrimWhiteSpaceAroundPage.pdf");
    var device = new Aspose.Pdf.Devices.PngDevice(new Resolution(300));

    using var imageStr = new MemoryStream();

    // Convert page to PNG image
    device.Process(document.Pages[1], imageStr);
    using var pageBitmap = new Bitmap(imageStr);
    document.Pages[1].CropBox = GetNewCropBox(pageBitmap, document.Pages[1].CropBox);

    // Save PDF document
    document.Save(dataDir + "TrimWhiteSpaceAroundPage_out.pdf");
}

// Determine white areas with System.Drawing
private static Aspose.Pdf.Rectangle GetNewCropBox(Bitmap pageBitmap, Aspose.Pdf.Rectangle prevCropBox)
{
    var imageBitmapData = pageBitmap.LockBits(new Rectangle(0, 0, pageBitmap.Width, pageBitmap.Height),
                            ImageLockMode.ReadOnly, PixelFormat.Format32bppRgb);

    int toHeight = pageBitmap.Height;
    int toWidth = pageBitmap.Width;

    int? leftNonWhite = null;
    int? rightNonWhite = null;
    int? topNonWhite = null;
    int? bottomNonWhite = null;

    var imageRowBytes = new byte[imageBitmapData.Stride];
    for (int y = 0; y < toHeight; y++)
    {

        // Copy the row data to byte array
        if (IntPtr.Size == 4)
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt32() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }
        else
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt64() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }

        int? leftNonWhite_row = null;
        int? rightNonWhite_row = null;

        for (int x = 0; x < toWidth; x++)
        {
            if (imageRowBytes[x * 4] != 255
                || imageRowBytes[x * 4 + 1] != 255
                || imageRowBytes[x * 4 + 2] != 255)
            {
                if (leftNonWhite_row == null)
                {
                    leftNonWhite_row = x;
                }

                rightNonWhite_row = x;
            }
        }

        if (leftNonWhite_row != null || rightNonWhite_row != null)
        {
            if (topNonWhite == null)
            {
                topNonWhite = y;
            }

            bottomNonWhite = y;
        }

        if (leftNonWhite_row != null
            && (leftNonWhite == null || leftNonWhite > leftNonWhite_row))
        {
            leftNonWhite = leftNonWhite_row;
        }
        if (rightNonWhite_row != null
            && (rightNonWhite == null || rightNonWhite < rightNonWhite_row))
        {
            rightNonWhite = rightNonWhite_row;
        }
    }

    leftNonWhite = leftNonWhite ?? 0;
    rightNonWhite = rightNonWhite ?? toWidth;
    topNonWhite = topNonWhite ?? 0;
    bottomNonWhite = bottomNonWhite ?? toHeight;

    double xCoef = prevCropBox.Width / toWidth;
    double yCoef = prevCropBox.Height / toHeight;

    pageBitmap.UnlockBits(imageBitmapData);
    
    // Create crop box with correction to previous crop box
    return
        new Aspose.Pdf.Rectangle(
            leftNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - bottomNonWhite.Value * yCoef,
            rightNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - topNonWhite.Value * yCoef
        );
}
```
{{< /tab >}}
{{< /tabs >}}

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