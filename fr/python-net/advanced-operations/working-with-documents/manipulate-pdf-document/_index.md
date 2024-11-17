---
title: Manipuler un document PDF en Python via .NET
linktitle: Manipuler un document PDF
type: docs
weight: 20
url: /fr/python-net/manipulate-pdf-document/
description: Cet article contient des informations sur la façon de valider un document PDF pour la norme PDF A en utilisant Python, comment travailler avec le TOC, comment définir une date d'expiration pour le PDF, etc.
lastmod: "2023-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipuler un document PDF via Python",
    "alternativeHeadline": "Comment manipuler un fichier PDF avec Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, dotnet, python, manipuler fichier pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
    "url": "/python-net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Cet article contient des informations sur la façon de valider un document PDF pour la norme PDF A en utilisant Python, comment travailler avec le TOC, comment définir une date d'expiration pour le PDF, etc."
}
</script>


## Manipuler un document PDF en Python

## Valider un document PDF pour la norme PDF A (A 1A et A 1B)

Pour valider un document PDF pour la compatibilité avec PDF/A-1a ou PDF/A-1b, utilisez la méthode [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Cette méthode vous permet de spécifier le nom du fichier dans lequel le résultat doit être enregistré et le type de validation requis de l'énumération PdfFormat : PDF_A_1A ou PDF_A_1B.

L'exemple de code suivant montre comment valider un document PDF pour PDF/A-1A.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Valider le PDF pour PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

L'exemple de code suivant montre comment valider un document PDF pour PDF/A-1b.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Valider le PDF pour PDF/A-1b
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```


## Travailler avec TOC

### Ajouter TOC à un PDF existant

TOC dans un PDF signifie "Table des matières". C'est une fonctionnalité qui permet aux utilisateurs de naviguer rapidement dans un document en fournissant une vue d'ensemble de ses sections et titres.

Pour ajouter une TOC à un fichier PDF existant, utilisez la classe Heading dans l'espace de noms [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). L'espace de noms [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) peut à la fois créer de nouveaux fichiers PDF et manipuler des fichiers PDF existants. Pour ajouter une TOC à un PDF existant, utilisez l'espace de noms Aspose.Pdf. L'extrait de code suivant montre comment créer une table des matières à l'intérieur d'un fichier PDF existant en utilisant Python via .NET.

```python

    import aspose.pdf as ap

    # Charger un fichier PDF existant
    doc = ap.Document(input_pdf)

    # Accéder à la première page du fichier PDF
    tocPage = doc.pages.insert(1)

    # Créer un objet pour représenter les informations du TOC
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table des matières")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Définir le titre pour le TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Créer des objets chaîne qui seront utilisés comme éléments du TOC
    titles = ["Première page", "Deuxième page", "Troisième page", "Quatrième page"]
    for i in range(0, 2):
        # Créer un objet Heading
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Spécifier la page de destination pour l'objet heading
        heading2.destination_page = doc.pages[i + 2]

        # Page de destination
        heading2.top = doc.pages[i + 2].rect.height

        # Coordonnée de destination
        segment2.text = titles[i]

        # Ajouter le heading à la page contenant le TOC
        tocPage.paragraphs.add(heading2)

    # Enregistrer le document mis à jour
    doc.save(output_pdf)
```


### Définir différents TabLeaderType pour différents niveaux de TOC

Aspose.PDF pour Python permet également de définir différents TabLeaderType pour différents niveaux de TOC. Vous devez définir la propriété [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # définir le LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table des Matières")
    title.text_state.font_size = 30
    toc_info.title = title

    # Ajouter la section de la liste à la collection de sections du document Pdf
    tocPage.toc_info = toc_info
    # Définir le format de la liste à quatre niveaux en définissant les marges de gauche
    # et
    # les paramètres de format de texte de chaque niveau

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Créer une section dans le document Pdf
    page = doc.pages.add()

    # Ajouter quatre titres dans la section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Titre Exemple" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Ajouter le titre dans la Table des Matières.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # enregistrer le Pdf
    doc.save(output_pdf)
```


### Masquer les numéros de page dans le sommaire

Dans le cas où vous ne souhaitez pas afficher les numéros de page avec les en-têtes dans le sommaire, vous pouvez utiliser la propriété [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de la classe [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) comme false. Veuillez consulter l'extrait de code suivant pour masquer les numéros de page dans le sommaire :

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table des Matières")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Ajouter la section de liste à la collection de sections du document Pdf
    toc_page.toc_info = toc_info
    # Définir le format de la liste à quatre niveaux en configurant les marges de gauche et
    # les paramètres de format de texte de chaque niveau

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Ajouter quatre en-têtes dans la section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "Ceci est l'en-tête du niveau " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```


### Personnaliser les numéros de page lors de l'ajout de la table des matières

Il est courant de personnaliser la numérotation des pages dans la table des matières lors de l'ajout de celle-ci dans un document PDF. Par exemple, nous pourrions avoir besoin d'ajouter un préfixe avant le numéro de page comme P1, P2, P3, etc. Dans ce cas, Aspose.PDF pour Python fournit la propriété [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de la classe [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) qui peut être utilisée pour personnaliser les numéros de page comme montré dans l'exemple de code suivant.

```python

    import aspose.pdf as ap

    # Charger un fichier PDF existant
    doc = ap.Document(input_pdf)
    # Accéder à la première page du fichier PDF
    toc_page = doc.pages.insert(1)
    # Créer un objet pour représenter les informations de la table des matières
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table des Matières")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Définir le titre pour la table des matières
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Créer un objet de titre
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Spécifier la page de destination pour l'objet de titre
        heading2.destination_page = doc.pages[i + 1]
        # Page de destination
        heading2.top = doc.pages[i + 1].rect.height
        # Coordonnée de destination
        segment2.text = "Page " + str(i)
        # Ajouter le titre à la page contenant la table des matières
        toc_page.paragraphs.add(heading2)

    # Enregistrer le document mis à jour
    doc.save(output_pdf)

```


## Comment définir la date d'expiration d'un PDF

Nous appliquons des privilèges d'accès sur les fichiers PDF afin qu'un certain groupe d'utilisateurs puisse accéder à des fonctionnalités/objets particuliers des documents PDF. Afin de restreindre l'accès au fichier PDF, nous appliquons généralement un cryptage et nous pouvons avoir besoin de définir l'expiration du fichier PDF, de sorte que l'utilisateur accédant/visualisant le document reçoive une invite valide concernant l'expiration du fichier PDF.

```python

    import aspose.pdf as ap

    # Instancier un objet Document
    doc = ap.Document()
    # Ajouter une page à la collection de pages du fichier PDF
    doc.pages.add()
    # Ajouter un fragment de texte à la collection de paragraphes de l'objet page
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Bonjour le monde..."))
    # Créer un objet JavaScript pour définir la date d'expiration du PDF
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('Le fichier est expiré. Vous avez besoin d'un nouveau.');"
    )
    # Définir JavaScript comme action d'ouverture du PDF
    doc.open_action = javaScript

    # Enregistrer le document PDF
    doc.save(output_pdf)
```


## Aplatir un PDF remplissable en Python

Les documents PDF incluent souvent des formulaires avec des widgets interactifs remplissables tels que des boutons radio, des cases à cocher, des zones de texte, des listes, etc. Pour le rendre non modifiable à des fins d'application variées, nous devons aplatir le fichier PDF. Aspose.PDF fournit la fonction pour aplatir votre PDF en Python avec seulement quelques lignes de code :

```python

    import aspose.pdf as ap

    # Charger le formulaire PDF source
    doc = ap.Document(input_pdf)

    # Aplatir le PDF remplissable
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Enregistrer le document mis à jour
    doc.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://releases.aspose.com/pdf/python-net",
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