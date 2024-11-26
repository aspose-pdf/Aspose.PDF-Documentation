---
title: PHP via COM Interop
type: docs
weight: 50
url: /net/php-via-com-interop/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PHP via COM Interop",
    "alternativeHeadline": "Seamlessly Integrate PHP with Aspose.PDF for .NET via COM",
    "abstract": "Introducing the PHP via COM Interop feature, which allows seamless integration of Aspose.PDF for .NET within PHP applications. This functionality enables developers to create and manipulate PDF files using PHP, enhancing productivity by leveraging .NET\u2019s powerful capabilities directly from PHP scripts. Experience efficient PDF to Excel conversions and more with this innovative interoperability solution",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Prerequisites

{{% alert color="primary" %}}
Configure your PHP to work with COM. See <http://www.php.net/manual/en/ref.com.php>. For more information, please check the article named [Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## Hello World! Example

{{% alert color="primary" %}}
This is a simple application that shows you how to create a new PDF file and add text to the PDF file using [Aspose.PDF for .NET](/pdf/net/) in PHP via COM Interop.

{{% /alert %}}

```php
<?php
echo "<h2>Calling Aspose.PDF for .NET from PHP using COM Interoperatibility</h2>";
echo "<h3>PDF to Excel Conversion</h3>";

//set license
$lic = new COM("Aspose.Pdf.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//Load Pdf Document
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.Pdf.ComHelper");

$pdf = $helper->OpenFile($input);

// Save the PDF document  to desired file format by passing  SaveFormat enum value for the format in this case we pass 9 for excel.

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```
