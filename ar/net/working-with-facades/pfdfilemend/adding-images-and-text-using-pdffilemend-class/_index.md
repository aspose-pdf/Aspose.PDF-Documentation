---
title: إضافة الصور والنصوص
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/adding-images-and-text-using-pdffilemend-class/
description: يشرح هذا القسم كيفية إضافة الصور والنصوص باستخدام فئة PdfFileMend.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Images and Text",
    "alternativeHeadline": "Enhance PDF by Adding Images and Text Precisely",
    "abstract": "قم بتحسين مستندات PDF الخاصة بك بسهولة مع فئة PdfFileMend الجديدة، التي تتيح لك إضافة الصور والنصوص في مواقع محددة داخل ملفات PDF الموجودة. استخدم طرق AddImage و AddText البديهية لدمج تنسيقات الصور المختلفة والنص المنسق بسلاسة، مما يضمن الدقة في التحديد والمكان. قم بتبسيط مهام معالجة PDF الخاصة بك مع القدرة على تخصيص تراكبات الصور وتغليف النص، مما يجعل مستنداتك جذابة بصريًا ومفيدة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1324",
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
    "url": "/net/adding-images-and-text-using-pdffilemend-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-images-and-text-using-pdffilemend-class/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

يمكن أن تساعدك فئة [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) في إضافة الصور والنصوص في مستند PDF موجود، في موقع محدد. توفر طريقتين تحملان أسماء [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) و [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). تتيح لك طريقة [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) إضافة صور من نوع JPG و GIF و PNG و BMP. تأخذ طريقة [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) وسيطًا من نوع [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) وتضيفه في ملف PDF الموجود. يمكن إضافة الصور والنصوص في منطقة مستطيلة محددة بواسطة إحداثيات النقاط السفلية اليسرى والعلوية اليمنى. أثناء إضافة الصور، يمكنك تحديد إما مسار ملف الصورة أو دفق ملف الصورة. لتحديد رقم الصفحة التي تحتاج إلى إضافة الصورة أو النص فيها، توفر كلتا الطريقتين وسيطًا لرقم الصفحة. لذا، يمكنك إضافة الصور والنصوص ليس فقط في الموقع المحدد ولكن أيضًا في صفحة محددة.

تعتبر الصور جزءًا مهمًا من محتويات مستند PDF. إن معالجة الصور في ملف PDF موجود هي متطلب شائع للأشخاص الذين يعملون مع ملفات PDF. في هذه المقالة، سنستكشف كيفية معالجة الصور في ملف PDF موجود، بمساعدة [مساحة أسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) من [Aspose.PDF for .NET](/pdf/ar/net/). تم تجميع جميع العمليات المتعلقة بالصور من [مساحة أسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في هذه المقالة.

## تفاصيل التنفيذ

تتيح لك [مساحة أسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) إضافة صور جديدة في ملف PDF موجود. يمكنك أيضًا استبدال صورة موجودة أو إزالتها. يمكن أيضًا تحويل ملف PDF إلى صور. يمكنك إما تحويل كل صفحة فردية إلى صورة واحدة أو تحويل ملف PDF كامل إلى صورة واحدة. يسمح لك بتنسيقات مثل JPEG و BMP و PNG و TIFF وغيرها. يمكنك أيضًا استخراج الصور من ملف PDF. يمكنك استخدام أربع فئات من [مساحة أسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) لتنفيذ هذه العمليات وهي [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend)، [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)، [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) و [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## عمليات الصورة

في هذا القسم، سنلقي نظرة مفصلة على هذه العمليات المتعلقة بالصور. سنرى أيضًا مقتطفات من التعليمات البرمجية لإظهار استخدام الفئات والطرق ذات الصلة. أولاً، دعونا نلقي نظرة على إضافة صورة في ملف PDF موجود. يمكننا استخدام طريقة [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) من فئة [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) لإضافة صورة جديدة. باستخدام هذه الطريقة، يمكنك تحديد رقم الصفحة التي تريد إضافة الصورة عليها، ولكن أيضًا يمكن تحديد موقع الصورة.

## إضافة صورة في ملف PDF موجود (Facades)

يمكنك استخدام طريقة [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) من فئة [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend). تتطلب طريقة [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) الصورة التي سيتم إضافتها، ورقم الصفحة التي تحتاج إلى إضافة الصورة فيها ومعلومات الإحداثيات. بعد ذلك، احفظ ملف PDF المحدث باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

في المثال التالي، نضيف صورة إلى الصفحة باستخدام imageStream:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images(); 

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                // Add image to first page
                mender.AddImage(imageStream, 1, 10, 650, 110, 750);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![إضافة صورة](/pdf/ar/net/images/add_image1.png)

بمساعدة [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1)، يمكننا وضع صورة فوق أخرى:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters for the image
                var compositingParameters = new Aspose.Pdf.CompositingParameters(Aspose.Pdf.BlendMode.Multiply);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![إضافة صورة](/pdf/ar/net/images/add_image2.png)

هناك عدة طرق لتخزين صورة في ملف PDF. سنوضح واحدة منها في المثال التالي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Exclusion and ImageFilterType.Flate
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Exclusion,
                    Aspose.Pdf.ImageFilterType.Flate);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Multiply, ImageFilterType.Flate and false
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Multiply,
                    Aspose.Pdf.ImageFilterType.Flate,
                    false);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_outp.pdf");
            }
        }
    }
}
```

## إضافة نص في ملف PDF موجود (facades)

يمكننا إضافة نص بعدة طرق. لنأخذ الطريقة الأولى. نأخذ [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) ونضيفه إلى الصفحة. بعد ذلك، نشير إلى إحداثيات الزاوية السفلية اليسرى، ثم نضيف نصنا إلى الصفحة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

        // Add text to the first page at position (10, 750)
        mender.AddText(message, 1, 10, 750);

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

تحقق كيف يبدو:

![إضافة نص](/pdf/ar/net/images/add_text.png)

الطريقة الثانية لإضافة [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). بالإضافة إلى ذلك، نشير إلى مستطيل يجب أن يتناسب فيه نصنا.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose! Welcome to Aspose!");

        // Add text to the first page at the specified position with wrapping
        mender.AddText(message, 1, 10, 700, 55, 810);

        // Set word wrapping mode to wrap by words
        mender.WrapMode = Aspose.Pdf.Facades.WordWrapMode.ByWords;

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

المثال الثالث يوفر القدرة على إضافة نص إلى صفحات محددة. في مثالنا، دعونا نضيف عنوانًا على الصفحتين 1 و 3 من المستند.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();

        // Create PdfFileMend object
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Bind PDF document
            mender.BindPdf(document);

            // Create formatted text
            var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

            // Specify the pages where text should be added
            int[] pageNums = new int[] { 1, 3 };

            // Add text to the specified pages at the specified coordinates
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // Save PDF document
            mender.Save(dataDir + "AddText_out.pdf");
        }
    }
}
```