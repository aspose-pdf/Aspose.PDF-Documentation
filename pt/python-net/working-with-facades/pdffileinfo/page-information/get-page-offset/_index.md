---
title: Obter Deslocamento da Página
type: docs
weight: 20
url: /pt/python-net/get-page-offset/
description: Este exemplo demonstra como usar PdfFileInfo para obter os deslocamentos X e Y de uma página específica e convertê-los em polegadas para análise precisa de layout e posicionamento.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obter Deslocamentos de Página PDF usando Python
Abstract: A função 'get_page_offsets' extrai os deslocamentos horizontais (X) e verticais (Y) de cada página em um arquivo PDF. Esses deslocamentos representam a posição do conteúdo da página em relação à origem do PDF. Ao converter pontos em polegadas, a função fornece medições precisas e legíveis que podem ser usadas para o posicionamento exato de anotações, imagens ou texto. Ela suporta PDFs com várias páginas e destina‑se a desenvolvedores que trabalham com layout de PDF, automação ou tarefas de alinhamento de conteúdo.
---

A função 'get_page_offsets' fornece aos desenvolvedores os deslocamentos horizontais (X) e verticais (Y) exatos das páginas em um arquivo PDF. Em documentos PDF, cada página pode ter um ponto de origem interno que difere do canto superior esquerdo da página, o que pode afetar o posicionamento de texto, imagens, anotações ou outro conteúdo.

Ao usar Aspose.PDF Facades, esta função extrai esses deslocamentos em pontos e os converte para polegadas para fácil interpretação. Ela suporta PDFs de várias páginas, tornando-a adequada para fluxos de trabalho automatizados que exigem posicionamento preciso do conteúdo.

1. Crie o objeto PDF facade.
1. Obtenha o número de páginas no PDF.
1. Percorra cada página para obter os deslocamentos.
1. Imprima ou armazene os deslocamentos.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```
