---
title: Добавить поля формы PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/add-form-fields/
description: Эта тема объясняет, как работать с полями формы с помощью Aspose.PDF Facades, используя класс FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Form Fields",
    "alternativeHeadline": "Effortlessly Enhance PDFs with Custom Form Fields",
    "abstract": "Улучшите свои PDF-документы динамической интерактивностью, добавляя поля формы с помощью класса FormEditor в Aspose.PDF for .NET. Эта функция позволяет вам легко включать текстовые поля, кнопки отправки с URL-адресами и функциональность JavaScript для кнопок, упрощая ввод данных и отправку данных в ваших PDF.",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Добавить поле формы в существующий PDF файл

Чтобы добавить поле формы в существующий PDF файл, вам нужно использовать метод [AddField](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/addfield/index) класса [FormEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor). Этот метод требует от вас указать тип поля, которое вы хотите добавить, вместе с именем и местоположением поля. Вам нужно создать объект класса [FormEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor), использовать метод [AddField](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/addfield/index) для добавления нового поля в PDF. Также вы можете указать ограничение на количество символов в вашем поле с помощью [SetFieldLimit](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) и, наконец, использовать метод [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/save/index) для сохранения обновленного PDF файла. Следующий фрагмент кода показывает, как добавить поле формы в существующий PDF файл.

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

## Добавить URL кнопки отправки в существующий PDF файл

Метод [AddSubmitBtn](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) позволяет вам установить URL кнопки отправки в PDF файле. Это URL, по которому данные отправляются, когда кнопка отправки нажата. В нашем примере кода мы указываем URL, имя нашего поля, номер страницы, на которую мы хотим добавить, и координаты размещения кнопки. Метод [AddSubmitBtn](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) требует имя поля кнопки отправки и URL. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Следующий фрагмент кода показывает, как установить URL кнопки отправки.

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

## Добавить JavaScript для кнопки

Метод [AddFieldScript](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/addfieldscript) позволяет вам добавить JavaScript к кнопке в PDF файле. Этот метод требует имя кнопки и JavaScript. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Следующий фрагмент кода показывает, как установить JavaScript для кнопки. 

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