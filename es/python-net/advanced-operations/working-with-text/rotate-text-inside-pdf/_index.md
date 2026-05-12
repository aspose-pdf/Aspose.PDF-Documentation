---
title: Rotar texto PDF en Python
linktitle: Rotar texto dentro del PDF
type: docs
weight: 50
url: /es/python-net/rotate-text-inside-pdf/
description: Aprenda cómo rotar fragmentos de texto y párrafos dentro de documentos PDF en Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotar fragmentos de texto y párrafos en documentos PDF con Python
Abstract: Este artículo explica cómo rotar texto en documentos PDF usando Aspose.PDF for Python via .NET. Muestra cómo establecer la propiedad `rotation` en `TextFragment`, crear contenido rotado con `TextBuilder` y `TextParagraph`, y añadir texto rotado directamente a los párrafos de la página para diferentes escenarios de diseño.
---

Gire fragmentos de texto en un documento PDF usando Aspose.PDF for Python via .NET. Esta página muestra cómo controlar la posición y rotación del texto mediante `TextFragment`, `TextState`, y `TextBuilder`. Ajustando los ángulos de rotación, puedes crear diseños como encabezados diagonales, etiquetas verticales y anotaciones rotadas.

## Rotar fragmentos de texto usando TextBuilder en PDF

Crea un archivo PDF llamado `rotated_fragments.pdf` contiene tres fragmentos de texto alineados horizontalmente:

- el primer texto está sin rotar
- el segundo está rotado 45°
- el tercero está rotado 90°

1. Crear un nuevo documento PDF.
1. Inserte una nueva página para alojar el texto rotado.
1. Cree el primer fragmento de texto (sin rotación).
1. Cree el segundo fragmento de texto (rotación de 45°).
1. Cree el tercer fragmento de texto (rotación de 90°).
1. Agregar fragmentos de texto usando `TextBuilder`.
1. Guarde el documento.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotar fragmentos de texto individuales dentro de un párrafo en PDF

Rotar fragmentos de texto individuales dentro de un párrafo. Muestra cómo crear un párrafo de varias líneas (TextParagraph) que contiene múltiples fragmentos (TextFragment), cada uno con su propio ángulo de rotación. Esta técnica es útil para crear documentos visualmente ricos que combinan texto orientado horizontal y diagonalmente — por ejemplo, encabezados estilizados, diagramas o etiquetas anotadas.

Crea un PDF llamado `rotated_paragraph_fragments.pdf` contiene un párrafo con tres líneas de texto, cada línea rotada de manera diferente:

- la primera línea está rotada 45°
- la segunda línea permanece horizontal (0°)
- la tercera línea está rotada -45°

1. Crear un nuevo documento PDF.
1. Agrega una página en blanco donde aparecerá el texto rotado.
1. Cree un `TextParagraph`.
1. Crea y configura el primer fragmento de texto (+45° de rotación).
1. Crea el segundo fragmento de texto (sin rotación).
1. Crea el tercer fragmento de texto (-45° de rotación).
1. Agregar fragmentos de texto al párrafo.
1. Agregar el párrafo a la página usando `TextBuilder`.
1. Guarde el documento.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Rotar texto usando párrafos de página en PDF

Esta sección muestra un método simplificado para rotar texto dentro de un PDF utilizando Aspose.PDF for Python via .NET.
A diferencia de los enfoques de bajo nivel con `TextBuilder` o `TextParagraph`, este método agrega fragmentos de texto rotados directamente a la colección de párrafos de la página (`page.paragraphs`). Es ideal cuando necesitas rotación básica de texto pero no requieres posicionamiento preciso ni estructuración de párrafos.

Genera un archivo llamado `simple_rotated_text.pdf` contiene:

- un fragmento de texto horizontal principal con rotación 0°
- Fragmento rotado 315°
- Fragmento rotado 270°

1. Inicializar un nuevo documento PDF.
1. Crear una página donde se colocará el texto rotado.
1. Cree el primer fragmento de texto (sin rotación).
1. Crea el segundo fragmento de texto (rotación de 315°).
1. Crea el tercer fragmento de texto (rotación de 270°).
1. Agregar fragmentos de texto directamente a los párrafos de la página.
1. Guarde el documento PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotar párrafos completos en un PDF

Este ejemplo muestra la rotación avanzada de texto a nivel de párrafo en un PDF. A diferencia de la rotación a nivel de fragmento (donde cada pieza de texto se rota individualmente), este método rota párrafos enteros como bloques unificados en diferentes ángulos.
Cada párrafo contiene múltiples fragmentos de texto con estilo, y el párrafo completo se gira en ángulos específicos — permitiendo transformaciones de diseño complejas y consistentes.
Esto es ideal para diseños artísticos, marcas de agua o PDFs con mucho diseño donde se necesitan orientar secciones completas de texto en varias direcciones.

Crea `rotated_paragraphs.pdf`, que contiene cuatro párrafos totalmente estilizados y girados:

- cada uno rotado a un ángulo único (45°, 135°, 225° y 315°)
- cada párrafo tiene tres líneas de texto con fondos de colores, subrayado y estilo coherente

1. Crear un nuevo documento PDF.
1. Agregar una página en blanco para contener los párrafos rotados.
1. Iterar para crear varios párrafos.
1. Crear y posicionar el párrafo.
1. Crear fragmentos de texto con formato.
1. Aplicar formato de texto.
1. Agregar fragmentos de texto al párrafo.
1. Agregar el párrafo a la página usando `TextBuilder`.
1. Repita para las cuatro rotaciones.
1. Guarde el documento PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Temas de texto relacionados

- [Trabajar con texto en PDF usando Python](/pdf/es/python-net/working-with-text/)
- [Agregar texto al PDF](/pdf/es/python-net/add-text-to-pdf-file/)
- [Formatear texto PDF en Python](/pdf/es/python-net/text-formatting-inside-pdf/)
- [Reemplazar texto en PDF con Python](/pdf/es/python-net/replace-text-in-pdf/)