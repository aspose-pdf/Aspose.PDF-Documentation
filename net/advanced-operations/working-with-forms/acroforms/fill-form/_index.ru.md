---
title: Заполнение AcroForm - Заполнение формы PDF с использованием C#
linktitle: Заполнение AcroForm
type: docs
weight: 20
url: /net/fill-form/
keywords: Заполнение формы PDF C#
description: Вы можете заполнять формы в вашем PDF-документе с помощью библиотеки Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Заполнение AcroForm",
    "alternativeHeadline": "Как заполнить AcroForm в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, заполнение acroform",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "url": "/net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/fill-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Вы можете заполнять формы в вашем PDF-документе с помощью библиотеки Aspose.PDF для .NET."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Заполнение поля формы в документе PDF

Чтобы заполнить поле формы, получите поле из коллекции Form объекта Document, затем установите значение поля, используя свойство Value поля.

В этом примере выбирается TextBoxField и устанавливается его значение с использованием свойства Value.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Открыть документ
Document pdfDocument = new Document(dataDir + "FillFormField.pdf");

// Получить поле
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// Изменить значение поля
textBoxField.Value = "Значение, которое должно быть заполнено в поле";
dataDir = dataDir + "FillFormField_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```

