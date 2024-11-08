---
title: Generate Thumbnail Images from PDF
linktitle: Generate Thumbnail Images
type: docs
weight: 110
url: /fr/net/generate-thumbnail-images-from-pdf-documents/
description: Cette section décrit comment générer des images miniatures à partir de documents PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "How to generate Thumbnail Images from PDF file",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, generate thumbnail Images",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette section décrit comment générer des images miniatures à partir de documents PDF"
}
</script>
{{% alert color="primary" %}}

Le SDK Adobe Acrobat est un ensemble d'outils qui vous aide à développer des logiciels qui interagissent avec la technologie Acrobat. Le SDK contient des fichiers d'en-tête, des bibliothèques de types, des utilitaires simples, des exemples de code et de la documentation.

En utilisant le SDK Acrobat, vous pouvez développer des logiciels qui s'intègrent avec Acrobat et Adobe Reader de plusieurs manières :

- **JavaScript** — Écrire des scripts, soit dans un document PDF individuel soit de manière externe, pour étendre les fonctionnalités d'Acrobat ou d'Adobe Reader.
- **Plug-ins** — Créer des plug-ins qui sont liés dynamiquement et étendent les fonctionnalités d'Acrobat ou d'Adobe Reader.
- **Communication interapplication** — Écrire un processus d'application séparé qui utilise la communication interapplication (IAC) pour contrôler les fonctionnalités d'Acrobat. DDE et OLE sont pris en charge sur Microsoft® Windows®, et les événements Apple/AppleScript sur Mac OS®. L'IAC n'est pas disponible sur UNIX®.

Aspose.PDF pour .NET offre beaucoup des mêmes fonctionnalités, vous libérant de la dépendance à l'automatisation d'Adobe Acrobat.
Aspose.PDF pour .NET offre beaucoup des mêmes fonctionnalités, vous libérant de la dépendance à l'automatisation d'Adobe Acrobat.

{{% /alert %}}

## Développement d'application en utilisant l'API de communication interapplication Acrobat

Pensez à l'API Acrobat comme ayant deux couches distinctes qui utilisent les objets de communication interapplication (IAC) d'Acrobat :

- La couche d'application Acrobat (AV). La couche AV vous permet de contrôler la manière dont le document est visualisé. Par exemple, la vue d'un objet document réside dans la couche associée à Acrobat.
- La couche de document portable (PD). La couche PD donne accès aux informations contenues dans un document, telles qu'une page. Depuis la couche PD, vous pouvez effectuer des manipulations de base des documents PDF, telles que supprimer, déplacer ou remplacer des pages, ainsi que modifier les attributs des annotations. Vous pouvez également imprimer des pages PDF, sélectionner du texte, accéder au texte manipulé et créer ou supprimer des vignettes.

Notre intention étant de convertir des pages PDF en images miniatures, nous nous concentrons davantage sur l'IAC.
Comme notre intention est de convertir les pages PDF en images miniatures, nous nous concentrons davantage sur l'IAC.

### Approche Acrobat

Pour générer les images miniatures de chaque document, nous avons utilisé l'Adobe Acrobat 7.0 SDK et le Microsoft .NET 2.0 Framework.

Le [SDK Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) combiné avec la version complète d'Adobe Acrobat expose une bibliothèque COM d'objets (malheureusement, le lecteur Adobe gratuit n'expose pas les interfaces COM) qui peut être utilisée pour manipuler et accéder aux informations PDF. En utilisant ces objets COM via COM Interop, chargez le document PDF, obtenez la première page et faites un rendu de cette page dans le presse-papiers. Ensuite, avec le .NET Framework, copiez ceci dans un bitmap, redimensionnez et combinez l'image et sauvegardez le résultat en tant que fichier GIF ou PNG.

Une fois Adobe Acrobat installé, utilisez regedit.exe et recherchez sous HKEY_CLASSES_ROOT une entrée appelée AcroExch.PDDoc.

**Le registre montrant l'entrée AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)
![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImagesUsingAdobe-CreateThumbnailImagesUsingAdobe.cs" >}}

## Approche Aspose.PDF pour .NET

Aspose.PDF pour .NET offre un support étendu pour la manipulation de documents PDF. Il prend également en charge la capacité de convertir les pages de documents PDF dans une variété de formats d'image. La fonctionnalité décrite ci-dessus peut facilement être réalisée en utilisant Aspose.PDF pour .NET.

Aspose.PDF présente des avantages distincts :

- Vous n'avez pas besoin d'avoir Adobe Acrobat installé sur votre système pour travailler avec des fichiers PDF.
- Utiliser Aspose.PDF pour .NET est simple et facile à comprendre par rapport à l'automatisation Acrobat.

Si nous avons besoin de convertir des pages PDF en JPEGs, l'espace de noms [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) fournit une classe nommée [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) pour rendre les pages PDF en images JPEG.
Si nous devons convertir des pages PDF en JPEG, le namespace [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) fournit une classe nommée [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) pour rendre les pages PDF en images JPEG.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImages-CreateThumbnailImages.cs" >}}

{{% alert color="primary" %}}

- Merci à CodeProject pour [Générer une image miniature à partir d'un document PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Merci à Acrobat pour la [référence SDK Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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


