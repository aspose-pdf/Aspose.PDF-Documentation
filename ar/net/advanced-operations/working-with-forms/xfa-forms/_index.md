---
title: العمل مع نماذج XFA
linktitle: نماذج XFA
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/xfa-forms/
description: تتيح لك واجهة برمجة التطبيقات Aspose.PDF for .NET العمل مع حقول XFA و XFA Acroform في مستند PDF. Aspose.Pdf.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with XFA Forms",
    "alternativeHeadline": "Enhance PDF handling with XFA form support",
    "abstract": "تقدم Aspose.PDF for .NET الآن قدرات متقدمة للعمل مع نماذج XFA، مما يسمح للمطورين بملء وتحويل وإدارة حقول XFA Acroform داخل مستندات PDF. تسهل هذه الميزة التلاعب بالنماذج الديناميكية، مما يتيح الوصول السلس إلى قيم الحقول وخصائصها مع توفير تحويل فعال من XFA إلى AcroForms القياسية. عزز سير عمل معالجة PDF الخاص بك مع هذا الحل القوي للتعامل مع هياكل النماذج المعقدة",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "XFA Forms, Aspose.PDF for .NET, fill XFA form, convert XFA to Acroform, get XFA field properties, dynamic forms, XML Forms Architecture, manipulate XFA fields, AcroForm fields, PDF document generation",
    "wordcount": "684",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2024-11-25",
    "description": "تتيح لك واجهة برمجة التطبيقات Aspose.PDF for .NET العمل مع حقول XFA و XFA Acroform في مستند PDF. Aspose.Pdf.Facades."
}
</script>

{{% alert color="primary" %}}

تستند النماذج الديناميكية إلى مواصفة XML تعرف باسم XFA، "بنية النماذج XML". يمكنها أيضًا تحويل نموذج XFA الديناميكي إلى Acroform القياسي. المعلومات حول النموذج (بقدر ما يتعلق الأمر بـ PDF) غامضة جدًا - تحدد أن الحقول موجودة، مع خصائص، وأحداث JavaScript، ولكن لا تحدد أي عرض. يتم رسم كائنات نموذج XFA عند تحميل المستند.

{{% /alert %}}

تقدم فئة النموذج القدرة على التعامل مع AcroForm الثابت ويمكنك الحصول على مثيل حقل معين باستخدام طريقة Form.GetFieldFacade(..). ومع ذلك، لا يمكن الوصول إلى حقول XFA عبر طريقة Form.GetFieldFacade(..). بدلاً من ذلك، استخدم [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) للحصول على/تعيين قيم الحقول والتلاعب بقالب حقل XFA (تعيين خصائص الحقل).

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## ملء حقول XFA

تظهر مقتطفات الكود التالية كيفية ملء الحقول في نموذج XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillXFAFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FillXFAFields.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
}
```

## تحويل XFA إلى Acroform

{{% alert color="primary" %}}

جرب عبر الإنترنت
يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت في هذا الرابط: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

تستند النماذج الديناميكية إلى مواصفة XML تعرف باسم XFA، "بنية النماذج XML". المعلومات حول النموذج (بقدر ما يتعلق الأمر بـ PDF) غامضة جدًا - تحدد أن الحقول موجودة، مع خصائص، وأحداث JavaScript، ولكن لا تحدد أي عرض.

حاليًا، يدعم PDF طريقتين مختلفتين لدمج البيانات ونماذج PDF:

- AcroForms (المعروفة أيضًا باسم نماذج Acrobat)، تم تقديمها وتضمينها في مواصفة تنسيق PDF 1.2.
- نماذج بنية النماذج XML من Adobe (XFA)، تم تقديمها في مواصفة تنسيق PDF 1.5 كميزة اختيارية (لم يتم تضمين مواصفة XFA في مواصفة PDF، بل تم الإشارة إليها فقط).

لا يمكننا استخراج أو التلاعب بصفحات نماذج XFA، لأن محتوى النموذج يتم إنشاؤه في وقت التشغيل (أثناء عرض نموذج XFA) داخل التطبيق الذي يحاول عرض أو رسم نموذج XFA. تحتوي Aspose.PDF على ميزة تسمح للمطورين بتحويل نماذج XFA إلى AcroForms القياسية.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDynamicXFAToAcroForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load dynamic XFA form
    using (var document = new Aspose.Pdf.Document(dataDir + "DynamicXFAToAcroForm.pdf"))
    {
        // Set the form fields type as standard AcroForm
        document.Form.Type = Aspose.Pdf.Forms.FormType.Standard;

        // Save PDF document
        document.Save(dataDir + "StandardAcroForm_out.pdf");
    }
}
```

## الحصول على خصائص حقل XFA

للوصول إلى خصائص الحقل، استخدم أولاً Document.Form.XFA.Template للوصول إلى قالب الحقل. تظهر مقتطفات الكود التالية خطوات الحصول على إحداثيات X و Y لحقل نموذج XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXFAProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXFAProperties.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Get field position
        if (names.Length > 0)
        {
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
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