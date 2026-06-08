---
title: Converter PDF para PowerPoint em Python
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: /pt/python-net/convert-pdf-to-powerpoint/
description: Saiba como converter PDF para PowerPoint em Python, incluindo PDF para PPTX, slides como imagens e resolução de imagem personalizada com Aspose.PDF.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Converter PDF para slides PowerPoint PPTX em Python
Abstract: Este artigo mostra como converter arquivos PDF em apresentações PowerPoint com Aspose.PDF for Python via .NET. Ele cobre a conversão de PDF para PPTX, a conversão de slides em imagens e a definição da resolução da imagem para a saída da apresentação.
---

## Converter PDF para PowerPoint em Python

**Aspose.PDF for Python via .NET** permite converter arquivos PDF em apresentações PowerPoint PPTX a partir de código Python.

Use este fluxo de trabalho quando precisar reutilizar relatórios PDF, apresentações de slides, brochuras ou folhetos como arquivos PowerPoint. Durante a conversão, páginas individuais do PDF são convertidas em slides separados no arquivo PPTX.

Durante a conversão de PDF para PPTX, o texto pode ser renderizado como texto selecionável que você pode atualizar no PowerPoint. Para converter arquivos PDF para o formato PPTX, Aspose.PDF fornece o [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe. Passe um `PptxSaveOptions` objeto como o segundo argumento para o [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

## Converter PDF para PPTX em Python

Para converter PDF para PPTX, use as seguintes etapas de código.

Etapas: Converter PDF para PowerPoint em Python

1. Criar uma instância de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Criar uma instância de [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe.
1. Chame o [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## Converter PDF para PPTX com Slides como Imagens

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF fornece um online ["PDF para PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) aplicação onde você pode testar a qualidade da conversão.


[![Aspose.PDF Conversão PDF para PPTX com App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Caso você precise converter um PDF pesquisável para PPTX como imagens em vez de texto selecionável, o Aspose.PDF oferece esse recurso via [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe. Para isso, defina a propriedade [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) de [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe para 'true' como mostrado no exemplo de código a seguir.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## Converter PDF para PPTX com Resolução de Imagem Personalizada

Este método converte um documento PDF em um arquivo PowerPoint (PPTX) enquanto define uma resolução de imagem personalizada (300 DPI) para melhorar a qualidade.

1. Carregue o PDF em um objeto 'ap.Document'.
1. Crie uma instância de 'PptxSaveOptions'.
1. Defina a propriedade 'image_resolution' para 300 DPI para renderização de alta qualidade.
1. Salve o PDF como um arquivo PPTX usando as opções de salvamento definidas.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## Conversões relacionadas

- [Converter PDF para Word](/pdf/pt/python-net/convert-pdf-to-word/) para saída de documento editável em vez de slides.
- [Converter PDF para Excel](/pdf/pt/python-net/convert-pdf-to-excel/) quando o PDF de origem contém dados empresariais com muitas tabelas.
- [Converter PDF para HTML](/pdf/pt/python-net/convert-pdf-to-html/) para fluxos de trabalho de publicação prontos para o navegador.
