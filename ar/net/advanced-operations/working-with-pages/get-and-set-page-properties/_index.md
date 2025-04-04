---
title: الحصول على خصائص الصفحة وتعيينها
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /ar/net/get-and-set-page-properties/
description: تعلم كيفية الحصول على خصائص الصفحة وتعيينها لوثائق PDF باستخدام Aspose.PDF for .NET، مما يسمح بتنسيق مستندات مخصص.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Set Page Properties",
    "alternativeHeadline": "Manage PDF Page Properties with Ease",
    "abstract": "تتيح ميزة الحصول على خصائص الصفحة وتعيينها في Aspose.PDF for .NET للمطورين الوصول بسهولة إلى خصائص صفحات PDF والتلاعب بها. تتيح هذه الوظيفة للمستخدمين استرداد معلومات حيوية، مثل عدد الصفحات وخصائص معينة مثل أنواع الألوان وصناديق الوسائط وصناديق القص، كل ذلك في بضع أسطر من التعليمات البرمجية. عزز قدرات إدارة مستندات PDF الخاصة بك اليوم من خلال الاستفادة من هذه الميزة القوية للتلاعب الفعال في PDF في تطبيقات .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1117",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

Aspose.PDF for .NET يتيح لك قراءة وتعيين خصائص الصفحات في ملف PDF في تطبيقات .NET الخاصة بك. يوضح هذا القسم كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وتعيين خصائص الصفحة. الأمثلة المعطاة بلغة C# ولكن يمكنك استخدام أي لغة .NET مثل VB.NET لتحقيق نفس الشيء.

تعمل مقتطفات التعليمات البرمجية التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## الحصول على عدد الصفحات في ملف PDF

عند العمل مع المستندات، غالبًا ما تريد معرفة عدد الصفحات التي تحتوي عليها. مع Aspose.PDF، لا يستغرق ذلك أكثر من سطرين من التعليمات البرمجية.

للحصول على عدد الصفحات في ملف PDF:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document).
1. ثم استخدم خاصية Count لمجموعة [PageCollection](https://reference.aspose.com/pdf/ar/net/aspose.pdf/pagecollection) (من كائن Document) للحصول على العدد الإجمالي للصفحات في المستند.

تظهر مقتطفات التعليمات البرمجية التالية كيفية الحصول على عدد صفحات ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetNumberOfPagesInAPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetNumberofPages.pdf"))
    {
        // Get page count
        System.Console.WriteLine("Page Count : {0}", document.Pages.Count);
    }
}
```

### الحصول على عدد الصفحات دون حفظ المستند

أحيانًا نقوم بإنشاء ملفات PDF على الفور وأثناء إنشاء ملف PDF، قد نواجه الحاجة (إنشاء جدول المحتويات، إلخ) للحصول على عدد الصفحات في ملف PDF دون حفظ الملف على النظام أو التدفق. لذلك، من أجل تلبية هذه الحاجة، تم تقديم طريقة [ProcessParagraphs](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/processparagraphs) في فئة Document. يرجى إلقاء نظرة على مقتطف التعليمات البرمجية التالية التي توضح الخطوات للحصول على عدد الصفحات دون حفظ المستند.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPageCountWithoutSavingTheDocument()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create loop instance
        for (var i = 0; i < 300; i++)
        {
            // Add TextFragment to paragraphs collection of page object
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Pages count test"));
        }
        // Process the paragraphs in PDF file to get accurate page count
        document.ProcessParagraphs();
        // Print number of pages in document
        Console.WriteLine("Number of pages in document = " + document.Pages.Count);
    }
}
```

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF لها عدد من الخصائص، مثل العرض والارتفاع وصندوق النزيف وصندوق القص وصندوق القص النهائي. يتيح لك Aspose.PDF الوصول إلى هذه الخصائص.

### **فهم خصائص الصفحة: الفرق بين Artbox وBleedBox وCropBox وMediaBox وTrimBox وRect property**

- **صندوق الوسائط**: صندوق الوسائط هو أكبر صندوق صفحة. يتوافق مع حجم الصفحة (على سبيل المثال A4، A5، US Letter، إلخ) الذي تم اختياره عند طباعة المستند إلى PostScript أو PDF. بعبارة أخرى، يحدد صندوق الوسائط الحجم الفعلي للوسائط التي يتم عرض مستند PDF عليها أو طباعته.
- **صندوق النزيف**: إذا كان المستند يحتوي على نزيف، فسيكون لملف PDF أيضًا صندوق نزيف. النزيف هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما وراء حافة الصفحة. يُستخدم لضمان أنه عند طباعة المستند وقطعه إلى الحجم ("قصه")، سيصل الحبر إلى حافة الصفحة. حتى إذا تم قص الصفحة بشكل غير دقيق - قطعها قليلاً بعيدًا عن علامات القص - فلن تظهر أي حواف بيضاء على الصفحة.
- **صندوق القص**: يشير صندوق القص إلى الحجم النهائي للمستند بعد الطباعة والقص.
- **صندوق الفن**: صندوق الفن هو الصندوق المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يُستخدم هذا الصندوق عند استيراد مستندات PDF في تطبيقات أخرى.
- **صندوق القص**: صندوق القص هو حجم "الصفحة" الذي يتم عرض مستند PDF الخاص بك فيه في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق القص فقط في Adobe Acrobat.
  للحصول على أوصاف مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وخاصة 10.10.1 حدود الصفحة.
- **Page.Rect**: التقاطع (المستطيل المرئي عادةً) بين MediaBox وDropBox. توضح الصورة أدناه هذه الخصائص.

للحصول على مزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **الوصول إلى خصائص الصفحة**

توفر فئة [Page](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page) جميع الخصائص المتعلقة بصفحة PDF معينة. جميع صفحات ملفات PDF موجودة في مجموعة [PageCollection](https://reference.aspose.com/pdf/ar/net/aspose.pdf/pagecollection) لكائن [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document).

من هناك، من الممكن الوصول إلى كائنات Page الفردية باستخدام فهرسها، أو التكرار عبر المجموعة، باستخدام حلقة foreach، للحصول على جميع الصفحات. بمجرد الوصول إلى صفحة فردية، يمكننا الحصول على خصائصها. توضح مقتطفات التعليمات البرمجية التالية كيفية الحصول على خصائص الصفحة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessingPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetProperties.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Get page properties
        System.Console.WriteLine("ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.ArtBox.Height, pdfPage.ArtBox.Width, pdfPage.ArtBox.LLX,
            pdfPage.ArtBox.LLY, pdfPage.ArtBox.URX, pdfPage.ArtBox.URY);
        System.Console.WriteLine("BleedBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.BleedBox.Height, pdfPage.BleedBox.Width, pdfPage.BleedBox.LLX,
            pdfPage.BleedBox.LLY, pdfPage.BleedBox.URX, pdfPage.BleedBox.URY);
        System.Console.WriteLine("CropBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.CropBox.Height, pdfPage.CropBox.Width, pdfPage.CropBox.LLX,
            pdfPage.CropBox.LLY, pdfPage.CropBox.URX, pdfPage.CropBox.URY);
        System.Console.WriteLine("MediaBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.MediaBox.Height, pdfPage.MediaBox.Width, pdfPage.MediaBox.LLX,
            pdfPage.MediaBox.LLY, pdfPage.MediaBox.URX, pdfPage.MediaBox.URY);
        System.Console.WriteLine("TrimBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.TrimBox.Height, pdfPage.TrimBox.Width, pdfPage.TrimBox.LLX,
            pdfPage.TrimBox.LLY, pdfPage.TrimBox.URX, pdfPage.TrimBox.URY);
        System.Console.WriteLine("Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.Rect.Height, pdfPage.Rect.Width, pdfPage.Rect.LLX, pdfPage.Rect.LLY,
            pdfPage.Rect.URX, pdfPage.Rect.URY);
        System.Console.WriteLine("Page Number : {0}", pdfPage.Number);
        System.Console.WriteLine("Rotate : {0}", pdfPage.Rotate);
    }
}
```

## الحصول على صفحة معينة من ملف PDF

يتيح لك Aspose.PDF [تقسيم PDF إلى صفحات فردية](/pdf/ar/net/split-pdf-document/) وحفظها كملفات PDF. الحصول على صفحة محددة في ملف PDF وحفظها كملف PDF جديد هو عملية مشابهة جدًا: افتح المستند المصدر، والوصول إلى الصفحة، وإنشاء مستند جديد وإضافة الصفحة إلى هذا المستند.

تحتوي مجموعة [PageCollection](https://reference.aspose.com/pdf/ar/net/aspose.pdf/pagecollection) لكائن [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) على الصفحات في ملف PDF. للحصول على صفحة معينة من هذه المجموعة:

1. حدد فهرس الصفحة باستخدام خاصية Pages.
1. أنشئ كائن [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) جديد.
1. أضف كائن [Page](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page) إلى كائن [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) الجديد.
1. احفظ الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf.document/save/methods/4).

تظهر مقتطفات التعليمات البرمجية التالية كيفية الحصول على صفحة معينة من ملف PDF وحفظها كملف جديد.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAParticularPageOfThePdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get particular page
        var pdfPage = document.Pages[2];
        // Save the page as PDF file
        using (var newDocument = new Aspose.Pdf.Document())
        {
            newDocument.Pages.Add(pdfPage);
            // Save PDF document
            newDocument.Save(dataDir + "GetParticularPage_out.pdf");
        }
    }
}
```

## تحديد لون الصفحة

توفر فئة [Page](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page) الخصائص المتعلقة بصفحة معينة في مستند PDF، بما في ذلك نوع اللون - RGB، بالأبيض والأسود، تدرج الرمادي أو غير محدد - الذي تستخدمه الصفحة.

تحتوي جميع صفحات ملفات PDF على مجموعة [PageCollection](https://reference.aspose.com/pdf/ar/net/aspose.pdf/pagecollection). تحدد خاصية ColorType لون العناصر على الصفحة. للحصول على معلومات اللون أو تحديدها لصفحة PDF معينة، استخدم خاصية [ColorType](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page/properties/colortype) لكائن [Page](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page).

تظهر مقتطفات التعليمات البرمجية التالية كيفية التكرار عبر صفحة فردية من ملف PDF للحصول على معلومات اللون.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeterminePageColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through all the page of PDF file
        for (var pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Get the color type information for particular PDF page
            Aspose.Pdf.ColorType pageColorType = document.Pages[pageCount].ColorType;
            switch (pageColorType)
            {
                case Aspose.Pdf.ColorType.BlackAndWhite:
                    Console.WriteLine("Page # -" + pageCount + " is Black and white..");
                    break;
                case Aspose.Pdf.ColorType.Grayscale:
                    Console.WriteLine("Page # -" + pageCount + " is Gray Scale...");
                    break;
                case Aspose.Pdf.ColorType.Rgb:
                    Console.WriteLine("Page # -" + pageCount + " is RGB..", pageCount);
                    break;
                case Aspose.Pdf.ColorType.Undefined:
                    Console.WriteLine("Page # -" + pageCount + " Color is undefined..");
                    break;
            }
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