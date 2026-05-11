---
title: Eliminar páginas de PDF
linktitle: Eliminar páginas de PDF
type: docs
weight: 20
url: /es/python-net/delete-pages-from-pdf/
description: Eliminar páginas seleccionadas de un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar páginas específicas de un documento PDF en Python
Abstract: Aprenda cómo eliminar páginas seleccionadas de un documento PDF usando Aspose.PDF for Python. Este ejemplo demuestra cómo eliminar páginas específicas de un archivo PDF existente de forma programática, creando un nuevo documento sin las páginas eliminadas.
---

A veces los documentos PDF contienen páginas innecesarias o sensibles que deben eliminarse. Usando Aspose.PDF for Python, los desarrolladores pueden eliminar programáticamente páginas específicas de un PDF sin editar manualmente el archivo.

Nuestro ejemplo muestra cómo usar el método delete de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase para eliminar páginas de un documento PDF. Al especificar los números de página a borrar, puedes crear un nuevo PDF que excluya las páginas no deseadas. Esta funcionalidad es útil para limpiar informes, eliminar información confidencial o preparar extractos de documentos personalizados.

1. Crear un objeto PdfFileEditor.
1. Definir páginas a eliminar.
1. Eliminar las páginas.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir


    # Delete Pages from PDF
    def delete_pages_from_pdf(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be deleted (1-based index)
        pages_to_delete = [2, 4]

        # Delete the specified pages from the PDF document
        pdf_editor.delete(infile, pages_to_delete, outfile)
```