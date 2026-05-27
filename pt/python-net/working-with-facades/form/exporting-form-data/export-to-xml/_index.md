---
title: Exportar para XML
type: docs
weight: 40
url: /pt/python-net/export-to-xml/
description: Este exemplo demonstra como exportar os dados de formulário PDF para um arquivo XML usando Aspose.PDF for Python via .NET. Ele mostra como carregar um documento PDF, acessar seus campos de formulário através da fachada Form, e salvar os dados extraídos como XML estruturado usando a classe Form.
lastmod: "2026-05-18"
---

Exportar dados de formulário permite que os desenvolvedores reutilizem as informações armazenadas em PDF AcroForms sem copiar manualmente os valores dos campos. Neste exemplo, um [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto é criado a partir do aspose.pdf. No módulo facades, o PDF de origem é vinculado a ele, e os dados do formulário são gravados em um fluxo XML.

1. Crie um Objeto Form. Inicialize pdf_facades.Form() para acessar e gerenciar os campos de formulário.
1. Use 'bind_pdf()' para anexar o documento PDF de origem à instância Form.
1. Crie um fluxo de arquivo gravável usando 'FileIO()'.
1. Chame 'export_xml()' para extrair todos os valores dos campos de formulário e escrevê-los no arquivo XML.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```
