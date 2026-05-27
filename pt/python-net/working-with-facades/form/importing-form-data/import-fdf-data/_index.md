---
title: Importar Dados FDF
type: docs
weight: 10
url: /pt/python-net/import-fdf-data/
description: Este exemplo demonstra como importar dados de formulário de um arquivo FDF para um formulário PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF, ler valores de campos de formulário a partir de um fluxo FDF e preencher automaticamente os campos correspondentes.
lastmod: "2026-05-18"
---

FDF (Forms Data Format) é um formato leve usado para armazenar e transferir valores de campos de formulário PDF sem incluir o documento completo. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) é usado para carregar um formulário PDF e importar dados de campo de um arquivo FDF externo. Após o processo de importação, o PDF atualizado é salvo como um novo arquivo.

1. Inicialize pdf_facades.Form() para trabalhar com campos de formulário PDF interativos.
1. Chame 'bind_pdf()' para anexar o modelo de formulário PDF.
1. Use 'open()' para ler o arquivo FDF em modo binário.
1. Chame 'import_fdf()' para preencher os campos PDF com dados do arquivo FDF.
1. Salve o PDF atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
