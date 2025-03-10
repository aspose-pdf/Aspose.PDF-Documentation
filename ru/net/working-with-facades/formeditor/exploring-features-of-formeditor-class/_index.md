---
title: Изучение возможностей класса FormEditor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/exploring-features-of-formeditor-class/
description: Вы можете узнать подробности об изучении возможностей класса FormEditor с библиотекой Aspose. PDF для .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exploring features of FormEditor class",
    "alternativeHeadline": "Enhancing PDF Forms with FormEditor Class",
    "abstract": "Откройте для себя расширенные возможности класса FormEditor в библиотеке Aspose.PDF для .NET, предназначенные для удобной работы с интерактивными PDF-формами. Эта функция позволяет разработчикам легко добавлять, редактировать и настраивать поля форм с помощью удобных методов, упрощающих процесс изменения. Оптимизируйте работу с PDF-формами, используя широкие функциональные возможности FormEditor для улучшения рабочих процессов обработки документов",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "358",
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
    "url": "/net/exploring-features-of-formeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/exploring-features-of-formeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

Документы PDF иногда содержат интерактивные формы, известные как AcroForm. Они похожи на формы, используемые на веб-страницах. Эти формы содержат различные типы элементов управления, такие как текстовые поля, флажки и кнопки и т. д. Разработчику, работающему с файлами PDF, иногда может потребоваться отредактировать эти формы. В этой статье мы подробно рассмотрим, как [пространство имён Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) позволяет нам это сделать.

{{% /alert %}}

## Детали реализации

Разработчики могут использовать [пространство имён Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) не только для добавления новых форм и полей форм в документ PDF, но и для редактирования существующих полей. Объём данной статьи ограничен возможностями [Aspose.PDF for .NET](/pdf/net/), которые касаются редактирования форм.

[FormEditor] (https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) — это класс, который содержит большинство методов и свойств, позволяющих разработчикам редактировать поля форм. Вы можете не только добавлять новые поля, но и удалять существующие поля, перемещать одно поле в другое место, изменять имя поля или атрибуты и т.д. Список функций, предоставляемых этим классом, довольно обширен, и работать с полями форм с его помощью очень просто.

Эти методы можно разделить на две основные категории, одна из которых используется для управления полями, а другая — для установки новых атрибутов этих полей. Методы, которые мы можем отнести к первой категории, включают AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField и RenameField и т.д. Ко второй категории методов можно отнести SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit и SetFieldScript. Следующий фрагмент кода демонстрирует работу некоторых методов класса FormEditor:


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExploringFormEditorFeatures()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "inFile.pdf"))
    {
        // Create instance of FormEditor
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            // Add field in the PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "field1", 1, 300, 500, 350, 525);

            // Add List field in PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "field2", 1, 300, 200, 350, 225);

            // Add list items
            editor.AddListItem("field2", "item 1");
            editor.AddListItem("field2", "item 2");

            // Add submit button
            editor.AddSubmitBtn("submitbutton", 1, "Submit Form", "http:// Testwebsite.com/testpage", 200, 200, 250, 225);

            // Delete list item
                editor.DelListItem("field2", "item 1");

            // Move field to new position
            editor.MoveField("field1", 10, 10, 50, 50);

            // Remove existing field from the PDF
            editor.RemoveField("field1");

            // Rename an existing field
            editor.RenameField("field1", "newfieldname");

            // Reset all visual attributes to empty value
            editor.ResetFacade();

            // Set the alignment style of a text field
            editor.SetFieldAlignment("field1", Aspose.Pdf.Facades.FormFieldFacade.AlignLeft);

            // Set appearance of the field
            editor.SetFieldAppearance("field1", Aspose.Pdf.Annotations.AnnotationFlags.NoRotate);

            // Set field attributes i.e. ReadOnly, Required
            editor.SetFieldAttribute("field1", Aspose.Pdf.Facades.PropertyFlag.ReadOnly);

            // Set field limit
            editor.SetFieldLimit("field1", 25);

            // Save modifications in the output file
            editor.Save(dataDir + "FormEditorFeatures2_out.pdf");                    
        }
    }
}
```