---
title: Adicionar Link de Ação Personalizada
type: docs
weight: 20
url: /pt/python-net/add-custom-action-link/
description: Este exemplo vincula um PDF de entrada, adiciona um link de ação personalizada na primeira página e salva o documento modificado. Uma lista de ações vazia é usada para simplificar, mas implementações reais podem incluir ações reais.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar um Link de Ação Personalizada a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar um link de ação personalizada a um documento PDF usando Aspose.PDF for Python via the Facades API. Ele mostra como criar uma área clicável em uma página, atribuir uma ação personalizada e salvar o documento atualizado.
---

Links de ação personalizados permitem definir áreas interativas em um PDF que podem disparar ações específicas quando clicadas, como executar scripts, navegar entre páginas ou executar comandos específicos de aplicativos. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode criar um link de ação personalizada especificando a página, o retângulo, a cor e as ações.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Defina um retângulo para o link clicável.
1. Especifique o número da página e a cor do link.
1. Atribua ações personalizadas (vazio neste exemplo).
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```
