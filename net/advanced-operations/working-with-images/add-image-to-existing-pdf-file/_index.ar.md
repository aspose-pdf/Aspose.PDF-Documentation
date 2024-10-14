---
title: إضافة صورة إلى ملف PDF باستخدام C#
linktitle: إضافة صورة
type: docs
weight: 10
url: /net/add-image-to-existing-pdf-file/
description: تصف هذه القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام مكتبة C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة صورة إلى ملف PDF باستخدام C#",
    "alternativeHeadline": "كيفية إضافة صورة إلى ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, إضافة صورة إلى pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "dateModified": "2022-02-04",
    "description": "تصف هذه القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام مكتبة C#."
}
</script>
## إضافة صورة في ملف PDF موجود

كل صفحة PDF تحتوي على خصائص الموارد والمحتويات. يمكن أن تكون الموارد صورًا ونماذج على سبيل المثال، بينما يتم تمثيل المحتوى بمجموعة من مُشغلات PDF. كل مُشغل له اسمه وحجته. يستخدم هذا المثال مشغلات لإضافة صورة إلى ملف PDF.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

لإضافة صورة إلى ملف PDF موجود:

- إنشاء كائن Document وفتح مستند PDF الإدخال.
- الحصول على الصفحة التي تريد إضافة صورة إليها.
- إضافة الصورة إلى مجموعة الموارد في الصفحة.
- استخدم المشغلات لوضع الصورة على الصفحة:
- استخدم مُشغل GSave لحفظ الحالة الرسومية الحالية.
- استخدم مُشغل ConcatenateMatrix لتحديد مكان وضع الصورة.
- استخدم مُشغل Do لرسم الصورة على الصفحة.
- أخيرًا، استخدم مُشغل GRestore لحفظ الحالة الرسومية المحدثة.
- حفظ الملف.
توضح الشفرة التالية كيفية إضافة الصورة في مستند PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "AddImage.pdf");

// تعيين الإحداثيات
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// الحصول على الصفحة حيث تحتاج إلى إضافة الصورة
Page page = pdfDocument.Pages[1];
// تحميل الصورة في تيار
FileStream imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open);
// إضافة الصورة إلى مجموعة الصور في موارد الصفحة
page.Resources.Images.Add(imageStream);
// باستخدام مُشغل GSave: يحفظ هذا المشغل الحالة الرسومية الحالية
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// إنشاء كائنات Rectangle و Matrix
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// باستخدام ConcatenateMatrix (تقارن الطاقم) المُشغل: يُعرف كيف يجب وضع الصورة
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// باستخدام مُشغل Do: يرسم هذا المشغل الصورة
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// باستخدام مُشغل GRestore: يستعيد هذا المُشغل الحالة الرسومية
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "AddImage_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```
{{% alert color="primary" %}}

بشكل افتراضي، جودة الJPEG مضبوطة على 100%. لتطبيق ضغط وجودة أفضل، استخدم الطرق البديلة التالية:

{{% /alert %}}

- تم إضافة تحميل لطريقة Replace في صف XImageCollection: public void Replace(int index, Stream stream, int quality)
- تم إضافة تحميل لطريقة Add في صف XImageCollection: public void Add(Stream stream, int quality)

## إضافة صورة في ملف PDF موجود (Facades)

هناك أيضًا طريقة بديلة وأسهل لإضافة صورة إلى ملف PDF.
هناك أيضاً طريقة بديلة وأسهل لإضافة صورة إلى ملف PDF.

```csharp
string imageFileName = Path.Combine(_dataDir, "Images", "Sample-01.jpg");
string outputPdfFileName = Path.Combine(_dataDir, "Example-add-image-mender.pdf");
Document document = new Document();
Page page = document.Pages.Add();
page.SetPageSize(PageSize.A3.Height, PageSize.A3.Width);
page = document.Pages.Add();
Aspose.Pdf.Facades.PdfFileMend mender = new Aspose.Pdf.Facades.PdfFileMend(document);
mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);
document.Save(outputPdfFileName);
```

## وضع الصورة على الصفحة والحفاظ على نسبة الأبعاد (التحكم)

إذا لم نكن نعرف أبعاد الصورة فهناك فرصة كبيرة للحصول على صورة مشوهة على الصفحة. يوضح المثال التالي إحدى الطرق لتجنب ذلك.

```csharp
public static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    var bitmap = System.Drawing.Image.FromFile(_dataDir + "3410492.jpg");

    int width;
    int height;

    width = bitmap.Width;
    height = bitmap.Height;

    var document = new Aspose.Pdf.Document();

    var page = document.Pages.Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page.AddImage(_dataDir + "3410492.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));
    document.Save(_dataDir + "sample_image.pdf");
}
```
## تحديد ما إذا كانت الصورة داخل ملف PDF ملونة أو أبيض وأسود

يمكن تطبيق أنواع مختلفة من الضغط على الصور لتقليل حجمها. نوع الضغط المطبق على الصورة يعتمد على فضاء الألوان للصورة المصدر، أي إذا كانت الصورة ملونة (RGB)، يتم تطبيق ضغط JPEG2000، وإذا كانت أبيض وأسود، ينبغي تطبيق ضغط JBIG2/JBIG2000. لذلك، تحديد نوع كل صورة واستخدام نوع الضغط المناسب سيخلق ناتجًا مثاليًا/مُحسنًا.

قد يحتوي ملف PDF على عناصر مثل النص، الصورة، الرسم البياني، المرفق، التعليق التوضيحي وغيرها، وإذا كان ملف PDF المصدر يحتوي على صور، يمكننا تحديد فضاء الألوان للصورة وتطبيق الضغط المناسب للصورة لتقليل حجم ملف PDF. يوضح الشفرة التالية الخطوات لتحديد ما إذا كانت الصورة داخل PDF ملونة أو أبيض وأسود.

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// عداد للصور بالرمادي
int grayscaled = 0;
// عداد للصور RGB
int rgd = 0;

using (Document document = new Document(dataDir + "ExtractImages.pdf"))
{
    foreach (Page page in document.Pages)
    {
        Console.WriteLine("--------------------------------");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
        page.Accept(abs);
        // احصل على عدد الصور على صفحة معينة
        Console.WriteLine("Total Images = {0} over page number {1}", abs.ImagePlacements.Count, page.Number);
        // Document.Pages[29].Accept(abs);
        int image_counter = 1;
        foreach (ImagePlacement ia in abs.ImagePlacements)
        {
            ColorType colorType = ia.Image.GetColorType();
            switch (colorType)
            {
                case ColorType.Grayscale:
                    ++grayscaled;
                    Console.WriteLine("Image {0} is GrayScale...", image_counter);
                    break;
                case ColorType.Rgb:
                    ++rgd;
                    Console.WriteLine("Image {0} is RGB...", image_counter);
                    break;
            }
            image_counter += 1;
        }
    }
}
```
## التحكم في جودة الصورة

من الممكن التحكم في جودة الصورة التي يتم إضافتها إلى ملف PDF. استخدم الطريقة [Replace](https://reference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) المعدلة في فئة [XImageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection).

يوضح الشفرة التالية كيفية تحويل جميع صور المستند إلى صور JPEG التي تستخدم جودة 80% للضغط.

```csharp
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document(inFile);
foreach (Aspose.PDF.Page page in pdfDocument.Pages)
{
    int idx = 1;
    foreach (Aspose.PDF.XImage image in page.Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            page.Resources.Images.Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }
}

// pdfDocument.OptimizeResources();

pdfDocument.Save(outFile);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "AU",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة تعديل PDF لـ .NET",
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
```

