---
title: العمل مع نماذج XFA
linktitle: نماذج XFA
type: docs
weight: 20
url: ar/net/xfa-forms/
description: تتيح لك واجهة برمجة تطبيقات Aspose.PDF لـ .NET العمل مع حقول XFA و XFA Acroform في مستند PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع نماذج XFA",
    "alternativeHeadline": "ملء وتحويل والحصول على نماذج XFA في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, ملء نموذج xfa, الحصول على نموذج xfa, تحويل نموذج xfa",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2022-02-04",
    "description": "تتيح لك واجهة برمجة تطبيقات Aspose.PDF لـ .NET العمل مع حقول XFA و XFA Acroform في مستند PDF."
}
</script>
{{% alert color="primary" %}}

النماذج الديناميكية تعتمد على تخصيص XML المعروف بـ XFA، أو "هندسة النماذج XML". يمكنها أيضًا تحويل نموذج XFA الديناميكي إلى Acroform القياسي. المعلومات حول النموذج (بقدر ما يتعلق الأمر بـ PDF) غامضة جدًا - فهي تحدد أن هناك حقولًا موجودة، مع خصائص، وأحداث JavaScript، لكنها لا تحدد أي تصيير. يتم رسم كائنات نموذج XFA في وقت تحميل الوثيقة.

{{% /alert %}}

توفر فئة النموذج القدرة على التعامل مع AcroForm الثابت ويمكنك الحصول على نموذج حقل معين باستخدام طريقة GetFieldFacade(..) لفئة النموذج. ومع ذلك، لا يمكن الوصول إلى حقول XFA عبر طريقة Form.GetFieldFacade(..). بدلاً من ذلك، استخدم [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) للحصول على/تعيين قيم الحقل ومعالجة قالب حقل XFA (تعيين خصائص الحقل).

يعمل أيضًا الجزء التالي من الكود مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## ملء حقول XFA

يوضح لك جزء الكود التالي كيفية ملء الحقول في نموذج XFA.
يوضح الجزء التالي من الشفرة كيفية ملء الحقول في نموذج XFA.

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// تحميل نموذج XFA
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// الحصول على أسماء حقول نموذج XFA
string[] names = doc.Form.XFA.FieldNames;

// تعيين قيم الحقول
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// حفظ الوثيقة المحدثة
doc.Save(dataDir);
```

## تحويل XFA إلى Acroform

{{% alert color="primary" %}}

جرب عبر الإنترنت
يمكنك التحقق من جودة تحويل Aspose.PDF ومشاهدة النتائج عبر الإنترنت على هذا الرابط: [products.aspose.app/pdf/xfa/](https://products.aspose.app/pdf/xfa/)

{{% /alert %}}

النماذج الديناميكية تعتمد على مواصفات XML المعروفة باسم XFA، "الهندسة المعمارية للنماذج XML".
النماذج الديناميكية مبنية على مواصفات XML تعرف بـ XFA، أو "هندسة نماذج XML".

حاليًا، يدعم PDF طريقتين مختلفتين لدمج البيانات ونماذج PDF:

- AcroForms (المعروفة أيضًا باسم نماذج Acrobat)، تم تقديمها وتضمينها في مواصفات تنسيق PDF 1.2.
- نماذج هندسة نماذج XML من Adobe (XFA)، تم تقديمها في مواصفات تنسيق PDF 1.5 كميزة اختيارية (مواصفات XFA غير مدرجة في مواصفات PDF، فهي مشار إليها فقط.)

لا يمكننا استخراج أو التلاعب بصفحات نماذج XFA، لأن محتوى النموذج يتم توليده في وقت التشغيل (أثناء عرض نموذج XFA) داخل التطبيق الذي يحاول عرض أو تقديم نموذج XFA. يحتوي Aspose.PDF على ميزة تتيح للمطورين تحويل نماذج XFA إلى AcroForms قياسية.

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// تحميل نموذج XFA الديناميكي
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// تعيين نوع حقول النموذج كـ AcroForm قياسي
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// حفظ PDF الناتج
document.Save(dataDir);
```
## الحصول على خصائص حقل XFA

للوصول إلى خصائص الحقل، استخدم أولاً Document.Form.XFA.Teamplate للوصول إلى قالب الحقل. يوضح مقتطف الكود التالي خطوات الحصول على إحداثيات X و Y لحقل نموذج XFA.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// تحميل نموذج XFA
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// تعيين قيم الحقول
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";

// الحصول على موضع الحقل
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// الحصول على موضع الحقل
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// حفظ الوثيقة المحدثة
doc.Save(dataDir);
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


