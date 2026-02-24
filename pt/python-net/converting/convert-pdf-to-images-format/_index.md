---
title: Converter PDF para Diferentes Formatos de Imagem em Python
linktitle: Converter PDF para Imagens
type: docs
weight: 70
url: /pt/python-net/convert-pdf-to-images-format/
lastmod: "2025-09-27"
description: Explore como converter páginas de PDF em imagens como PNG, JPEG ou TIFF usando Aspose.PDF em Python via .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Como Converter PDF para Formatos de Imagem em Python
Abstract: Este artigo fornece um guia abrangente sobre como converter arquivos PDF em vários formatos de imagem usando Python, aproveitando especificamente a biblioteca Aspose.PDF para Python. O documento descreve métodos para converter PDFs para formatos de imagem incluindo TIFF, BMP, EMF, JPG, PNG, GIF e SVG. Duas abordagens principais de conversão são discutidas – usando a abordagem Device e SaveOption. A abordagem Device envolve a utilização de classes como `DocumentDevice` e `ImageDevice` para conversões de documento inteiro ou de página específica. Etapas detalhadas e exemplos de código Python são fornecidos para converter páginas de PDF para diferentes formatos, como TIFF usando `TiffDevice`, e BMP, EMF, JPEG, PNG e GIF usando as respectivas classes de dispositivo (`BmpDevice`, `EmfDevice`, `JpegDevice`, `PngDevice`, `GifDevice`). Para a conversão SVG, a classe `SvgSaveOptions` é apresentada. O artigo também destaca ferramentas online para experimentar essas conversões.
---

## Python Converter PDF para Imagem

**Aspose.PDF for Python** usa várias abordagens para converter PDF em imagem. De modo geral, usamos duas abordagens: conversão usando a abordagem Device e conversão usando SaveOption. Esta seção mostrará como converter documentos PDF para formatos de imagem como BMP, JPEG, GIF, PNG, EMF, TIFF e SVG usando uma dessas abordagens.

Existem várias classes na biblioteca que permitem usar um dispositivo virtual para transformar imagens. DocumentDevice é orientado para a conversão de todo o documento, mas ImageDevice – para uma página específica.

## Converter PDF usando a classe DocumentDevice

**Aspose.PDF for Python** torna possível converter páginas de PDF em imagens TIFF.

A classe [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (baseada em DocumentDevice) permite converter páginas de PDF em imagens TIFF. Esta classe fornece um método chamado [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) que permite converter todas as páginas de um arquivo PDF em uma única imagem TIFF.

{{% alert color="success" %}}
**Tente converter PDF para TIFF online**

Aspose.PDF for Python via .NET apresenta a você o aplicativo gratuito online ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode experimentar a funcionalidade e a qualidade do que ele oferece.

[![Conversão Aspose.PDF de PDF para TIFF com Aplicativo Gratuito](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Converter Páginas de PDF em Uma Imagem TIFF

Aspose.PDF for Python explica como converter todas as páginas de um arquivo PDF em uma única imagem TIFF:

Etapas: Converter PDF para TIFF em Python

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie objetos [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) e [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).
1. Chame o método [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) para converter o documento PDF em TIFF.
1. Para definir as propriedades do arquivo de saída, use a classe [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

O trecho de código a seguir mostra como converter todas as páginas PDF em uma única imagem TIFF.

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    resolution = apdf.devices.Resolution(300)
    tiffSettings = apdf.devices.TiffSettings()
    tiffSettings.compression = apdf.devices.CompressionType.LZW
    tiffSettings.depth = apdf.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = apdf.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, path_outfile)

    print(infile + " converted into " + outfile)
```

## Converter PDF usando a classe ImageDevice

`ImageDevice` é a classe ancestral de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` e `EmfDevice`.

- A classe [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) permite converter páginas de PDF em imagens <abbr title="Bitmap Image File">BMP</abbr>.
- A classe [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) permite converter páginas de PDF em imagens <abbr title="Enhanced Meta File">EMF</abbr>.
- A classe [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) permite converter páginas de PDF em imagens JPEG.
- A classe [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) permite converter páginas de PDF em imagens <abbr title="Portable Network Graphics">PNG</abbr>.
- A classe [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) permite converter páginas de PDF em imagens <abbr title="Graphics Interchange Format">GIF</abbr>.

Vamos dar uma olhada em como converter uma página de PDF em uma imagem.

A classe [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) fornece um método chamado [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) que permite converter uma página específica do arquivo PDF para o formato de imagem BMP. As outras classes têm o mesmo método. Portanto, se precisarmos converter uma página de PDF em uma imagem, basta instanciar a classe necessária.

Os passos a seguir e o trecho de código em Python mostram essa possibilidade:

- [Converter PDF para BMP em Python](#python-pdf-to-image)
- [Converter PDF para EMF em Python](#python-pdf-to-image)
- [Converter PDF para JPG em Python](#python-pdf-to-image)
- [Converter PDF para PNG em Python](#python-pdf-to-image)
- [Converter PDF para GIF em Python](#python-pdf-to-image)

Etapas: PDF para Imagem (BMP, EMF, JPG, PNG, GIF) em Python

1. Carregue o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie uma instância da subclasse de [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/), ou seja.
* [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (para converter PDF em BMP)
* [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (para converter PDF em Emf)
* [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (para converter PDF em JPG)
* [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (para converter PDF em PNG)
* [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (para converter PDF em GIF)
1. Chame o método [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) para realizar a conversão de PDF em imagem.

### Converter PDF em BMP

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Converter PDF em EMF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### Converter PDF em JPEG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```


### Converter PDF em PNG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)

    device = apdf.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Converter PDF em PNG com fonte padrão

```python

    from os import path
    import aspose.pdf as ap
    from io import FileIO


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Converter PDF em GIF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como exemplo de como nossas aplicações gratuitas funcionam, veja o próximo recurso.

Aspose.PDF for Python apresenta a você a aplicação gratuita online ["PDF para PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode experimentar a funcionalidade e a qualidade com que ela funciona.

[![Como converter PDF para PNG usando o Aplicativo Gratuito](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF usando a classe SaveOptions

Esta parte do artigo mostra como converter PDF para <abbr title="Scalable Vector Graphics">SVG</abbr> usando Python e a classe SaveOptions.

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF for Python via .NET apresenta a você a aplicação gratuita online ["PDF para SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para SVG com Aplicativo Gratuito](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

Imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que podem ser pesquisados, indexados, scriptados e, se necessário, comprimidos. Como arquivos XML, imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas muitas vezes é mais conveniente criá‑las com programas de desenho como o Inkscape.

Aspose.PDF for Python oferece o recurso de converter imagem SVG para formato PDF e também permite converter arquivos PDF para formato SVG. Para atender a essa necessidade, a classe [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) foi introduzida no namespace Aspose.PDF. Instancie um objeto SvgSaveOptions e passe‑o como segundo argumento ao método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

O trecho de código a seguir mostra as etapas para converter um arquivo PDF para o formato SVG com Python.

Etapas: Converter PDF para SVG em Python

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie um objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) com as configurações necessárias.
1. Chame o método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) e passe o objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) para converter o documento PDF em SVG.

### Converter PDF para SVG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    save_options = apdf.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

