---
title: Importar Dados XFDF
type: docs
weight: 20
url: /pt/python-net/import-xfdf-data/
description: Este exemplo demonstra como importar dados de formulário de um arquivo XFDF para um formulário PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF, ler dados XFDF baseados em XML através de um fluxo de arquivo e preencher automaticamente os campos de formulário correspondentes. Importar dados XFDF possibilita a troca eficiente de dados de formulário e suporta fluxos de trabalho de documentos automatizados que dependem de formatos XML estruturados.
lastmod: "2026-05-18"
---

XFDF (Formato de Dados de Formulários XML) é uma representação XML dos dados de formulário PDF projetada para interoperabilidade e troca de dados. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada do [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo é usado para vincular um formulário PDF e importar valores de campo de um arquivo XFDF externo. Após a importação dos dados, o PDF atualizado é salvo como um novo documento.

1. Inicialize pdf_facades.Form() para interagir com os campos de formulário PDF.
1. Chame 'bind_pdf()' para anexar o modelo de formulário PDF.
1. Use 'open()' para ler o arquivo XFDF.
1. Chame 'import_xfdf()' para preencher os campos PDF com valores do arquivo XFDF.
1. Salve o Document atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
