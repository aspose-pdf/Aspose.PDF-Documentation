---
title: إضافة صورة إلى PDF باستخدام C#
linktitle: إضافة صورة
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/add-image-to-existing-pdf-file/
description: يصف هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام مكتبة C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image to PDF using C#",
    "alternativeHeadline": "Add Images PDFs in C#",
    "abstract": "تتيح الوظيفة الجديدة في مكتبة Aspose.PDF للمستخدمين إضافة صور بسلاسة إلى ملفات PDF الموجودة باستخدام C#. تبسط هذه الميزة معالجة PDF من خلال تمكين تحديد المواقع الدقيقة وتغيير حجم الصور مباشرة داخل المستند، مما يضمن تكاملًا عالي الجودة والتحكم في العناصر المرئية. مع دعم تنسيقات الصور المختلفة والتكوينات، تعزز هذه الأداة مرونة إدارة محتوى PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Image to PDF, C#, Aspose.PDF, PDF document generation, image compression, image aspect ratio, PDF file manipulation, add image method, XImage class, clipping mask",
    "wordcount": "2095",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2025-04-08",
    "description": "يصف هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام مكتبة C#."
}
</script>

## إضافة صورة في ملف PDF موجود

كل صفحة PDF تحتوي على خصائص الموارد والمحتويات. يمكن أن تكون الموارد صورًا ونماذج على سبيل المثال، بينما يتم تمثيل المحتوى بمجموعة من مشغلات PDF. لكل مشغل اسم وحجة. يستخدم هذا المثال المشغلات لإضافة صورة إلى ملف PDF.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

لإضافة صورة إلى ملف PDF موجود:

- أنشئ كائن Document وافتح مستند PDF المدخل.
- احصل على الصفحة التي تريد إضافة صورة إليها.
- أضف الصورة إلى مجموعة موارد الصفحة.
- استخدم المشغلات لوضع الصورة على الصفحة:
- استخدم مشغل GSave لحفظ الحالة الرسومية الحالية.
- استخدم مشغل ConcatenateMatrix لتحديد مكان وضع الصورة.
- استخدم مشغل Do لرسم الصورة على الصفحة.
- أخيرًا، استخدم مشغل GRestore لحفظ الحالة الرسومية المحدثة.
- احفظ الملف.
تظهر مقتطفات الكود التالية كيفية إضافة الصورة في مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where image needs to be added
        var page = document.Pages[1];

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "AddImage.jpg", FileMode.Open))
        {
            // Add image to Images collection of Page Resources
            page.Resources.Images.Add(imageStream);

            // Using GSave operator: this operator saves the current graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GSave());

            // Create Rectangle and Matrix objects to define image positioning
            var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
            var matrix = new Aspose.Pdf.Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });

            // Using ConcatenateMatrix operator: defines how the image must be placed
            page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

            // Retrieve the added image and use Do operator to draw it
            var ximage = page.Resources.Images[page.Resources.Images.Count];
            page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

            // Using GRestore operator: this operator restores the graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
        }

        // Save PDF document
        document.Save(dataDir + "AddImage_out.pdf");
    }
}
```

{{% alert color="primary" %}}

بشكل افتراضي، يتم تعيين جودة JPEG إلى 100%. لتطبيق ضغط وجودة أفضل، استخدم التحميلات التالية:

{{% /alert %}}

- تم إضافة تحميل طريقة Replace إلى فئة XImageCollection: public void Replace(int index, Stream stream, int quality)
- تم إضافة تحميل طريقة Add إلى فئة XImageCollection: public void Add(Stam stream, int quality)

## إضافة صورة في ملف PDF موجود (واجهات)

هناك أيضًا طريقة بديلة وأسهل لإضافة صورة إلى ملف PDF. يمكنك استخدام طريقة [AddImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) من فئة [PdfFileMend](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilemend). تتطلب طريقة [AddImage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) الصورة التي يجب إضافتها، ورقم الصفحة التي تحتاج إلى إضافة الصورة إليها ومعلومات الإحداثيات. بعد ذلك، احفظ ملف PDF المحدث باستخدام طريقة Close. تظهر مقتطفات الكود التالية كيفية إضافة صورة في ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDFUsingPdfFileMender()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add first page with specified size
        var page = document.Pages.Add();
        page.SetPageSize(Aspose.Pdf.PageSize.A3.Height, Aspose.Pdf.PageSize.A3.Width);

        // Add second page
        page = document.Pages.Add();

        // Create PdfFileMend object
        var mender = new Aspose.Pdf.Facades.PdfFileMend(document);

        // Add image to the first page using the mender
        mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);

        // Save PDF document
        document.Save(dataDir + "AddImageMender_out.pdf");
    }
}
```

أحيانًا، من الضروري قص صورة قبل إدراجها في PDF. يمكنك استخدام طريقة `AddImage()` لدعم إضافة الصور المقصوصة:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");
    var outputPdfFileName = dataDir + "Example-add-image-mender.pdf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (var imgStream = File.OpenRead(imageFileName))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add page
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document to the specified file path
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## وضع الصورة على الصفحة والحفاظ على (التحكم في) نسبة العرض إلى الارتفاع

إذا لم نكن نعرف أبعاد الصورة، فهناك فرصة كبيرة للحصول على صورة مشوهة على الصفحة. يظهر المثال التالي إحدى الطرق لتجنب ذلك.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Load the image
    using (var bitmap = System.Drawing.Image.FromFile(dataDir + "InputImage.jpg"))
    {
        // Get the original width and height of the image
        int width = bitmap.Width;
        int height = bitmap.Height;

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Define the scaled width and height while preserving the aspect ratio
            int scaledWidth = 400;
            int scaledHeight = scaledWidth * height / width;

            // Add the image to the page
            page.AddImage(dataDir + "InputImage.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));

            // Save PDF document
            document.Save(dataDir + "PreserveAspectRatio.pdf");
        }
    }
}
```

أحيانًا، تواجه صورة كبيرة مشاكل في تغيير الحجم عند إضافتها إلى PDF. تقوم مقتطفات الكود التالية بتغيير حجم الصورة وفقًا لأبعاد صفحة PDF، مما يضمن أن الصورة تناسب بشكل صحيح وتبدو أفضل.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();
    var file = dataDir + "AddImageAccordingToPage.jpg";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var pdfImageSection = document.Pages.Add();
        using (var stream = new FileStream(file, FileMode.Open))
        {
            // Open bitmap
            using (var img = new Bitmap(stream))
            {
                // Scale image according to page dimensions
                using (var scaledImg = ScaleImage(img, (int)pdfImageSection.PageInfo.Width, (int)pdfImageSection.PageInfo.Height))
                {
                    using (var ms = new MemoryStream())
                    {
                        scaledImg.Save(ms, ImageFormat.Jpeg);
                        ms.Seek(0, SeekOrigin.Begin);
                        var image = new Aspose.Pdf.Image
                        {
                            ImageStream = ms
                        };

                        // Add the image to the page
                        pdfImageSection.Paragraphs.Add(image);

                        // Save PDF document
                        document.Save("AddImageAccordingToPage.pdf");
                    }
                }
            }
        }
    }
}

private static Image ScaleImage(Image image, int maxWidth, int maxHeight)
{
    var ratioX = (double)maxWidth / image.Width;
    var ratioY = (double)maxHeight / image.Height;
    var ratio = Math.Min(ratioX, ratioY);
    var newWidth = (int)(image.Width * ratio);
    var newHeight = (int)(image.Height * ratio);
    var newImage = new Bitmap(newWidth, newHeight);
    using (var graphics = Graphics.FromImage(newImage))
    {
        graphics.DrawImage(image, 0, 0, newWidth, newHeight);
    }
    return newImage;
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();
    var file = dataDir + "AddImageAccordingToPage.jpg";

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    
    // Add page
    var pdfImageSection = document.Pages.Add();
    using var stream = new FileStream(file, FileMode.Open);
    // Open bitmap
    using var img = new Bitmap(stream);
    // Scale image according to page dimensions
    using var scaledImg = ScaleImage(img, (int)pdfImageSection.PageInfo.Width, (int)pdfImageSection.PageInfo.Height);
    using var ms = new MemoryStream();
    scaledImg.Save(ms, ImageFormat.Jpeg);
    ms.Seek(0, SeekOrigin.Begin);
    var image = new Aspose.Pdf.Image
    {
        ImageStream = ms
    };

    // Add the image to the page
    pdfImageSection.Paragraphs.Add(image);

    // Save PDF document
    document.Save("AddImageAccordingToPage.pdf");

}

private static Image ScaleImage(Image image, int maxWidth, int maxHeight)
{
    var ratioX = (double)maxWidth / image.Width;
    var ratioY = (double)maxHeight / image.Height;
    var ratio = Math.Min(ratioX, ratioY);
    var newWidth = (int)(image.Width * ratio);
    var newHeight = (int)(image.Height * ratio);
    var newImage = new Bitmap(newWidth, newHeight);
    using var graphics = Graphics.FromImage(newImage);
    graphics.DrawImage(image, 0, 0, newWidth, newHeight);
    return newImage;
}
```
{{< /tab >}}
{{< /tabs >}}

## تحديد ما إذا كانت الصورة داخل PDF ملونة أو بالأبيض والأسود

يمكن تطبيق نوع مختلف من الضغط على الصور لتقليل حجمها. يعتمد نوع الضغط المطبق على الصورة على ColorSpace للصورة المصدر، أي إذا كانت الصورة ملونة (RGB)، فيجب تطبيق ضغط JPEG2000، وإذا كانت بالأبيض والأسود، فيجب تطبيق ضغط JBIG2/JBIG2000. لذلك، فإن تحديد كل نوع من الصور واستخدام نوع الضغط المناسب سيخلق أفضل/أمثل مخرجات.

قد يحتوي ملف PDF على عناصر نصوص وصور ورسوم بيانية ومرفقات وتعليقات وما إلى ذلك، وإذا كان ملف PDF المصدر يحتوي على صور، يمكننا تحديد مساحة لون الصورة وتطبيق الضغط المناسب لتقليل حجم ملف PDF. تظهر مقتطفات الكود التالية الخطوات لتحديد ما إذا كانت الصورة داخل PDF ملونة أو بالأبيض والأسود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageTypesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Counters for grayscale and RGB images
    int grayscaled = 0;
    int rgb = 0;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            Console.WriteLine("--------------------------------");
            var abs = new Aspose.Pdf.ImagePlacementAbsorber();
            page.Accept(abs);

            // Get the count of images on the current page
            Console.WriteLine("Total Images = {0} on page number {1}", abs.ImagePlacements.Count, page.Number);

            // Iterate through all the image placements on the page
            int image_counter = 1;
            foreach (Aspose.Pdf.ImagePlacement ia in abs.ImagePlacements)
            {
                // Determine the color type of the image
                var colorType = ia.Image.GetColorType();
                switch (colorType)
                {
                    case Aspose.Pdf.ColorType.Grayscale:
                        ++grayscaled;
                        Console.WriteLine("Image {0} is Grayscale...", image_counter);
                        break;
                    case Aspose.Pdf.ColorType.Rgb:
                        ++rgb;
                        Console.WriteLine("Image {0} is RGB...", image_counter);
                        break;
                }
                image_counter += 1;
            }
        }
    }
}
```

## التحكم في جودة الصورة

من الممكن التحكم في جودة الصورة التي تتم إضافتها إلى ملف PDF. استخدم طريقة [Replace](https://reference.aspose.com/pdf/ar/net/aspose.pdf.ximagecollection/replace/methods/1) المحملة في فئة [XImageCollection](https://reference.aspose.com/pdf/ar/net/aspose.pdf/ximagecollection).

توضح مقتطفات الكود التالية كيفية تحويل جميع صور المستند إلى JPEGs تستخدم جودة 80% للضغط.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImagesInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            int idx = 1;
            // Iterate through all images in the page's resources
            foreach (Aspose.Pdf.XImage image in page.Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save the image as JPEG with 80% quality
                    image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
                    // Replace the image in the page's resources
                    page.Resources.Images.Replace(idx, imageStream, 80);
                    idx = idx + 1;
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceImages_out.pdf");
    }
}
```

## دعم تطبيق قناع قص على الصور

يعمل وضع شكل متجه فوق الصورة النقطية الأساسية كقناع، مما يكشف فقط الجزء من التصميم الأساسي الذي يتماشى مع الشكل المتجه. ستظل جميع المناطق خارج الشكل مخفية.

تقوم مقتطفات الكود بتحميل PDF، وفتح ملفي صورة، وتطبيق تلك الصور كأقنعة قوالب على أول صورتين في الصفحة الأولى من PDF.

يمكن إضافة قناع القالب بواسطة طريقة 'XImage.AddStencilMask(Stream maskStream)':

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStencilMasksToImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStencilMasksToImages.pdf"))
    {
        // Open the first mask image file
        using (var fs1 = new FileStream(dataDir + "mask1.jpg", FileMode.Open))
        {
            // Open the second mask image file
            using (var fs2 = new FileStream(dataDir + "mask2.png", FileMode.Open))
            {
                // Apply stencil mask to the first image on the first page
                document.Pages[1].Resources.Images[1].AddStencilMask(fs1);

                // Apply stencil mask to the second image on the first page
                document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddStencilMasksToImages_out.pdf");
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