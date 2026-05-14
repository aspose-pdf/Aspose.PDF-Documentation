---
title: Удалить страницы из PDF
type: docs
weight: 20
url: /python-net/delete-pages-from-pdf/
description: Удалить выбранные страницы из PDF-документа с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить конкретные страницы из PDF-документа на Python
Abstract: Узнайте, как удалить выбранные страницы из PDF-документа с помощью Aspose.PDF for Python. Этот пример демонстрирует, как программно удалить конкретные страницы из существующего PDF‑файла, создав новый документ без удалённых страниц.
---

Иногда PDF-документы содержат ненужные или конфиденциальные страницы, которые необходимо удалить. С помощью Aspose.PDF for Python разработчики могут программно удалять конкретные страницы из PDF, не редактируя файл вручную.

Наш пример показывает, как использовать метод delete в [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) классе для удаления страниц из PDF‑документа. Указывая номера страниц для удаления, вы можете создать новый PDF, который исключает нежелательные страницы. Эта функция полезна для очистки отчетов, удаления конфиденциальной информации или подготовки пользовательских извлечений документов.

1. Создайте объект PdfFileEditor.
1. Определите страницы для удаления.
1. Удалите страницы.

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