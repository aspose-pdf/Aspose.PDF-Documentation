---
title: Trabajando con tablas en PDFs etiquetados usando Python
linktitle: Trabajando con tablas en PDFs etiquetados
type: docs
weight: 40
url: /es/python-net/working-with-table-in-tagged-pdfs/
description: Este artículo explica cómo trabajar con tablas en un documento PDF etiquetado con Aspose.PDF para Python a través de .NET.
lastmod: "2025-06-17"
sitemap: 
changefreq: "monthly"
priority: 0.7
---

## Crear tabla en PDF etiquetado

Sigue los pasos para crear una tabla en PDF etiquetado:

1. Inicializa un nuevo documento PDF.
1. Define los metadatos del documento.
1. Crea y agrega un elemento de tabla.
1. Personaliza la apariencia de la tabla.
1. Crea y da estilo a la fila de encabezado.
1. Genera filas del cuerpo de la tabla.
1. Agrega una fila de pie de página.
1. Añade atributos de accesibilidad.
1. Guarda el PDF etiquetado.
1. Valida el cumplimiento de PDF/UA.

Al seguir los pasos anteriores, puedes generar una tabla semánticamente rica y accesible en un documento PDF usando Aspose.PDF para Python. El archivo resultante cumple con los estándares de cumplimiento PDF/UA-1, garantizando compatibilidad con lectores de pantalla y tecnologías asistivas. Esto es ideal para casos de uso que implican cumplimiento normativo, auditoría de accesibilidad y publicación de contenido inclusivo.

El siguiente fragmento de código muestra cómo crear una tabla en el documento PDF etiquetado:

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Example table")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)

        table_element.border = ap.BorderInfo(ap.BorderSide.ALL, 1.2, ap.Color.dark_blue)

        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 50
        col_count = 4

        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"
        head_tr_element.background_color = ap.Color.light_gray

        for column_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text(f"Head {column_index}")

            th_element.background_color = ap.Color.green_yellow
            th_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

            th_element.is_no_border = True
            th_element.margin = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)

            th_element.alignment = ap.HorizontalAlignment.RIGHT

        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = f"Row {row_index}"

            for column_index in range(col_count):
                col_span = 1
                row_span = 1

                if column_index == 1 and row_index == 1:
                    col_span = 2
                    row_span = 2
                elif column_index == 2 and (row_index == 1 or row_index == 2):
                    continue
                elif row_index == 2 and (column_index == 1 or column_index == 2):
                    continue

                td_element = tr_element.create_td()
                td_element.set_text(f"Cell [{row_index}, {column_index}]")

                td_element.background_color = ap.Color.yellow
                td_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

                td_element.is_no_border = False
                td_element.margin = ap.MarginInfo(8.0, 2.0, 8.0, 2.0)

                td_element.alignment = ap.HorizontalAlignment.CENTER

                cell_text_state = ap.text.TextState()
                cell_text_state.foreground_color = ap.Color.dark_blue
                cell_text_state.font_size = 7.5
                cell_text_state.font_style = ap.text.FontStyles.BOLD
                cell_text_state.font = ap.text.FontRepository.find_font("Arial")
                td_element.default_cell_text_state = cell_text_state

                td_element.is_word_wrapped = True
                td_element.vertical_alignment = ap.VerticalAlignment.CENTER

                td_element.col_span = col_span
                td_element.row_span = row_span

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"
        foot_tr_element.background_color = ap.Color.light_sea_green

        for column_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text(f"Foot {column_index}")

            td_element.alignment = ap.HorizontalAlignment.CENTER
            td_element.structure_text_state.font_size = 7
            td_element.structure_text_state.font_style = ap.text.FontStyles.BOLD

        table_attributes = table_element.attributes.get_attributes(
            ap.logicalstructure.AttributeOwnerStandard.TABLE)
        summary_attribute = ap.logicalstructure.StructureAttribute(
            ap.logicalstructure.AttributeKey.SUMMARY)
        summary_attribute.set_string_value("The summary text for table")
        table_attributes.set_attribute(summary_attribute)

        # Save Tagged PDF Document
        document.save(path_outfile)

    # Check PDF/UA compliance
        with ap.Document(path_outfile) as document:
            is_pdf_ua_compliance = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
            print(f"PDF/UA compliance: {is_pdf_ua_compliance}")
```

## Estilizar elemento de tabla

Aspose.PDF para Python a través de .NET permite aplicar estilo a una tabla en un documento PDF etiquetado. Para estilizar una tabla, puedes crear una tabla usando el método [CreateTableElement()](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/) de la interfaz [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) y establecer el estilo de la tabla usando las propiedades de la clase [TableElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/) .

A continuación se muestra la lista de propiedades que puedes usar para estilizar una tabla:

- [background_color](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [alignmen](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [broken](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [column_widths](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [default_cell_text_state](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [default_column_width](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [is_broken](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [is_borders_included](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [left](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).
- [top](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tableelement/#properties).

El siguiente fragmento de código muestra cómo estilizar una tabla en un documento PDF etiquetado:

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Example table style")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        # Create table structure element
        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)

        table_element.background_color = ap.Color.beige
        table_element.border = ap.BorderInfo(ap.BorderSide.ALL, 0.80, ap.Color.gray)
        table_element.alignment = ap.HorizontalAlignment.CENTER
        table_element.broken = ap.TableBroken.VERTICAL
        table_element.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
        table_element.column_widths = "80 80 80 80 80"
        table_element.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.50,
                                                                    ap.Color.dark_blue)
        table_element.default_cell_padding = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)
        table_element.default_cell_text_state.foreground_color = ap.Color.dark_cyan
        table_element.default_cell_text_state.font_size = 8.0
        table_element.default_column_width = "70"

        table_element.is_broken = False
        table_element.is_borders_included = True

        table_element.left = 0.0
        table_element.top = 40.0

        table_element.repeating_columns_count = 2
        table_element.repeating_rows_count = 3
        row_style = ap.text.TextState()
        row_style.background_color = ap.Color.light_coral
        table_element.repeating_rows_style = row_style

        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 10
        col_count = 5

        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"

        for col_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text(f"Head {col_index}")

        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = f"Row {row_index}"

            for col_index in range(col_count):
                td_element = tr_element.create_td()
                td_element.set_text(f"Cell [{row_index}, {col_index}]")

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"

        for col_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text(f"Foot {col_index}")

        # Save Tagged PDF Document
        document.save(path_outfile)

    # Check PDF/UA compliance
    with ap.Document(path_outfile) as document:
        is_pdf_ua_compliance = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
        print(f"PDF/UA compliance: {is_pdf_ua_compliance}")
```

## Estilizar fila de tabla

Aspose.PDF para Python a través de .NET permite aplicar estilo a una fila de tabla en un documento PDF etiquetado. Para estilizar una fila de tabla, puedes usar las propiedades de la clase [TableTRElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/) . A continuación se muestra la lista de propiedades que puedes usar para estilizar una fila de tabla:

- [background_color](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).
- [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).
- [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).
- [min_row_height](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).
- [fixed_row_height](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).
- [is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).
- [is_row_broken](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).
- [default_cell_text_state](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).
- [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).
- [vertical_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tabletrelement/#properties).

El siguiente fragmento de código muestra cómo aplicar estilo a una fila de tabla en el documento PDF etiquetado:

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Example table style")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        # Create table structure element
        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)
        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 7
        col_count = 3
        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"
        for col_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text("Head {}".format(col_index))
        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = "Row {}".format(row_index)
            tr_element.background_color = ap.Color.light_goldenrod_yellow
            tr_element.border = ap.BorderInfo(ap.BorderSide.ALL, 0.75, ap.Color.dark_gray)
            tr_element.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.50, ap.Color.blue)
            tr_element.min_row_height = 100.0
            tr_element.fixed_row_height = 120.0
            tr_element.is_in_new_page = (row_index % 3 == 1)
            tr_element.is_row_broken = True

            cell_text_state = ap.text.TextState()
            cell_text_state.foreground_color = ap.Color.red
            tr_element.default_cell_text_state = cell_text_state
            tr_element.default_cell_padding = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)
            tr_element.vertical_alignment = ap.VerticalAlignment.BOTTOM
            for col_index in range(col_count):
                td_element = tr_element.create_td()
                td_element.set_text("Cell [{0}, {1}]".format(row_index,col_index))

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"

        for col_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text("Foot {}".format(col_index))

        # Save Tagged PDF Document
        document.save(path_outfile)

    # Check PDF/UA compliance
    with ap.Document(path_outfile) as document:
        is_pdf_ua_compliance = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
        print("PDF/UA compliance: {}".format(is_pdf_ua_compliance))
```

## Estilo de celda de tabla

Aspose.PDF para Python a través de .NET permite aplicar estilo a una celda de tabla en un documento PDF etiquetado. Para aplicar estilo a una celda de tabla, puedes usar las propiedades de la clase [TableCellElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/) . La siguiente es la lista de propiedades que puedes usar para estilizar una celda de tabla:

- [background_color](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).
- [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).
- [is_no_border](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).
- [margin](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).
- [alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).
- [default_cell_text_state](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).
- [is_word_wrapped](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).
- [vertical_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).
- [col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).
- [row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/tablecellelement/#properties).

El siguiente fragmento de código muestra cómo aplicar estilo a una celda de tabla en el documento PDF etiquetado:

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Example table cell style")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        # Create table structure element
        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)

        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 4
        col_count = 4

        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"

        for col_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text("Head {}".format(col_index))

            th_element.background_color = ap.Color.green_yellow
            th_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

            th_element.is_no_border = True
            th_element.margin = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)

            th_element.alignment = ap.HorizontalAlignment.RIGHT

        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = "Row {}".format(row_index)

            for col_index in range(col_count):
                col_span = 1
                row_span = 1

                if col_index == 1 and row_index == 1:
                    col_span = 2
                    row_span = 2
                elif col_index == 2 and (row_index == 1 or row_index == 2):
                    continue
                elif row_index == 2 and (col_index == 1 or col_index == 2):
                    continue

                td_element = tr_element.create_td()
                td_element.set_text("Cell [{}, {}]".format(row_index, col_index))

                td_element.background_color = ap.Color.yellow
                td_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

                td_element.is_no_border = False
                td_element.margin = ap.MarginInfo(8.0, 2.0, 8.0, 2.0)

                td_element.alignment = ap.HorizontalAlignment.CENTER

                cell_text_state = ap.text.TextState()
                cell_text_state.foreground_color = ap.Color.dark_blue
                cell_text_state.font_size = 7.5
                cell_text_state.font_style = ap.text.FontStyles.BOLD
                cell_text_state.font = ap.text.FontRepository.find_font("Arial")
                td_element.default_cell_text_state = cell_text_state

                td_element.is_word_wrapped = True
                td_element.vertical_alignment = ap.VerticalAlignment.CENTER

                td_element.col_span = col_span
                td_element.row_span = row_span

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"

        for col_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text("Foot {}".format(col_index))

        # Save Tagged PDF Document
        document.save(path_outfile)

    # Check PDF/UA compliance
    with ap.Document(path_outfile) as document:
        is_pdf_ua_compliance = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
        print("PDF/UA compliance: {}".format(is_pdf_ua_compliance))
```

## Ajustar posición de la tabla

El siguiente fragmento de código muestra cómo ajustar la posición de la tabla en el documento PDF etiquetado:

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        # Create tagged content
        tagged_content = document.tagged_content
        tagged_content.set_title("Example table cell style")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        # Create table structure element
        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)

        # Create position settings
        position_settings = ap.tagged.PositionSettings()
        position_settings.horizontal_alignment = ap.HorizontalAlignment.NONE
        position_settings.margin = ap.MarginInfo(left=20, right=0, top=0, bottom=0)
        position_settings.vertical_alignment = ap.VerticalAlignment.NONE
        position_settings.is_first_paragraph_in_column = False
        position_settings.is_kept_with_next = False
        position_settings.is_in_new_page = False
        position_settings.is_in_line_paragraph = False

        # Adjust table position
        table_element.adjust_position(position_settings)

        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 4
        col_count = 4

        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"

        for col_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text(f"Head {col_index}")

            th_element.background_color = ap.Color.green_yellow
            th_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

            th_element.is_no_border = True
            th_element.margin = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)

            th_element.alignment = ap.HorizontalAlignment.RIGHT

        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = f"Row {row_index}"

            for col_index in range(col_count):
                col_span = 1
                row_span = 1

                if col_index == 1 and row_index == 1:
                    col_span = 2
                    row_span = 2
                elif col_index == 2 and (row_index == 1 or row_index == 2):
                    continue
                elif row_index == 2 and (col_index == 1 or col_index == 2):
                    continue

                td_element = tr_element.create_td()
                td_element.set_text(f"Cell [{row_index}, {col_index}]")

                td_element.background_color = ap.Color.yellow
                td_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

                td_element.is_no_border = False
                td_element.margin = ap.MarginInfo(8.0, 2.0, 8.0, 2.0)

                td_element.alignment = ap.HorizontalAlignment.CENTER

                cell_text_state = ap.text.TextState()
                cell_text_state.foreground_color = ap.Color.dark_blue
                cell_text_state.font_size = 7.5
                cell_text_state.font_style = ap.text.FontStyles.BOLD
                cell_text_state.font = ap.text.FontRepository.find_font("Arial")
                td_element.default_cell_text_state = cell_text_state

                td_element.is_word_wrapped = True
                td_element.vertical_alignment = ap.VerticalAlignment.CENTER

                td_element.col_span = col_span
                td_element.row_span = row_span

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"

        for col_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text(f"Foot {col_index}")

        # Save Tagged PDF Document
        document.save(path_outfile)

    # Check PDF/UA compliance
    with ap.Document(path_outfile) as document:
        is_pdf_ua_compliance = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
        print(f"PDF/UA compliance: {is_pdf_ua_compliance}")
```

