---
title: تحويل PDF إلى PostScript
linktitle: تحويل PDF إلى PostScript
type: docs
weight: 30
url: /ar/net/pdf-to-postscript-conversion/
keywords: "pdf to postscript c#"
description: لدينا حل لتحويل PDF إلى PostScript. استخدم لهذه المهمة الطباعة وفئة PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تحويل PDF إلى PostScript",
    "alternativeHeadline": "تحويل PDF إلى PostScript",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, pdf to postscript",
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
    "url": "/net/pdf-to-postscript-conversion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-to-postscript-conversion/"
    },
    "dateModified": "2022-02-04",
    "description": "لدينا حل لتحويل PDF إلى PostScript. استخدم لهذه المهمة الطباعة وفئة PdfViewer."
}
</script>

الكود التالي يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## **تحويل PDF إلى Postscript في C#**

توفر فئة PdfViewer القدرة على طباعة مستندات PDF وبمساعدتها، يمكننا أيضًا تحويل ملفات PDF إلى تنسيق PostScript. لتحويل ملف PDF إلى PostScript، قم أولاً بتثبيت أي طابعة PS وببساطة اطبع الملف باستخدام PdfViewer. يمكنك اتباع التعليمات التي حددتها جامعة هاواي حول كيفية تثبيت طابعة PS. يوضح الكود التالي كيفية الطباعة وتحويل PDF إلى تنسيق PostScript.

```csharp
public static void PrintToPostscriptFile()
{
    // مسار إلى مجلد المستندات.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // تعيين إعدادات الطابعة وإعدادات الصفحة
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // تعيين طابعة PS، يمكن العثور على هذا البرنامج في قائمة برامج تشغيل الطابعات المثبتة مسبقًا في Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // تعيين اسم ملف الإخراج وسمة PrintToFile
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // تعطيل حوار صفحة الطباعة
    viewer.PrintPageDialog = false;
    // إرسال كائن إعدادات الطابعة إلى الطريقة
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```
## التحقق من حالة مهمة الطباعة

يمكن طباعة ملف PDF إلى طابعة فعلية بالإضافة إلى Microsoft XPS Document Writer، دون إظهار حوار طباعة، باستخدام فئة PdfViewer. عند طباعة ملفات PDF كبيرة، قد يستغرق الأمر وقتا طويلا لذا قد لا يكون المستخدم متأكدا مما إذا كانت عملية الطباعة قد اكتملت أو واجهت مشكلة. لتحديد حالة مهمة الطباعة، استخدم خاصية PrintStatus. يوضح الجزء التالي من الكود كيفية طباعة ملف PDF إلى ملف XPS والحصول على حالة الطباعة.

```csharp
public static void CheckingPrintJobStatus()
{
    // للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
    // المسار إلى دليل المستندات.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // إنشاء كائن PdfViewer
    PdfViewer viewer = new PdfViewer();

    // ربط ملف PDF المصدر
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // إخفاء حوار الطباعة
    viewer.PrintPageDialog = false;

    // إنشاء كائن إعدادات الطابعة
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // تحديد اسم الطابعة
    ps.PrinterName = "Microsoft XPS Document Writer";

    // اسم النتيجة المطبوعة
    ps.PrintFileName = "ResultantPrintout.xps";

    // طباعة النتيجة إلى ملف
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // تحديد حجم الصفحة للمطبوعات
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // طباعة المستند بالإعدادات المحددة أعلاه
    viewer.PrintDocumentWithSettings(pgs, ps);

    // التحقق من حالة الطباعة
    if (viewer.PrintStatus != null)
    {
        // تم إلقاء استثناء
        if (viewer.PrintStatus is Exception ex)
        {
            // الحصول على رسالة الاستثناء
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // لم يتم العثور على أخطاء. تم إكمال مهمة الطباعة بنجاح
        Console.WriteLine("تم إكمال الطباعة دون أي مشكلة..");
    }
}
```
## اسم مالك مهمة الطباعة

مؤخرًا، تلقينا متطلبًا للحصول على/تعيين اسم مالك مهمة الطباعة (المستخدم الفعلي الذي ضغط على زر الطباعة في صفحة الويب). هذه المعلومات مطلوبة عند طباعة ملف PDF. لتحقيق هذا المتطلب، يمكنك استخدام الخاصية باسم PrinterJobName:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// ربط ملف PDF المصدر
viewer.BindPdf(dataDir + "input.pdf");
// تحديد اسم مهمة الطباعة
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static string GetCurrentUserCredentials()
{
    // التنفيذ يعتمد على نوع التطبيق الجاري تشغيله (ASP.NET، نماذج Windows، إلخ.)
    string userCredentials = string.Empty;
    return userCredentials;
}
```
## استخدام التقمص

طريقة أخرى للحصول على اسم صاحب وظيفة الطباعة هي استخدام التقمص (تشغيل روتينات الطباعة في سياق مستخدم آخر) أو يمكن للمستخدم تغيير اسم المالك مباشرة باستخدام روتين SetJob.

يرجى ملاحظة أنه لا توجد إمكانية لتعيين قيمة المالك باستخدام واجهة برمجة تطبيقات الطباعة Aspose.PDF بسبب اعتبارات الأمان. يمكن استخدام خاصية PrinterJobName لتعيين قيمة عمود اسم المستند في تطبيق طباعة السبولر. يوضح الشيفرة المشتركة أعلاه كيف يمكن للمستخدم دمج اسم المستخدم في عمود اسم المستند (على سبيل المثال باستخدام بناء الجملة UserName\documentName). لكن يمكن تنفيذ إعداد أعمدة المالك بالطرق التالية مباشرة من قبل المستخدم:

1) التقمص. حيث يحتوي قيمة عمود المالك على قيمة المستخدم الذي يشغل كود الطباعة، وهناك طريقة لاستدعاء واجهة برمجة تطبيقات طباعة Aspose.PDF داخل سياق مستخدم آخر. على سبيل المثال، يرجى الاطلاع على الحل الموصوف هنا. باستخدام هذه الفئة، يمكن للمستخدم تحقيق الهدف:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf( dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// عدم إنتاج حوار رقم الصفحة عند الطباعة
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName هي قيمة عمود المالك في تطبيق السبولر
    viewer.Close();
}
```
2) استخدام واجهة برمجة تطبيقات Spooler وروتين SetJob

الشفرة التالية توضح كيفية طباعة بعض صفحات ملف PDF بوضع Simplex وبعض الصفحات بوضع Duplex.

```csharp
struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public System.Drawing.Printing.Duplex Mode { get; set; }
}
```

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

int printingJobIndex = 0;
string inPdf = dataDir + "input.pdf";
string output = dataDir;
IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

PrintingJobSettings printingJob1 = new PrintingJobSettings();
printingJob1.FromPage = 1;
printingJob1.ToPage = 3;
printingJob1.OutputFile = output + "35925_1_3.xps";
printingJob1.Mode = Duplex.Default;

printingJobs.Add(printingJob1);

PrintingJobSettings printingJob2 = new PrintingJobSettings();
printingJob2.FromPage = 4;
printingJob2.ToPage = 6;
printingJob2.OutputFile = output + "35925_4_6.xps";
printingJob2.Mode = Duplex.Simplex;

printingJobs.Add(printingJob2);

PrintingJobSettings printingJob3 = new PrintingJobSettings();
printingJob3.FromPage = 7;
printingJob3.ToPage = 7;
printingJob3.OutputFile = output + "35925_7.xps";
printingJob3.Mode = Duplex.Default;

printingJobs.Add(printingJob3);

PdfViewer viewer = new PdfViewer();

viewer.BindPdf(inPdf);
viewer.AutoResize = true;
viewer.AutoRotate = true;
viewer.PrintPageDialog = false;

PrinterSettings ps = new PrinterSettings();
PageSettings pgs = new PageSettings();

ps.PrinterName = "Microsoft XPS Document Writer";
ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
ps.PrintToFile = true;
ps.FromPage = printingJobs[printingJobIndex].FromPage;
ps.ToPage = printingJobs[printingJobIndex].ToPage;
ps.Duplex = printingJobs[printingJobIndex].Mode;
ps.PrintRange = PrintRange.SomePages;

pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);
viewer.EndPrint += (sender, args) =>
{
    if (++printingJobIndex < printingJobs.Count)
    {
        ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
        ps.FromPage = printingJobs[printingJobIndex].FromPage;
        ps.ToPage = printingJobs[printingJobIndex].ToPage;
        ps.Duplex = printingJobs[printingJobIndex].Mode;
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
};

viewer.PrintDocumentWithSettings(pgs, ps);
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
                "areaServed": "الولايات المتحدة الأمريكية",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "بريطانيا العظمى",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
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
    "operatingSystem": "ويندوز، ماك أو إس، لينكس",
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

