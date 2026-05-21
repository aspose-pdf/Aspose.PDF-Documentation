---
title: Preencher Campos de Botão de Rádio
type: docs
weight: 30
url: /pt/python-net/fill-radio-button-fields/
description: Este exemplo demonstra como preencher programaticamente campos de botão de rádio em um formulário PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF, selecionar uma opção de botão de rádio por índice e salvar o arquivo atualizado.
lastmod: "2026-05-18"
---

Botões de rádio permitem que os usuários selecionem uma única opção de um grupo predefinido, como campos de gênero ou preferências. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada do [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo é usado para vincular o PDF de origem e atribuir uma opção selecionada pelo seu valor de índice. Uma vez que a opção desejada é escolhida, o documento modificado é salvo.

1. Inicialize pdf_facades.Form() para gerenciar campos de formulário PDF.
1. Chame 'bind_pdf()' para anexar o PDF que contém campos de botão de rádio.
1. Use 'fill_field()' para selecionar a primeira opção (índice 0).
1. Salve o PDF atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```
