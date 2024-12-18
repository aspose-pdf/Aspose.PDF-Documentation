---
title: Formatage du document PDF en utilisant Python
linktitle: Formatage du document PDF
type: docs
weight: 11
url: /fr/python-net/formatting-pdf-document/
description: Créer et formater le document PDF avec Aspose.PDF pour Python via .NET. Utilisez le prochain extrait de code pour résoudre vos tâches.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatage du document PDF en utilisant Python",
    "alternativeHeadline": "Comment formater un document PDF en Python via .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, dotnet, python, formater document pdf",
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
                "contactType": "vente",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vente",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vente",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/formatting-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Créer et formater le document PDF avec Aspose.PDF pour Python via .NET. Utilisez le prochain extrait de code pour résoudre vos tâches."
}
</script>


## Mise en Forme du Document PDF

### Obtenir les Propriétés de la Fenêtre du Document et de l'Affichage des Pages

Ce sujet vous aide à comprendre comment obtenir les propriétés de la fenêtre du document, de l'application de visualisation, et comment les pages sont affichées. Pour définir ces propriétés :

Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Maintenant, vous pouvez définir les propriétés de l'objet Document, telles que

- CenterWindow – Centre la fenêtre du document sur l'écran. Par défaut : faux.
- Direction – Ordre de lecture. Cela détermine comment les pages sont disposées lorsqu'elles sont affichées côte à côte. Par défaut : de gauche à droite.
- DisplayDocTitle – Affiche le titre du document dans la barre de titre de la fenêtre du document. Par défaut : faux (le titre est affiché).
- HideMenuBar – Masquer ou afficher la barre de menu de la fenêtre du document. Par défaut : faux (la barre de menu est affichée).
- HideToolBar – Masquer ou afficher la barre d'outils de la fenêtre du document. Par défaut : faux (la barre d'outils est affichée).
- HideWindowUI – Masquer ou afficher des éléments de la fenêtre du document comme les barres de défilement.
 Default: false (Les éléments de l'interface utilisateur sont affichés).
- NonFullScreenPageMode – Comment le document est affiché lorsqu'il n'est pas en mode plein écran.
- PageLayout – La mise en page.
- PageMode – Comment le document est affiché lorsqu'il est ouvert pour la première fois. Les options sont afficher les miniatures, plein écran, afficher le panneau des pièces jointes.

Le fragment de code suivant vous montre comment obtenir les propriétés à l'aide de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Obtenir différentes propriétés du document
    # Position de la fenêtre du document - Par défaut : faux
    print("CenterWindow :", document.center_window)

    # Ordre de lecture prédominant ; détermine la position de la page
    # Lorsqu'elle est affichée côte à côte - Par défaut : L2R
    print("Direction :", document.direction)

    # Si la barre de titre de la fenêtre doit afficher le titre du document
    # Si faux, la barre de titre affiche le nom du fichier PDF - Par défaut : faux
    print("DisplayDocTitle :", document.display_doc_title)

    # Si la fenêtre du document doit être redimensionnée pour s'adapter à la taille de
    # La première page affichée - Par défaut : faux
    print("FitWindow :", document.fit_window)

    # Si la barre de menu de l'application de visualisation doit être cachée - Par défaut : faux
    print("HideMenuBar :", document.hide_menubar)

    # Si la barre d'outils de l'application de visualisation doit être cachée - Par défaut : faux
    print("HideToolBar :", document.hide_tool_bar)

    # Si des éléments de l'interface utilisateur tels que les barres de défilement doivent être cachés
    # Et ne laissant que le contenu de la page affiché - Par défaut : faux
    print("HideWindowUI :", document.hide_window_ui)

    # Mode de page du document. Comment afficher le document lors de la sortie du mode plein écran.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # La mise en page c'est-à-dire une seule page, une colonne
    print("PageLayout :", document.page_layout)

    # Comment le document doit s'afficher lorsqu'il est ouvert
    # C'est-à-dire afficher les miniatures, plein écran, afficher le panneau des pièces jointes
    print("pageMode :", document.page_mode)

```

### Définir les propriétés de la fenêtre du document et de l'affichage de la page

Ce sujet explique comment définir les propriétés de la fenêtre du document, de l'application de visualisation et de l'affichage de la page. Pour définir ces différentes propriétés :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Définissez les propriétés de l'objet Document.
3. Enregistrez le fichier PDF mis à jour en utilisant la méthode save.

Les propriétés disponibles sont :

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Chacune est utilisée et décrite dans le code ci-dessous. Le code suivant vous montre comment définir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Définir différentes propriétés du document
    # Spécifier pour positionner la fenêtre du document - Par défaut : faux
    document.center_window = True

    # Ordre de lecture prédominant ; détermine la position de la page
    # Lorsqu'elle est affichée côte à côte - Par défaut : L2R
    document.direction = ap.Direction.R2L

    # Spécifier si la barre de titre de la fenêtre doit afficher le titre du document
    # Si faux, la barre de titre affiche le nom du fichier PDF - Par défaut : faux
    document.display_doc_title = True

    # Spécifier si redimensionner la fenêtre du document pour s'adapter à la taille de
    # La première page affichée - Par défaut : faux
    document.fit_window = True

    # Spécifier si masquer la barre de menu de l'application de visualisation - Par défaut : faux
    document.hide_menubar = True

    # Spécifier si masquer la barre d'outils de l'application de visualisation - Par défaut : faux
    document.hide_tool_bar = True

    # Spécifier si masquer les éléments de l'interface utilisateur comme les barres de défilement
    # Et laisser seulement le contenu de la page affiché - Par défaut : faux
    document.hide_window_ui = True

    # Mode de page du document. spécifier comment afficher le document en quittant le mode plein écran.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Spécifier la mise en page, c'est-à-dire une seule page, une colonne
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Spécifier comment le document doit s'afficher lorsqu'il est ouvert
    # C'est-à-dire afficher les vignettes, plein écran, afficher le panneau des pièces jointes
    document.page_mode = ap.PageMode.USE_THUMBS

    # Enregistrer le fichier PDF mis à jour
    document.save(output_pdf)
```


### Incorporation de polices Type 1 standard

Certains documents PDF contiennent des polices d'un ensemble de polices Adobe spécial. Les polices de cet ensemble sont appelées "Polices Type 1 standard". Cet ensemble comprend 14 polices et l'intégration de ce type de polices nécessite l'utilisation de drapeaux spéciaux, c'est-à-dire [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Voici l'extrait de code qui peut être utilisé pour obtenir un document avec toutes les polices intégrées, y compris les Polices Type 1 standard :

```python

    import aspose.pdf as ap

    # Charger un document PDF existant
    document = ap.Document(input_pdf)
    # Définir la propriété EmbedStandardFonts du document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Vérifier si la police est déjà incorporée
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Incorporation des polices lors de la création d'un PDF

Si vous devez utiliser une police autre que les 14 polices de base prises en charge par Adobe Reader, vous devez intégrer la description de la police lors de la génération du fichier PDF. Si les informations sur la police ne sont pas intégrées, Adobe Reader les prendra du système d'exploitation si elles sont installées sur le système, ou il construira une police de substitution selon le descripteur de police dans le PDF.

>Veuillez noter que la police intégrée doit être installée sur la machine hôte, c'est-à-dire dans le cas du code suivant, la police 'Univers Condensed' est installée sur le système.

Nous utilisons la propriété 'is_embedded' pour intégrer les informations de police dans le fichier PDF. Définir la valeur de cette propriété sur 'True' intégrera le fichier de police complet dans le PDF, sachant que cela augmentera la taille du fichier PDF. Voici l'extrait de code qui peut être utilisé pour intégrer les informations de police dans le PDF.

```python

    import aspose.pdf as ap

    # Instancier un objet Pdf en appelant son constructeur vide
    doc = ap.Document()

    # Créer une section dans l'objet Pdf
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" Ceci est un texte d'exemple utilisant une police personnalisée.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Enregistrer le document PDF
    doc.save(output_pdf)
```


### Définir le nom de police par défaut lors de l'enregistrement en PDF

Lorsqu'un document PDF contient des polices qui ne sont pas disponibles dans le document lui-même et sur l'appareil, l'API remplace ces polices par la police par défaut. Si la police est disponible (installée sur l'appareil ou intégrée dans le document), le PDF de sortie doit avoir la même police (ne doit pas être remplacée par la police par défaut). La valeur de la police par défaut doit contenir le nom de la police (pas le chemin vers les fichiers de police). Nous avons implémenté une fonctionnalité pour définir le nom de police par défaut lors de l'enregistrement d'un document en tant que PDF. Le snippet de code suivant peut être utilisé pour définir la police par défaut :

```python

    import aspose.pdf as ap

    # Charger un document PDF existant avec une police manquante
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Spécifier le nom de police par défaut
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Obtenir toutes les polices d'un document PDF

Dans le cas où vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) fournie dans la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
 Veuillez vérifier l'extrait de code suivant afin d'obtenir toutes les polices d'un document PDF existant :

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Améliorer l'Incorporation des Polices en utilisant FontSubsetStrategy

L'extrait de code suivant montre comment définir la propriété [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) utilisée dans [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) :

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # Toutes les polices seront incorporées en tant que sous-ensemble dans le document en cas de SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Le sous-ensemble de polices sera incorporé pour les polices entièrement intégrées mais les polices qui ne sont pas intégrées dans le document ne seront pas affectées.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Obtenir-Définir le Facteur de Zoom du Fichier PDF

Parfois, vous souhaitez déterminer quel est le facteur de zoom actuel d'un document PDF. Avec Aspose.Pdf, vous pouvez connaître la valeur actuelle ainsi qu'en définir une.

La propriété Destination de la classe [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) vous permet d'obtenir la valeur de zoom associée à un fichier PDF. De même, elle peut être utilisée pour définir le facteur de zoom d'un fichier.

#### Définir le Facteur de Zoom

Le snippet de code suivant montre comment définir le facteur de zoom d'un fichier PDF.

```python

    import aspose.pdf as ap

    # Instancier un nouvel objet Document
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Enregistrer le document
    doc.save(output_pdf)
```

#### Obtenir le Facteur de Zoom

Le snippet de code suivant montre comment obtenir le facteur de zoom d'un fichier PDF.

```python

    import aspose.pdf as ap

    # Instancier un nouvel objet Document
    doc = ap.Document(input_pdf)

    # Créer un objet GoToAction
    action = doc.open_action

    # Obtenir le facteur de zoom du fichier PDF
    print(action.destination.zoom)
```


### Définition des Propriétés Prédéfinies pour la Boîte de Dialogue d'Impression

Aspose.PDF permet de définir les membres [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) d'un document PDF. Cela vous permet de modifier la propriété DuplexMode d'un document PDF qui est définie sur simplex par défaut. Cela peut être réalisé en utilisant deux méthodologies différentes comme illustré ci-dessous.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Définition des Propriétés Prédéfinies pour la Boîte de Dialogue d'Impression en Utilisant l'Éditeur de Contenu PDF

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("Le fichier a une inversion dupliquée bord court")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```