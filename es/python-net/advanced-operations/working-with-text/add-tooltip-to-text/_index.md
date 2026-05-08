---
title: Agregar información sobre herramientas al texto PDF en Python
linktitle: Información sobre herramientas PDF
type: docs
weight: 20
url: /es/python-net/pdf-tooltip/
description: Aprenda cómo agregar información sobre herramientas a fragmentos de texto en documentos PDF con Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar información sobre herramientas interactivas a fragmentos de texto PDF usando Python
Abstract: Este artículo ofrece dos ejemplos de Python para agregar ayuda interactiva al texto PDF usando Aspose.PDF for Python via .NET. El primer ejemplo añade descripciones emergentes a fragmentos de texto coincidentes al colocar elementos `ButtonField` invisibles y establecer `alternate_name`. El segundo ejemplo crea un `TextBoxField` oculto que aparece al pasar el cursor al conectar eventos `HideAction` a un `ButtonField` invisible.
---

## Agregar descripción emergente al texto buscado en un PDF

Este fragmento de código muestra cómo superponer invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) elementos en específico [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) objetos en un PDF para mostrar información sobre herramientas cuando el usuario pasa el cursor sobre ellos. Soporta tanto mensajes de información sobre herramientas cortos como largos utilizando el `alternate_name` propiedad de `ButtonField`.

Utilice esta página cuando necesite hacer el texto PDF más interactivo añadiendo ayuda emergente, explicaciones en línea o notas contextuales.

1. Crear un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Guarde el documento inicial.
1. Vuelva a abrir el documento PDF.
1. Buscar texto objetivo usando [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Añadir un invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) con una descripción breve.
1. Buscar el segundo texto objetivo.
1. Añadir un invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) con una descripción larga sobre el fragmento coincidente.
1. Guarda el documento final.

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

## Crear un bloque de texto oculto que aparece al pasar el cursor en un PDF

Agregar texto flotante interactivo a un documento PDF. Se superpone a un invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) en una frase objetivo y revela un oculto [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) cuando el usuario pasa el cursor sobre él. Esta técnica es ideal para ayuda contextual, anotaciones o presentación de contenido dinámico.

1. Crear un nuevo documento PDF.
1. Guarde el PDF para que pueda ser reabierto para la configuración de interactividad.
1. Vuelva a abrir el documento PDF.
1. Ubique el texto objetivo usando [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Crear un oculto [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. Agregar el campo oculto al documento [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) colección.
1. Crear un invisible [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. Asignar acciones del ratón ("`on_enter`, `on_exit`) usando [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) para mostrar/ocultar el campo oculto.
1. Guarda el documento final.

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

## Temas de texto relacionados

- [Trabajar con texto en PDF usando Python](/pdf/es/python-net/working-with-text/)
- [Utilice FloatingBox para el diseño de texto PDF en Python](/pdf/es/python-net/floating-box/)
- [Buscar y extraer texto PDF en Python](/pdf/es/python-net/search-and-get-text-from-pdf/)
- [Agregar texto al PDF](/pdf/es/python-net/add-text-to-pdf-file/)
