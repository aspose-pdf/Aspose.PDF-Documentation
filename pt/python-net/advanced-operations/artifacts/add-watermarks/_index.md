---
title: Adicionar marcas d'água a PDF em Python
linktitle: Adicionar marcas d'água
type: docs
weight: 30
url: /pt/python-net/add-watermarks/
description: Adicionar artefatos de marca d'água de texto estilizado a páginas de PDF em Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar marcas d'água em um PDF com Python
Abstract: Adicionar artefatos de marca d'água de texto estilizado a páginas de PDF em Python.
---

Usar `WatermarkArtifact` para adicionar uma marca d'água de texto à primeira página de um PDF.

## Adicionar uma marca d'água ao PDF

Defina o texto e o estilo, depois configure o alinhamento, rotação e opacidade. Defina `is_background` para colocar a marca d'água atrás do conteúdo da página.

```python
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)
```

## Tópicos relacionados

- [Extrair Detalhes da Marca d'Água](/pdf/pt/python-net/extract-watermarks/)
- [Remover Marcas d'Água](/pdf/pt/python-net/remove-watermarks/)
- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)
