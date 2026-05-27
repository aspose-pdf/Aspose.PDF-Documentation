---
title: Ajouter des infobulles au texte PDF en Python
linktitle: Infobulle PDF
type: docs
weight: 20
url: /fr/python-net/pdf-tooltip/
description: Apprenez comment ajouter des infobulles aux fragments de texte dans les documents PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajoutez des infobulles interactives aux fragments de texte PDF à l'aide de Python
Abstract: Cet article fournit deux exemples Python pour ajouter de l'aide interactive au texte PDF en utilisant Aspose.PDF for Python via .NET. Le premier exemple ajoute des infobulles aux fragments de texte correspondants en plaçant des éléments `ButtonField` invisibles et en définissant `alternate_name`. Le deuxième exemple crée un `TextBoxField` caché qui apparaît au survol en reliant des événements `HideAction` à un `ButtonField` invisible.
---

## Ajouter une infobulle au texte recherché dans un PDF

Cet extrait de code montre comment superposer invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) éléments sur spécifique [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) objets dans un PDF pour afficher des infobulles lorsque l'utilisateur survole ceux-ci. Il prend en charge les messages d'infobulles courts et longs en utilisant le `alternate_name` propriété de `ButtonField`.

Utilisez cette page lorsque vous devez rendre le texte PDF plus interactif en ajoutant de l'aide au survol, des explications en ligne ou des notes contextuelles.

1. Créer un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Enregistrez le document initial.
1. Rouvrez le document PDF.
1. Recherchez le texte cible en utilisant [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Ajouter un invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) avec une info-bulle courte.
1. Rechercher le deuxième texte cible.
1. Ajouter un invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) avec une info-bulle longue au-dessus du fragment correspondant.
1. Enregistrez le document final.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

# region PDF Tooltip
def add_tool_tip_to_searched_text(outfile):
    # Create PDF document
    with ap.Document() as document:
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display a tooltip")
        )
        document.pages[1].paragraphs.add(
            ap.text.TextFragment(
                "Move the mouse cursor here to display a very long tooltip"
            )
        )
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a tooltip"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the extracted text fragments
        text_fragments = absorber.text_fragments

        # Loop through the fragments
        for fragment in text_fragments:
            # Create invisible button on text fragment position
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # alternate_name value will be displayed as tooltip by a viewer application
            field.alternate_name = "Tooltip for text."
            # Add button field to the document
            document.form.add(field)

        # Next will be sample of very long tooltip
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a very long tooltip"
        )
        document.pages.accept(absorber)
        text_fragments = absorber.text_fragments

        for fragment in text_fragments:
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # Set very long text
            field.alternate_name = (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                " sed do eiusmod tempor incididunt ut labore et dolore magna"
                " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                " Duis aute irure dolor in reprehenderit in voluptate velit"
                " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                " occaecat cupidatat non proident, sunt in culpa qui officia"
                " deserunt mollit anim id est laborum."
            )
            document.form.add(field)

        # Save document
        document.save(outfile)
```

## Créer un bloc de texte caché qui apparaît au survol dans un PDF

Ajouter du texte flottant interactif à un document PDF. Il superpose un invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) sur une phrase cible et révèle un caché [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) lorsque l'utilisateur survole l'élément. Cette technique est idéale pour l'aide contextuelle, les annotations ou la présentation de contenu dynamique.

1. Créer un nouveau document PDF.
1. Enregistrez le PDF afin de pouvoir le rouvrir pour configurer l'interactivité.
1. Rouvrez le document PDF.
1. Localisez le texte cible en utilisant [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Créer un caché [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. Ajoutez le champ caché au document [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) collection.
1. Créer un invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. Attribuer des actions de la souris ("`on_enter`, `on_exit`) en utilisant [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) pour afficher/masquer le champ caché.
1. Enregistrez le document final.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

def create_hidden_text_block(outfile):
    # Create PDF document
    with ap.Document() as document:
        #  Add paragraph with text
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display floating text")
        )
        # Save PDF document
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the first extracted text fragment
        text_fragments = absorber.text_fragments
        fragment = text_fragments[1]

        # Create hidden text field for floating text in the specified rectangle of the page
        floating_field = ap.forms.TextBoxField(
            fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
        )
        # Set text to be displayed as field value
        floating_field.value = 'This is the "floating text field".'
        # We recommend to make field 'readonly' for this scenario
        floating_field.read_only = True
        # Set 'hidden' flag to make field invisible on document opening
        floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

        # Setting a unique field name isn't necessary but allowed
        floating_field.partial_name = "FloatingField_1"

        # Setting characteristics of field appearance isn't necessary but makes it better
        floating_field.default_appearance = ap.annotations.DefaultAppearance(
            "Helv", 10, drawing.Color.blue
        )
        floating_field.characteristics.background = drawing.Color.light_blue
        floating_field.characteristics.border = drawing.Color.dark_blue
        floating_field.border = ap.annotations.Border(floating_field)
        floating_field.border.width = 1
        floating_field.multiline = True

        # Add text field to the document
        document.form.add(floating_field)
        # Create invisible button on text fragment position
        button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Create new hide action for specified field (annotation) and invisibility flag.
        # (You also may refer floating field by the name if you specified it above.)
        # Add actions on mouse enter/exit at the invisible button field

        button_field.actions.on_enter = ap.annotations.HideAction(floating_field, False)
        button_field.actions.on_exit = ap.annotations.HideAction(floating_field)

        # Add button field to the document
        document.form.add(button_field)

        # Save document
        document.save(outfile)
```

## Sujets de texte associés

- [Travailler avec le texte dans le PDF en utilisant Python](/pdf/fr/python-net/working-with-text/)
- [Utilisez FloatingBox pour la mise en page du texte PDF en Python](/pdf/fr/python-net/floating-box/)
- [Rechercher et extraire le texte PDF en Python](/pdf/fr/python-net/search-and-get-text-from-pdf/)
- [Ajout de texte au PDF](/pdf/fr/python-net/add-text-to-pdf-file/)