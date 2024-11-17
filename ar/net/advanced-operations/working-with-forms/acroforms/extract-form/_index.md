---
title: استخراج AcroForm - استخراج بيانات النموذج من PDF في C#
linktitle: استخراج AcroForm
type: docs
weight: 30
url: /ar/net/extract-form/
description: استخرج النموذج من مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ .NET. احصل على قيمة من حقل فردي لملف PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "استخراج AcroForm",
    "alternativeHeadline": "كيفية استخراج AcroForm من PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, استخراج acroform",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2022-02-04",
    "description": "استخرج النموذج من مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ .NET. احصل على قيمة من حقل فردي لملف PDF."
}
</script>
الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## استخراج البيانات من النموذج

### الحصول على القيم من جميع حقول مستند PDF

للحصول على القيم من جميع الحقول في مستند PDF، تحتاج إلى التنقل خلال جميع حقول النموذج ثم الحصول على القيمة باستخدام خاصية القيمة. احصل على كل حقل من مجموعة النموذج، في نوع الحقل الأساسي المسمى Field واستخدم خاصية القيمة.

الشفرات التالية بلغة C# تظهر كيفية الحصول على قيم جميع الحقول من مستند PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// الحصول على القيم من جميع الحقول
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("اسم الحقل : {0} ", formField.PartialName);
    Console.WriteLine("القيمة : {0} ", formField.Value);
}
```
### الحصول على قيمة من حقل فردي في مستند PDF

خاصية القيمة لحقل النموذج تتيح لك الحصول على قيمة حقل معين. للحصول على القيمة، احصل على حقل النموذج من مجموعة النموذج في كائن المستند. هذا مثال بلغة C# يختار [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) ويسترجع قيمته باستخدام خاصية القيمة.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// الحصول على حقل
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// الحصول على قيمة الحقل
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

للحصول على URL زر الإرسال، استخدم الأسطر التالية من الكود.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated as SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### الحصول على حقول النموذج من منطقة محددة في ملف PDF

أحيانًا، قد تعرف أين في الوثيقة يوجد حقل النموذج، ولكن لا تملك اسمه. على سبيل المثال، إذا كان كل ما لديك هو مخطط لنموذج مطبوع. مع Aspose.PDF لـ .NET، هذه ليست مشكلة. يمكنك معرفة الحقول الموجودة في منطقة معينة من ملف PDF. للحصول على حقول النموذج من منطقة محددة في ملف PDF:

1. افتح ملف PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. احصل على النموذج من مجموعة Forms في المستند.
1. حدد المنطقة المستطيلة وأرسلها إلى طريقة GetFieldsInRect لكائن Form. يتم إرجاع مجموعة Fields.
1. استخدم هذا للتلاعب بالحقول.

يوضح الجزء التالي من الكود بلغة C# كيفية الحصول على حقول النموذج في منطقة مستطيلة محددة من ملف PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// فتح ملف pdf
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// إنشاء كائن المستطيل للحصول على الحقول في تلك المنطقة
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// الحصول على نموذج PDF
Aspose.Pdf.Forms.Form form = doc.Form;

// الحصول على حقول في المنطقة المستطيلة
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// عرض أسماء الحقول وقيمها
foreach (Field field in fields)
{
    // عرض خصائص وضع الصورة لجميع الوضعيات
    Console.Out.WriteLine("اسم الحقل: " + field.FullName + "-" + "قيمة الحقل: " + field.Value);
}
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
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
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
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
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

