---
title: Manipuler les tables dans un PDF existant
linktitle: Manipuler les tables
type: docs
weight: 40
url: /python-net/manipulate-tables-in-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipuler les tables dans un PDF existant",
    "alternativeHeadline": "Comment mettre à jour le contenu des tables dans un PDF existant",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, python, manipuler tables",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe Doc Aspose.PDF",
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
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


## Manipuler des tables dans un PDF existant

L'une des premières fonctionnalités prises en charge par Aspose.PDF pour Python via .NET est sa capacité à Travailler avec des Tables et il offre un excellent support pour l'ajout de tables dans des fichiers PDF générés à partir de zéro ou dans tout fichier PDF existant. Dans cette nouvelle version, nous avons implémenté une nouvelle fonctionnalité de recherche et d'analyse de tables simples qui existent déjà sur la page d'un document PDF. Une nouvelle classe nommée [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) fournit ces capacités. L'utilisation de TableAbsorber est très similaire à la classe existante [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/). Le code suivant montre les étapes pour mettre à jour le contenu dans une cellule de table particulière.

```python

    import aspose.pdf as ap

    # Charger un fichier PDF existant
    pdf_document = ap.Document(input_file)
    # Créer un objet TableAbsorber pour trouver des tables
    absorber = ap.text.TableAbsorber()
    # Visiter la première page avec l'absorbeur
    absorber.visit(pdf_document.pages[1])
    # Accéder à la première table sur la page, à leur première cellule et aux fragments de texte qu'elle contient
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # Changer le texte du premier fragment de texte dans la cellule
    fragment.text = "bonjour le monde"
    pdf_document.save(output_file)
```


## Remplacer l'ancienne table par une nouvelle dans le document PDF

Dans le cas où vous devez trouver une table particulière et la remplacer par celle souhaitée, vous pouvez utiliser la méthode [replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) de la classe [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) pour le faire. L'exemple suivant démontre la fonctionnalité pour remplacer la table à l'intérieur du document PDF :

```python

    import aspose.pdf as ap

    # Charger un document PDF existant
    pdf_document = ap.Document(input_file)
    # Créer un objet TableAbsorber pour trouver les tables
    absorber = ap.text.TableAbsorber()
    # Visiter la première page avec l'absorbeur
    absorber.visit(pdf_document.pages[1])
    # Obtenir la première table sur la page
    table = absorber.table_list[0]
    # Créer une nouvelle table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")

    # Remplacer la table par la nouvelle
    absorber.replace(pdf_document.pages[1], table, new_table)
    # Enregistrer le document
    pdf_document.save(output_file)
```


## Comment déterminer si une table va casser dans la page actuelle

Ce code génère un document PDF contenant une table, calcule l'espace disponible sur la page et vérifie si l'ajout de plus de lignes à la table entraînera un saut de page en fonction des contraintes d'espace. Le résultat est enregistré dans un fichier de sortie.

```python

    import aspose.pdf as ap

    # Instancier un objet de la classe PDF
    pdf = ap.Document()
    # Ajouter la section à la collection de sections du document PDF
    page = pdf.pages.add()
    # Instancier un objet table
    table1 = ap.Table()
    table1.margin.top = 300
    # Ajouter la table dans la collection de paragraphes de la section souhaitée
    page.paragraphs.add(table1)
    # Définir les largeurs de colonne de la table
    table1.column_widths = "100 100 100"
    # Définir la bordure de cellule par défaut à l'aide de l'objet BorderInfo
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Définir la bordure de la table à l'aide d'un autre objet BorderInfo personnalisé
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Créer un objet MarginInfo et définir ses marges gauche, inférieure, droite et supérieure
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Définir le remplissage des cellules par défaut à l'objet MarginInfo
    table1.default_cell_padding = margin
    # Si vous augmentez le compteur à 17, la table se cassera
    # Parce qu'elle ne peut plus être accommodée sur cette page
    for row_counter in range(0, 17):
        # Créer des lignes dans la table et ensuite des cellules dans les lignes
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # Obtenir l'information de hauteur de la page
    page_height = pdf.page_info.height
    # Obtenir l'information de hauteur totale de la marge supérieure et inférieure de la page,
    # marge supérieure de la table et hauteur de la table.
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # Afficher la hauteur de la page, la hauteur de la table, la marge supérieure de la table et la marge supérieure
    # et inférieure de la page
    print("Hauteur du document PDF = " + str(pdf.page_info.height) + "\nInfo de la marge supérieure = " + str(page.page_info.margin.top)
          + "\nInfo de la marge inférieure = " + str(page.page_info.margin.bottom) + "\n\nInfo de la marge supérieure de la table = "
          + str(table1.margin.top) + "\nHauteur moyenne de la ligne = " + str(table1.rows[0].min_row_height) + " \nHauteur de la table "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\nHauteur totale de la page ="
          + str(page_height) + "\nHauteur cumulative incluant la table =" + str(total_objects_height))
    # Vérifier si nous déduisons la somme de la marge supérieure de la page + marge inférieure de la page
    # + marge supérieure de la table et hauteur de la table de la hauteur de la page et que c'est inférieur
    # à 10 (une ligne moyenne peut être supérieure à 10)
    if (page_height - total_objects_height) <= 10:
        # Si la valeur est inférieure à 10, alors afficher le message.
        # Ce qui montre qu'une autre ligne ne peut pas être placée et si nous ajoutons une nouvelle
        # ligne, la table se cassera. Cela dépend de la valeur de la hauteur de la ligne.
        print("Hauteur de la page - Hauteur des objets < 10, donc la table se cassera")
    # Enregistrer le document pdf
    pdf.save(output_file)
```


## Ajouter une colonne répétée dans le tableau

Dans la classe [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), vous pouvez définir un [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) qui répétera les lignes si le tableau est trop long verticalement et déborde sur la page suivante. Cependant, dans certains cas, les tableaux sont trop larges pour tenir sur une seule page et doivent être continués sur la page suivante. Afin de répondre à cet objectif, nous avons implémenté la propriété [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) dans la classe [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/). Définir cette propriété fera en sorte que le tableau se casse à la page suivante par colonne et répète le nombre de colonnes donné au début de la page suivante. Le code suivant montre l'utilisation de la propriété [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) :

```python

    import aspose.pdf as ap

    # Créer un nouveau document
    doc = ap.Document()
    page = doc.pages.add()
    # Instancier un tableau extérieur qui occupe toute la page
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Instancier un objet de table qui sera imbriqué à l'intérieur de outerTable qui se cassera à l'intérieur de la même page
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Ajouter le outerTable aux paragraphes de la page
    # Ajouter ma table à outerTable
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # Ajouter la ligne d'en-tête
    row = my_table.rows.add()
    row.cells.add("en-tête 1")
    row.cells.add("en-tête 2")
    row.cells.add("en-tête 3")
    row.cells.add("en-tête 4")
    row.cells.add("en-tête 5")
    row.cells.add("en-tête 6")
    row.cells.add("en-tête 7")
    row.cells.add("en-tête 11")
    row.cells.add("en-tête 12")
    row.cells.add("en-tête 13")
    row.cells.add("en-tête 14")
    row.cells.add("en-tête 15")
    row.cells.add("en-tête 16")
    row.cells.add("en-tête 17")
    for row_counter in range(0, 6):
        # Créer des lignes dans le tableau puis des cellules dans les lignes
        row1 = my_table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
    doc.save(output_file)
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour Python via .NET",
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