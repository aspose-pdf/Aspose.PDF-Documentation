---
title: Внешний вид и атрибуты полей
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/changing-field-appearance-and-attributes/
description: В этом разделе объясняется, как вы можете изменить внешний вид и атрибуты полей с помощью класса FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Field appearance and attributes",
    "alternativeHeadline": "Enhance Form Fields with Custom Appearance and Behavior",
    "abstract": "Функция, представленная в классе FormEditor пространства имен Aspose.Pdf.Facades, позволяет пользователям настраивать как внешний вид, так и атрибуты полей формы в PDF-документах. Используя такие методы, как SetFieldAppearance и SetFieldAttributes, разработчики могут легко изменять визуальные элементы и поведение, включая ограничения полей, чтобы улучшить взаимодействие с пользователем и эффективность ввода данных. Эта функциональность предлагает большую гибкость в проектировании полей формы, адаптированных к конкретным потребностям приложения.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/changing-field-appearance-and-attributes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-field-appearance-and-attributes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

[FormEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/FormEditor) класс пространства имен [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades) позволяет вам не только изменить внешний вид поля формы, но и поведение поля. В этой статье мы увидим, как мы можем использовать класс FormEditor для изменения внешнего вида поля, атрибутов поля и ограничения поля.

{{% /alert %}}

## Подробности реализации

Метод [SetFieldAppearance](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) используется для изменения внешнего вида поля формы. Он принимает AnnotationFlag в качестве параметра. AnnotationFlag — это перечисление, которое имеет различные члены, такие как Hidden или NoRotate и т. д.

Метод [SetFieldAttributes](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) используется для изменения атрибута поля формы. Параметр, передаваемый этому методу, — это перечисление PropertyFlag, которое содержит члены, такие как ReadOnly или Required и т. д.

Класс [FormEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/FormEditor) также предоставляет метод для установки ограничения поля. Он сообщает полю, сколько символов можно заполнить. Приведенный ниже фрагмент кода показывает, как все эти методы могут быть использованы.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddFieldAndSetAttributes()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var doc = new Aspose.Pdf.Document(dataDir + "FilledForm.pdf"))
     {
         // Create an instance of FormEditor to manipulate form fields
         using (var formEditor = new Aspose.Pdf.Facades.FormEditor(doc))
         {
             // Add a new text field to the form on page 1 at the specified coordinates and size
             formEditor.AddField(Aspose.Pdf.Facades.FieldType.Text, "text1", 1, 200, 550, 300, 575);

             // Set the field attribute to make the text field required (user must fill it)
             formEditor.SetFieldAttribute("text1", Aspose.Pdf.Facades.PropertyFlag.Required);

             // Set a character limit for the field (maximum 20 characters)
             formEditor.SetFieldLimit("text1", 20);

             // Save PDF document
             formEditor.Save(dataDir + "ChangingFieldAppearance_out.pdf");
         }
     }
 }
```