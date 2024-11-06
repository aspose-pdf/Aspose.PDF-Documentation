---
title: Ajouter du texte au PDF avec Python
linktitle: Ajouter du texte au PDF
type: docs
weight: 10
url: fr/python-net/add-text-to-pdf-file/
description: Cet article décrit divers aspects du travail avec le texte dans Aspose.PDF. Apprenez à ajouter du texte au PDF, à ajouter des fragments HTML, ou à utiliser des polices OTF personnalisées.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter du texte au PDF avec Python",
    "alternativeHeadline": "Comment ajouter du texte au PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, ajouter du texte au pdf",
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
    "url": "/python-net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-02-04",
    "description": "Cet article décrit divers aspects du travail avec le texte dans Aspose.PDF pour Python. Apprenez à ajouter du texte au PDF, à ajouter des fragments HTML, ou à utiliser des polices OTF personnalisées."
}
</script>


## Ajout de Texte

1. Ouvrez le document PDF d'entrée à l'aide de Aspose.PDF.
1. Sélectionnez la page particulière à laquelle vous souhaitez ajouter le texte.
1. Créez un objet TextFragment. Un fragment de texte est créé avec le contenu 'texte principal'. Ce fragment est positionné aux coordonnées (100, 600) sur la page.
1. Définition des Propriétés du Texte. Diverses propriétés du texte sont définies, telles que la taille de la police, le type de police (Times New Roman), la couleur de fond (gris clair), et la couleur de premier plan (rouge).
1. Créez l'Objet TextBuilder. Un objet TextBuilder est instancié avec la page sélectionnée.
1. Ajoutez le Fragment de Texte. Le fragment de texte créé précédemment est ajouté à la page PDF en utilisant l'objet TextBuilder.
1. Appelez la méthode [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) et enregistrez le fichier PDF de sortie.

Le code suivant vous montre comment ajouter du texte dans un fichier PDF existant :

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Obtenir la page particulière
    page = document.pages[1]

    # Créer un fragment de texte
    text_fragment = ap.text.TextFragment("texte principal")
    text_fragment.position = ap.text.Position(100, 600)

    # Définir les propriétés du texte
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Créer un objet TextBuilder
    builder = ap.text.TextBuilder(page)

    # Ajouter le fragment de texte à la page PDF
    builder.append_text(text_fragment)

    # Enregistrer le document PDF résultant.
    document.save(output_pdf)             
```


## Chargement de la police à partir d'un flux

Le fragment de code suivant montre comment charger une police à partir d'un objet flux lors de l'ajout de texte à un document PDF.

```python

    import aspose.pdf as ap

    # Charger le fichier PDF d'entrée
    document = ap.Document()
    document.pages.add()
    # Créer un objet constructeur de texte pour la première page du document
    text_builder = ap.text.TextBuilder(document.pages[1])
    # Créer un fragment de texte avec une chaîne d'exemple
    text_fragment = ap.text.TextFragment("Hello world")

    if input_ttf != "":
        # Charger la police TrueType dans l'objet flux
        font_stream = open(input_ttf, "rb")
        # Définir le nom de la police pour la chaîne de texte
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # Spécifier la position pour le fragment de texte
        text_fragment.position = ap.text.Position(10, 10)
        # Ajouter le texte au TextBuilder afin qu'il puisse être placé sur le fichier PDF
        text_builder.append_text(text_fragment)
        # Enregistrer le document PDF résultant.
        document.save(output_pdf)
```


## Ajouter du texte en utilisant TextParagraph

Le code suivant vous montre comment ajouter du texte dans un document PDF en utilisant la classe [TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/).

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document()
    # Ajouter une page à la collection de pages de l'objet Document
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # Créer un paragraphe de texte
    paragraph = ap.text.TextParagraph()
    # Définir l'indentation des lignes suivantes
    paragraph.subsequent_lines_indent = 20
    # Spécifier l'emplacement pour ajouter TextParagraph
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # Spécifier le mode de retour à la ligne
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # Créer un fragment de texte
    fragment1 = ap.text.TextFragment("the quick brown fox jumps over the lazy dog")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # Ajouter le fragment au paragraphe
    paragraph.append_line(fragment1)
    # Ajouter le paragraphe
    builder.append_paragraph(paragraph)

    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```


## Ajouter un Hyperlien au TextSegment

Ce code démontre comment créer un contenu dynamique et interactif dans un document PDF, y compris des hyperliens vers des ressources externes.

Une page PDF peut comprendre un ou plusieurs objets TextFragment, où chaque objet TextFragment peut avoir une ou plusieurs instances de [TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/).

Veuillez essayer d'utiliser l'extrait de code suivant pour répondre à cette exigence :

```python

    import aspose.pdf as ap

    # Créer une instance de document
    document = ap.Document()
    # Ajouter une page à la collection de pages du fichier PDF
    page1 = document.pages.add()
    # Créer une instance de TextFragment
    tf = ap.text.TextFragment("Fragment de texte d'exemple")
    # Définir l'alignement horizontal pour TextFragment
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # Créer un textsegment avec un texte d'exemple
    segment = ap.text.TextSegment(" ... Segment de texte 1...")
    # Ajouter le segment à la collection de segments de TextFragment
    tf.segments.append(segment)
    # Créer un nouveau TextSegment
    segment = ap.text.TextSegment("Lien vers Google")
    # Ajouter le segment à la collection de segments de TextFragment
    tf.segments.append(segment)
    # Définir l'hyperlien pour TextSegment
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # Définir la couleur de premier plan pour le segment de texte
    segment.text_state.foreground_color = ap.Color.blue
    # Définir la mise en forme du texte en italique
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # Créer un autre objet TextSegment
    segment = ap.text.TextSegment("TextSegment sans hyperlien")
    # Ajouter le segment à la collection de segments de TextFragment
    tf.segments.append(segment)
    # Ajouter TextFragment à la collection de paragraphes de l'objet page
    page1.paragraphs.add(tf)
    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```


## Utiliser la police OTF

Aspose.PDF pour Python via .NET offre la fonctionnalité d'utiliser des polices personnalisées/TrueType lors de la création/manipulation des contenus de fichiers PDF afin que les contenus du fichier soient affichés en utilisant des polices autres que les polices système par défaut.

```python

    import aspose.pdf as ap

    # Créer une nouvelle instance de document
    document = ap.Document()
    # Ajouter une page à la collection de pages du fichier PDF
    page = document.pages.add()
    # Créer une instance de TextFragment avec un texte d'exemple
    fragment = ap.text.TextFragment("Texte d'exemple en police OTF")
    # Ou vous pouvez même spécifier le chemin de la police OTF dans le répertoire système
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # Spécifier pour intégrer la police à l'intérieur du fichier PDF, afin qu'elle soit affichée correctement,
    # Même si la police spécifique n'est pas installée/présente sur la machine cible
    fragment.text_state.font.is_embedded = True
    # Ajouter TextFragment à la collection de paragraphes de l'instance Page
    page.paragraphs.add(fragment)
    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```


## Ajouter une chaîne HTML en utilisant le DOM

Le code Python suivant utilise la bibliothèque Aspose.PDF pour créer un document PDF avec un fragment HTML.

1. Instancier Document. Une instance de la classe Document est créée, représentant le document PDF.
1. Ajouter une page au document PDF.
1. Instancier un objet HtmlFragment avec le contenu HTML.
1. Définir les marges pour le fragment HTML. Dans ce cas, la marge inférieure est fixée à 10 points et la marge supérieure à 200 points.
1. Ajouter le fragment HTML à la page.
1. Enregistrer le fichier PDF.

```python

    import aspose.pdf as ap

    # Instancier l'objet Document
    doc = ap.Document()
    # Ajouter une page à la collection de pages du fichier PDF
    page = doc.pages.add()
    # Instancier HtmlFragment avec le contenu HTML
    title = ap.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")
    # Définir l'information de marge inférieure
    title.margin.bottom = 10
    # Définir l'information de marge supérieure
    title.margin.top = 200
    # Ajouter le fragment HTML à la collection de paragraphes de la page
    page.paragraphs.add(title)
    # Enregistrer le fichier PDF
    doc.save(output_pdf)
```


### Style de ligne personnalisé pour FootNote

L'exemple suivant démontre comment ajouter des notes de bas de page en bas de la page PDF et définir un style de ligne personnalisé.

```python

    import aspose.pdf as ap

    # Créer une instance de Document
    doc = ap.Document()
    # Ajouter une page à la collection de pages du PDF
    page = doc.pages.add()
    # Créer un objet GraphInfo
    graph = ap.GraphInfo()
    # Définir la largeur de ligne à 2
    graph.line_width = 2
    # Définir la couleur pour l'objet graph
    graph.color = ap.Color.red
    # Définir la valeur du tableau de tirets à 3
    graph.dash_array = [3]
    # Définir la valeur de phase de tiret à 1
    graph.dash_phase = 1
    # Définir le style de ligne de note pour la page comme graph
    page.note_line_style = graph
    # Créer une instance de TextFragment
    text = ap.text.TextFragment("Hello World")
    # Définir la valeur de FootNote pour TextFragment
    text.foot_note = ap.Note("note de bas de page pour le texte de test 1")
    # Ajouter TextFragment à la collection de paragraphes de la première page du document
    page.paragraphs.add(text)
    # Créer le deuxième TextFragment
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # Définir FootNote pour le deuxième fragment de texte
    text.foot_note = ap.Note("note de bas de page pour le texte de test 2")
    # Ajouter le deuxième fragment de texte à la collection de paragraphes du fichier PDF
    page.paragraphs.add(text)
    # Enregistrer le document PDF résultant.
    doc.save(output_pdf)
```


### Personnaliser le libellé de la note de bas de page

Le code suivant montre comment créer un document PDF avec un fragment de texte contenant une note de bas de page.

Par défaut, le numéro de la note de bas de page est incrémentiel à partir de 1. Cependant, nous pouvons avoir besoin de définir un libellé personnalisé pour la note de bas de page. Pour répondre à cette exigence, veuillez essayer d'utiliser le code suivant

```python

    import aspose.pdf as ap

    # Créer une instance de Document
    document = ap.Document()
    # Ajouter une page à la collection de pages du PDF
    page = document.pages.add()
    # Créer un objet GraphInfo
    graph = ap.GraphInfo()
    # Définir la largeur de ligne à 2
    graph.line_width = 2
    # Définir la couleur de l'objet graphique
    graph.color = ap.Color.red
    # Définir la valeur du tableau de tirets à 3
    graph.dash_array = [3]
    # Définir la phase des tirets à 1
    graph.dash_phase = 1
    # Définir le style de ligne de note de bas de page pour la page comme graphique
    page.note_line_style = graph
    # Créer une instance de TextFragment
    text = ap.text.TextFragment("Hello World")
    # Définir la valeur de la note de bas de page pour TextFragment
    text.foot_note = ap.Note("note de bas de page pour le texte de test 1")
    # Spécifier un libellé personnalisé pour la note de bas de page
    text.foot_note.text = " Aspose"
    # Ajouter le TextFragment à la collection de paragraphes de la première page du document
    page.paragraphs.add(text)
    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```


## Ajout d'image et de tableau à la note de bas de page

Ce code démontre comment créer un document PDF avec un fragment de texte contenant une note de bas de page complexe qui inclut une image, du texte et un tableau en utilisant Aspose.PDF pour Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("du texte")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("texte de la note de bas de page")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Ligne 1 Cellule 1"))
    text.foot_note.paragraphs.add(table)

    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```

## Comment créer des notes de fin

Une note de fin est une citation de source qui renvoie les lecteurs à un endroit spécifique à la fin du document où ils peuvent trouver la source de l'information ou des mots cités ou mentionnés dans le document.
 Lorsque vous utilisez des notes de fin, votre phrase citée, paraphrasée ou le matériel résumé est suivi d'un numéro en exposant.

Ce code démontre comment ajouter un fragment de texte avec une note de fin à un document PDF en utilisant Aspose.PDF pour Python :

```python

    import aspose.pdf as ap

    # Créer une instance de Document
    document = ap.Document()
    # Ajouter une page à la collection de pages du PDF
    page = document.pages.add()
    # Créer une instance de TextFragment
    text = ap.text.TextFragment("Bonjour le monde")
    # Définir la valeur de la note de fin pour TextFragment
    text.end_note = ap.Note("exemple de note de fin")
    # Spécifier un libellé personnalisé pour la note de bas de page
    text.end_note.text = " Aspose"
    # Ajouter TextFragment à la collection de paragraphes de la première page du document
    page.paragraphs.add(text)
    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```

## Texte et Image en tant que Paragraphe EnLigne

La mise en page par défaut du fichier PDF est une mise en page de flux (de Haut-Gauche à Bas-Droit). Par conséquent, chaque nouvel élément ajouté au fichier PDF est ajouté dans le flux en bas à droite. Cependant, nous pouvons avoir besoin d'afficher divers éléments de page, c'est-à-dire une image et du texte au même niveau (l'un après l'autre). Une approche peut être de créer une instance de Table et d'ajouter les deux éléments à des objets de cellule individuels. Cependant, une autre approche peut être le paragraphe en ligne. En définissant la propriété IsInLineParagraph de l'image et du texte sur true, ces paragraphes apparaîtront en ligne avec d'autres éléments de page.

Le code suivant vous montre comment ajouter du texte et une image en tant que paragraphes en ligne dans un fichier PDF.

```python

    import aspose.pdf as ap

    # Instancier l'instance Document
    document = ap.Document()
    # Ajouter une page à la collection de pages de l'instance Document
    page = document.pages.add()
    # Créer un TextFragment
    text = ap.text.TextFragment("Bonjour le monde.. ")
    # Ajouter un fragment de texte à la collection de paragraphes de l'objet Page
    page.paragraphs.add(text)
    # Créer une instance d'image
    image = ap.Image()
    # Définir l'image en tant que paragraphe en ligne afin qu'elle apparaisse juste après
    # L'objet paragraphe précédent (TextFragment)
    image.is_in_line_paragraph = True
    # Spécifier le chemin du fichier image
    image.file = input_jpg
    # Définir la hauteur de l'image (optionnel)
    image.fix_height = 30
    # Définir la largeur de l'image (optionnel)
    image.fix_width = 100
    # Ajouter l'image à la collection de paragraphes de l'objet page
    page.paragraphs.add(image)
    # Réinitialiser l'objet TextFragment avec des contenus différents
    text = ap.text.TextFragment(" Bonjour encore..")
    # Définir TextFragment en tant que paragraphe en ligne
    text.is_in_line_paragraph = True
    # Ajouter le nouveau TextFragment créé à la collection de paragraphes de la page
    page.paragraphs.add(text)
    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```

## Spécifier l'espacement des caractères lors de l'ajout de texte

L'extrait de code suivant montre comment générer un document PDF contenant un fragment de texte avec un espacement des caractères accru.

Le texte peut être ajouté à l'intérieur d'une collection de paragraphes de fichiers PDF en utilisant l'instance TextFragment ou en utilisant l'objet TextParagraph et vous pouvez même tamponner le texte à l'intérieur du PDF en utilisant la classe TextStamp.

### Utilisation de TextBuilder et TextFragment

```python

    import aspose.pdf as ap

    # Créer une instance de Document
    document = ap.Document()
    # Ajouter une page à la collection de pages du document
    document.pages.add()
    # Créer une instance de TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Créer une instance de fragment de texte avec des contenus d'exemple
    wide_fragment = ap.text.TextFragment("Texte avec un espacement des caractères accru")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # Spécifier l'espacement des caractères pour TextFragment
    wide_fragment.text_state.character_spacing = 2.0
    # Spécifier la position de TextFragment
    wide_fragment.position = ap.text.Position(100, 650)
    # Ajouter le TextFragment à l'instance de TextBuilder
    builder.append_text(wide_fragment)
    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```


### Utilisation de TextParagraph

```python

    import aspose.pdf as ap

    # Créer une instance de Document
    document = ap.Document()
    # Ajouter une page à la collection de pages du Document
    document.pages.add()
    # Créer une instance de TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Instancier une instance de TextParagraph
    paragraph = ap.text.TextParagraph()
    # Créer une instance de TextState pour spécifier le nom et la taille de la police
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # Spécifier l'espacement des caractères
    state.character_spacing = 1.5
    # Ajouter du texte à l'objet TextParagraph
    tt = "Ceci est un paragraphe avec espacement des caractères"
    paragraph.append_line(tt, state)
    # Spécifier la position pour TextParagraph
    paragraph.position = ap.text.Position(100, 550)
    # Ajouter TextParagraph à l'instance de TextBuilder
    builder.append_paragraph(paragraph)
    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```

### Utilisation de TextStamp

```python

    import aspose.pdf as ap

    # Créer une instance de Document
    document = ap.Document()
    # Ajouter une page à la collection de pages du Document
    page = document.pages.add()
    # Instancier une instance de TextStamp avec du texte d'exemple
    stamp = ap.TextStamp("Ceci est un tampon texte avec espacement des caractères")
    # Spécifier le nom de la police pour l'objet Stamp
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # Spécifier la taille de la police pour TextStamp
    stamp.text_state.font_size = 12
    # Spécifier l'espacement des caractères à 1
    stamp.text_state.character_spacing = 1
    # Définir le x_indent pour Stamp
    stamp.x_indent = 100
    # Définir le y_indent pour Stamp
    stamp.y_indent = 500
    # Ajouter le tampon textuel à l'instance de page
    stamp.put(page)
    # Enregistrer le document PDF résultant.
    document.save(output_pdf)
```


## Créer un document PDF à colonnes multiples

[Aspose.PDF pour Python via .NET](https://docs.aspose.com/pdf/python-net/) offre également la fonctionnalité de créer plusieurs colonnes à l'intérieur des pages de documents PDF. Afin de créer un fichier PDF à colonnes multiples, nous pouvons utiliser la classe FloatingBox car elle fournit la propriété column_info pour spécifier le nombre de colonnes à l'intérieur de FloatingBox et nous pouvons également spécifier l'espacement entre les colonnes et les largeurs des colonnes en utilisant les propriétés column_spacing et width en conséquence.

L'espacement des colonnes signifie l'espace entre les colonnes et l'espacement par défaut entre les colonnes est de 1,25 cm. Si la largeur des colonnes n'est pas spécifiée, alors [Aspose.PDF pour Python via .NET](https://docs.aspose.com/pdf/python-net/) calcule automatiquement la largeur de chaque colonne en fonction de la taille de la page et de l'espacement entre les colonnes.

Un exemple est donné ci-dessous pour démontrer la création de deux colonnes avec des objets Graphs (Ligne) et ils sont ajoutés à la collection de paragraphes de FloatingBox, qui est ensuite ajoutée à la collection de paragraphes de l'instance Page.

```python

    import aspose.pdf as ap

    document = ap.Document()
    # Spécifiez les informations de marge gauche pour le fichier PDF
    document.page_info.margin.left = 40
    # Spécifiez les informations de marge droite pour le fichier PDF
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # Ajoutez la ligne à la collection de paragraphes de l'objet section
    page.paragraphs.add(graph1)

    # Spécifiez les coordonnées pour la ligne
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # Créez des variables de chaîne avec du texte contenant des balises HTML
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> Comment éviter les arnaques d'argent</<strong> "
        + "</font>"
    )
    # Créez des paragraphes de texte contenant du texte HTML
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # Ajoutez quatre colonnes dans la section
    box.column_info.column_count = 2
    # Réglez l'espacement entre les colonnes
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("Par A Googler (Le Blog Officiel de Google)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # Créez un objet graph pour dessiner une ligne
    graph2 = ap.drawing.Graph(50, 10)
    # Spécifiez les coordonnées pour la ligne
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # Ajoutez la ligne à la collection de paragraphes de l'objet section
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # Enregistrez le fichier PDF
    document.save(output_pdf)
```


## Travailler avec des tabulations personnalisées

Cet extrait de code Python montre comment créer un document PDF contenant des fragments de texte disposés à l'aide de tabulations pour simuler une structure de tableau.

Voici un exemple de comment définir des tabulations personnalisées.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "Ceci est un exemple de formation de table avec des tabulations", ts
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts)

    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts)
    text2 = ap.text.TextFragment("#$TABdata21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```


## Comment ajouter du texte transparent dans un PDF

Un fichier PDF contient des objets Image, Texte, Graphique, pièce jointe, Annotations et lors de la création d'un TextFragment, vous pouvez définir des informations sur la couleur de premier plan, d'arrière-plan ainsi que la mise en forme du texte. Aspose.PDF pour Python via .NET prend en charge la fonctionnalité d'ajouter du texte avec un canal de couleur Alpha.

Le code suivant montre comment ajouter du texte avec une couleur transparente.

```python

    import aspose.pdf as ap

    # Créer une instance de Document
    document = ap.Document()
    # Créer une page pour la collection de pages du fichier PDF
    page = document.pages.add()

    # Créer une instance de TextFragment avec une valeur d'exemple
    text = ap.text.TextFragment(
        "texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent "
    )
    # Créer un objet couleur à partir du canal Alpha
    color = ap.Color.from_argb(30, 0, 255, 0)
    # Définir les informations de couleur pour l'instance de texte
    text.text_state.foreground_color = color
    # Ajouter du texte à la collection de paragraphes de l'instance de page
    page.paragraphs.add(text)

    document.save(output_pdf)
```


## Spécifier l'espacement des lignes pour les polices

Chaque police a un carré abstrait, dont la hauteur est la distance prévue entre les lignes de texte de même taille. Ce carré est appelé le carré em et c'est la grille de conception sur laquelle les contours des glyphes sont définis. De nombreuses lettres de la police d'entrée ont des points qui sont placés en dehors des limites du carré em de la police, donc pour afficher correctement la police, l'utilisation d'un paramètre spécial est nécessaire.

Le prochain extrait de code charge un PDF, ajoute un fragment de texte avec un espacement de ligne spécifique en utilisant une police TrueType, et enregistre le document PDF modifié :

```python

    import aspose.pdf as ap

    # Charger le fichier PDF d'entrée
    document = ap.Document()
    # Créer TextFormattingOptions avec LineSpacingMode.FULL_SIZE
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # Créer un fragment de texte avec une chaîne d'exemple
    text_fragment = ap.text.TextFragment("Hello world")

    # Charger la police TrueType dans l'objet flux
    font_stream = open(input_ttf, "rb")
    # Définir le nom de la police pour la chaîne de texte
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # Spécifier la position pour le fragment de texte
    text_fragment.position = ap.text.Position(100, 600)
    # Définir TextFormattingOptions du fragment actuel sur prédéfini (qui pointe vers LineSpacingMode.FULL_SIZE)
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # Enregistrer le document PDF résultant
    document.save(output_pdf)
```


## Obtenez la largeur du texte dynamiquement

Ce bout de code Python effectue une comparaison entre les mesures de chaînes obtenues à partir d'un objet police et d'un objet état de texte dans Aspose.PDF :

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Mesure de chaîne de police inattendue!")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Mesure de chaîne de police inattendue!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("La mesure de chaîne de police et d'état ne correspond pas!")

        c_code += 1
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>