---
title: Campo de linha única para campo de múltiplas linhas
type: docs
weight: 80
url: /pt/python-net/single-to-multiple/
description: Converta um campo de texto de linha única em um campo de múltiplas linhas em um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Converta um Campo de Texto de Linha Única em um Campo de Múltiplas Linhas em um PDF Usando Python
Abstract: Este exemplo demonstra como converter um campo de texto de linha única em um campo de múltiplas linhas em um documento PDF usando Aspose.PDF for Python. O código carrega um formulário PDF existente, modifica o campo especificado para permitir várias linhas de texto e salva o documento atualizado.
---

Formulários PDF às vezes contêm campos de texto projetados para entrada de linha única, o que pode não ser suficiente para certos tipos de dados. Com Aspose.PDF for Python, os desenvolvedores podem converter facilmente esses campos em campos de texto de múltiplas linhas sem precisar recriá-los.

Usando o [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class, os desenvolvedores podem modificar campos de texto existentes sem afetar sua posição ou outras propriedades.

1. Carregue o documento PDF existente.
1. Crie uma instância de FormEditor.
1. Vincule o documento PDF ao editor.
1. Converta o campo selecionado para várias linhas.
1. Salve o documento atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```

