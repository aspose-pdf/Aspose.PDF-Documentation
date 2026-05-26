---
title: Supprimer des pages du PDF
type: docs
weight: 20
url: /fr/python-net/delete-pages-from-pdf/
description: Supprimer les pages sélectionnées d'un document PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer des pages spécifiques d'un document PDF en Python
Abstract: Apprenez comment supprimer les pages sélectionnées d'un document PDF à l'aide d'Aspose.PDF for Python. Cet exemple montre comment supprimer des pages spécifiques d'un fichier PDF existant de façon programmatique, en créant un nouveau document sans les pages supprimées.
---

Parfois, les documents PDF contiennent des pages inutiles ou sensibles qui doivent être supprimées. À l'aide d'Aspose.PDF for Python, les développeurs peuvent supprimer de façon programmatique des pages spécifiques d'un PDF sans modifier le fichier manuellement.

Notre exemple montre comment utiliser la méthode delete de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe pour supprimer des pages d'un document PDF. En spécifiant les numéros de pages à supprimer, vous pouvez créer un nouveau PDF qui exclut les pages indésirables. Cette fonctionnalité est utile pour nettoyer des rapports, supprimer des informations confidentielles ou préparer des extraits de documents personnalisés.

1. Créer un objet PdfFileEditor.
1. Définir les pages à supprimer.
1. Supprimer les pages.

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