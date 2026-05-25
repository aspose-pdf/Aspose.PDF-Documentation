---
title: Obter informações da página
type: docs
weight: 10
url: /pt/python-net/get-page-info/
description: Aprenda como acessar programaticamente informações ao nível de página em um PDF usando Aspose.PDF for Python. Este guia mostra como recuperar a largura, altura, rotação e deslocamentos de uma página específica em um documento PDF.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obter informações da página PDF usando Aspose.PDF for Python
Abstract: A função extrai a largura, altura, rotação e os deslocamentos horizontal (X) e vertical (Y) de uma página PDF. Essas propriedades são retornadas em pontos e refletem o tamanho físico da página e o posicionamento do conteúdo dentro do PDF. A função imprime os valores recuperados, permitindo que os desenvolvedores compreendam o layout e a orientação da página para manipulação adicional do PDF.
---

A função utilitária ‘get_page_information’ ajuda os desenvolvedores a entender a estrutura e o layout das páginas PDF. Cada página PDF pode ter dimensões, rotação e deslocamentos internos diferentes, o que pode impactar a colocação de conteúdo ou tarefas de automação.

Ela apresenta a recuperação de metadados chave e informações de layout para uma página específica em um arquivo PDF. A API Aspose.PDF Facades fornece detalhes como largura, altura, rotação da página e deslocamentos X/Y. Essas informações são essenciais para tarefas como análise de layout de página, colocação de anotações ou processamento automatizado de PDF.

1. Criar um objeto fachada de PDF.
1. Recuperar dimensões e layout da página.
1. Imprimir ou armazenar os valores recuperados.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```
