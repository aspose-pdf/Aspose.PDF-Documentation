---
title: Obtenir et Définir les Propriétés des Pages avec Python
linktitle: Obtenir et Définir les Propriétés des Pages
type: docs
weight: 90
url: /python-net/get-and-set-page-properties/
description: Cette section montre comment obtenir le nombre de pages dans un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés des pages.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obtenir et Définir les Propriétés des Pages avec Python",
    "alternativeHeadline": "Obtenez et Définissez les Propriétés des Pages PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, obtenir propriétés des pages, définir propriétés des pages",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-and-set-page-properties/"
    },
    "dateModified": "2023-04-04",
    "description": ""
}
</script>


Aspose.PDF pour Python via .NET vous permet de lire et de définir les propriétés des pages dans un fichier PDF dans vos applications Python. Cette section montre comment obtenir le nombre de pages dans un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés des pages. Les exemples donnés sont en Python.

## Obtenir le Nombre de Pages dans un Fichier PDF

Lorsque vous travaillez avec des documents, vous souhaitez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF, cela ne prend pas plus de deux lignes de code.

Pour obtenir le nombre de pages dans un fichier PDF :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Utilisez ensuite la propriété Count de la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (à partir de l'objet Document) pour obtenir le nombre total de pages dans le document.

L'extrait de code suivant montre comment obtenir le nombre de pages d'un fichier PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Obtenir le nombre de pages
    print("Nombre de pages :", str(len(document.pages)))
```


### Obtenez le nombre de pages sans enregistrer le document

Parfois, nous générons des fichiers PDF à la volée et, lors de la création d'un fichier PDF, nous pouvons rencontrer le besoin (création de table des matières, etc.) d'obtenir le nombre de pages d'un fichier PDF sans enregistrer le fichier sur le système ou le flux. Donc, afin de répondre à ce besoin, une méthode [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) a été introduite dans la classe Document. Veuillez consulter l'extrait de code suivant qui montre les étapes pour obtenir le nombre de pages sans enregistrer le document.

```python

    import aspose.pdf as ap

    # Instancier une instance de Document
    document = ap.Document()
    # Ajouter une page à la collection de pages du fichier PDF
    page = document.pages.add()
    # Créer une instance de boucle
    for i in range(0, 300):
        # Ajouter TextFragment à la collection de paragraphes de l'objet page
        page.paragraphs.add(ap.text.TextFragment("Test de comptage de pages"))
    # Traiter les paragraphes dans le fichier PDF pour obtenir un nombre de pages précis
    document.process_paragraphs()
    # Imprimer le nombre de pages dans le document
    print("Nombre de pages dans le document =", str(len(document.pages)))
```


## Obtenir les Propriétés de la Page

Chaque page dans un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, la boîte de fond perdu, de rognage et de découpe. Aspose.PDF vous permet d'accéder à ces propriétés.

### **Comprendre les Propriétés de la Page: la Différence entre Artbox, BleedBox, CropBox, MediaBox, TrimBox et la Propriété Rect**

- **Boîte des médias**: La boîte des médias est la plus grande boîte de la page. Elle correspond à la taille de la page (par exemple A4, A5, Lettre US, etc.) sélectionnée lorsque le document a été imprimé au format PostScript ou PDF. En d'autres termes, la boîte des médias détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Boîte de fond perdu**: Si le document a du fond perdu, le PDF aura également une boîte de fond perdu.
 Bleed est la quantité de couleur (ou d'œuvre) qui s'étend au-delà du bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et coupé à la taille ("coupé"), l'encre ira jusqu'au bord de la page. Même si la page est mal coupée - légèrement décalée par rapport aux marques de coupe - aucun bord blanc n'apparaîtra sur la page.
- **Trim box**: La boîte de coupe indique la taille finale d'un document après impression et découpe.
- **Art box**: La boîte d'art est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Crop box**: La boîte de découpe est la taille "page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seuls les contenus de la boîte de découpe sont affichés dans Adobe Acrobat.
  Pour des descriptions détaillées de ces propriétés, lisez la spécification Adobe.Pdf, en particulier 10.10.1 Page Boundaries.
- **Page.Rect**: l'intersection (rectangle généralement visible) du MediaBox et du DropBox. La figure ci-dessous illustre ces propriétés.

Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Accéder aux propriétés de la page**

La classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) fournit toutes les propriétés liées à une page PDF particulière. Toutes les pages des fichiers PDF sont contenues dans la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

À partir de là, il est possible d'accéder à des objets Page individuels en utilisant leur index, ou de parcourir la collection en utilisant une boucle foreach pour obtenir toutes les pages. Une fois qu'une page individuelle est accédée, nous pouvons obtenir ses propriétés. Le snippet de code suivant montre comment obtenir les propriétés de la page.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Obtenir une page particulière
    page = document.pages[1]
    # Obtenir les propriétés de la page
    print(
        "ArtBox : Hauteur={},Largeur={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : Hauteur={},Largeur={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : Hauteur={},Largeur={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : Hauteur={},Largeur={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : Hauteur={},Largeur={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : Hauteur={},Largeur={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("Numéro de page :", page.number)
    print("Rotation :", page.rotate)
```

## Obtenir une Page Particulière du Fichier PDF

Aspose.PDF pour Python vous permet de [diviser un PDF en pages individuelles](/pdf/python-net/split-pdf-document/) et de les enregistrer sous forme de fichiers PDF. Obtenir une page spécifiée dans un fichier PDF et l'enregistrer en tant que nouveau PDF est une opération très similaire : ouvrez le document source, accédez à la page, créez un nouveau document et ajoutez la page à celui-ci.

L'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) de [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection) contient les pages du fichier PDF. Pour obtenir une page particulière de cette collection :

1. Spécifiez l'index de la page en utilisant la propriété Pages.
2. Créez un nouvel objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Ajoutez l'objet [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) au nouvel objet Document.
4. Enregistrez la sortie en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Le fragment de code suivant montre comment obtenir une page particulière d'un fichier PDF et l'enregistrer en tant que nouveau fichier.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Obtenir une page particulière
    page = document.pages[2]

    # Enregistrer la page en tant que fichier PDF
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## Déterminer la couleur de la page

La classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) fournit les propriétés relatives à une page particulière dans un document PDF, y compris le type de couleur - RGB, noir et blanc, niveaux de gris ou indéfinie - utilisé par la page.

Toutes les pages des fichiers PDF sont contenues dans la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
 Le [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) propriété spécifie la couleur des éléments sur la page. Pour obtenir ou déterminer l'information de couleur pour une page PDF particulière, utilisez la propriété [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de l'objet [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

Le code ci-dessous montre comment parcourir chaque page d'un fichier PDF pour obtenir l'information de couleur.

```python

    import aspose.pdf as ap

    # Ouvrir le fichier PDF source
    document = ap.Document(input_pdf)
    # Parcourir toutes les pages du fichier PDF
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # Obtenir l'information du type de couleur pour une page PDF particulière
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("Page # " + str(page_number) + " est en Noir et blanc.")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("Page # " + str(page_number) + " est en Échelle de gris.")

        if page_color_type == ap.ColorType.RGB:
            print("Page # " + str(page_number) + " est en RGB.")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("Page # " + str(page_number) + " La couleur est indéfinie.")
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Bibliothèque de manipulation PDF pour Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>