---
title: Работа с JavaScript
type: docs
url: ru/net/working-with-javascript/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с JavaScript",
    "alternativeHeadline": "Как работать с JavaScript в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, javascript в pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## Добавление JavaScript (DOM)

### Что такое Acrobat JavaScript?

Acrobat JavaScript — это язык, основанный на ядре JavaScript версии 1.5 ISO-16262, ранее известного как ECMAScript, объектно-ориентированный сценарный язык, разработанный компанией Netscape Communications. JavaScript был создан для переноса обработки веб-страниц с сервера на клиент в веб-приложениях. Acrobat JavaScript реализует расширения в виде новых объектов и соответствующих им методов и свойств для языка JavaScript. Эти объекты, специфичные для Acrobat, позволяют разработчику управлять безопасностью документов, взаимодействовать с базами данных, обрабатывать файлы вложений, манипулировать файлом PDF так, чтобы он вел себя как интерактивная, веб-активированная форма и т. д. Поскольку объекты, специфичные для Acrobat, добавлены поверх основного JavaScript, у вас все еще есть доступ к его стандартным классам, включая Math, String, Date, Array и RegExp.

### Acrobat JavaScript против HTML (Web) JavaScript

Документы PDF обладают большой универсальностью, поскольку их можно отображать как в программном обеспечении Acrobat, так и в веб-браузере.
PDF-документы обладают большой универсальностью, поскольку их можно отображать как в программном обеспечении Acrobat, так и в веб-браузере.

- JavaScript в Acrobat не имеет доступа к объектам внутри HTML-страницы. Аналогично, JavaScript в HTML не может получить доступ к объектам внутри PDF-файла.
- JavaScript в HTML может манипулировать такими объектами, как Window. JavaScript в Acrobat не может получить доступ к этому конкретному объекту, но может манипулировать объектами, специфичными для PDF.

Вы можете добавить JavaScript как на уровне документа, так и на уровне страницы с помощью [Aspose.PDF для .NET](/pdf/net/). Для добавления JavaScript:

### Добавление JavaScript к действию документа или страницы

1. Объявите и создайте объект JavascriptAction с желаемым выражением JavaScript в качестве аргумента конструктора.
1. Назначьте объект JavascriptAction желаемому действию документа PDF или страницы.

Пример ниже применяет OpenAction к конкретному документу.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddJavaScriptToPage-AddJavaScriptToPage.cs" >}}

### **Добавление/Удаление JavaScript на уровне документа**
### **Добавление/Удаление JavaScript на уровне документа**

В классе Document добавлено новое свойство с именем JavaScript, которое имеет тип коллекции JavaScript и предоставляет доступ к сценариям JavaScript по их ключу. Это свойство используется для добавления JavaScript на уровне документа. Коллекция JavaScript имеет следующие свойства и методы:

- string this(string key) – Получает или задает JavaScript по его имени
- IList Keys – предоставляет список существующих ключей в коллекции JavaScript
- bool Remove(string key) – удаляет JavaScript по его ключу.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddRemoveJavascriptToDoc-AddRemoveJavascriptToDoc.cs" >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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

