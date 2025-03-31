---
title: Идентификация имён полей форм
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/identifying-form-fields-names/
description: Aspose.Pdf.Facades позволяет идентифицировать имена полей форм с помощью класса Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "Функционал Aspose.PDF для .NET упрощает процесс определения имён полей форм в PDF-документах. Используя класс Form и его атрибуты, пользователи могут легко получать и отображать имена полей вместе с соответствующими полями, упрощая заполнение и редактирование PDF-форм. Эта функция улучшает взаимодействие с пользователем, обеспечивая точное управление полями, особенно при работе с формами, созданными во внешних инструментах, таких как Adobe Designer",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

[Aspose.PDF for .NET](/pdf/ru/net/) предоставляет возможность создавать, редактировать и заполнять уже созданные PDF-формы. Пространство имён [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades) содержит класс [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form), который содержит функцию с именем [FillField](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/fillfield/index), и она принимает два аргумента, то есть имя поля и значение поля. Итак, чтобы заполнить поля формы, вы должны знать точное имя поля формы.

## Детали реализации

Мы часто сталкиваемся со сценарием, когда нам нужно заполнить форму, созданную в каком-либо инструменте, например, в Adobe Designer, и мы не уверены в именах полей формы. Итак, чтобы заполнить поля формы, сначала нам нужно прочитать имена всех полей PDF-формы. Класс [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form) предоставляет свойство с именем [FieldNames](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/properties/fieldnames), которое возвращает имена всех полей и возвращает null, если PDF не содержит ни одного поля. Однако при использовании этого свойства мы получаем имена всех полей в форме PDF, и мы можем не быть уверены, какое имя соответствует какому полю в форме.

В качестве решения этой проблемы мы будем использовать атрибуты внешнего вида каждого поля. Класс Form имеет функцию с именем [GetFieldFacade](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/getfieldfacade), которая возвращает атрибуты, включая расположение, цвет, стиль границы, шрифт, элемент списка и так далее. Чтобы сохранить эти значения, нам нужно использовать класс [FormFieldFacade](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/FormFieldFacade), который используется для записи визуальных атрибутов полей. Получив эти атрибуты, мы можем добавить текстовое поле под каждым полем, которое будет отображать имя поля.

{{% alert color="primary" %}}
На этом этапе возникает вопрос: «Как мы определим место, куда добавить текстовое поле?»
{{% /alert %}}

{{% alert color="primary" %}}
Решением этой проблемы является свойство Box в классе [FormFieldFacade](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/FormFieldFacade), которое содержит местоположение поля. Нам нужно сохранить эти значения в массиве типа прямоугольника и использовать эти значения для определения позиции, где добавить новые текстовые поля.

{{% /alert %}}

В пространстве имён [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades) у нас есть класс с именем [FormEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/FormEditor), который позволяет управлять PDF-формами. Откройте PDF-форму, добавьте текстовое поле под каждое существующее поле формы и сохраните PDF-форму под новым именем.

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