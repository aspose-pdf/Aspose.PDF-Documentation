---
title: Obtenir et définir les propriétés de la page
type: docs
url: /fr/net/get-and-set-page-properties/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obtenir et définir les propriétés de la page",
    "alternativeHeadline": "Obtenir et définir les propriétés des pages PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, obtenir les propriétés de la page, définir les propriétés de la page",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
Aspose.PDF pour .NET vous permet de lire et de définir les propriétés des pages dans un fichier PDF dans vos applications .NET. Cette section montre comment obtenir le nombre de pages dans un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés des pages. Les exemples donnés sont en C#, mais vous pouvez utiliser n'importe quel langage .NET comme VB.NET pour obtenir le même résultat.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Obtenir le Nombre de Pages dans un Fichier PDF

Lorsque vous travaillez avec des documents, vous voulez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF, cela ne prend pas plus de deux lignes de code.

Pour obtenir le nombre de pages dans un fichier PDF :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Utilisez ensuite la propriété Count de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (de l'objet Document) pour obtenir le nombre total de pages dans le document.

Le code suivant montre comment obtenir le nombre de pages d'un fichier PDF.
Le code suivant montre comment obtenir le nombre de pages d'un fichier PDF.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetNumberofPages-GetNumberofPages.cs" >}}

### Obtenir le nombre de pages sans sauvegarder le document

Parfois, nous générons des fichiers PDF à la volée et lors de la création de fichiers PDF, nous pouvons rencontrer le besoin (création de la Table des Matières, etc.) d'obtenir le nombre de pages du fichier PDF sans sauvegarder le fichier sur le système ou le flux. Pour répondre à ce besoin, une méthode [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) a été introduite dans la classe Document. Veuillez regarder le code suivant qui montre les étapes pour obtenir le nombre de pages sans sauvegarder le document.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetPageCount-GetPageCount.cs" >}}

## Obtenir les propriétés de la page

Chaque page d'un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, les boîtes de saignement, de coupe et de rognage.
Chaque page d'un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, le fond perdu, la boîte de rognage et la boîte de coupe.

### **Comprendre les propriétés des pages : la différence entre Artbox, BleedBox, CropBox, MediaBox, TrimBox et la propriété Rect**

- **Boîte de média** : La boîte de média est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, Lettre US, etc.) sélectionnée lors de l'impression du document en PostScript ou PDF. En d'autres termes, la boîte de média détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Boîte de fond perdu** : Si le document comporte un fond perdu, le PDF aura également une boîte de fond perdu. Le fond perdu est la quantité de couleur (ou d'œuvre d'art) qui dépasse le bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et coupé à la taille (« rogné »), l'encre ira jusqu'au bord de la page. Même si la page est mal coupée - légèrement décalée par rapport aux marques de coupe - aucun bord blanc n'apparaîtra sur la page.
- **Boîte de coupe** : La boîte de coupe indique la taille finale d'un document après impression et rognage.
- **Trim box** : Le trim box indique la taille finale d'un document après impression et découpe.
- **Art box** : L'art box est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Crop box** : La crop box est la taille de “page” à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seul le contenu de la crop box est affiché dans Adobe Acrobat.
  Pour des descriptions détaillées de ces propriétés, consultez la spécification Adobe.Pdf, en particulier 10.10.1 Limites de page.
- **Page.Rect** : l'intersection (rectangle communément visible) du MediaBox et du DropBox. L'image ci-dessous illustre ces propriétés.

Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Accéder aux propriétés de la page**

La classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fournit toutes les propriétés liées à une page PDF particulière.
La classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fournit toutes les propriétés relatives à une page PDF particulière.

À partir de là, il est possible d'accéder soit à des objets Page individuels en utilisant leur index, soit de parcourir la collection, en utilisant une boucle foreach, pour obtenir toutes les pages. Une fois qu'une page individuelle est accédée, nous pouvons obtenir ses propriétés. Le fragment de code suivant montre comment obtenir les propriétés d'une page.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetProperties-GetProperties.cs" >}}

## Obtenir une Page Particulière du Fichier PDF

Aspose.PDF permet de [diviser un PDF en pages individuelles](/pdf/fr/net/split-pdf-document/) et de les enregistrer en tant que fichiers PDF. Obtenir une page spécifiée dans un fichier PDF et l'enregistrer comme un nouveau PDF est une opération très similaire : ouvrir le document source, accéder à la page, créer un nouveau document et ajouter la page à celui-ci.

L'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec sa [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) contient les pages du fichier PDF.
L'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) contient la [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) qui détient les pages du fichier PDF.

1. Spécifiez l'indice de la page en utilisant la propriété Pages.
1. Créez un nouvel objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Ajoutez l'objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) au nouvel objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Sauvegardez le résultat en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le code suivant montre comment obtenir une page particulière d'un fichier PDF et la sauvegarder comme un nouveau fichier.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetParticularPage-GetParticularPage.cs" >}}

## Déterminer la couleur de la page

La classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fournit les propriétés liées à une page particulière dans un document PDF, y compris le type de couleur - RVB, noir et blanc, niveaux de gris ou indéfini - utilisé par la page.
La classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fournit les propriétés relatives à une page particulière dans un document PDF, y compris le type de couleur - RVB, noir et blanc, niveaux de gris ou indéfini - utilisée par la page.

Toutes les pages des fichiers PDF sont contenues par la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). La propriété ColorType spécifie la couleur des éléments sur la page. Pour obtenir ou déterminer les informations de couleur pour une page PDF particulière, utilisez la propriété [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) de l'objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

Le code suivant montre comment itérer à travers chaque page individuelle d'un fichier PDF pour obtenir des informations sur la couleur.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-DeterminePageColor-DeterminePageColor.cs" >}}

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


