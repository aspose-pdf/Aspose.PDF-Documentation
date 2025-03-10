---
title: PHP melalui COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/php-via-com-interop/
description: Integrasikan Aspose.PDF for .NET ke dalam aplikasi PHP menggunakan COM Interop. Tambahkan fitur pemrosesan PDF yang kuat ke dalam alur kerja Anda.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PHP via COM Interop",
    "alternativeHeadline": "Seamlessly Integrate PHP with Aspose.PDF for .NET via COM",
    "abstract": "Memperkenalkan fitur PHP melalui COM Interop, yang memungkinkan integrasi mulus Aspose.PDF for .NET dalam aplikasi PHP. Fungsionalitas ini memungkinkan pengembang untuk membuat dan memanipulasi file PDF menggunakan PHP, meningkatkan produktivitas dengan memanfaatkan kemampuan kuat .NET langsung dari skrip PHP. Rasakan konversi PDF ke Excel yang efisien dan lebih banyak lagi dengan solusi interoperabilitas inovatif ini.",
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
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Prasyarat

{{% alert color="primary" %}}
Konfigurasikan PHP Anda untuk bekerja dengan COM. Lihat <http://www.php.net/manual/en/ref.com.php>. Untuk informasi lebih lanjut, silakan periksa artikel yang berjudul [Gunakan Aspose.pdf untuk .NET melalui COM Interop](/pdf/id/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## Contoh Hello World!

{{% alert color="primary" %}}
Ini adalah aplikasi sederhana yang menunjukkan kepada Anda cara membuat file PDF baru dan menambahkan teks ke file PDF menggunakan [Aspose.PDF for .NET](/pdf/id/net/) dalam PHP melalui COM Interop.

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