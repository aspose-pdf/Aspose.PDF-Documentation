---
title: Converter PDF para Diferentes Formatos de Imagem em Python
linktitle: Converter PDF para Imagens
type: docs
weight: 70
url: pt/python-java/convert-pdf-to-images-format/
lastmod: "2023-04-06"
description: Este tópico mostra como usar o Aspose.PDF para Python para converter PDF em vários formatos de imagem, por exemplo, TIFF, BMP, EMF, JPEG, PNG, GIF, SVG com algumas linhas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Visão Geral

Este artigo explica como converter PDF para diferentes formatos de imagem usando Python. Ele abrange os seguintes tópicos.

_Formato de Imagem_: **TIFF**
- [Python PDF para TIFF](#python-pdf-to-tiff)
- [Python Converter PDF para TIFF](#python-pdf-to-tiff)
- [Python Converter Páginas Únicas ou Específicas de PDF para TIFF](#python-pdf-to-tiff-pages)


_Formato de Imagem_: **BMP**
- [Python PDF para BMP](#python-pdf-to-bmp)
- [Python Converter PDF para BMP](#python-pdf-to-bmp)
- [Python Conversor de PDF para BMP](#python-pdf-to-bmp)

_Formato de Imagem_: **EMF**
- [Python PDF para EMF](#python-pdf-to-emf)
- [Python Converter PDF para EMF](#python-pdf-to-emf)
 - [Python PDF para EMF Converter](#python-pdf-to-emf)


_Formato de Imagem_: **JPG**
- [Python PDF para JPG](#python-pdf-to-jpg)
- [Python Converter PDF para JPG](#python-pdf-to-jpg)
- [Python PDF para JPG Converter](#python-pdf-to-jpg)


_Formato de Imagem_: **PNG**
- [Python PDF para PNG](#python-pdf-to-png)
- [Python Converter PDF para PNG](#python-pdf-to-png)
- [Python PDF para PNG Converter](#python-pdf-to-png)


_Formato de Imagem_: **GIF**
- [Python PDF para GIF](#python-pdf-to-gif)
- [Python Converter PDF para GIF](#python-pdf-to-gif)
- [Python PDF para GIF Converter](#python-pdf-to-gif)

_Formato de Imagem_: **SVG**
- [Python PDF para SVG](#python-pdf-to-svg)
- [Python Converter PDF para SVG](#python-pdf-to-svg)
- [Python PDF para SVG Converter](#python-pdf-to-svg)

## Python Converter PDF para Imagem

**Aspose.PDF para Python** usa várias abordagens para converter PDF em imagem.
 Geralmente falando, usamos duas abordagens: conversão usando a abordagem Device e conversão usando SaveOption. Esta seção mostrará como converter documentos PDF para formatos de imagem, como BMP, JPEG, GIF, PNG, EMF, TIFF e SVG, usando uma dessas abordagens.

Existem várias classes na biblioteca que permitem usar um dispositivo virtual para transformar imagens. DocumentDevice é orientado para conversão de documento inteiro, mas ImageDevice - para uma página específica.

## Converter PDF usando a classe DocumentDevice

**Aspose.PDF para Python** possibilita converter Páginas PDF para imagens TIFF.

A classe [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/) (baseada em DocumentDevice) permite converter páginas PDF em imagens TIFF. Esta classe fornece um método chamado [`Process`](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) que permite converter todas as páginas em um arquivo PDF para uma única imagem TIFF.

{{% alert color="success" %}}

**Tente converter PDF para TIFF online**
Aspose.PDF for Python via .NET apresenta a você o aplicativo online gratuito ["PDF para TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode experimentar para investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para TIFF com App Gratuito](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Converter Páginas PDF para Uma Imagem TIFF

Aspose.PDF para Python explica como converter todas as páginas em um arquivo PDF para uma única imagem TIFF:

<a name="csharp-pdf-to-tiff"><strong>Passos: Converter PDF para TIFF em Python</strong></a>

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Crie objetos [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) e [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/)

3. Chame o método [TiffDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) para converter o documento PDF para TIFF.
4. Para definir as propriedades do arquivo de saída, use a classe [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/).

O trecho de código a seguir mostra como converter todas as páginas do PDF em uma única imagem TIFF.

```python


from asposepdf import Api, Device

# inicializar licença
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Abrir documento PDF
DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "source.pdf"
output_image = DIR_OUTPUT + "image.tiff"
# Abrir documento PDF
document = Api.Document(input_pdf)
# Criar objeto Resolution
resolution = Device.Resolution(300)

# Criar objeto TiffSettings
tiffSettings = Device.TiffSettings()
tiffSettings._CompressionType = Device.CompressionType.LZW
tiffSettings._ColorDepth = Device.ColorDepth.Default
tiffSettings._Skip_blank_pages = False

# Criar dispositivo TIFF
tiffDevice = Device.TiffDevice(resolution, tiffSettings)

# Converter uma página específica e salvar a imagem no fluxo
tiffDevice.process(document, output_image)
```


## Converter PDF usando a classe ImageDevice

`ImageDevice` é o ancestral de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` e `EmfDevice`.

- A classe [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) permite converter páginas PDF em imagens <abbr title="Bitmap Image File">BMP</abbr>.
- A classe [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) permite converter páginas PDF em imagens <abbr title="Enhanced Meta File">EMF</abbr>.
- A classe [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) permite converter páginas PDF em imagens JPEG.
- A classe [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) permite converter páginas PDF em imagens <abbr title="Portable Network Graphics">PNG</abbr>.

- A classe [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) permite converter páginas PDF em imagens <abbr title="Graphics Interchange Format">GIF</abbr>.

Vamos dar uma olhada em como converter uma página PDF para uma imagem.

A classe [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) fornece um método chamado [Process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) que permite converter uma página específica do arquivo PDF para o formato de imagem BMP. As outras classes possuem o mesmo método. Portanto, se precisarmos converter uma página PDF para uma imagem, basta instanciar a classe necessária.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>

Os seguintes passos e trecho de código em Python mostram essa possibilidade

- [Converter PDF para BMP em Python](#python-pdf-to-image)
- [Converter PDF para EMF em Python](#python-pdf-to-image)
- [Converter PDF para JPG em Python](#python-pdf-to-image)
- [Converter PDF para PNG em Python](#python-pdf-to-image)
- [Converter PDF para GIF em Python](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Passos: PDF para Imagem (BMP, EMF, JPG, PNG, GIF) em Python</strong></a>

1. Carregar o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Criar uma instância da subclasse de [ImageDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/), ou seja,
   * [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) (para converter PDF para BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) (para converter PDF para Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) (para converter PDF para JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) (para converter PDF para PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) (para converter PDF para GIF)
3. Chamar o método [ImageDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/#methods) para realizar a conversão de PDF para Imagem.

### Converter PDF para BMP

```python
from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Criar objeto Resolution
resolution = Device.Resolution(300)
device = Device.BmpDevice(resolution)

for i in range(0, document.getPages.size):
    # Criar nome de arquivo para salvar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.bmp"
    # Converter uma página específica e salvar a imagem no arquivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### Converter PDF para EMF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Criar objeto de Resolução
resolution = Device.Resolution(300)
device = Device.EmfDevice(resolution)

for i in range(0, document.getPages.size):
    # Criar nome de arquivo para salvar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.emf"
    # Converter uma página específica e salvar a imagem no arquivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```  

### Converter PDF para JPEG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Criar objeto de Resolução
resolution = Device.Resolution(300)
device = Device.JpegDevice(resolution)

for i in range(0, document.getPages.size):
    # Criar nome de arquivo para salvar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.jpeg"
    # Converter uma página específica e salvar a imagem no arquivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


### Converter PDF para PNG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Criar objeto Resolution
resolution = Device.Resolution(300)
device = Device.PngDevice(resolution)

for i in range(0, document.getPages.size):
    # Criar nome de arquivo para salvar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.png"
    # Converter uma página específica e salvar a imagem no arquivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 

### Converter PDF para GIF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Criar objeto Resolution
resolution = Device.Resolution(300)
device = Device.GifDevice(resolution)

for i in range(0, document.getPages.size):
    # Criar nome de arquivo para salvar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.gif"
    # Converter uma página específica e salvar a imagem no arquivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como um exemplo de como nossas aplicações gratuitas funcionam, por favor verifique a próxima funcionalidade.

Aspose.PDF para Python apresenta a você uma aplicação online gratuita ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Como converter PDF para PNG usando App Gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF usando a classe SaveOptions

Esta parte do artigo mostra como converter PDF para <abbr title="Gráficos Vetoriais Escaláveis">SVG</abbr> usando Python e a classe SaveOptions.

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF para Python via .NET apresenta a você uma aplicação online gratuita ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF PDF para SVG com App Gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

Imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que eles podem ser pesquisados, indexados, roteirizados e, se necessário, comprimidos. Como arquivos XML, imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas geralmente é mais conveniente criá-las com programas de desenho como o Inkscape.

Aspose.PDF para Python suporta o recurso de converter imagem SVG para formato PDF e também oferece a capacidade de converter arquivos PDF para formato SVG.
 Para cumprir este requisito, a classe [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) foi introduzida no namespace Aspose.PDF. Instancie um objeto de SvgSaveOptions e passe-o como segundo argumento para o método [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

O seguinte trecho de código mostra os passos para converter um arquivo PDF para o formato SVG com Python.

<a name="csharp-pdf-to-svg"><strong>Passos: Converter PDF para SVG em Python</strong></a>

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Crie um objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) com as configurações necessárias.
3. Chame o método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) e passe o objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) para converter o documento PDF em SVG.

### Converter PDF para SVG

```python

from asposepdf import Api

documentName = "testdata/input.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.svg"
doc.save(documentOutName, Api.SaveFormat.Svg)
```