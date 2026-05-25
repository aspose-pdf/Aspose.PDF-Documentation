---
title: Importar Dados XML
type: docs
weight: 40
url: /pt/python-net/import-xml-data/
description: Este exemplo demonstra como importar dados de formulário de um arquivo XML para campos de formulário PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF, ler dados XML estruturados através de um fluxo de arquivo e preencher automaticamente os campos de formulário correspondentes.
lastmod: "2026-05-18"
---

XML é comumente usado para armazenar dados de formulário estruturados, tornando‑o um formato prático para transferir valores entre sistemas. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) é usado para carregar um formulário PDF e aplicar valores de campo diretamente de um arquivo XML. Após importar os dados, o PDF atualizado é salvo como um novo documento.

1. Inicialize pdf_facades.Form() para interagir com os campos de formulário PDF.
1. Chame 'bind_pdf()' para anexar o modelo de formulário PDF.
1. Use 'FileIO()' para acessar o arquivo XML que contém os dados do formulário.
1. Chame 'import_xml()' para preencher os campos PDF com valores do arquivo XML.
1. Salve o PDF atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
