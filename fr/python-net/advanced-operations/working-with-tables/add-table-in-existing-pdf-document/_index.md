---
title: Créer ou Ajouter une Table dans un PDF en utilisant Python 
linktitle: Créer ou Ajouter une Table
type: docs
weight: 10
url: fr/python-net/add-table-in-existing-pdf-document/
description: Aspose.PDF pour Python via .NET est une bibliothèque utilisée pour créer, lire et éditer des Tables PDF. Consultez d'autres fonctions avancées dans ce sujet.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Créer ou Ajouter une Table dans un PDF en utilisant Python ",
    "alternativeHeadline": "Comment ajouter une Table dans un PDF avec Python via .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, créer une table dans un pdf, ajouter une table",
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
    "url": "/python-net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF pour Python via .NET est une bibliothèque utilisée pour créer, lire et éditer des Tables PDF. Consultez d'autres fonctions avancées dans ce sujet."
}
</script>


## Création de Table avec Python

Les tables sont importantes lors du travail avec des documents PDF. Elles offrent d'excellentes fonctionnalités pour afficher des informations de manière systématique. L'espace de noms Aspose.PDF contient des classes nommées [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/), et [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) qui fournissent des fonctionnalités pour créer des tables lors de la génération de documents PDF à partir de zéro.

Une table peut être créée en créant un objet de la classe Table.

```python

    table = ap.Table()
```

### Ajout de Table dans un Document PDF Existant

Pour ajouter une table à un fichier PDF existant avec Aspose.PDF pour Python via .NET, suivez les étapes suivantes :

1. Chargez le fichier source.
1. Initialisez une table et définissez ses colonnes et lignes.
1. Définissez les paramètres de la table (nous avons défini les bordures).
1. Remplissez la table.
1. Ajoutez la table à une page.
1. Enregistrez le fichier.

Les extraits de code suivants montrent comment ajouter du texte dans un fichier PDF existant.

```python

    import aspose.pdf as ap

    # Charger le document PDF source
    doc = ap.Document(input_file)
    # Initialise une nouvelle instance du Tableau
    table = ap.Table()
    # Définir la couleur de la bordure du tableau comme LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Définir la bordure pour les cellules du tableau
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Créer une boucle pour ajouter 10 lignes
    for row_count in range(0, 10):
        # Ajouter une ligne au tableau
        row = table.rows.add()
        # Ajouter des cellules au tableau
        row.cells.add("Colonne (" + str(row_count) + ", 1)")
        row.cells.add("Colonne (" + str(row_count) + ", 2)")
        row.cells.add("Colonne (" + str(row_count) + ", 3)")
    # Ajouter l'objet tableau à la première page du document d'entrée
    doc.pages[1].paragraphs.add(table)
    # Enregistrer le document mis à jour contenant l'objet tableau
    doc.save(output_file)
```

### ColSpan et RowSpan dans les Tables

Aspose.PDF pour Python via .NET fournit la propriété [col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) pour fusionner les colonnes dans un tableau et la propriété [row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) pour fusionner les lignes.


Nous utilisons la propriété `col_span` ou `row_span` sur l'objet `Cell` qui crée la cellule de tableau. Après avoir appliqué les propriétés requises, la cellule créée peut être ajoutée au tableau.

```python

    import aspose.pdf as ap

    # Initialisez l'objet Document en appelant son constructeur vide
    pdf_document = ap.Document()
    pdf_document.pages.add()
    # Initialise une nouvelle instance de Table
    table = ap.Table()
    # Définissez la couleur de la bordure du tableau comme LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Définissez la bordure pour les cellules du tableau
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Ajoutez la 1ère ligne au tableau
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Ajoutez des cellules au tableau
        row1.cells.add("Test 1" + str(cellCount))

    # Ajoutez la 2ème ligne au tableau
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Ajoutez la 3ème ligne au tableau
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Ajoutez la 4ème ligne au tableau
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Ajoutez la 5ème ligne au tableau
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Ajoutez l'objet tableau à la première page du document d'entrée
    pdf_document.pages[1].paragraphs.add(table)
    # Enregistrez le document mis à jour contenant l'objet tableau
    pdf_document.save(output_file)
```


Le résultat de l'exécution du code ci-dessous est le tableau représenté sur l'image suivante :

![Démonstration de ColSpan et RowSpan](colspan_rowspan.png)

## Travailler avec les Bordures, Marges et Espacement

Veuillez noter qu'il prend également en charge la fonctionnalité de définir le style de bordure, les marges et l'espacement des cellules pour les tableaux. Avant d'entrer dans les détails techniques, il est important de comprendre les concepts de bordure, marges et espacement qui sont présentés ci-dessous dans un diagramme :

![Bordures, marges et espacement](set-border-style-margins-and-padding-of-table_1.png)

Dans la figure ci-dessus, vous pouvez voir que les bordures du tableau, de la ligne et de la cellule se chevauchent. En utilisant Aspose.PDF, un tableau peut avoir des marges et les cellules peuvent avoir des espacements. Pour définir les marges des cellules, nous devons définir l'espacement des cellules.

### Bordures

Pour définir les bordures des objets Table, [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) et [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/), utilisez les propriétés Table.border, Row.border et Cell.border.
 Les bordures des cellules peuvent également être définies à l'aide de la propriété [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) de la classe [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) ou Row. Toutes les propriétés liées aux bordures discutées ci-dessus sont assignées à une instance de la classe Row, qui est créée en appelant son constructeur. La classe Row possède de nombreuses surcharges qui prennent presque tous les paramètres nécessaires pour personnaliser la bordure.

### Marges ou Espacement

L'espacement des cellules peut être géré à l'aide de la propriété [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/#properties) de la classe Table. Toutes les propriétés liées à l'espacement sont assignées à une instance de la classe [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) qui prend des informations sur les paramètres `left`, `right`, `top` et `bottom` pour créer des marges personnalisées.
Dans l'exemple suivant, la largeur de la bordure de la cellule est définie à 0,1 point, la largeur de la bordure de la table est définie à 1 point et le remplissage de la cellule est défini à 5 points.

![Marge et Bordure dans un Tableau PDF](margin-border.png)

```python

    import aspose.pdf as ap

    # Instancier l'objet Document en appelant son constructeur vide
    doc = ap.Document()
    page = doc.pages.add()
    # Instancier un objet table
    tab1 = ap.Table()
    # Ajouter la table dans la collection de paragraphes de la section désirée
    page.paragraphs.add(tab1)
    # Définir les largeurs de colonne de la table
    tab1.column_widths = "50 50 50"
    # Définir la bordure de cellule par défaut en utilisant l'objet BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Définir la bordure de la table en utilisant un autre objet BorderInfo personnalisé
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Créer un objet MarginInfo et définir ses marges gauche, bas, droite et haut
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Définir le remplissage de cellule par défaut sur l'objet MarginInfo
    tab1.default_cell_padding = margin
    # Créer des lignes dans la table puis des cellules dans les lignes
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    my_text = ap.text.TextFragment("col3 avec une longue chaîne de texte")
    # Row1.Cells.Add("col3 avec une longue chaîne de texte à placer dans la cellule")
    row1.cells[2].paragraphs.add(my_text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Enregistrer le Pdf
    doc.save(output_file)
```


Pour créer une table avec des coins arrondis, utilisez la valeur [rounded_border_radius](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/#properties) de la classe [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) et définissez le style des coins de la table comme arrondi.

```python
    
    import aspose.pdf as ap
    
    tab1 = ap.Table()
    graph = ap.GraphInfo()
    graph.color = ap.Color.red
    # Créer un objet BorderInfo vide
    b_info = ap.BorderInfo(ap.BorderSide.ALL, graph)
    # Définir la bordure comme une bordure arrondie où le rayon est de 15
    b_info.rounded_border_radius = 15
    # Définir le style des coins de la table comme arrondi
    tab1.corner_style = ap.BorderCornerStyle.ROUND
    # Définir les informations de bordure de la table
    tab1.border = b_info
```

## Appliquer différents réglages AutoFit à une table

Lors de la conception d'une table à l'aide d'un outil visuel comme Microsoft Word, vous utiliserez fréquemment l'une des fonctionnalités AutoFit pour ajuster commodément la taille de la table à la largeur souhaitée.
 Par exemple, vous pouvez utiliser l'option "AUTO_FIT_TO_WINDOW" pour adapter la largeur du tableau à la page ou AUTO_FIT_TO_CONTENT. Par défaut, lors de l'utilisation d'Aspose.Pdf pour créer un nouveau tableau, il utilise le [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) avec une valeur "Customized". Dans l'extrait de code suivant, nous définissons les paramètres de l'objet [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) et les objets [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) dans le tableau. Testez l'exemple et évaluez le résultat.

```python

    import aspose.pdf as ap

    # Instancier l'objet Pdf en appelant son constructeur vide
    doc = ap.Document()
    # Créer la section dans l'objet Pdf
    sec1 = doc.pages.add()
    # Instancier un objet table
    tab1 = ap.Table()
    # Ajouter le tableau dans la collection de paragraphes de la section souhaitée
    sec1.paragraphs.add(tab1)
    # Définir les largeurs de colonne du tableau
    tab1.column_widths = "50 50 50"
    tab1.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
    # Définir la bordure de cellule par défaut à l'aide de l'objet BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Définir la bordure du tableau à l'aide d'un autre objet BorderInfo personnalisé
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Créer un objet MarginInfo et définir ses marges gauche, bas, droite et haut
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Définir le remplissage de cellule par défaut sur l'objet MarginInfo
    tab1.default_cell_padding = margin
    # Créer des lignes dans le tableau puis des cellules dans les lignes
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Enregistrer le document mis à jour contenant l'objet table
    doc.save(output_file)
```

### Obtenir la Largeur de la Table

Parfois, il est nécessaire d'obtenir la largeur de la table dynamiquement. La classe Aspose.PDF.Table possède une méthode [get_width()](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#methods) à cet effet. Par exemple, vous n'avez pas défini explicitement la largeur des colonnes de la table et vous avez défini [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) sur 'AUTO_FIT_TO_CONTENT'. Dans ce cas, vous pouvez obtenir la largeur de la table comme suit.

```python

    import aspose.pdf as ap

    # Créer un nouveau document
    doc = ap.Document()
    # Ajouter une page dans le document
    page = doc.pages.add()
    # Initialiser une nouvelle table
    table = ap.Table()
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Ajouter une ligne dans la table
    row = table.rows.add()
    # Ajouter une cellule dans la table
    cell = row.cells.add("Texte de la cellule 1")
    cell = row.cells.add("Texte de la cellule 2")
    # Obtenir la largeur de la table
    print(table.get_width())
```

## Ajouter une Image SVG à une Cellule de Table

Aspose.PDF pour Python via .NET offre la possibilité d'insérer des cellules de tableau dans un fichier PDF.
 Lors de la construction d'un tableau, vous pouvez inclure à la fois du texte et des images dans ces cellules. De plus, l'API offre la fonctionnalité de transformer des fichiers SVG en format PDF. En utilisant ces fonctionnalités ensemble, vous pouvez charger une image SVG et la placer dans une cellule de tableau.

L'extrait de code suivant démontre le processus de création d'un objet de tableau et d'intégration d'une image SVG à l'intérieur de l'une de ses cellules.

```python

    import aspose.pdf as ap

    # Instancier un objet Document
    doc = ap.Document()
    # Créer une instance d'image
    img = ap.Image()
    # Définir le type d'image comme SVG
    img.file_type = ap.ImageFileType.SVG
    # Chemin pour le fichier source
    img.file = DIR_INPUT_TABLE + "SVGToPDF.svg"
    # Définir la largeur pour l'instance d'image
    img.fix_width = 50
    # Définir la hauteur pour l'instance d'image
    img.fix_height = 50
    # Créer une instance de table
    table = ap.Table()
    # Définir la largeur pour les cellules du tableau
    table.column_widths = "100 100"
    # Créer un objet ligne et l'ajouter à l'instance de tableau
    row = table.rows.add()
    # Créer un objet cellule et l'ajouter à l'instance de ligne
    cell = row.cells.add()
    # Ajouter un texte à la collection de paragraphes de l'objet cellule
    cell.paragraphs.add(ap.text.TextFragment("Première cellule"))
    # Ajouter une autre cellule à l'objet ligne
    cell = row.cells.add()
    # Ajouter l'image SVG à la collection de paragraphes de l'instance de cellule récemment ajoutée
    cell.paragraphs.add(img)
    # Créer un objet page et l'ajouter à la collection de pages de l'instance de document
    page = doc.pages.add()
    # Ajouter le tableau à la collection de paragraphes de l'objet page
    page.paragraphs.add(table)
    # Enregistrer le fichier PDF
    doc.save(output_file)
```

## Insérer un saut de page entre les lignes du tableau

Par défaut, lorsque vous créez un tableau dans un fichier PDF, le tableau s'étend sur plusieurs pages s'il dépasse la marge inférieure du tableau. Cependant, il existe des situations où nous devons imposer des sauts de page après qu'un certain nombre de lignes ont été ajoutées au tableau. L'extrait de code suivant décrit le processus d'insertion d'un saut de page lorsque 10 lignes ont été incluses dans le tableau.

```python

    import aspose.pdf as ap

    # Instancier une instance de Document
    doc = ap.Document()
    # Ajouter une page à la collection de pages du fichier PDF
    doc.pages.add()
    # Créer une instance de tableau
    tab = ap.Table()
    # Définir le style de bordure pour le tableau
    tab.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Définir le style de bordure par défaut pour le tableau avec la couleur de bordure rouge
    tab.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Spécifier la largeur des colonnes du tableau
    tab.column_widths = "100 100"
    # Créer une boucle pour ajouter 200 lignes au tableau
    for counter in range(0, 201):
        row = ap.Row()
        tab.rows.add(row)
        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment("Cellule " + str(counter) + ", 0"))
        row.cells.add(cell1)
        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment("Cellule " + str(counter) + ", 1"))
        row.cells.add(cell2)
        # Lorsque 10 lignes sont ajoutées, rendre la nouvelle ligne sur une nouvelle page
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True
    # Ajouter le tableau à la collection de paragraphes du fichier PDF
    doc.pages[1].paragraphs.add(tab)
    # Enregistrer le document PDF
    doc.save(output_file)
```


## Rendre un Tableau sur une Nouvelle Page

Par défaut, les paragraphes sont ajoutés à la collection Paragraphs d'un objet Page. Cependant, il est possible de rendre un tableau sur une nouvelle page au lieu de directement après l'objet de niveau paragraphe précédemment ajouté sur la page.

### Exemple : Comment Rendre un Tableau sur une Nouvelle Page en utilisant Python

Pour rendre un tableau sur une nouvelle page, utilisez la propriété [is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) dans la classe [BaseParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/baseparagraph/). Le code suivant montre comment faire.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    page_info = doc.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37

    page_info.is_landscape = True

    table = ap.Table()
    table.column_widths = "50 100"
    # Page ajoutée.
    cur_page = doc.pages.add()
    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Contenu 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("HHHHH"))
    paragraphs = cur_page.paragraphs
    paragraphs.add(table)

    table1 = ap.Table()
    table1.column_widths = "100 100"
    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("LAAAAAAA"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("LAAGGGGGG"))
    table1.is_in_new_page = True
    # Je veux garder le tableau 1 à la page suivante s'il vous plaît...
    paragraphs.add(table1)
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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