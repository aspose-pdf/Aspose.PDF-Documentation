---
title: PHP via l'interopérabilité COM
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/php-via-com-interop/
description: Intégrez Aspose.PDF for .NET dans des applications PHP en utilisant COM Interop. Ajoutez des fonctionnalités puissantes de traitement PDF à votre flux de travail.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PHP via COM Interop",
    "alternativeHeadline": "Seamlessly Integrate PHP with Aspose.PDF for .NET via COM",
    "abstract": "Présentation de la fonctionnalité PHP via COM Interop, qui permet une intégration transparente de Aspose.PDF for .NET au sein des applications PHP. Cette fonctionnalité permet aux développeurs de créer et de manipuler des fichiers PDF en utilisant PHP, améliorant ainsi la productivité en tirant parti des puissantes capacités de .NET directement à partir des scripts PHP. Découvrez des conversions efficaces de PDF en Excel et plus encore avec cette solution d'interopérabilité innovante.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Prérequis

{{% alert color="primary" %}}
Configurez votre PHP pour travailler avec COM. Voir <http://www.php.net/manual/en/ref.com.php>. Pour plus d'informations, veuillez consulter l'article intitulé [Utiliser Aspose.pdf pour .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## Exemple Hello World!

{{% alert color="primary" %}}
Ceci est une application simple qui vous montre comment créer un nouveau fichier PDF et ajouter du texte au fichier PDF en utilisant [Aspose.PDF for .NET](/pdf/net/) en PHP via COM Interop.

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