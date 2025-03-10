---
title: PHP через COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/php-via-com-interop/
description: Интеграция Aspose.PDF for .NET в приложения PHP с использованием COM Interop. Добавьте мощные функции обработки PDF в свой рабочий процесс.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PHP via COM Interop",
    "alternativeHeadline": "Seamlessly Integrate PHP with Aspose.PDF for .NET via COM",
    "abstract": "Представляем функцию PHP через COM Interop, которая позволяет легко интегрировать Aspose.PDF для .NET в приложения PHP. Эта функция позволяет разработчикам создавать PDF-файлы и управлять ими с помощью PHP, повышая производительность за счёт использования мощных возможностей .NET непосредственно из PHP-скриптов. Испытайте эффективное преобразование PDF в Excel и многое другое с этим инновационным решением для обеспечения взаимодействия",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PHP, COM Interop, Aspose.PDF, PDF file creation, Excel conversion, Aspose.License, COM interoperability, PHP integration, SaveFormat enum, .NET integration",
    "wordcount": "192",
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
    "url": "/net/php-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/php-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Предварительные требования

{{% alert color="primary" %}}
Настройте ваш PHP для работы с COM. См. http://www.php.net/manual/ru/ref.com.php. Для получения дополнительной информации ознакомьтесь со статьёй под названием «Использование Aspose.pdf для .NET через COM Interop» (Use Aspose.pdf for .NET via COM Interop).

{{% /alert %}}

## Пример Hello World!

{{% alert color="primary" %}}
Это простое приложение, которое показывает вам, как создать новый PDF-файл и добавить текст в PDF-файл с помощью Aspose.PDF for .NET на PHP через COM Interop.

{{% /alert %}}

```php
<?php
echo "<h2>Calling Aspose.PDF for .NET from PHP using COM Interoperatibility</h2>";
echo "<h3>PDF to Excel Conversion</h3>";

// Set license
$lic = new COM("Aspose.Pdf.License");
$lic->SetLicense("Aspose.Total.lic");

// Open PDF document
$input = "HelloWorld.pdf";
$helper = new COM("Aspose.Pdf.ComHelper");

$pdf = $helper->OpenFile($input);

// Save PDF document to desired file format by passing  SaveFormat enum value for the format in this case we pass 9 for excel.
$output = "test_php.xls";
$pdf->Save_4($output, 9);
?>
```