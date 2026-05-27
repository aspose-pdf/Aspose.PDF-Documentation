---
title: Aplanar Todos os Campos
type: docs
weight: 10
url: /pt/python-net/flatten-all-fields/
description: Este exemplo demonstra como achatar todos os campos de formulário em um PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF, converter cada elemento de formulário interativo em conteúdo estático de página e salvar o arquivo finalizado.
lastmod: "2026-05-18"
---

Aplainamento remove a interatividade dos formulários PDF ao mesclar os valores dos campos diretamente ao layout do documento. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) é usado para vincular o PDF de origem e aplicar o método flatten_all_fields(), que converte todos os campos em conteúdo não editável.

1. Inicialize pdf_facades.Form() para interagir com os campos de formulário PDF.
1. Chame 'bind_pdf()' para anexar o documento de origem.
1. Chame 'flatten_all_fields()' para converter todos os campos interativos em conteúdo estático.
1. Salve o Document atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```
