---
title: Renomear Campos de Formulário
type: docs
weight: 30
url: /pt/python-net/rename-form-fields/
description: Este exemplo demonstra como renomear campos de formulário em um documento PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um formulário PDF, atualizar programaticamente os nomes de campos existentes e salvar o arquivo modificado. Renomear campos ajuda a padronizar estruturas de formulários, melhorar o mapeamento de dados e simplificar a integração com fluxos de trabalho automatizados ou sistemas externos.
lastmod: "2026-05-18"
---

Renomear campos de formulário é útil ao alinhar formulários PDF com convenções de nomenclatura internas ou ao preparar documentos para processamento estruturado de dados. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada do [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo é usado para vincular o PDF de origem e aplicar um mapeamento que substitui os nomes antigos dos campos por novos. Após atualizar os identificadores dos campos, o documento é salvo com as alterações aplicadas.

1. Inicialize pdf_facades.Form() para interagir com os campos de formulário PDF.
1. Chame 'bind_pdf()' para anexar o documento PDF.
1. Crie uma lista de tuplas contendo os nomes antigos dos campos e seus respectivos novos nomes.
1. Itere pelo mapeamento e chame 'rename_field()' para cada entrada.
1. Salve o Document atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
