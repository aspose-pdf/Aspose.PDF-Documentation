---
title: تزيين حقل النموذج في PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/decorate-form-field/
description: استكشف كيفية تزيين حقول النموذج في مستند PDF، وإضافة تحسينات بصرية مثل الحدود، في .NET مع Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decorate Form Field in PDF",
    "alternativeHeadline": "Enhance PDF Forms with Custom Field Decorations",
    "abstract": "تقديم ميزة قوية تعزز إدارة نماذج PDF: القدرة على تزيين حقل نموذج فردي أو جميع حقول النموذج باستخدام فئة FormEditor. تتيح هذه الوظيفة للمستخدمين تخصيص سمات الحقل مثل نمط الخط، الحجم، لون الحدود، والمحاذاة، مما يسهل عملية إنشاء نماذج PDF جذابة بصريًا ومنظمة بشكل جيد. عزز سير العمل الخاص بك في PDF مع هذه الطريقة البديهية للتزيين لتقديم مستند أكثر تميزًا.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "609",
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
    "url": "/net/decorate-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decorate-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## تزيين حقل نموذج معين في ملف PDF موجود

تتيح لك طريقة [DecorateField](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/decoratefield) الموجودة في فئة [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor) تزيين حقل نموذج معين في ملف PDF. إذا كنت ترغب في تزيين حقل معين، فيجب عليك تمرير اسم الحقل إلى هذه الطريقة. ومع ذلك، قبل استدعاء هذه الطريقة، تحتاج إلى إنشاء كائنات من فئات [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor) و [FormFieldFacade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formfieldfacade). تحتاج أيضًا إلى تعيين كائن [FormFieldFacade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formfieldfacade) إلى خاصية [Facade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/facade/properties/index) لكائن [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). بعد ذلك، يمكنك تعيين أي سمات يوفرها كائن [FormFieldFacade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formfieldfacade). بمجرد تعيين السمات، يمكنك استدعاء طريقة [DecorateField](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/decoratefield) وأخيرًا حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/save/index) لفئة [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor). 
تظهر لك الشيفرة البرمجية التالية كيفية تزيين حقل نموذج معين.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define decoration properties for the field
        var cityDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set the font style to Courier
            Font = Aspose.Pdf.Facades.FontStyle.Courier,
            // Set the font size to 12
            FontSize = 12,
            // Set the border color to black
            BorderColor = System.Drawing.Color.Black,
            // Set the border width to 2
            BorderWidth = 2
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = cityDecoration;

        // Apply the decoration to the field named "City"
        editor.DecorateField("City");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-02.pdf");
    }
}
```

## تزيين جميع حقول نوع معين في ملف PDF موجود

تتيح لك طريقة [DecorateField](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) تزيين جميع حقول النموذج من نوع معين في ملف PDF دفعة واحدة. إذا كنت ترغب في تزيين جميع حقول نوع معين، فيجب عليك تمرير نوع الحقل إلى هذه الطريقة. ومع ذلك، قبل استدعاء هذه الطريقة، تحتاج إلى إنشاء كائنات من فئات [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor) و [FormFieldFacade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formfieldfacade). تحتاج أيضًا إلى تعيين كائن [FormFieldFacade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formfieldfacade) إلى خاصية [Facade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/facade/properties/index) لكائن [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). بعد ذلك، يمكنك تعيين أي سمات يوفرها كائن [FormFieldFacade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formfieldfacade). بمجرد تعيين السمات، يمكنك استدعاء طريقة [DecorateField](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) وأخيرًا حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/save/index) لفئة [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor). تظهر لك الشيفرة البرمجية التالية كيفية تزيين جميع حقول نوع معين.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define alignment properties for text fields
        var textFieldDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set text alignment to center
            Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignCenter
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = textFieldDecoration;

        // Apply the alignment decoration to all text fields in the PDF
        editor.DecorateField(Aspose.Pdf.Facades.FieldType.Text);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-align-text.pdf");
    }
}
```