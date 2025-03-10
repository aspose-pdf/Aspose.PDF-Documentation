---
title: COM 상호 운용을 통한 PHP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/php-via-com-interop/
description: COM Interop을 사용하여 PHP 애플리케이션에 Aspose.PDF for .NET을 통합합니다. 워크플로에 강력한 PDF 처리 기능을 추가하세요.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PHP via COM Interop",
    "alternativeHeadline": "Seamlessly Integrate PHP with Aspose.PDF for .NET via COM",
    "abstract": "PHP 애플리케이션 내에서 Aspose.PDF for .NET의 원활한 통합을 가능하게 하는 PHP via COM Interop 기능을 소개합니다. 이 기능은 개발자가 PHP를 사용하여 PDF 파일을 생성하고 조작할 수 있게 하여, PHP 스크립트에서 .NET의 강력한 기능을 직접 활용하여 생산성을 향상시킵니다. 이 혁신적인 상호 운용성 솔루션을 통해 효율적인 PDF에서 Excel로의 변환 등을 경험해 보세요.",
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
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 필수 조건

{{% alert color="primary" %}}
COM과 함께 작동하도록 PHP를 구성하세요. 자세한 내용은 <http://www.php.net/manual/en/ref.com.php>를 참조하세요. 추가 정보는 [COM Interop을 통해 .NET용 Aspose.pdf 사용하기](/pdf/ko/net/use-aspose-pdf-for-net-via-com-interop/)라는 기사를 확인하세요.

{{% /alert %}}

## Hello World! 예제

{{% alert color="primary" %}}
이것은 PHP를 통해 COM Interop을 사용하여 새로운 PDF 파일을 생성하고 PDF 파일에 텍스트를 추가하는 방법을 보여주는 간단한 애플리케이션입니다. [Aspose.PDF for .NET](/pdf/ko/net/)을 사용하세요.

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