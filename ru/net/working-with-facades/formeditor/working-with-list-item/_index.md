---
title: Работа с элементом списка
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/working-with-list-item/
description: Этот раздел объясняет, как работать с элементом списка с помощью Aspose.PDF Facades, используя класс FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with List Item",
    "alternativeHeadline": "Enhance PDF Forms with List Item Management",
    "abstract": "Улучшите свои PDF формы с помощью функции элемента списка в Aspose.PDF for .NET. Легко добавляйте или удаляйте элементы из полей ListBox с помощью класса FormEditor, позволяя динамический и настраиваемый ввод от пользователей. Эта функциональность упрощает управление формами, делая его проще для адаптации контента под ваши нужды.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "325",
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
    "url": "/net/working-with-list-item/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-list-item/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Добавить элемент списка в существующий PDF файл

[AddListItem](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/addlistitem) метод позволяет вам добавить элемент в поле [ListBox](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/listboxfield). Первый аргумент — это имя поля, а второй аргумент — элемент поля. Вы можете передать либо один элемент поля, либо массив строк, содержащий список элементов. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor). Следующий фрагмент кода показывает, как добавить элементы списка в PDF файл.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a ListBox field for selecting country, placed at the specified coordinates on page 1
         formEditor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f,
             514.03f);

         // Add list items to the 'Country' ListBox field
         formEditor.AddListItem("Country", "USA");
         formEditor.AddListItem("Country", "Canada");
         formEditor.AddListItem("Country", "France");
         formEditor.AddListItem("Country", "Spain");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## Удалить элемент списка из существующего PDF файла

[DelListItem](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/dellistitem) метод позволяет вам удалить определенный элемент из [ListBox](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/listboxfield). Первый параметр — это имя поля, а второй параметр — это элемент, который вы хотите удалить из списка. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor). Следующий фрагмент кода показывает, как удалить элемент списка из PDF файла.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void DelListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-04.pdf");

         // Delete the list item "France" from the 'Country' ListBox field
         formEditor.DelListItem("Country", "France");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-04-mod.pdf");
     }
 }
```