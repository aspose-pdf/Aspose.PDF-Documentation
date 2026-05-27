---
title: Adicionar marcas d'água ao PDF em Python
linktitle: Adicionando marca d'água
type: docs
weight: 30
url: /pt/python-net/add-watermarks/
description: Aprenda como adicionar artefatos de marca d'água a arquivos PDF em Python usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar marca d'água ao PDF com Python
Abstract: O artigo discute o uso do Aspose.PDF for Python via .NET para adicionar marcas d'água a documentos PDF por meio da gestão de artifacts. Ele apresenta as classes principais para manipular artifacts – `Artifact` e `ArtifactCollection` – e descreve como acessá‑las através da propriedade `Artifacts` da classe `Page`. O artigo detalha as propriedades da classe `Artifact`, incluindo atributos como `contents`, `form`, `image`, `text`, `rectangle`, `rotation` e `opacity`, que permitem a manipulação abrangente de artifacts dentro de arquivos PDF. Além disso, é fornecido um exemplo prático, demonstrando como adicionar programaticamente uma marca d'água à primeira página de um PDF usando Python. O trecho de código ilustra a criação e configuração de um `WatermarkArtifact`, definindo seu texto, alinhamento, rotação e opacidade, antes de adicioná‑lo a um documento PDF e salvar as alterações.
---

Adicionar um artefato de marca d'água a um PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF for Python via .NET. Uma marca d'água é uma sobreposição visual aplicada às páginas para branding, segurança ou fins informacionais. O exemplo mostra como configurar [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) aparência, posicionamento com [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) e [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), rotação e transparência antes de aplicar a marca d'água a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## Extrair marcas d'água de PDF

1. Carregue o documento PDF.
1. Acessar artefatos de página.
1. Filtrar artefatos de marca d'água.
1. Coletar elementos de marca d'água.
1. Extrair propriedades da marca d'água.
1. Exibir informações da marca d'água.

```python
from os import path
import sys
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## Adicionar uma marca d'água ao PDF

Adicionar uma marca d'água de texto a um documento PDF usando Aspose.PDF for Python:

1. Carregue o documento PDF.
1. Criar um estado de texto.
1. Criar um artefato de marca d'água.
1. Definir o texto e o estilo da marca d'água.
1. Configurar posicionamento e rotação.
1. Defina a opacidade e o comportamento de fundo.
1. Anexe a marca d'água a uma página.
1. Salve o documento atualizado.

```python
from os import path
import sys
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

## Remover artefatos de marca d'água da página PDF

Remover artefatos de marca d'água de uma página específica em um documento PDF usando a API Aspose.PDF for Python. A abordagem tem como alvo os elementos de marca d'água armazenados como artefatos de página (especificamente aqueles classificados como subtipos de marca d'água de paginação), itera sobre eles e os exclui antes de salvar o documento atualizado.

1. Carregue o documento PDF.
1. Acessar artefatos de página.
1. Filtrar artefatos de marca d'água.
1. Excluir artefatos de marca d'água.
1. Salve o documento atualizado.

```python
from os import path
import sys
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## Tópicos de Artefatos Relacionados

- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)
- [Adicionar fundos PDF em Python](/pdf/pt/python-net/add-backgrounds/)
- [Adicionar numeração Bates ao PDF em Python](/pdf/pt/python-net/add-bates-numbering/)
- [Contar tipos de artefato em arquivos PDF](/pdf/pt/python-net/counting-artifacts/)