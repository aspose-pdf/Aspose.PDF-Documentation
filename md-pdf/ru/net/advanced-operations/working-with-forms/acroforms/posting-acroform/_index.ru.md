---
title: Публикация данных AcroForm
linktitle: Публикация AcroForm
type: docs
weight: 50
url: /net/posting-acroform-data/
description: Вы можете импортировать и экспортировать данные формы в XML-файл с помощью пространства имен Aspose.Pdf.Facades в Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Публикация данных AcroForm",
    "alternativeHeadline": "Импорт и экспорт данных формы в XML-файл",
    "author": {
        "@type": "Person",
        "name": "Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, публикация данных acroform",
    "wordcount": "302",
    "proficiencyLevel": "Начинающий",
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2022-02-04",
    "description": "Вы можете импортировать и экспортировать данные формы в XML-файл с помощью пространства имен Aspose.Pdf.Facades в Aspose.PDF для .NET."
}
</script>

{{% alert color="primary" %}}

AcroForm — важный тип документа PDF. Вы можете не только создавать и редактировать AcroForm с использованием [пространства имен Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace), но также импортировать и экспортировать данные формы в XML-файл и из него. Пространство имен Aspose.Pdf.Facades в Aspose.PDF для .NET позволяет реализовать ещё одну функцию AcroForm, которая помогает отправлять данные AcroForm на внешнюю веб-страницу. Эта веб-страница затем читает переменные POST и использует эти данные для дальнейшей обработки. Эта функция полезна в случаях, когда вы не просто хотите сохранить данные в файле PDF, а хотите отправить их на свой сервер, а затем сохранить в базе данных и т.д.

{{% /alert %}}

## Детали реализации

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

В данной статье мы попытались создать AcroForm, используя [пространство имен Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).
В этой статье мы попытались создать AcroForm с использованием [пространства имен Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).

```csharp
// Создаем экземпляр класса FormEditor и связываем входные и выходные PDF-файлы
Aspose.Pdf.Facades.FormEditor editor = new Aspose.Pdf.Facades.FormEditor("input.pdf","output.pdf");

// Создаем поля AcroForm - для простоты я создал только два поля
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

// Добавляем кнопку отправки и устанавливаем целевой URL
editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

// Сохраняем выходной PDF-файл
editor.Save();
```

{{% alert color="primary" %}}

Следующий фрагмент кода показывает, как получить отправленные значения на целевой веб-странице.
Следующий фрагмент кода показывает, как получить значения, отправленные на целевую веб-страницу.
{{% /alert %}}

```csharp
// Показать отправленные значения на целевой веб-странице
Response.Write("Привет " + Request.Form.Get("firstname") + " " + Request.Form.Get("lastname"));
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


