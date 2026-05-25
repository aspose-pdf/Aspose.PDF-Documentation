---
title: Converter PDF para formatos de imagem em Python
linktitle: Converter PDF para imagens
type: docs
weight: 70
url: /pt/python-net/convert-pdf-to-images-format/
lastmod: "2026-05-21"
description: Aprenda como renderizar páginas PDF como arquivos TIFF, BMP, EMF, JPEG, PNG, GIF e SVG em Python com Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Converta páginas PDF para TIFF, PNG, JPEG, GIF, BMP, EMF e SVG em Python.
Abstract: Este artigo explica como converter arquivos PDF para formatos de imagem comuns com Aspose.PDF for Python via .NET. Ele cobre exportação de TIFF em todo o documento com `TiffDevice`, geração de imagens raster por página com subclasses de `ImageDevice` como `BmpDevice`, `JpegDevice`, `PngDevice`, `GifDevice` e `EmfDevice`, e exportação vetorial para SVG com `SvgSaveOptions`. Cada seção inclui as etapas principais e exemplos em Python necessários para salvar o conteúdo do PDF como saída de imagem.
---

## Python Converter PDF para Imagem

**Aspose.PDF for Python via .NET** suporta várias maneiras de converter o conteúdo de PDF em imagens. Na prática, a maioria dos fluxos de trabalho usa uma das duas opções:

- a abordagem Device para renderizar páginas PDF em formatos de imagem raster
- a abordagem SaveOptions para exportar conteúdo PDF para SVG

Este artigo mostra como converter arquivos PDF para TIFF, BMP, EMF, JPEG, PNG, GIF e SVG.

A biblioteca inclui várias classes de renderização. `DocumentDevice` é projetado para conversão de documento inteiro, enquanto `ImageDevice` visa páginas individuais.

## Converter PDF usando a classe DocumentDevice

Use `DocumentDevice` quando você deseja renderizar o PDF inteiro em um único arquivo TIFF multipágina.

O [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) classe é baseada em `DocumentDevice` e fornece o [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) método para converter todas as páginas de um arquivo PDF em uma única saída TIFF.

{{% alert color="success" %}}
**Tente converter PDF para TIFF online**

Aspose.PDF for Python via .NET apresenta-lhe a aplicação online ["PDF para TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para TIFF com App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Converter páginas PDF em uma única imagem TIFF

Aspose.PDF for Python via .NET pode renderizar cada página de um arquivo PDF em uma imagem TIFF.

Passos: Converter PDF para TIFF em Python

1. Carregue o PDF de origem com o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Criar [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) e [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) objetos.
1. Configure as opções TIFF, como compressão, profundidade de cor e tratamento de páginas em branco.
1. Chame o [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) método para gravar o arquivo TIFF.

O trecho de código a seguir mostra como converter todas as páginas do PDF em uma única imagem TIFF.

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_TIFF(infile, outfile):
    document = ap.Document(infile)

    resolution = ap.devices.Resolution(300)
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, f"{outfile}.tiff")

    print(infile + " converted into " + outfile)
```

## Converter PDF usando a classe ImageDevice

Use `ImageDevice` quando você precisa de saída página por página em um formato de imagem raster.

`ImageDevice` é a classe base para `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, e `EmfDevice`.

- O [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) A classe permite converter páginas PDF em imagens BMP.
- O [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) A classe permite converter páginas de PDF em imagens EMF.
- O [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) classe permite converter páginas de PDF em imagens JPEG.
- O [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) classe permite que você converta páginas PDF em imagens PNG.
- O [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) classe permite converter páginas PDF em imagens GIF.

O fluxo de trabalho é o mesmo para cada formato: carregue o documento, crie o dispositivo apropriado e, em seguida, processe a página necessária.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) expõe o [processo](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) método para renderizar uma página específica como BMP. As outras classes de dispositivo de imagem seguem o mesmo padrão, portanto você pode mudar os formatos alterando a classe de dispositivo.

Os links e exemplos de código a seguir mostram como renderizar páginas de PDF para formatos de imagem comuns:

- [Converter PDF para BMP em Python](#convert-pdf-to-bmp)
- [Converter PDF para EMF em Python](#convert-pdf-to-emf)
- [Converter PDF para JPEG em Python](#convert-pdf-to-jpeg)
- [Converter PDF para PNG em Python](#convert-pdf-to-png)
- [Converter PDF para GIF em Python](#convert-pdf-to-gif)

Etapas: PDF para Imagem (BMP, EMF, JPG, PNG, GIF) em Python

1. Carregue o arquivo PDF com o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Crie uma instância do necessário [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) subclasse:
    - [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (para converter PDF para BMP)
    - [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (para converter PDF em EMF)
    - [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (para converter PDF para JPG)
    - [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (para converter PDF em PNG)
    - [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (para converter PDF em GIF)
1. Percorra as páginas que você deseja exportar.
1. Chame o [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) método para salvar cada página como uma imagem.

### Converter PDF para BMP

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_BMP(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Converter PDF para EMF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_EMF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### Converter PDF para JPEG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_JPEG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Converter PDF para PNG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    device = ap.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Converter PDF para PNG com fonte padrão

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG_with_default_font(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Converter PDF para GIF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_GIF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como exemplo de como nossas aplicações funcionam, por favor, verifique a próxima funcionalidade.

Aspose.PDF for Python apresenta a você aplicação online [PDF para PNG](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Como converter PDF para PNG usando o App](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF usando a classe SaveOptions

Use `SaveOptions` quando você quiser exportar o conteúdo do PDF para SVG.

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF for Python via .NET apresenta-lhe a aplicação online ["PDF para SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para SVG com App](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** é um formato baseado em XML para gráficos vetoriais bidimensionais. Como o SVG continua sendo baseado em vetores, ele é útil quando você precisa de saída escalável para web, UI ou fluxos de trabalho de design.

Os arquivos SVG são baseados em texto, pesquisáveis e fáceis de pós-processar em outras ferramentas.

Aspose.PDF for Python via .NET pode tanto converter SVG para PDF quanto exportar páginas de PDF para SVG. Para a conversão de PDF para SVG, crie um [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) objeto e passá-lo para o [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

Os passos a seguir mostram como converter um arquivo PDF para SVG com Python.

Passos: Converter PDF para SVG em Python

1. Carregue o PDF de origem usando o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Criar um [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) objeto e configure as opções necessárias.
1. Chame o [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método com o `SvgSaveOptions` instância para escrever a saída SVG.

### Converter PDF para SVG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_SVG(infile, outfile):
    document = ap.Document(infile)

    save_options = ap.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(f"{outfile}.svg", save_options)
```

## Conversões relacionadas

- [Converter formatos de imagem para PDF](/pdf/pt/python-net/convert-images-format-to-pdf/) quando você precisar reconstruir PDFs a partir de JPG, PNG, TIFF, SVG ou outras fontes de imagem.
- [Converter PDF para HTML](/pdf/pt/python-net/convert-pdf-to-html/) para saída amigável ao navegador em vez de imagens raster.
- [Converter PDF para outros formatos](/pdf/pt/python-net/convert-pdf-to-other-files/) para fluxos de exportação de EPUB, Markdown, texto e XPS.
