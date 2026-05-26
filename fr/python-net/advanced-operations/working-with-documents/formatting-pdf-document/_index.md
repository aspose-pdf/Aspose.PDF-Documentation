---
title: Formater des documents PDF en Python
linktitle: Mise en forme du document PDF
type: docs
weight: 11
url: /fr/python-net/formatting-pdf-document/
description: Apprenez à formater les documents PDF, à incorporer des polices, à contrôler les paramètres du visualiseur et à ajuster les options d'affichage en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formater des documents PDF avec Python
Abstract: L'article propose un guide complet sur la manipulation et le formatage des documents PDF à l'aide de la bibliothèque Aspose.PDF en Python. Il couvre divers aspects de la personnalisation des PDF, notamment la configuration des propriétés de la fenêtre du document et de l'affichage des pages, telles que le centrage de la fenêtre, la direction de lecture et la dissimulation des éléments de l'interface utilisateur. L'article explique comment récupérer et définir ces propriétés programmatiquement en utilisant la classe `Document`. En outre, il aborde la gestion des polices, détaillant comment intégrer les polices Standard Type 1 et d'autres polices dans les PDF, assurant la portabilité du document et la cohérence visuelle sur différents systèmes. Il met également en avant des techniques pour définir un nom de police par défaut, récupérer toutes les polices d'un PDF et améliorer l'intégration des polices à l'aide de `FontSubsetStrategy`. De plus, l'article développe l'ajustement du facteur de zoom des documents PDF en utilisant la classe `GoToAction` et la configuration des propriétés prédéfinies de la boîte de dialogue d'impression, y compris les options d'impression recto‑verso. Des extraits de code accompagnent chaque section, fournissant des exemples pratiques pour implémenter ces fonctionnalités.
---

Ce guide est utile lorsque vous devez contrôler le comportement du visualiseur PDF, l'intégration de polices, les paramètres d'affichage par défaut ou les préférences d'impression dans des documents générés en Python.

## Mise en forme du document PDF

### Obtenir les propriétés d’affichage de la fenêtre du document et de la page

Ce sujet vous aide à comprendre comment obtenir les propriétés de la fenêtre du document, de l'application de visualisation, et comment les pages sont affichées. Pour définir ces propriétés :

Ouvrez le fichier PDF en utilisant le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe. Maintenant, vous pouvez définir les propriétés de l'objet Document, telles que

- CenterWindow – Centrer la fenêtre du document à l'écran. Valeur par défaut : false.
- Direction – Ordre de lecture. Ceci détermine comment les pages sont disposées lorsqu'elles sont affichées côte à côte. Par défaut : de gauche à droite.
- DisplayDocTitle – Affiche le titre du document dans la barre de titre de la fenêtre du document. Valeur par défaut : false (le titre est affiché).
- HideMenuBar – Masquer ou afficher la barre de menu de la fenêtre du document. Par défaut : false (la barre de menu est affichée).
- HideToolBar – Masquer ou afficher la barre d'outils de la fenêtre du document. Par défaut : false (la barre d'outils est affichée).
- HideWindowUI – Masquer ou afficher les éléments de la fenêtre du document, comme les barres de défilement. Par défaut : false (les éléments d’interface sont affichés).
- NonFullScreenPageMode – Comment le document est affiché lorsqu’il n’est pas en mode plein écran.
- PageLayout – La mise en page.
- PageMode – Comment le document est affiché lors de la première ouverture. Les options sont afficher les vignettes, plein écran, afficher le panneau des pièces jointes.

Le fragment de code suivant vous montre comment obtenir les propriétés en utilisant [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### Définir les propriétés d'affichage de la fenêtre du Document et de la Page

Ce sujet explique comment définir les propriétés de la fenêtre du document, de l'application de visualisation et de l'affichage de la page. Pour définir ces différentes propriétés :

1. Ouvrez le fichier PDF en utilisant le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Définissez les propriétés de l'objet Document.
1. Enregistrez le fichier PDF mis à jour en utilisant la méthode save.

Propriétés disponibles :

- Centrer la fenêtre
- Direction
- AfficherDocTitre
- Ajuster à la fenêtre
- Masquer la barre de menus
- Masquer la barre d'outils
- MasquerInterfaceFenêtre
- ModePageNonPleinEcran
- Mise en page
- ModePage

Chacun est utilisé et décrit dans le code ci‑dessous. Le fragment de code suivant montre comment définir les propriétés en utilisant le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### Intégration des polices de type 1 standard

Some PDF documents have fonts from a special Adobe font set. Fonts from this set are called “Standard Type 1 Fonts”. This set includes 14 fonts and embedding this type of fonts requires using of special flags i.e [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Le fragment de code suivant peut être utilisé pour obtenir un document avec toutes les polices incorporées, y compris les polices Type 1 standard :

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Intégration des polices lors de la création de PDF

Si vous devez utiliser une police autre que les 14 polices de base prises en charge par Adobe Reader, vous devez intégrer la description de la police lors de la génération du fichier PDF. Si les informations de police ne sont pas intégrées, Adobe Reader les prendra du système d’exploitation si elle est installée sur le système, ou il construira une police de substitution selon le descripteur de police dans le PDF.

>Veuillez noter que la police incorporée doit être installée sur la machine hôte, c.-à-d. dans le cas du code suivant, la police ‘Univers Condensed’ est installée sur le système.

Nous utilisons la propriété 'is_embedded' pour intégrer les informations de police dans le fichier PDF. Définir la valeur de cette propriété sur 'True' intégrera le fichier de police complet dans le PDF, en sachant que cela augmentera la taille du fichier PDF. Voici le fragment de code qui peut être utilisé pour intégrer les informations de police dans le PDF.

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### Définir le nom de police par défaut lors de l'enregistrement du PDF

Lorsqu'un document PDF contient des polices qui ne sont pas disponibles dans le document lui‑même et sur l'appareil, l'API remplace ces polices par la police par défaut. Si la police est disponible (installée sur l'appareil ou incorporée dans le document), le PDF généré doit conserver la même police (ne doit pas être remplacée par la police par défaut). La valeur de la police par défaut doit contenir le nom de la police (et non le chemin vers les fichiers de police). Nous avons implémenté une fonctionnalité permettant de définir le nom de la police par défaut lors de l'enregistrement d'un document au format PDF. Le fragment de code suivant peut être utilisé pour définir la police par défaut :

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### Obtenir toutes les polices du PDF Document

Dans le cas où vous souhaitez obtenir toutes les polices d’un document PDF, vous pouvez utiliser [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) méthode fournie dans [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe. Veuillez vérifier le fragment de code suivant afin d'obtenir toutes les polices d'un document PDF existant :

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### Améliorer l'intégration des polices en utilisant FontSubsetStrategy

Le fragment de code suivant montre comment définir [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) utilisé [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) propriété:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### Obtenir‑définir le facteur de zoom du fichier PDF

Parfois, vous souhaitez déterminer quel est le facteur de zoom actuel d’un document PDF. Avec Aspose.Pdf, vous pouvez connaître la valeur actuelle ainsi qu’en définir une.

Le [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) La propriété Destination de la classe permet d'obtenir la valeur de zoom associée à un fichier PDF. De même, elle peut être utilisée pour définir le facteur de zoom d'un fichier.

#### Définir le facteur de zoom

L'extrait de code suivant montre comment définir le facteur de zoom d'un fichier PDF.

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### Obtenir le facteur de zoom

L'extrait de code suivant montre comment obtenir le facteur de zoom d'un fichier PDF.

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## Sujets de documents associés

- [Travailler avec des documents PDF en Python](/pdf/fr/python-net/working-with-documents/)
- [Créer des fichiers PDF en Python](/pdf/fr/python-net/create-pdf-document/)
- [Manipuler des documents PDF en Python](/pdf/fr/python-net/manipulate-pdf-document/)
- [Optimiser les fichiers PDF en Python](/pdf/fr/python-net/optimize-pdf/)
