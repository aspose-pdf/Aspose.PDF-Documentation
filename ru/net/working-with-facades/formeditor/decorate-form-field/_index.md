---
title: Украшение полей формы в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/decorate-form-field/
description: Узнайте, как украшать поля формы в документе PDF, добавляя визуальные улучшения, такие как границы, в .NET с помощью Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decorate Form Field in PDF",
    "alternativeHeadline": "Enhance PDF Forms with Custom Field Decorations",
    "abstract": "Представляем мощную функцию, которая улучшает управление PDF формами: возможность украшать отдельные или все поля формы с помощью класса FormEditor. Эта функциональность позволяет пользователям настраивать атрибуты полей, такие как стиль шрифта, размер, цвет границы и выравнивание, упрощая процесс создания визуально привлекательных и хорошо структурированных PDF форм. Улучшите свои PDF рабочие процессы с помощью этого интуитивного метода украшения для более качественного представления документа",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Украшение конкретного поля формы в существующем PDF файле

Метод [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield), присутствующий в классе [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor), позволяет вам украшать конкретное поле формы в PDF файле. Если вы хотите украсить конкретное поле, вам нужно передать имя поля этому методу. Однако перед вызовом этого метода вам необходимо создать объекты классов [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) и [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Вам также нужно назначить объект [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) свойству [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) объекта [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). После этого вы можете установить любые атрибуты, предоставленные объектом [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Как только вы установили атрибуты, вы можете вызвать метод [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) и, наконец, сохранить обновленный PDF, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) класса [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Следующий фрагмент кода показывает, как украсить конкретное поле формы.

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

## Украшение всех полей определенного типа в существующем PDF файле

Метод [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) позволяет вам украшать все поля формы определенного типа в PDF файле сразу. Если вы хотите украсить все поля определенного типа, вам нужно передать тип поля этому методу. Однако перед вызовом этого метода вам необходимо создать объекты классов [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) и [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Вам также нужно назначить объект [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) свойству [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) объекта [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). После этого вы можете установить любые атрибуты, предоставленные объектом [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Как только вы установили атрибуты, вы можете вызвать метод [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) и, наконец, сохранить обновленный PDF, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) класса [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Следующий фрагмент кода показывает, как украсить все поля определенного типа.

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