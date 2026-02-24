---
title: Adicionando Marca d'água ao PDF usando Python
linktitle: Adicionando Marca d'água
type: docs
weight: 30
url: /pt/python-net/add-watermarks/
description: Este artigo explica os recursos de trabalhar com artefatos e obter marcas d'água em PDFs usando programaticamente o Python.
lastmod: "2025-11-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar marca d'água a PDF com Python
Abstract: O artigo discute o uso do Aspose.PDF para Python via .NET para adicionar marcas d'água a documentos PDF por meio da gestão de artefatos. Ele apresenta as classes principais para manipular artefatos - `Artifact` e `ArtifactCollection` - e descreve como acessá‑las através da propriedade `Artifacts` da classe `Page`. O artigo detalha as propriedades da classe `Artifact`, incluindo atributos como `contents`, `form`, `image`, `text`, `rectangle`, `rotation` e `opacity`, que permitem a manipulação abrangente de artefatos dentro de arquivos PDF. Além disso, é fornecido um exemplo prático, demonstrando como adicionar programaticamente uma marca d'água à primeira página de um PDF usando Python. O trecho de código ilustra a criação e configuração de um `WatermarkArtifact`, definindo seu texto, alinhamento, rotação e opacidade, antes de adicioná‑lo a um documento PDF e salvar as alterações.
---

## Exemplos de Programação: Como Adicionar Marca d'água em Arquivos PDF

Adicionar um artefato de marca d'água a um PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF para Python via .NET. Uma marca d'água é uma sobreposição visual aplicada às páginas para branding, segurança ou fins informativos. O exemplo mostra como configurar a aparência do [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), o posicionamento com [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) e [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), rotação e transparência antes de aplicar a marca d'água a uma [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

1. Crie um artefato de marca d'água (veja [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)).
1. Configure o estado de texto (veja [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)).
1. Vincule o texto à marca d'água.
1. Defina o posicionamento e o estilo usando [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) e [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/).
1. Anexe a marca d'água a uma [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) via a coleção [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página (veja [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)).
1. Salve o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) atualizado usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```


