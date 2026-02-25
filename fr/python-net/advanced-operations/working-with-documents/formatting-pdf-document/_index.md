---
title: Mise en forme du document PDF avec Python
linktitle: Mise en forme du document PDF
type: docs
weight: 11
url: /fr/python-net/formatting-pdf-document/
description: Créez et formatez le document PDF avec Aspose.PDF pour Python via .NET. Utilisez l'extrait de code suivant pour résoudre vos tâches.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mise en forme des documents PDF avec Python
Abstract: L'article fournit un guide complet sur la manipulation et le formatage des documents PDF en utilisant la bibliothèque Aspose.PDF en Python. Il couvre divers aspects de la personnalisation des PDF, y compris la définition des propriétés de la fenêtre du document et de l'affichage des pages telles que le centrage de la fenêtre, le sens de lecture et le masquage des éléments de l'interface utilisateur. L'article explique comment récupérer et définir ces propriétés par programme à l'aide de la classe `Document`. De plus, il traite de la gestion des polices, détaillant comment incorporer les polices Standard Type 1 et d'autres polices dans les PDF, garantissant la portabilité du document et la cohérence visuelle sur les systèmes. Il met également en évidence les techniques pour définir un nom de police par défaut, récupérer toutes les polices d'un PDF et améliorer l'incorporation des polices à l'aide de `FontSubsetStrategy`. En outre, l'article développe l'ajustement du facteur de zoom des documents PDF à l'aide de la classe `GoToAction` et la configuration des propriétés prédéfinies de la boîte de dialogue d'impression, y compris les options d'impression recto verso. Des extraits de code accompagnent chaque section, offrant des exemples pratiques pour implémenter ces fonctionnalités.
---

## Mise en forme du document PDF

### Obtenir les propriétés de la fenêtre du document et de l'affichage des pages

Ce sujet vous aide à comprendre comment obtenir les propriétés de la fenêtre du document, de l'application de visualisation, et comment les pages sont affichées. Pour définir ces propriétés :

Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Vous pouvez maintenant définir les propriétés de l'objet Document, telles que

- CenterWindow – Centre la fenêtre du document à l'écran. Par défaut : false.
- Direction – Ordre de lecture. Cela détermine la façon dont les pages sont disposées lorsqu'elles sont affichées côte à côte. Par défaut : de gauche à droite.
- DisplayDocTitle – Affiche le titre du document dans la barre de titre de la fenêtre du document. Par défaut : false (le titre est affiché).
- HideMenuBar – Masque ou affiche la barre de menus de la fenêtre du document. Par défaut : false (la barre de menus est affichée).
- HideToolBar – Masque ou affiche la barre d'outils de la fenêtre du document. Par défaut : false (la barre d'outils est affichée).
- HideWindowUI – Masque ou affiche les éléments de l'interface de la fenêtre du document comme les barres de défilement. Par défaut : false (les éléments UI sont affichés).
- NonFullScreenPageMode – Comment le document se comporte lorsqu'il n'est pas affiché en mode plein écran.
- PageLayout – La mise en page.
- PageMode – Comment le document est affiché lors de la première ouverture. Les options sont afficher les vignettes, plein écran, afficher le panneau des pièces jointes.

Le fragment de code suivant vous montre comment obtenir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get different document properties
    # Position of document's window - Default: false
    print("CenterWindow :", document.center_window)

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    print("Direction :", document.direction)

    # Whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    print("FitWindow :", document.fit_window)

    # Whether to hide menu bar of the viewer application - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Whether to hide tool bar of the viewer application - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Document's page mode. How to display document on exiting full-screen mode.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # The page layout i.e. single page, one column
    print("PageLayout :", document.page_layout)

    # How the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    print("pageMode :", document.page_mode)

```

### Définir les propriétés de la fenêtre du document et de l'affichage des pages

Ce sujet explique comment définir les propriétés de la fenêtre du document, de l'application de visualisation et de l'affichage des pages. Pour définir ces différentes propriétés :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Définissez les propriétés de l'objet Document.
1. Enregistrez le fichier PDF mis à jour en utilisant la méthode save.

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

Chacune est utilisée et décrite dans le code ci-dessous. Le fragment de code suivant vous montre comment définir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set different document properties
    # Sepcify to position document's window - Default: false
    document.center_window = True

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    document.direction = ap.Direction.R2L

    # Specify whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    document.display_doc_title = True

    # Specify whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    document.fit_window = True

    # Specify whether to hide menu bar of the viewer application - Default: false
    document.hide_menubar = True

    # Specify whether to hide tool bar of the viewer application - Default: false
    document.hide_tool_bar = True

    # Specify whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    document.hide_window_ui = True

    # Document's page mode. specify how to display document on exiting full-screen mode.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Specify the page layout i.e. single page, one column
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Specify how the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_THUMBS

    # Save updated PDF file
    document.save(output_pdf)
```

### Incorporation des polices Standard Type 1

Certains documents PDF contiennent des polices provenant d'un ensemble spécial de polices Adobe. Les polices de cet ensemble sont appelées « Standard Type 1 Fonts ». Cet ensemble comprend 14 polices et l'incorporation de ce type de polices nécessite l'utilisation de drapeaux spéciaux, par exemple [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Voici le fragment de code qui peut être utilisé pour obtenir un document avec toutes les polices incorporées, y compris les polices Standard Type 1 :

```python

    import aspose.pdf as ap

    # Load an existing PDF Document
    document = ap.Document(input_pdf)
    # Set EmbedStandardFonts property of document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Check if font is already embedded
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Incorporation des polices lors de la création du PDF

Si vous avez besoin d'utiliser une police autre que les 14 polices de base prises en charge par Adobe Reader, vous devez incorporer la description de la police lors de la génération du fichier PDF. Si les informations de police ne sont pas incorporées, Adobe Reader les prendra depuis le système d'exploitation si elles y sont installées, ou il construira une police de substitution selon le descripteur de police dans le PDF.

>Veuillez noter que la police incorporée doit être installée sur la machine hôte, c'est-à-dire, dans le cas du code suivant, la police « Univers Condensed » est installée sur le système.

Nous utilisons la propriété 'is_embedded' pour incorporer les informations de police dans le fichier PDF. Le fait de régler la valeur de cette propriété sur 'True' incorporera le fichier de police complet dans le PDF, en sachant que cela augmentera la taille du fichier PDF. Voici le fragment de code qui peut être utilisé pour incorporer les informations de police dans le PDF.

```python

    import aspose.pdf as ap

    # Instantiate Pdf object by calling its empty constructor
    doc = ap.Document()

    # Create a section in the Pdf object
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Save PDF Document
    doc.save(output_pdf)
```

### Définir le nom de police par défaut lors de l'enregistrement du PDF

Lorsque un document PDF contient des polices qui ne sont pas disponibles dans le document lui‑même ni sur l’appareil, l’API remplace ces polices par la police par défaut. Si la police est disponible (installée sur l’appareil ou incorporée dans le document), le PDF de sortie doit conserver la même police (ne doit pas être remplacée par la police par défaut). La valeur de la police par défaut doit contenir le nom de la police (pas le chemin vers les fichiers de police). Nous avons implémenté une fonctionnalité permettant de définir le nom de la police par défaut lors de l’enregistrement d’un document au format PDF. Le fragment de code suivant peut être utilisé pour définir la police par défaut :

```python

    import aspose.pdf as ap

    # Load an existing PDF document with missing font
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Specify Default Font Name
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Récupérer toutes les polices d’un document PDF

Dans le cas où vous souhaitez récupérer toutes les polices d’un document PDF, vous pouvez utiliser la méthode [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) fournie dans la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Veuillez consulter le fragment de code suivant afin d’obtenir toutes les polices d’un document PDF existant :

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Améliorer l’intégration des polices avec FontSubsetStrategy

Le fragment de code suivant montre comment définir la propriété [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) utilisée par [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) :

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # All fonts will be embedded as subset into document in case of SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Obtenir et définir le facteur de zoom d’un fichier PDF

Parfois, vous souhaitez déterminer quel est le facteur de zoom actuel d’un document PDF. Avec Aspose.Pdf, vous pouvez connaître la valeur actuelle ainsi qu’en définir une.

La propriété Destination de la classe [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) vous permet d’obtenir la valeur de zoom associée à un fichier PDF. De même, elle peut être utilisée pour définir le facteur de zoom d’un fichier.

#### Définir le facteur de zoom

Le fragment de code suivant montre comment définir le facteur de zoom d’un fichier PDF.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Save the document
    doc.save(output_pdf)
```

#### Obtenir le facteur de zoom

Le fragment de code suivant montre comment obtenir le facteur de zoom d’un fichier PDF.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    # Create GoToAction object
    action = doc.open_action

    # Get the Zoom factor of PDF file
    print(action.destination.zoom)
```

### Définir les propriétés prédéfinies de la boîte de dialogue d’impression

Aspoose.PDF permet de définir les membres [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) d’un document PDF. Il vous permet de modifier la propriété DuplexMode d’un document PDF qui est réglée sur simplex par défaut. Cela peut être réalisé en utilisant deux méthodologies différentes comme indiqué ci‑dessous.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Définir les propriétés prédéfinies de la boîte de dialogue d’impression à l’aide de PDF Content Editor

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("The file has duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```


