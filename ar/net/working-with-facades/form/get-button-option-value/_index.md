---
title: الحصول على قيمة خيار الزر
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/get-button-option-value/
description: يشرح هذا القسم كيفية الحصول على قيمة خيار الزر باستخدام واجهات Aspose.PDF من خلال فئة النموذج.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Button Option Value",
    "alternativeHeadline": "Retrieve Button Option Values from PDF Efficiently",
    "abstract": "اكتشف كيفية استرجاع قيم خيارات الزر بكفاءة من ملفات PDF الموجودة باستخدام واجهات Aspose.PDF. باستخدام فئة النموذج GetButtonOptionValues و GetButtonOptionCurrentValue، يمكنك بسهولة الحصول على جميع الخيارات المتاحة لأزرار الاختيار، بالإضافة إلى القيمة المحددة حاليًا، مما يعزز قدرات إدارة نماذج PDF الخاصة بك.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "275",
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
    "url": "/net/get-button-option-value/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-button-option-value/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## الحصول على قيم خيارات الزر من ملف PDF موجود

توفر أزرار الاختيار وسيلة لعرض خيارات مختلفة. تتيح لك فئة [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form) الحصول على جميع قيم خيارات الزر لزر اختيار معين. يمكنك الحصول على هذه القيم باستخدام طريقة [GetButtonOptionValues](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues). تتطلب هذه الطريقة اسم زر الاختيار كمعامل إدخال وتعيد Hashtable. يمكنك التكرار عبر هذه Hashtable للحصول على قيم الخيارات. يوضح لك مقتطف الشيفرة التالي كيفية الحصول على قيم خيارات الزر من ملف PDF موجود.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetButtonOptions()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        var optionValues = pdfForm.GetButtonOptionValues("Gender");

        IDictionaryEnumerator optionValueEnumerator = optionValues.GetEnumerator();

        while (optionValueEnumerator.MoveNext())
        {
            Console.WriteLine("Key : {0} , Value : {1} ", optionValueEnumerator.Key, optionValueEnumerator.Value);
        }
    }
}
```

## الحصول على قيمة خيار الزر الحالي من ملف PDF موجود

توفر أزرار الاختيار وسيلة لتعيين قيم الخيارات، ومع ذلك يمكن اختيار واحد منها فقط في كل مرة. إذا كنت ترغب في الحصول على قيمة الخيار المحدد حاليًا، يمكنك استخدام [GetButtonOptionCurrentValue** method. توفر فئة [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form) هذه الطريقة. تتطلب طريقة [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) اسم زر الاختيار كمعامل إدخال وتعيد القيمة كسلسلة. يوضح لك مقتطف الشيفرة التالي كيفية الحصول على قيمة خيار الزر الحالي من ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetCurremtButtonOptionValue()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        string optionValue = pdfForm.GetButtonOptionCurrentValue("Gender");

        Console.WriteLine("Current Value : {0} ", optionValue);
    }
}
```