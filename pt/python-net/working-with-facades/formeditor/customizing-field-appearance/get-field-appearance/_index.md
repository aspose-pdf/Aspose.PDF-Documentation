---
title: Obter Aparência do Campo
type: docs
weight: 20
url: /pt/python-net/get-field-appearance/
description: Este artigo explica como abrir um PDF, acessar um campo de formulário, recuperar suas configurações de aparência e exibí‑las. O exemplo demonstra a recuperação da aparência de um campo chamado "Last Name".
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar Aparência do Campo de Formulário PDF Usando Python
Abstract: Este exemplo demonstra como recuperar as propriedades de aparência visual de um campo de formulário em um documento PDF usando Aspose.PDF for Python. O código abre um PDF existente, acessa um campo de formulário específico e imprime os detalhes da sua aparência, incluindo cor de fundo, cor do texto, cor da borda e alinhamento.
---

Campos de formulário em documentos PDF possuem propriedades visuais como cor de fundo, cor do texto, cor da borda e alinhamento. Com Aspose.PDF for Python, os desenvolvedores podem inspecionar programaticamente essas configurações de aparência usando o [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe.

1. Abra um documento PDF existente.
1. Crie um objeto FormEditor.
1. Recupere as informações de aparência de um campo específico.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))
```
