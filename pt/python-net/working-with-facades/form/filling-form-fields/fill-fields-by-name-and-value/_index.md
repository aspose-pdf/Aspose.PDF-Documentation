---
title: Preencher Campos por Nome e Valor
type: docs
weight: 60
url: /pt/python-net/fill-fields-by-name-and-value/
description: Este artigo demonstra como preencher dinamicamente múltiplos campos de formulário PDF por nome e valor usando Aspose.PDF for Python via .NET. Em vez de definir cada campo individualmente, ele usa uma estrutura de dicionário para mapear nomes de campos para valores e preenchê-los em um loop.
lastmod: "2026-05-18"
---

Preencher campos de formulário usando uma coleção de nome–valor permite que os desenvolvedores criem soluções escaláveis e flexíveis para automação de formulários PDF. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) é usado para vincular um documento PDF e iterar através de um dicionário de dados de campo. Cada entrada é aplicada usando o método ‘fill_field’, permitindo atualizações em massa eficientes dos campos de formulário.

1. Inicialize ‘pdf_facades.Form()’ para trabalhar com campos de formulário interativos.
1. Use 'bind_pdf()' para anexar o documento PDF de origem.
1. Crie um dicionário contendo nomes de campos e os valores que você deseja inserir.
1. Itere através do dicionário e chame 'fill_field()' para cada entrada.
1. Salve o Document atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```
