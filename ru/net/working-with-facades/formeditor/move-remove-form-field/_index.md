---
title: Перемещение и удаление поля формы
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ru/net/move-remove-form-field/
description: Узнайте, как управлять полями форм в PDF-файлах, включая их перемещение или удаление, с помощью Aspose.PDF for .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move and Remove Form Field",
    "alternativeHeadline": "Move and Remove Fields in PDF Forms Efficiently",
    "abstract": "Функция «Переместить и удалить поле формы» в классе FormEditor позволяет пользователям легко изменять положение полей формы и удалять их из существующих PDF-документов. Используя методы MoveField и RemoveField, пользователи могут эффективно настраивать формы, улучшая удобство использования и управление документами. Эта функция позволяет пользователям оптимизировать макеты PDF-файлов, не требуя глубоких технических знаний",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "416",
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
    "url": "/net/move-remove-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-remove-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Перемещение поля формы в новое место в существующем PDF-файле
Если вы хотите переместить поле формы в новое место, вы можете использовать метод MoveField класса FormEditor. Вам нужно всего лишь предоставить имя поля и новое местоположение этого поля методу MoveField. Также необходимо сохранить обновлённый PDF-файл с помощью метода Save класса FormEditor. Следующий фрагмент кода показывает, как переместить поле формы в новом месте в файле PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "MoveField.pdf");
        editor.MoveField("textbox1", 262.56f, 496.75f, 382.28f, 514.03f);
        // Save PDF document
        editor.Save(dataDir + "MoveField_out.pdf");
    }
}
```

## Удаление поля формы из существующего PDF-файла
Чтобы удалить поле формы из существующего PDF-файла, вы можете использовать метод RemoveField класса FormEditor. Этот метод принимает только один аргумент: имя поля. Вам нужно создать объект класса FormEditor, вызвать метод RemoveField для удаления определённого поля из PDF, а затем вызвать метод Save для сохранения обновлённого PDF-файла. Следующий фрагмент кода показывает, как удалить поля формы из существующего файла PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RemoveField("textbox1");
        // Save PDF document
        editor.Save(dataDir + "RemoveField_out.pdf");
    }
}
```

## Переименование полей формы в PDF
Также вы можете переименовать своё поле с помощью метода RenameField класса FormEditor.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenameFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RenameField("textbox1", "FirstName");
        // Save PDF document
        editor.Save(dataDir + "RenameField_out.pdf");
    }
}
```