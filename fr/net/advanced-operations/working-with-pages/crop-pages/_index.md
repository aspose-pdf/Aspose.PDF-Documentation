---
title: Rogner les pages PDF programmablement en C#
linktitle: Rogner les Pages
type: docs
weight: 80
url: fr/net/crop-pages/
description: Vous pouvez obtenir les propriétés des pages, telles que la largeur, la hauteur, les boîtes de saignement, de rognage et de coupe en utilisant Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "headline": "Rogner les pages PDF programmablement en C#",
    "alternativeHeadline": "Comment rogner les pages PDF en .NET",
    "author": {
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, rogner les pages PDF",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
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
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Vous pouvez obtenir les propriétés des pages, telles que la largeur, la hauteur, les boîtes de saignement, de rognage et de coupe en utilisant Aspose.PDF pour .NET."
}
</script>
## Propriétés de la page

Chaque page d'un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, ainsi que les zones de fond perdu, de rognage et de coupe. Aspose.PDF permet d'accéder à ces propriétés.

- **Boîte média** : La boîte média est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, Lettre US, etc.) sélectionnée lors de l'impression du document en PostScript ou PDF. En d'autres termes, la boîte média détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Boîte de fond perdu** : Si le document comporte un fond perdu, le PDF aura également une boîte de fond perdu. Le fond perdu est la quantité de couleur (ou d'œuvre d'art) qui dépasse au-delà du bord de la page. Il est utilisé pour s'assurer que lorsque le document est imprimé et découpé à la taille ("rogné"), l'encre ira jusqu'au bord de la page. Même si la page est mal rognée - coupée légèrement à côté des marques de coupe - aucun bord blanc n'apparaîtra sur la page.
- **Boîte de coupe** : La boîte de coupe indique la taille finale d'un document après impression et rognage.
- **Boîte d'art** : La boîte d'art est la boîte tracée autour du contenu réel des pages de vos documents.
- **Boîte artistique** : La boîte artistique est la boîte dessinée autour du contenu réel des pages de vos documents.
- **Boîte de rognage** : La boîte de rognage est la "taille de page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seul le contenu de la boîte de rognage est affiché dans Adobe Acrobat. Pour des descriptions détaillées de ces propriétés, consultez la spécification Adobe.Pdf, particulièrement 10.10.1 Limites de page.
- **Page.Rect** : l'intersection (rectangle communément visible) du MediaBox et du DropBox. L'image ci-dessous illustre ces propriétés.
Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Le snippet ci-dessous montre comment rogner la page :

```csharp
public static void CropPagesPDF()
{
    var pdfDocument1 = new Aspose.Pdf.Document("crop_page.pdf");
    Console.WriteLine(pdfDocument1.Pages[1].CropBox);
    Console.WriteLine(pdfDocument1.Pages[1].TrimBox);
    Console.WriteLine(pdfDocument1.Pages[1].ArtBox);
    Console.WriteLine(pdfDocument1.Pages[1].BleedBox);
    Console.WriteLine(pdfDocument1.Pages[1].MediaBox);

    // Créer un nouveau Rectangle de Boîte
    var newBox = new Rectangle(200, 220, 2170, 1520);
    pdfDocument1.Pages[1].CropBox = newBox;
    pdfDocument1.Pages[1].TrimBox = newBox;
    pdfDocument1.Pages[1].ArtBox = newBox;
    pdfDocument1.Pages[1].BleedBox = newBox;
   
    pdfDocument1.Save("crop_page_modified.pdf");           
}
```
Dans cet exemple, nous avons utilisé un fichier exemple [ici](crop_page.pdf). Initialement, notre page ressemble à celle montrée sur la Figure 1.
![Figure 1. Page Croppée](crop_page.png)

Après le changement, la page ressemblera à la Figure 2.
![Figure 2. Page Croppée](crop_page2.png)

