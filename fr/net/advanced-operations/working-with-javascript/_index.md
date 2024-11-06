---
title: Travailler avec JavaScript
type: docs
url: fr/net/working-with-javascript/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec JavaScript",
    "alternativeHeadline": "Comment travailler avec JavaScript dans un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, javascript dans pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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

## Ajout de JavaScript (DOM)

### Qu'est-ce que Acrobat JavaScript ?

Acrobat JavaScript est un langage basé sur le noyau de la version 1.5 de JavaScript d'ISO-16262, anciennement connu sous le nom d'ECMAScript, un langage de script orienté objet développé par Netscape Communications. JavaScript a été créé pour décharger le traitement des pages Web d'un serveur vers un client dans les applications Web. Acrobat JavaScript implémente des extensions, sous forme de nouveaux objets et de leurs méthodes et propriétés associées, au langage JavaScript. Ces objets spécifiques à Acrobat permettent à un développeur de gérer la sécurité des documents, de communiquer avec une base de données, de gérer les pièces jointes de fichiers, de manipuler un fichier PDF de manière à ce qu'il se comporte comme un formulaire interactif et compatible avec le Web, etc. Étant donné que les objets spécifiques à Acrobat sont ajoutés au-dessus du JavaScript de base, vous avez toujours accès à ses classes standard, y compris Math, String, Date, Array, et RegExp.

### Acrobat JavaScript vs JavaScript HTML (Web)

Les documents PDF ont une grande polyvalence puisqu'ils peuvent être affichés à la fois dans le logiciel Acrobat ainsi que dans un navigateur Web.
Les documents PDF présentent une grande polyvalence puisqu'ils peuvent être affichés aussi bien dans le logiciel Acrobat que dans un navigateur Web.

- Le JavaScript d'Acrobat n'a pas accès aux objets d'une page HTML. De même, le JavaScript HTML ne peut pas accéder aux objets à l'intérieur d'un fichier PDF.
- Le JavaScript HTML peut manipuler des objets tels que Window. Le JavaScript d'Acrobat ne peut pas accéder à cet objet particulier mais il peut manipuler des objets spécifiques au PDF.

Vous pouvez ajouter du JavaScript aux niveaux du document et de la page en utilisant [Aspose.PDF pour .NET](/pdf/net/). Pour ajouter du JavaScript :

### Ajout de JavaScript à l'action du document ou de la page

1. Déclarez et instanciez un objet JavascriptAction avec l'instruction JavaScript souhaitée comme argument du constructeur.
1. Attribuez l'objet JavascriptAction à l'action désirée du document ou de la page PDF.

L'exemple ci-dessous applique l'OpenAction à un document spécifique.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddJavaScriptToPage-AddJavaScriptToPage.cs" >}}

### **Ajout/Suppression de JavaScript au niveau du document**
### **Ajout/Suppression de JavaScript au niveau du document**

Une nouvelle propriété nommée JavaScript est ajoutée dans la classe Document qui possède un type de collection JavaScript et fournit un accès aux scénarios JavaScript par sa clé. Cette propriété est utilisée pour ajouter du JavaScript au niveau du document. La collection JavaScript possède les propriétés et méthodes suivantes :

- string this(string key) – Obtient ou définit le JavaScript par son nom
- IList Keys – fournit une liste des clés existantes dans la collection JavaScript
- bool Remove(string key) – supprime le JavaScript par sa clé.

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


