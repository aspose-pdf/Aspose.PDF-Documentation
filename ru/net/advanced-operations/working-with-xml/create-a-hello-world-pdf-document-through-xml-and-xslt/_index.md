---
title: Создание PDF из XML с использованием XSLT
linktitle: Создать PDF из XML с использованием XSLT
type: docs
weight: 10
url: /ru/net/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Библиотека C# предоставляет возможность преобразования XML-файла в PDF-документ, при этом входной XML-файл должен соответствовать схеме Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Создание PDF из XML с использованием XSLT",
    "alternativeHeadline": "Как создать PDF из XML с использованием XSLT",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, создание pdf xml, pdf с xslt",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/"
    },
    "dateModified": "2022-02-04",
    "description": "Библиотека C# предоставляет возможность преобразования XML-файла в PDF-документ, при этом входной XML-файл должен соответствовать схеме Aspose.PDF."
}
</script>
```
The following code snippet also work with [Aspose.PDF.Drawing](/pdf/ru/net/drawing/) library.

Иногда у вас могут быть существующие XML-файлы, содержащие данные приложения, и вы хотите создать PDF-отчет, используя эти файлы. Вы можете использовать XSLT для преобразования вашего существующего XML-документа в совместимый с Aspose.Pdf XML-документ, а затем создать PDF-файл. Существует 3 шага для создания PDF, используя XML и XSLT.

Пожалуйста, выполните следующие шаги для преобразования XML-файла в PDF-документ с помощью XSLT:

* Создайте экземпляр класса PDF, который представляет PDF-документ
* Если вы приобрели лицензию, то также следует встроить код для использования этой лицензии с помощью класса License в пространстве имен Aspose.Pdf
* Привяжите входные XML и XSLT файлы к экземпляру класса PDF, вызвав его метод BindXML
* Сохраните привязанный XML с экземпляром PDF как PDF-документ

## Input XML File

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## Input XSLT File

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```
{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Working-Document-HelloWorldPDFUsingXmlAndXslt-HelloWorldPDFUsingXmlAndXslt.cs" >}}

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

---
sidebar_position: 1
sidebar_label: 'Начало работы'
slug: / 
title: Начало работы
pagination_next: null
pagination_prev: null
---

# Начало работы 

## Описание

`docusaurus-plugin-openapi-docs` упрощает создание документации для OpenAPI с использованием Docusaurus. Этот плагин генерирует документацию из спецификаций OpenAPI.

## Установка

```bash
npm install docusaurus-plugin-openapi-docs
```

## Конфигурация

```js
// docusaurus.config.js
module.exports = {
  // ...
  plugins: [
    [
      'docusaurus-plugin-openapi-docs',
      {
        // ключи и их значения
      },
    ],
  ],
};
```

## Использование

```md
---
id: 'openapi'
title: 'OpenAPI Документация'
sidebar_label: 'API'
sidebar_position: 2
---

import { RedocStandalone } from 'redoc';

<RedocStandalone specUrl="/api/openapi.yaml" />
```

## Настройки

- `specPath`: Путь к файлу спецификации OpenAPI.
- `outputDir`: Директория для сохранения сгенерированной документации.
- `sidebarOptions`: Опции для конфигурирования боковой панели.

## Сторонние зависимости

Плагин использует `redoc` для рендеринга документации OpenAPI.

## Обновление документации

Не забывайте периодически обновлять вашу OpenAPI спецификацию и регенерировать документацию с помощью этого плагина.

## Пример конфигурации

```js
// docusaurus.config.js
module.exports = {
  // ...
  plugins: [
    [
      'docusaurus-plugin-openapi-docs',
      {
        id: 'openapi',
        specPath: 'api/openapi.yaml',
        outputDir: 'docs/api',
        sidebarOptions: {
          groupPathsBy: 'tag',
          changefreq: "monthly",
        },
      },
    ],
  ],
};
```
```
