---
title: Substituir Dados XFA
type: docs
weight: 50
url: /pt/python-net/replace-xfa-data/
description: Este exemplo demonstra como substituir os dados de formulário XFA existentes em um PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF baseado em XFA, carregar novos dados de um arquivo XFA externo e atualizar o conteúdo do formulário programaticamente.
lastmod: "2026-05-18"
---

Formulários XFA (XML Forms Architecture) armazenam seus dados em formato XML dentro da estrutura do PDF. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada do [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo é usado para vincular um PDF e substituir seu conjunto de dados XFA existente usando um fluxo XML externo. Após aplicar os novos dados, o PDF atualizado é salvo como um arquivo separado.

1. Inicialize pdf_facades.Form() para gerenciar dados de formulário XFA.
1. Chame 'bind_pdf()' para anexar o PDF contendo formulários XFA.
1. Use 'FileIO()' para ler o arquivo XML XFA.
1. Chame 'set_xfa_data()' para atualizar o PDF com novo conteúdo XFA.
1. Salve o Document atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```
