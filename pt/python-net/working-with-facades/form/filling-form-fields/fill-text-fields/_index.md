---
title: Preencher Campos de Texto
type: docs
weight: 10
url: /pt/python-net/fill-text-fields/
description: Este exemplo demonstra como preencher automaticamente campos de texto em um formulário PDF usando Aspose.PDF for Python via .NET. Ele mostra como carregar um documento PDF, preencher campos de formulário específicos pelo nome e salvar o arquivo atualizado.
lastmod: "2026-05-18"
---

Preencher campos de texto programaticamente permite que aplicativos reutilizem modelos PDF e insiram conteúdo dinâmico sem edição manual. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) é usado para vincular um formulário PDF e atualizar vários campos, como nome, endereço e e‑mail. Após atribuir valores, o PDF modificado é salvo como um novo documento.

1. Inicialize 'pdf_facades.Form()' para gerenciar operações de campos de formulário.
1. Use 'bind_pdf()' para anexar o PDF de entrada que contém campos de texto.
1. Chame 'fill_field()' para inserir dados em campos como nome, endereço e e‑mail.
1. Salve o PDF atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```
