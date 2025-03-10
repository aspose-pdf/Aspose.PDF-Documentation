---
title: تعديل AcroForm
linktitle: تعديل AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/modifing-form/
description: تعديل النموذج في ملف PDF الخاص بك باستخدام مكتبة Aspose.PDF for .NET. يمكنك إضافة أو إزالة حقول في النموذج الحالي، والحصول على وتعيين حد الحقل وما إلى ذلك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modifing AcroForm",
    "alternativeHeadline": "Modify and Manage AcroForm Fields in PDF",
    "abstract": "تتيح ميزة تعديل AcroForm الجديدة في مكتبة Aspose.PDF for .NET للمستخدمين إضافة أو إزالة حقول من نماذج PDF الحالية بسلاسة. تتضمن هذه الوظيفة أيضًا تعيين حدود الحقول وتخصيص مظهر الخطوط لتجربة مستخدم مصقولة، مما يعزز إدارة وتفاعل نماذج PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Modifing AcroForm, Aspose.PDF for .NET, PDF form fields, SetFieldLimit, custom font, Add/remove fields, Document Form collection, DefaultAppearance, manage form fields, PDF manipulation",
    "wordcount": "601",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2024-11-25",
    "description": "تعديل النموذج في ملف PDF الخاص بك باستخدام مكتبة Aspose.PDF for .NET. يمكنك إضافة أو إزالة حقول في النموذج الحالي، والحصول على وتعيين حد الحقل وما إلى ذلك."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/) .

## الحصول على أو تعيين حد الحقل

تتيح لك طريقة FormEditor class SetFieldLimit(field, limit) تعيين حد الحقل، وهو الحد الأقصى لعدد الأحرف التي يمكن إدخالها في حقل.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFieldLimit()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create FormEditor instance
    using (var form = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Set field limit for "textbox1"
        form.SetFieldLimit("textbox1", 15);

        // Save PDF document
        form.Save(dataDir + "SetFieldLimit_out.pdf");
    }
}
```

وبالمثل، تحتوي Aspose.PDF على طريقة للحصول على حد الحقل باستخدام نهج DOM. يوضح مقتطف الشيفرة التالية الخطوات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldLimit.pdf"))
    {
        // Get the field and its maximum limit
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            Console.WriteLine("Limit: " + textBoxField.MaxLen);
        }
    }
}
```

يمكنك أيضًا الحصول على نفس القيمة باستخدام مساحة أسماء *Aspose.Pdf.Facades* باستخدام مقتطف الشيفرة التالي.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingFacades()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create Form instance
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "FieldLimit.pdf");

        // Get the field limit for "textbox1"
        Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
    }
}
```

## تعيين خط مخصص لحقل النموذج

يمكن تكوين حقول النموذج في ملفات PDF من Adobe لاستخدام خطوط افتراضية محددة. في الإصدارات المبكرة من Aspose.PDF، كانت تدعم فقط 14 خطًا افتراضيًا. سمحت الإصدارات اللاحقة للمطورين بتطبيق أي خط. لتعيين وتحديث الخط الافتراضي المستخدم لحقول النموذج، استخدم DefaultAppearance(Font font, double size, Color color) class. يمكن العثور على هذه الفئة تحت مساحة أسماء Aspose.Pdf.InteractiveFeatures. لاستخدام هذا الكائن، استخدم خاصية DefaultAppearance لفئة Field.

يوضح مقتطف الشيفرة التالي كيفية تعيين الخط الافتراضي لحقول نموذج PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFormFieldFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FormFieldFont14.pdf"))
    {
        // Get particular form field from document
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.Field field)
        {
            // Create font object
            var font = Aspose.Pdf.Text.FontRepository.FindFont("ComicSansMS");

            // Set the font information for form field
            field.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance(font, 10, System.Drawing.Color.Black);
        }

        // Save PDF document
        document.Save(dataDir + "FormFieldFont14_out.pdf");
    }
}
```

## إضافة/إزالة حقول في النموذج الحالي

تحتوي جميع حقول النموذج على مجموعة Form لكائن Document. توفر هذه المجموعة طرقًا مختلفة تدير حقول النموذج، بما في ذلك طريقة Delete. إذا كنت ترغب في حذف حقل معين، مرر اسم الحقل كمعامل إلى طريقة Delete ثم احفظ مستند PDF المحدث. يوضح مقتطف الشيفرة التالي كيفية حذف حقل معين من مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteFormField.pdf"))
    {
        // Delete a particular field by name
        document.Form.Delete("textbox1");

        // Save PDF document
        document.Save(dataDir + "DeleteFormField_out.pdf");
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