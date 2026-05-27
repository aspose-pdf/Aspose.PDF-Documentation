---
title: Preencher caixa de lista
type: docs
weight: 40
url: /pt/python-net/fill-list-box/
description: Este exemplo demonstra como preencher programaticamente caixas de lista e campos de seleção múltipla em um formulário PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF, selecionar valores dentro de um campo de formulário baseado em lista e salvar o arquivo atualizado.
lastmod: "2026-05-18"
---

Campos de caixa de lista e de seleção múltipla permitem que os usuários escolham um ou vários valores de um conjunto pré-definido de opções. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) é usado para acessar o formulário PDF e atribuir um valor selecionado ao campo favorite_colors. Depois que a opção desejada é selecionada, o documento atualizado é salvo.

1. Inicialize 'pdf_facades.Form()' para gerenciar e atualizar os campos de formulário.
1. Chame 'bind_pdf()' para anexar o PDF de origem contendo caixas de lista ou campos de seleção múltipla.
1. Use 'fill_field()' para selecionar um valor entre as opções disponíveis.
1. Salve o Document atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```
