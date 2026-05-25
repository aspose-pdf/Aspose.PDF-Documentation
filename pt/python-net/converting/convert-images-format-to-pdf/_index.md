---
title: Converter formatos de imagem para PDF em Python
linktitle: Converter imagens para PDF
type: docs
weight: 60
url: /pt/python-net/convert-images-format-to-pdf/
lastmod: "2026-05-18"
description: Aprenda como converter BMP, CGM, DICOM, PNG, TIFF, EMF, SVG e outros formatos de imagem para PDF em Python com Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Como Converter Imagens para PDF em Python
Abstract: Este artigo fornece um guia abrangente sobre a conversão de vários formatos de imagem para PDF usando Python, aproveitando especificamente a biblioteca Aspose.PDF para Python via .NET. O artigo cobre uma variedade de formatos de imagem, incluindo BMP, CGM, DICOM, EMF, GIF, PNG, SVG e TIFF. Cada seção detalha as etapas necessárias para realizar a conversão, fornecendo trechos de código para ilustrar o processo. Por exemplo, converter BMP para PDF envolve criar um novo documento PDF, definir a posição da imagem, inserir a imagem e salvar o documento. Da mesma forma, para formatos como CGM, DICOM e outros, são descritas opções de carregamento específicas e etapas de processamento. O artigo também destaca as vantagens de usar Aspose.PDF para essas tarefas, como seu suporte a diferentes métodos de codificação e a capacidade de processar imagens de quadro único e de múltiplos quadros.
---

## Conversões relacionadas

- [Converter PDF para formatos de imagem](/pdf/pt/python-net/convert-pdf-to-images-format/) quando você precisar do fluxo de trabalho reverso.
- [Converter HTML para PDF](/pdf/pt/python-net/convert-html-to-pdf/) para conteúdo web e fontes MHTML.
- [Converter outros formatos de arquivo para PDF](/pdf/pt/python-net/convert-other-files-to-pdf/) para EPUB, XPS, texto e outras entradas não‑imagem.

## Conversões de Imagens Python para PDF

**Aspose.PDF for Python via .NET** permite que você converta diferentes formatos de imagens em arquivos PDF. Nossa biblioteca demonstra trechos de código para converter os formatos de imagem mais populares, como - BMP, CGM, DICOM, EMF, JPG, PNG, SVG e TIFF.

## Converter BMP para PDF

Converter arquivos BMP para documento PDF usando a biblioteca **Aspose.PDF for Python via .NET**.

<abbr title="Bitmap Image File">BMP</abbr> imagens são arquivos que possuem extensão. BMP representa arquivos de imagem bitmap que são usados para armazenar imagens digitais em bitmap. Essas imagens são independentes do adaptador gráfico e também são chamadas de formato de arquivo bitmap independente de dispositivo (DIB).

Você pode converter BMP em arquivos PDF com Aspose.PDF for Python via .NET API. Portanto, você pode seguir os passos a seguir para converter imagens BMP:

Etapas para Converter BMP para PDF em Python:

1. Crie um documento PDF vazio.
1. Crie a página que você precisa, por exemplo, criamos A4, mas você pode especificar seu próprio formato.
1. Coloca a imagem (de infile) dentro da página usando o retângulo definido.
1. Salve o documento como PDF.

Então o seguinte trecho de código segue estas etapas e mostra como converter BMP para PDF usando Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter BMP para PDF online**

A Aspose apresenta a você o aplicativo online ["BMP para PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão BMP para PDF usando App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Converter CGM para PDF

Converta um CGM (Computer Graphics Metafile) para PDF (ou outro formato suportado) usando Aspose.PDF for Python via .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> é uma extensão de arquivo para um formato Computer Graphics Metafile comumente usado em CAD (projeto assistido por computador) e aplicações de gráficos de apresentação. CGM é um formato de gráficos vetoriais que suporta três diferentes métodos de codificação: binário (melhor para velocidade de leitura do programa), baseado em caracteres (produz o menor tamanho de arquivo e permite transferências de dados mais rápidas) ou codificação em texto claro (permite que os usuários leiam e modifiquem o arquivo com um editor de texto).

Confira o próximo trecho de código para converter arquivos CGM para o formato PDF.

Etapas para Converter CGM em PDF em Python:

1. Definir caminhos de arquivo
1. Definir opções de carregamento para CGM.
1. Converter CGM para PDF
1. Mensagem de Conversão de Impressão

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Converter DICOM para PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> O formato é o padrão da indústria médica para a criação, armazenamento, transmissão e visualização de imagens médicas digitais e documentos de pacientes examinados.

**Aspose.PDF for Python** permite converter imagens DICOM e SVG, mas por razões técnicas ao adicionar imagens você precisa especificar o tipo de arquivo a ser adicionado ao PDF.

O trecho de código a seguir mostra como converter arquivos DICOM para o formato PDF com Aspose.PDF. Você deve carregar a imagem DICOM, colocar a imagem em uma página de um arquivo PDF e salvar a saída como PDF. Usamos a biblioteca adicional pydicom para definir as dimensões desta imagem. Se você quiser posicionar a imagem na página, pode pular este trecho de código.

1. Carregue o arquivo DICOM.
1. Extrair dimensões da imagem.
1. Imprimir tamanho da imagem.
1. Crie um novo documento PDF.
1. Prepare a imagem DICOM para PDF.
1. Defina o tamanho da página PDF e as margens.
1. Adicione a imagem à página.
1. Salvar o PDF.
1. Mensagem de Conversão de Impressão.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter DICOM para PDF online**

A Aspose apresenta a você o aplicativo online ["DICOM para PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão DICOM para PDF usando App](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Converter EMF para PDF

<abbr title="Enhanced metafile format">EMF</abbr> armazena imagens gráficas independentemente do dispositivo. Metafiles de EMF são compostos por registros de comprimento variável em ordem cronológica que podem renderizar a imagem armazenada após a análise em qualquer dispositivo de saída.

O trecho de código a seguir demonstra como converter um EMF para PDF com Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter EMF para PDF online**

A Aspose apresenta a você o aplicativo online ["EMF para PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão EMF para PDF usando App](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Converter GIF para PDF

Converter arquivos GIF em documento PDF usando a biblioteca **Aspose.PDF for Python via .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> é capaz de armazenar dados compactados sem perda de qualidade em um formato de no máximo 256 cores. O formato GIF independente de hardware foi desenvolvido em 1987 (GIF87a) pela CompuServe para transmitir imagens bitmap por redes.

Então o seguinte trecho de código segue estas etapas e mostra como converter BMP para PDF usando Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter GIF para PDF online**

A Aspose apresenta a você o aplicativo online [GIF para PDF](https://products.aspose.app/pdf/conversion/gif-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de GIF para PDF usando o App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Converter PNG para PDF

**Aspose.PDF for Python via .NET** suporta recurso para converter imagens PNG para formato PDF. Verifique o próximo trecho de código para realizar sua tarefa.

<abbr title="Portable Network Graphics">PNG</abbr> refere-se a um tipo de formato de arquivo de imagem raster que usa compressão sem perdas, o que o torna popular entre seus usuários.

Você pode converter PNG para imagem PDF usando as etapas abaixo:

1. Criar um Novo Documento PDF.
1. Definir Posicionamento de Imagem.
1. Salvar o PDF.
1. Mensagem de Conversão de Impressão.

Além disso, o trecho de código abaixo mostra como converter PNG para PDF com Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter PNG para PDF online**

A Aspose apresenta a você o aplicativo online [PNG para PDF](https://products.aspose.app/pdf/conversion/png-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PNG para PDF usando App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Converter SVG para PDF

**Aspose.PDF for Python via .NET** explica como converter imagens SVG para formato PDF e como obter as dimensões do arquivo SVG de origem.

Scalable Vector Graphics (SVG) é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está sendo desenvolvido pelo World Wide Web Consortium (W3C) desde 1999.

<abbr title="Scalable Vector Graphics">SVG</abbr> as imagens e seus comportamentos são definidos em arquivos de texto XML. Isso significa que podem ser pesquisadas, indexadas, scriptadas e, se necessário, compactadas. Como arquivos XML, imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas muitas vezes é mais conveniente criá‑las com programas de desenho como o Inkscape.

{{% alert color="success" %}}
**Tente converter o formato SVG para PDF online**

Aspose.PDF for Python via .NET apresenta a você um aplicativo online ["SVG para PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão de SVG para PDF com o App Aspose.PDF](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

O trecho de código a seguir mostra o processo de conversão de um arquivo SVG para o formato PDF com Aspose.PDF for Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Converter TIFF para PDF

**Aspose.PDF** formato de arquivo suportado, seja uma imagem TIFF de quadro único ou de vários quadros. Isso significa que você pode converter a imagem TIFF para PDF.

TIFF ou TIF, Tagged Image File Format, representa imagens raster que destinam‑se ao uso em uma variedade de dispositivos que suportam esse padrão de formato de arquivo. A imagem TIFF pode conter vários quadros com imagens diferentes. O formato de arquivo Aspose.PDF também é suportado, seja ele uma imagem TIFF de quadro único ou de múltiplos quadros.

Você pode converter TIFF para PDF da mesma maneira que os demais formatos de arquivos raster gráficos:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Converter CDR para PDF

O trecho de código a seguir demonstra como carregar um arquivo CorelDRAW (CDR) e salvá-lo como PDF usando 'CdrLoadOptions' no Aspose.PDF for Python via .NET.

1. Crie 'CdrLoadOptions()' para configurar como o arquivo CDR deve ser carregado.
1. Inicialize um objeto Document com o arquivo CDR e as opções de carregamento.
1. Salve o documento como um PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Converter JPEG para PDF

Este exemplo mostra como converter JPEG para arquivo PDF usando Aspose.PDF for Python via .NET.

1. Crie um novo documento PDF.
1. Adicionar uma nova página.
1. Defina o retângulo de posicionamento (tamanho A4: 595x842 pontos).
1. Insira a imagem na página.
1. Salvar o PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
