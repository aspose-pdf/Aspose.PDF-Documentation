---
title: تحديد أسماء حقول النموذج
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/identifying-form-fields-names/
description: Aspose.Pdf.Facades يتيح لك تحديد أسماء حقول النموذج باستخدام فئة Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "تعمل الوظيفة في Aspose.PDF for .NET على تبسيط عملية تحديد أسماء حقول النموذج في مستندات PDF. من خلال استخدام فئة Form وخصائصها، يمكن للمستخدمين استرداد وعرض أسماء الحقول بسهولة جنبًا إلى جنب مع حقولها المقابلة، مما يسهل ملء وتحرير نماذج PDF. تعزز هذه الميزة تجربة المستخدم من خلال ضمان التلاعب الدقيق بالحقول، خاصة عند العمل مع النماذج التي تم إنشاؤها في أدوات خارجية مثل Adobe Designer",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "511",
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
    "url": "/net/identifying-form-fields-names/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/identifying-form-fields-names/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

[Aspose.PDF for .NET](/pdf/ar/net/) يوفر القدرة على إنشاء وتحرير وملء نماذج PDF التي تم إنشاؤها مسبقًا. تحتوي مساحة أسماء [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades) على فئة [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form) ، والتي تحتوي على دالة تسمى [FillField](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/fillfield/index) وتأخذ وسيطين وهما اسم الحقل وقيمة الحقل. لذلك، لملء حقول النموذج، يجب أن تكون على دراية باسم حقل النموذج الدقيق.

## تفاصيل التنفيذ

غالبًا ما نواجه سيناريو حيث نحتاج إلى ملء النموذج الذي تم إنشاؤه في أداة ما، مثل Adobe Designer، ولسنا متأكدين من أسماء حقول النموذج. لذلك، لملء حقول النموذج، نحتاج أولاً إلى قراءة أسماء جميع حقول نموذج PDF. توفر فئة [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form) خاصية تسمى [FieldNames](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/properties/fieldnames) التي تعيد أسماء جميع الحقول وتعيد null إذا لم يحتوي PDF على أي حقل. ومع ذلك، عند استخدام هذه الخاصية، نحصل على أسماء جميع الحقول في نموذج PDF وقد لا نكون متأكدين من الاسم الذي يتوافق مع أي حقل في النموذج.

كحل لهذه المشكلة، سنستخدم خصائص المظهر لكل حقل. تحتوي فئة Form على دالة تسمى [GetFieldFacade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/getfieldfacade) التي تعيد الخصائص، بما في ذلك الموقع، اللون، نمط الحدود، الخط، عنصر القائمة، وما إلى ذلك. لحفظ هذه القيم، نحتاج إلى استخدام فئة [FormFieldFacade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/FormFieldFacade) ، والتي تستخدم لتسجيل الخصائص المرئية للحقول. بمجرد أن نحصل على هذه الخصائص، يمكننا إضافة حقل نصي تحت كل حقل يعرض اسم الحقل.

{{% alert color="primary" %}}
في هذه المرحلة، يطرح سؤال "كيف سنحدد الموقع الذي نضيف فيه حقل النص؟"
{{% /alert %}}

{{% alert color="primary" %}}
الحل لهذه المشكلة هو خاصية Box في فئة [FormFieldFacade](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/FormFieldFacade) ، التي تحتفظ بموقع الحقل. نحتاج إلى حفظ هذه القيم في مصفوفة من نوع المستطيل واستخدام هذه القيم لتحديد الموقع الذي نضيف فيه حقول النص الجديدة.

{{% /alert %}}

في مساحة أسماء [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades) لدينا فئة تسمى [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/FormEditor) التي توفر القدرة على التلاعب بنماذج PDF. افتح نموذج PDF؛ أضف حقل نصي تحت كل حقل نموذج موجود واحفظ نموذج PDF باسم جديد.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyFormFieldsNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // First a input pdf file should be assigned
    var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf");
    // Get all field names
    var allfields = form.FieldNames;
    // Create an array which will hold the location coordinates of Form fields
    var box = new System.Drawing.Rectangle[allfields.Length];
    for (int i = 0; i < allfields.Length; i++)
    {
        // Get the appearance attributes of each field, consequtively
        var facade = form.GetFieldFacade(allfields[i]);
        // Box in FormFieldFacade class holds field's location
        box[i] = facade.Box;
    }
    // Save PDF document
    form.Save(dataDir + "IdentifyFormFields_1_out.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
    {
        // Now we need to add a textfield just upon the original one
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, 
                "TextField" + i, allfields[i], 1, 
                box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "IdentifyFormFields_out.pdf");
        }
    }
}
```