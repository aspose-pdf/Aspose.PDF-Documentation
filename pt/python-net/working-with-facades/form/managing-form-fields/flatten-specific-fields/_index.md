---
title: Aplanar Campos Específicos
type: docs
weight: 20
url: /pt/python-net/flatten-specific-fields/
description: Esta seção demonstra como gerenciar e modificar campos de formulário PDF usando Aspose.PDF for Python via .NET. Ela apresenta exemplos práticos de aplainamento de campos específicos, aplainamento de todos os campos de formulário e renomeação de campos existentes programaticamente.
lastmod: "2026-05-18"
---

Gerenciar campos de formulário é uma parte importante dos fluxos de trabalho de processamento de PDF. Aplanar campos remove a interatividade ao converter os elementos do formulário em conteúdo regular da página, enquanto renomear campos ajuda a padronizar convenções de nomenclatura para facilitar o manuseio dos dados.

1. Inicialize pdf_facades.Form() para acessar e gerenciar campos de formulário PDF.
1. Use 'bind_pdf()' para anexar o documento de entrada.
1. Forneça nomes de campo e chame 'flatten_field()' para converter os campos selecionados em conteúdo estático.
1. Chame 'flatten_all_fields()' para remover a interatividade de cada campo de formulário.
1. Defina nomes antigos e novos dos campos e aplique 'rename_field()'.
1. Salve o PDF atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten specific fields
def flatten_specific_fields(infile, outfile):
    """Flatten specific fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten specific fields by their names
    fields_to_flatten = ["First Name", "Last Name"]
    for field_name in fields_to_flatten:
        pdf_form.flatten_field(field_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
