---
title: Excluir páginas de PDF
type: docs
weight: 20
url: /pt/python-net/delete-pages-from-pdf/
description: Remova páginas selecionadas de um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Excluir páginas específicas de um documento PDF em Python
Abstract: Aprenda como remover páginas selecionadas de um documento PDF usando Aspose.PDF for Python. Este exemplo demonstra como excluir páginas específicas de um arquivo PDF existente programaticamente, criando um novo documento sem as páginas removidas.
---

Às vezes, documentos PDF contêm páginas desnecessárias ou confidenciais que precisam ser removidas. Usando Aspose.PDF for Python, desenvolvedores podem excluir programaticamente páginas específicas de um PDF sem editar o arquivo manualmente.

Nosso exemplo mostra como usar o método delete do [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe para remover páginas de um documento PDF. Ao especificar os números das páginas a serem excluídas, você pode criar um novo PDF que exclui páginas indesejadas. Essa funcionalidade é útil para limpar relatórios, remover informações confidenciais ou preparar extratos personalizados de documentos.

1. Crie um objeto PdfFileEditor.
1. Defina as páginas a serem excluídas.
1. Exclua as páginas.

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