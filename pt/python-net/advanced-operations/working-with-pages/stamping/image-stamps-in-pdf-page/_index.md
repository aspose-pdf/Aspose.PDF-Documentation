---
title: Adicionando carimbos de imagem em PDF usando Python
linktitle: Carimbos de imagem em arquivo PDF
type: docs
weight: 10
url: /pt/python-net/image-stamps-in-pdf-page/
description: Adicione o Carimbo de Imagem no seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF para Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar carimbos de imagem em PDF usando Python
Abstract: Este artigo fornece um guia abrangente sobre como adicionar carimbos de imagem a arquivos PDF usando a biblioteca Aspose.PDF para Python. Ele detalha o uso da classe `ImageStamp`, que permite a personalização de carimbos baseados em imagens, incluindo propriedades como altura, largura, opacidade e rotação. O processo envolve a criação de um objeto `Document` e de um objeto `ImageStamp` com as propriedades desejadas, e então a adição do carimbo a uma página específica do PDF usando o método `add_stamp()`. O artigo inclui trechos de código Python que demonstram como aplicar um carimbo de imagem a um PDF e controlar sua qualidade usando a propriedade `quality`, que ajusta a qualidade da imagem em termos percentuais. Além disso, o artigo explica como usar carimbos de imagem como fundos em caixas flutuantes com a classe `FloatingBox`, fornecendo outro exemplo de código para mostrar como isso pode ser implementado. Este guia serve como um recurso útil para desenvolvedores que desejam aprimorar PDFs com carimbos de imagem usando Aspose.PDF.
---

## Adicionando Carimbo de Imagem em Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) para adicionar um carimbo de imagem a um arquivo PDF. A classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) fornece as propriedades necessárias para criar um carimbo baseado em imagem, como altura, largura, opacidade e assim por diante. O carimbo pode ser posicionado, redimensionado, girado e tornado parcialmente transparente, permitindo marca d'água, branding ou anotações.

O trecho de código a seguir mostra como adicionar um carimbo de imagem no arquivo PDF.

1. Carregue o PDF usando 'ap.Document()'.
1. Crie um carimbo de imagem com 'ImageStamp()'.
1. Configure as propriedades do carimbo.
1. Adicione o carimbo à página alvo.
1. Salve o PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Controle da Qualidade da Imagem ao Adicionar o Carimbo

Ao adicionar uma imagem como objeto de carimbo, você pode controlar a qualidade da imagem. A propriedade [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) da classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) é usada para esse fim. Ela indica a qualidade da imagem em porcentagem (valores válidos são 0..100).
Definindo a propriedade quality, você pode reduzir a resolução da imagem para otimizar o tamanho do PDF ou manter maior fidelidade para clareza.

1. Abra o documento PDF.
1. Crie um carimbo de imagem.
1. Defina a qualidade da imagem.
1. Adicione o carimbo à página alvo.
1. Salve o PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp_image_control_image_quality(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Carimbo de Imagem como Fundo em Caixa Flutuante

Crie uma [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) em um PDF e aplique uma imagem como fundo. Também mostra como adicionar texto, definir bordas, cor de fundo e posicionar a caixa precisamente na página. Isso é útil para criar conteúdo PDF visualmente rico, como chamadas, banners ou seções destacadas com texto sobre imagens.

1. Abra ou crie um documento PDF.
1. Crie um objeto 'FloatingBox'.
1. Adicione conteúdo de texto à caixa.
1. Defina a borda da caixa e a cor de fundo.
1. Adicione uma imagem de fundo.
1. Adicione o FloatingBox à página.
1. Salve o documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):

    document = ap.Document(infile)
    # Add page to PDF document
    page = document.pages.add()
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```


