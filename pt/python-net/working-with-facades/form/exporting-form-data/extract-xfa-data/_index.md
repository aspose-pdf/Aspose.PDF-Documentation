---
title: Extrair Dados XFA
type: docs
weight: 50
url: /pt/python-net/extract-xfa-data/
description: Este exemplo explica como extrair os dados de formulário XFA de um arquivo PDF usando Aspose.PDF for Python via .NET. Ele demonstra como vincular um documento PDF baseado em XFA ao facade Form e exportar sua estrutura de dados interna para um fluxo de arquivo.
lastmod: "2026-05-18"
---

Os formulários XFA (XML Forms Architecture) diferem dos AcroForm tradicionais porque seus dados são armazenados como XML dentro do PDF. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto do [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo é usado para vincular o PDF e extrair seus dados XFA diretamente para um arquivo.

1. Crie uma instância de pdf_facades.Form() para gerenciar os dados do formulário.
1. Chame 'bind_pdf()' para anexar o PDF de origem que contém formulários XFA.
1. Use 'FileIO()' para criar um fluxo de arquivo gravável.
1. Chame 'extract_xfa_data()' para exportar os dados XML XFA incorporados.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```
