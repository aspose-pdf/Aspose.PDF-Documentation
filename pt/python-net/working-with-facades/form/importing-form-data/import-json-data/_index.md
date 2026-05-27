---
title: Importar Dados JSON
type: docs
weight: 30
url: /pt/python-net/import-json-data/
description: Este exemplo demonstra como importar dados de campos de formulário de um arquivo JSON para um formulário PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF, ler dados JSON estruturados através de um fluxo de arquivo e preencher automaticamente os campos de formulário correspondentes.
lastmod: "2026-05-18"
---

JSON é amplamente usado para armazenar e transferir dados estruturados entre sistemas. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada do [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo é usado para vincular um formulário PDF e importar valores de campos de um arquivo JSON externo. Após o processo de importação, o documento atualizado é salvo como um novo PDF.

1. Inicialize pdf_facades.Form() para interagir com os campos de formulário PDF.
1. Chame 'bind_pdf()' para anexar o modelo de formulário PDF.
1. Use \u0027FileIO()\u0027 para ler o arquivo JSON contendo os valores do formulário.
1. Chame 'import_json()' para preencher os campos PDF usando pares chave–valor JSON.
1. Salve o PDF atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```
