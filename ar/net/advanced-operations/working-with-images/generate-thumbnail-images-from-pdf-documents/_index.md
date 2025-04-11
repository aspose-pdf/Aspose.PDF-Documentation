---
title: إنشاء صور مصغرة من PDF
linktitle: إنشاء صور مصغرة
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /ar/net/generate-thumbnail-images-from-pdf-documents/
description: يصف هذا القسم كيفية إنشاء صور مصغرة من مستندات PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "Generate Thumbnails from PDF Documents Effortlessly",
    "abstract": "تتيح الميزة الجديدة للمستخدمين إنشاء صور مصغرة بكفاءة مباشرة من مستندات PDF. تعزز هذه الوظيفة إدارة المستندات من خلال تحويل صفحات PDF إلى تنسيقات صور سهلة المشاركة، مما يسهل سير العمل للمطورين والمستخدمين على حد سواء. مع دعم لمجموعة متنوعة من تنسيقات الصور، تبسط هذه الميزة عملية تصور محتوى PDF دون الحاجة إلى برامج خارجية مثل Adobe Acrobat",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Generate Thumbnail Images, PDF documents, Aspose.PDF for .NET, Acrobat SDK, image formats, PDF Manipulation Library, JavaScript, interapplication communication, thumbnail images, JPEG conversion",
    "wordcount": "767",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "يصف هذا القسم كيفية إنشاء صور مصغرة من مستندات PDF"
}
</script>

{{% alert color="primary" %}}

مجموعة أدوات Adobe Acrobat SDK هي مجموعة من الأدوات التي تساعدك في تطوير البرمجيات التي تتفاعل مع تقنية Acrobat. تحتوي مجموعة الأدوات على ملفات رأس، ومكتبات نوع، وأدوات بسيطة، وأكواد نموذجية، ووثائق.

باستخدام مجموعة أدوات Acrobat SDK، يمكنك تطوير برمجيات تتكامل مع Acrobat وAdobe Reader بعدة طرق:

- **JavaScript** — كتابة نصوص، إما في مستند PDF فردي أو خارجي، لتوسيع وظائف Acrobat أو Adobe Reader.
- **الإضافات** — إنشاء إضافات مرتبطة ديناميكيًا وتوسيع وظائف Acrobat أو Adobe Reader.
- **الاتصال بين التطبيقات** — كتابة عملية تطبيق منفصلة تستخدم الاتصال بين التطبيقات (IAC) للتحكم في وظائف Acrobat. يتم دعم DDE وOLE على Microsoft® Windows®، وأحداث Apple/AppleScript على Mac OS®. الاتصال بين التطبيقات غير متاح على UNIX®.

توفر Aspose.PDF for .NET الكثير من نفس الوظائف، مما يحررك من الاعتماد على أتمتة Adobe Acrobat. يوضح هذا المقال كيفية إنشاء صور مصغرة من مستندات PDF باستخدام أولاً مجموعة أدوات Acrobat SDK ثم Aspose.PDF.

{{% /alert %}}

## تطوير تطبيق باستخدام واجهة برمجة التطبيقات للاتصال بين التطبيقات في Acrobat

فكر في واجهة برمجة التطبيقات الخاصة بـ Acrobat على أنها تحتوي على طبقتين متميزتين تستخدمان كائنات الاتصال بين التطبيقات (IAC):

- طبقة تطبيق Acrobat (AV). تتيح لك طبقة AV التحكم في كيفية عرض المستند. على سبيل المثال، يتم عرض كائن المستند في الطبقة المرتبطة بـ Acrobat.
- طبقة المستند القابل للنقل (PD). توفر طبقة PD الوصول إلى المعلومات داخل المستند، مثل صفحة. من طبقة PD يمكنك إجراء عمليات أساسية على مستندات PDF، مثل حذف أو نقل أو استبدال الصفحات، بالإضافة إلى تغيير خصائص التعليقات. يمكنك أيضًا طباعة صفحات PDF، وتحديد النص، والوصول إلى النص المعالج، وإنشاء أو حذف الصور المصغرة.

نظرًا لأن هدفنا هو تحويل صفحات PDF إلى صور مصغرة، فإننا نركز أكثر على IAC. تحتوي واجهة برمجة التطبيقات IAC على كائنات مثل PDDoc وPDPage وPDAnnot وغيرها، مما يمكّن المستخدم من التعامل مع طبقة المستند القابل للنقل (PD). يقوم نموذج الكود التالي بمسح مجلد وتحويل صفحات PDF إلى صور مصغرة. باستخدام مجموعة أدوات Acrobat SDK، يمكننا أيضًا قراءة بيانات التعريف الخاصة بـ PDF واسترداد عدد الصفحات في المستند.

### نهج Acrobat

من أجل إنشاء الصور المصغرة لكل مستند، استخدمنا مجموعة أدوات Adobe Acrobat 7.0 وMicrosoft .NET 2.0 Framework.

تجمع [مجموعة أدوات Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) مع النسخة الكاملة من Adobe Acrobat مكتبة COM من الكائنات (للأسف، لا تكشف Adobe Reader المجانية عن واجهات COM) التي يمكن استخدامها للتلاعب والوصول إلى معلومات PDF. باستخدام هذه الكائنات COM عبر COM Interop، قم بتحميل مستند PDF، واحصل على الصفحة الأولى وقم بعرض تلك الصفحة على الحافظة. ثم، باستخدام .NET Framework، انسخ هذا إلى صورة نقطية، وقم بتغيير حجم الصورة ودمجها واحفظ النتيجة كملف GIF أو PNG.

بمجرد تثبيت Adobe Acrobat، استخدم regedit.exe وابحث تحت HKEY_CLASSES_ROOT عن إدخال يسمى AcroExch.PDDoc.

**السجل يظهر إدخال AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // Acrobat objects
    Acrobat.CAcroPDDoc pdfDoc;
    Acrobat.CAcroPDPage pdfPage;
    Acrobat.CAcroRect pdfRect;
    Acrobat.CAcroPoint pdfPoint;

    AppSettingsReader appSettings = new AppSettingsReader();
    string pdfInputPath = appSettings.GetValue("pdfInputPath", typeof(string)).ToString();
    string pngOutputPath = appSettings.GetValue("pngOutputPath", typeof(string)).ToString();
    string templatePortraitFile = Application.StartupPath + @"\pdftemplate_portrait.gif";
    string templateLandscapeFile = Application.StartupPath + @"\pdftemplate_landscape.gif";

    // Get list of files to process from the input path
    string[] files = Directory.GetFiles(pdfInputPath, "*.pdf");

    for (int n = 0; n < files.Length; n++)
    {
        string inputFile = files[n];
        string outputFile = Path.Combine(pngOutputPath, Path.GetFileNameWithoutExtension(inputFile) + ".png");

        // Create PDF document
        pdfDoc = (Acrobat.CAcroPDDoc)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.PDDoc", "");

        if (pdfDoc.Open(inputFile) == 0)
        {
            throw new FileNotFoundException($"Unable to open PDF file: {inputFile}");
        }

        int pageCount = pdfDoc.GetNumPages();
        pdfPage = (Acrobat.CAcroPDPage)pdfDoc.AcquirePage(0);
        pdfPoint = (Acrobat.CAcroPoint)pdfPage.GetSize();

        pdfRect = (Acrobat.CAcroRect)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.Rect", "");
        pdfRect.Left = 0;
        pdfRect.right = pdfPoint.x;
        pdfRect.Top = 0;
        pdfRect.bottom = pdfPoint.y;

        pdfPage.CopyToClipboard(pdfRect, 0, 0, 100);
        IDataObject clipboardData = Clipboard.GetDataObject();

        if (clipboardData.GetDataPresent(DataFormats.Bitmap))
        {
            Bitmap pdfBitmap = (Bitmap)clipboardData.GetData(DataFormats.Bitmap);

            int thumbnailWidth = 45;
            int thumbnailHeight = 59;
            string templateFile = pdfPoint.x < pdfPoint.y ? templatePortraitFile : templateLandscapeFile;

            if (pdfPoint.x > pdfPoint.y)
            {
                // Swap width and height for landscape orientation
                (thumbnailWidth, thumbnailHeight) = (thumbnailHeight, thumbnailWidth);
            }

            Bitmap templateBitmap = new Bitmap(templateFile);
            Image pdfImage = pdfBitmap.GetThumbnailImage(thumbnailWidth, thumbnailHeight, null, IntPtr.Zero);

            Bitmap thumbnailBitmap = new Bitmap(thumbnailWidth + 7, thumbnailHeight + 7, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

            templateBitmap.MakeTransparent();

            using (Graphics thumbnailGraphics = Graphics.FromImage(thumbnailBitmap))
            {
                thumbnailGraphics.DrawImage(pdfImage, 2, 2, thumbnailWidth, thumbnailHeight);
                thumbnailGraphics.DrawImage(templateBitmap, 0, 0);
                thumbnailBitmap.Save(outputFile, System.Drawing.Imaging.ImageFormat.Png);
            }

            Console.WriteLine("Generated thumbnail: {0}", outputFile);

            pdfDoc.Close();
            Marshal.ReleaseComObject(pdfPage);
            Marshal.ReleaseComObject(pdfRect);
            Marshal.ReleaseComObject(pdfDoc);
        }
    }
}
```

## نهج Aspose.PDF for .NET

توفر Aspose.PDF for .NET دعمًا واسعًا للتعامل مع مستندات PDF. كما تدعم القدرة على تحويل صفحات مستندات PDF إلى مجموعة متنوعة من تنسيقات الصور. يمكن تحقيق الوظيفة الموضحة أعلاه بسهولة باستخدام Aspose.PDF for .NET.

تتمتع Aspose.PDF بمزايا مميزة:

- لا تحتاج إلى تثبيت Adobe Acrobat على نظامك للعمل مع ملفات PDF.
- استخدام Aspose.PDF for .NET بسيط وسهل الفهم مقارنةً بأتمتة Acrobat.

إذا كنا بحاجة إلى تحويل صفحات PDF إلى JPEGs، فإن مساحة أسماء [Aspose.PDF.Devices](https://reference.aspose.com/pdf/ar/net/aspose.pdf.devices) توفر فئة تسمى [JpegDevice](https://reference.aspose.com/pdf/ar/net/aspose.pdf.devices/jpegdevice) لعرض صفحات PDF كصور JPEG. يرجى إلقاء نظرة على نموذج الكود التالي.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Retrieve names of all the PDF files in a particular directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

    // Iterate through all the files entries in array
    for (int counter = 0; counter < fileEntries.Length; counter++)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(fileEntries[counter]))
        {
            for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
            {
                using (FileStream imageStream = new FileStream(dataDir + @"\Thumbanils" + counter.ToString() + "_" + pageCount + ".jpg", FileMode.Create))
                {
                    var resolution = new Aspose.Pdf.Devices.Resolution(300);
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(45, 59, resolution, 100);
                    // Convert a particular page and save the image to stream
                    jpegDevice.Process(document.Pages[pageCount], imageStream);
                }
            }
        }
    }
}
```

{{% alert color="primary" %}}

- شكرًا لـ CodeProject على [إنشاء صورة مصغرة من مستند PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- شكرًا لـ Acrobat على [مرجع مجموعة أدوات Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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