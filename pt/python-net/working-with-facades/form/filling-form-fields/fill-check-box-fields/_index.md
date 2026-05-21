---
title: Preencher Campos de Caixa de Seleção
type: docs
weight: 20
url: /pt/python-net/fill-check-box-fields/
description: Este exemplo demonstra como preencher programaticamente campos de caixa de seleção em um formulário PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF, atualizar os valores das caixas de seleção pelo nome do campo e salvar o arquivo modificado.
lastmod: "2026-05-18"
---

A caixa de seleção é comumente usada em formulários PDF para representar escolhas binárias, como assinaturas ou confirmações de acordo. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) é usado para acessar os campos do formulário e definir seus valores para o estado selecionado. Após atualizar as caixas de seleção, o PDF preenchido é salvo como um novo documento.

1. Inicialize 'pdf_facades.Form()' para gerenciar interações com campos de formulário.
1. Use 'bind_pdf()' para anexar o PDF de origem contendo campos de caixa de seleção.
1. Chame 'fill_field()' para marcar campos como 'subscribe_newsletter' e 'accept_terms' como selecionados.
1. Salve o Document atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```
