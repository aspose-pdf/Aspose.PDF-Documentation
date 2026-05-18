---
title: Tooltips zu PDF-Text in Python hinzufügen
linktitle: PDF-Tooltip
type: docs
weight: 20
url: /de/python-net/pdf-tooltip/
description: Erfahren Sie, wie Sie in Python Tooltips zu Textfragmenten in PDF-Dokumenten hinzufügen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Interaktive Tooltips zu PDF-Textfragmenten mit Python hinzufügen
Abstract: Dieser Artikel bietet zwei Python‑Beispiele für das Hinzufügen interaktiver Hilfen zu PDF‑Text mithilfe von Aspose.PDF for Python via .NET. Das erste Beispiel fügt Tooltips zu passenden Textfragmenten hinzu, indem unsichtbare `ButtonField`‑Elemente platziert und `alternate_name` gesetzt werden. Das zweite Beispiel erstellt ein verstecktes `TextBoxField`, das beim Darüberfahren erscheint, indem `HideAction`‑Ereignisse an ein unsichtbares `ButtonField` gebunden werden.
---

## Tooltip zum gesuchten Text in einem PDF hinzufügen

Dieses Code‑Snippet zeigt, wie man unsichtbare [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) Elemente auf spezifisch [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) Objekte in einem PDF, um Tooltips anzuzeigen, wenn der Benutzer mit der Maus darüber fährt. Es unterstützt sowohl kurze als auch lange Tooltip‑Nachrichten mithilfe von `alternate_name` Eigentum von `ButtonField`.

Verwenden Sie diese Seite, wenn Sie PDF‑Text interaktiver gestalten möchten, indem Sie Hover‑Hilfe, Inline‑Erklärungen oder kontextbezogene Notizen hinzufügen.

1. Neu erstellen [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Speichern Sie das ursprüngliche Dokument.
1. PDF-Dokument erneut öffnen.
1. Zieltext suchen mit [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Ein Unsichtbares hinzufügen [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) mit einem kurzen Tooltip.
1. Suche nach dem zweiten Zieltext.
1. Ein Unsichtbares hinzufügen [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) mit einem langen Tooltip über dem übereinstimmenden Fragment.
1. Speichern Sie das endgültige Dokument.

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

## Erstelle einen versteckten Textblock, der bei Mouseover in einem PDF erscheint

Füge interaktiven schwebenden Text zu einem PDF‑Dokument hinzu. Es legt ein unsichtbares [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) auf einen Zielausdruck und enthüllt ein verstecktes [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) wenn der Benutzer darüber hovert. Diese Technik ist ideal für kontextbezogene Hilfe, Anmerkungen oder die Darstellung dynamischer Inhalte.

1. Erstellen Sie ein neues PDF-Dokument.
1. Speichern Sie das PDF, damit es für die Einrichtung von Interaktivität erneut geöffnet werden kann.
1. PDF-Dokument erneut öffnen.
1. Lokalisieren Sie den Zieltext mithilfe von [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Erstellen Sie ein verstecktes [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. Fügen Sie das versteckte Feld zum Dokument hinzu [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) Sammlung.
1. Erstellen Sie ein unsichtbares [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. Mausaktionen zuweisen (`on_enter`, `on_exit`) verwenden [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) zum Anzeigen/Ausblenden des ausgeblendeten Feldes.
1. Speichern Sie das endgültige Dokument.

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

## Verwandte Textthemen

- [Arbeiten Sie mit Text in PDF mit Python](/pdf/de/python-net/working-with-text/)
- [Verwenden Sie FloatingBox für das PDF‑Textlayout in Python](/pdf/de/python-net/floating-box/)
- [PDF-Text in Python suchen und extrahieren](/pdf/de/python-net/search-and-get-text-from-pdf/)
- [Text zum PDF hinzufügen](/pdf/de/python-net/add-text-to-pdf-file/)