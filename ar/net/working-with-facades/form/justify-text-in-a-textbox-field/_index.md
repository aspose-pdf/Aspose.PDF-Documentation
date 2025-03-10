---
title: تبرير النص في حقل نصي
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/justify-text-in-a-textbox-field/
description: يوضح لك هذا المقال كيفية تبرير النص في حقل نصي باستخدام فئة النموذج.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Justify Text in a Textbox Field",
    "alternativeHeadline": "Justify Text in PDF Textbox Fields Effortlessly",
    "abstract": "تتيح هذه الميزة للمستخدمين تبرير النص داخل حقل نصي في مستندات PDF باستخدام فئة FormEditor من مساحة أسماء Aspose.Pdf.Facades. من خلال استخدام خيار AlignJustified، يمكن للمستخدمين تحقيق محاذاة نص جذابة بصريًا مع الحفاظ على الوظائف، على الرغم من أن المحاذاة المبررة غير مدعومة أثناء الإدخال النشط. هذا يعزز عرض بيانات النموذج في ملفات PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "283",
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
    "url": "/net/justify-text-in-a-textbox-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/justify-text-in-a-textbox-field/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

في هذا المقال، سنوضح لك كيفية تبرير النص في حقل نصي في ملف PDF.

{{% /alert %}}

## تفاصيل التنفيذ

تقدم فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) في [مساحة أسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) القدرة على تزيين حقل نموذج PDF. الآن، إذا كانت متطلباتك هي تبرير النص في حقل نصي، يمكنك تحقيق ذلك بسهولة باستخدام قيمة [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) من تعداد [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) واستدعاء طريقة [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). في المثال أدناه، سنقوم أولاً بملء حقل نصي باستخدام طريقة [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) من فئة [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form). بعد ذلك، سنستخدم فئة FormEditor لتبرير النص في الحقل النصي. يوضح لك مقتطف الكود التالي كيفية تبرير النص في حقل نصي.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void JustifyTextInTextboxField()
{
    // The path to the documents directory 
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Open PDF document
    using (var source = File.Open(dataDir + "JustifyText.pdf", FileMode.Open))
    {
        using (var ms = new MemoryStream())
        {
            // Create Form Object
            var form = new Aspose.Pdf.Facades.Form();
            // Bind PDF document
            form.BindPdf(source);
            // Fill Text Field
            form.FillField("Text1", "Thank you for using Aspose");
            // Save PDF document in Memory Stream
            form.Save(ms);
            ms.Seek(0, SeekOrigin.Begin);

            using (var dest = new FileStream(dataDir + "JustifyText_out.pdf", FileMode.Create))
            {
                // Create formEditor Object
                using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
                {
                    // Open PDF from memory stream
                    formEditor.BindPdf(ms);
                    // Set Text Alignment as Justified
                    formEditor.Facade.Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignJustified;
                    // Decorate form field
                    formEditor.DecorateField();
                    // Save PDF document
                    formEditor.Save(dest);
                }
            }
        }
    }
}
```
يرجى ملاحظة أن المحاذاة المبررة غير مدعومة من قبل PDF، لذلك سيتم محاذاة النص إلى اليسار عند إدخال النص في الحقل النصي. ولكن عندما يكون الحقل غير نشط، يتم تبرير النص.