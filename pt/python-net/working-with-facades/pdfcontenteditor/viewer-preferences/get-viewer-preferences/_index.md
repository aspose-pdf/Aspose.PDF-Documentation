---
title: Obter Preferências do Visualizador de PDF
type: docs
weight: 20
url: /pt/python-net/get-viewer-preferences/
description: Como ler e modificar as preferências do visualizador de PDF programaticamente usando Aspose.PDF for Python
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerenciar Preferências do Visualizador de PDF com Aspose.PDF em Python
Abstract: Este guia demonstra como ler e modificar as preferências do visualizador de PDF programaticamente usando Aspose.PDF for Python. As preferências do visualizador controlam como um PDF é exibido ao ser aberto em um visualizador de PDF, como abrir com contornos, ocultar barras de ferramentas ou usar layout de página única.
---

Aspose.PDF fornece ferramentas para acessar e atualizar as preferências do visualizador de PDF. Essas preferências definem o layout inicial e o comportamento de apresentação de um documento PDF nos leitores de PDF. Isso inclui opções como habilitar a visualização de contornos, ocultar barras de menus ou especificar modos de layout de página. Usando PdfContentEditor, você pode recuperar as preferências existentes, verificar flags específicas e atualizá‑las conforme necessário.

1. Definir sinalizadores de ViewerPreference.
1. Inicializar [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) e Vincular PDF.
1. Obter as preferências de visualização atuais.
1. Verificar Flags Específicas.
1. Exibir Preferências Atuais.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_viewer_preferences(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Read current viewer preference flags
    viewer_preference = ViewerPreference(content_editor.get_viewer_preference())
    if viewer_preference & ViewerPreference.PAGE_MODE_USE_OUTLINES:
        print("PageModeUseOutlines is enabled")
    print(f"Current viewer preference: {viewer_preference}")
```
