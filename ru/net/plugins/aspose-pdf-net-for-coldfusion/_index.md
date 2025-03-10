---
title: Использование Aspose.PDF for .NET с Coldfusion
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/using-aspose-pdf-for-net-with-coldfusion/
description: Вам следует работать с Aspose.PDF for .NET в Coldfusion, используя класс PdfFileInfo
lastmod: "2021-07-14"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Aspose.PDF for .NET with Coldfusion",
    "alternativeHeadline": "Integrate Aspose.PDF for .NET with Coldfusion Effortlessly",
    "abstract": "Откройте для себя бесшовную интеграцию Aspose.PDF для .NET с Coldfusion, которая позволит вам без труда управлять PDF-файлами и редактировать их. Узнайте, как использовать класс PdfFileInfo для извлечения важной информации из документа, расширяя возможности ваших приложений Coldfusion за счёт надёжных функций работы с PDF. Это руководство содержит наглядный пример, который поможет вам легко внедрить эту мощную функцию",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "634",
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
    "url": "/net/using-aspose-pdf-for-net-with-coldfusion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-aspose-pdf-for-net-with-coldfusion/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

В этой статье мы объясним, как использовать Aspose.PDF for .NET с Coldfusion. Это поможет вам понять детали интеграции Aspose.PDF for .NET и Coldfusion. С помощью простого примера я покажу вам, как внедрить функциональность Aspose.PDF for .NET в ваши приложения Coldfusion.

{{% /alert %}}

## Предыстория

Aspose.PDF for .NET — это компонент, который также позволяет редактировать существующие PDF-файлы и управлять ими. Aspose предоставляет этот компонент как для .NET, так и для Java, которые можно использовать в ваших приложениях .NET и Java соответственно, просто получив доступ к API компонента. Однако способ интеграции Aspose.PDF for .NET с Coldfusion немного отличается. В этой статье мы подробно рассмотрим его.

## Необходимые условия

Чтобы иметь возможность запускать Aspose.PDF for .NET на Coldfusion, вам потребуются IIS, .NET 2.0 и Coldfusion. Я протестировал компонент, используя IIS 5, .NET 2.0 и Colfusion 8. Есть ещё две вещи, на которые вы должны обратить внимание при установке Coldfusion. Во-первых, вы должны указать, какие сайты под управлением IIS будут работать под управлением Coldfusion. Во-вторых, вам нужно выбрать «Службы интеграции .NET» в установщике Coldfusion. Службы интеграции .NET позволяют получить доступ к сборке компонентов .NET в приложениях Coldfusion; в данном случае компонентом будет Aspose.PDF for .NET.

## Объяснение

Прежде всего, вы должны скопировать файл DLL (Aspose.PDF .dll) в место, откуда вы будете получать к нему доступ позже; это будет задано как путь и присвоено атрибуту assembly тега cfobject, как показано ниже:

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.Pdf.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```

Атрибут class в вышеуказанном теге указывает на класс фасадов Aspose.PDF, которым в данном случае является PdfFileInfo. Атрибут name — это имя экземпляра класса, которое будет использоваться позже в коде для доступа к методам или свойствам класса. Атрибут type определяет тип компонента — в нашем случае это .NET.

Один важный момент, о котором вы должны помнить при использовании компонента .NET в Coldfusion, заключается в том, что при получении или установке любого свойства объекта класса вы должны следовать определённой структуре. Чтобы установить значение свойства, вы будете использовать синтаксис Set_propertyname, а чтобы получить значение свойства — Get_propertyname.

Например, установите значение свойства:

```html
<cfset FilePath = ExpandPath("guide.pdf")>
```

Получите значение свойства:

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

Приведённый ниже базовый, но полный пример поможет вам понять процесс использования Aspose.PDF for .NET в Coldfusion.

### Давайте покажем информацию о PDF-файле

```html
<!--- create an instance of PdfFileInfo class --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.Pdf.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- get pdf file path --->

<cfset FilePath = ExpandPath("guide.pdf")>

<!--- assign pdf file path to the class object by setting its inputfile property--->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- Show file info --->

<cfoutput><b>Title:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>Subject:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>Author:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>Creator:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```

## Заключение

{{% alert color="primary" %}}
В этой статье мы увидели, что если мы будем следовать некоторым основным правилам интеграции Coldfusion и .NET, мы сможем включить множество функций и возможностей, связанных с работой с PDF-документами, используя Aspose.PDF for .NET в наших приложениях Coldfusion.
{{% /alert %}}