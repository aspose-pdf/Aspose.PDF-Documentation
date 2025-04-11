---
title: إضافة حقول نموذج PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/add-form-fields/
description: يشرح هذا الموضوع كيفية العمل مع حقول النموذج باستخدام واجهة Aspose.PDF من خلال فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Form Fields",
    "alternativeHeadline": "Effortlessly Enhance PDFs with Custom Form Fields",
    "abstract": "قم بتحسين مستندات PDF الخاصة بك مع تفاعلية ديناميكية من خلال إضافة حقول نموذج باستخدام فئة FormEditor في Aspose.PDF for .NET. تتيح لك هذه الميزة دمج حقول نصية، وأزرار إرسال مع عناوين URL، ووظائف JavaScript لدفع الأزرار، مما يسهل إدخال المستخدم وتقديم البيانات في مستندات PDF الخاصة بك.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/add-form-fields/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-form-fields/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إضافة حقل نموذج في ملف PDF موجود

لإضافة حقل نموذج في ملف PDF موجود، تحتاج إلى استخدام [AddField](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/addfield/index) من فئة [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor). تتطلب هذه الطريقة منك تحديد نوع الحقل الذي تريد إضافته مع الاسم وموقع الحقل. تحتاج إلى إنشاء كائن من فئة [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor)، واستخدام [AddField](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/addfield/index) لإضافة حقل جديد في PDF، كما يمكنك تحديد حد لعدد الأحرف في حقل الخاص بك باستخدام [SetFieldLimit](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) وأخيرًا استخدام [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/save/index) لحفظ ملف PDF المحدث. يوضح لك مقتطف الكود التالي كيفية إضافة حقل نموذج في ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a text field named "Country" to the first page of the PDF
        // Specify the coordinates of the field (left, bottom, right, top)
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);

        // Set a character limit for the "Country" field to 20 characters
        editor.SetFieldLimit("Country", 20);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```

## إضافة عنوان URL لزر الإرسال في ملف PDF موجود

تتيح لك طريقة [AddSubmitBtn](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) تعيين عنوان URL لزر الإرسال في ملف PDF. هذا هو عنوان URL الذي يتم نشر البيانات عليه عند النقر على زر الإرسال. في كود المثال الخاص بنا، نحدد عنوان URL، واسم حقلنا، ورقم الصفحة التي نريد الإضافة إليها، وإحداثيات وضع الزر. تتطلب طريقة [AddSubmitBtn](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) اسم حقل زر الإرسال وعنوان URL. يتم توفير هذه الطريقة من قبل فئة [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). يوضح لك مقتطف الكود التالي كيفية تعيين عنوان URL لزر الإرسال.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddSubmitBtn()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var editor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a submit button named "Submit" to the first page of the PDF
         // Specify the button text ("Submit"), the URL to which the form data will be submitted,
         // and the coordinates of the button (left, bottom, right, top)
         editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);

         // Save PDF document
         editor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## إضافة JavaScript لزر الدفع

تتيح لك طريقة [AddFieldScript](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/addfieldscript) إضافة JavaScript إلى زر دفع في ملف PDF. تتطلب هذه الطريقة اسم زر الدفع وJavaScript. يتم توفير هذه الطريقة من قبل فئة [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). يوضح لك مقتطف الكود التالي كيفية تعيين JavaScript لزر الدفع.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFieldScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a JavaScript action to the field named "Last Name"
        // The script displays an alert box with the message "Only one last name"
        editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```