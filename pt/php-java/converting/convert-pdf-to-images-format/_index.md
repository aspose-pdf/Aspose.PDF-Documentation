---
title: Converter PDF para Formatos de Imagens 
linktitle: Converter PDF para Imagens
type: docs
weight: 70
url: /pt/php-java/convert-pdf-to-images-format/
lastmod: "2024-05-20"
description: Este tópico mostra como o Aspose.PDF permite converter PDF para vários formatos de imagens. Converta páginas PDF para imagens PNG, JPEG, BMP com algumas linhas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF para PHP** permite converter documentos PDF para formatos de imagem como BMP, JPEG, GIF, PNG, EMF, TIFF e SVG usando duas abordagens. A conversão é feita usando `Device` e usando `SaveOption`.

Existem várias classes na biblioteca que permitem usar um dispositivo virtual para transformar imagens. `DocumentDevice` é orientado para a conversão de todo o documento, mas `ImageDevice` - para uma página específica.

## Converter PDF usando a classe DocumentDevice

**Aspose.PDF para PHP** possibilita converter Páginas PDF para imagens TIFF.

A [classe TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) permite converter páginas PDF para imagens TIFF.
 Esta classe fornece um método chamado Process que permite converter todas as páginas de um arquivo PDF em uma única imagem TIFF.

### Converter Páginas de PDF em Uma Imagem TIFF

Aspose.PDF para PHP explica como converter todas as páginas em um arquivo PDF em uma única imagem TIFF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Chame o método [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) para converter o documento.
1. Para definir as propriedades do arquivo de saída, use a classe [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

O trecho de código a seguir mostra como converter todas as páginas do PDF em uma única imagem TIFF.

```php
// Carregar o documento PDF
$document = new Document($inputFile);

// Criar um novo objeto TiffSettings
$tiffSettings = new devices_TiffSettings();

// Descomente as seguintes linhas para personalizar as configurações do TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Definir a resolução para a imagem TIFF
$resolution = new devices_Resolution(300);

// Criar um novo objeto TiffDevice com a resolução e configurações especificadas
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Converter o documento PDF para TIFF usando o TiffDevice
$tiffDevice->process($document, $outputFile);
```

### Converter Página Única para Imagem TIFF

Aspose.PDF para PHP permite converter uma página específica em um arquivo PDF para uma imagem TIFF, usando uma versão sobrecarregada do método Process(..) que leva um número de página como argumento para conversão. O trecho de código a seguir mostra como converter a primeira página de um PDF para o formato TIFF.

```php
// Carregar o documento PDF
$document = new Document($inputFile);

// Criar um novo objeto TiffSettings
$tiffSettings = new devices_TiffSettings();

// Descomente as linhas a seguir para personalizar as configurações do TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Definir a resolução para a imagem TIFF
$resolution = new devices_Resolution(300);

// Criar um novo objeto TiffDevice com a resolução e configurações especificadas
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Converter o documento PDF para TIFF usando o TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);
```


### Use o algoritmo Bradley durante a conversão

Aspose.PDF para PHP tem suportado o recurso para converter PDF para TIFF usando compressão LZW e então com o uso de AForge, a Binarização pode ser aplicada. No entanto, um dos clientes solicitou que para algumas imagens, eles precisam obter o Threshold usando Otsu, então eles também gostariam de usar Bradley.

```php
// Criar um novo objeto TiffSettings
$tiffSettings = new devices_TiffSettings();

// Descomente as linhas a seguir para personalizar as configurações de TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Define a resolução para a imagem TIFF
$resolution = new devices_Resolution(300);

// Criar um novo objeto TiffDevice com a resolução e configurações especificadas
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Converter o documento PDF para TIFF usando o TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Criar objeto de stream para salvar a imagem de saída
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


### Converter Páginas de PDF para Imagens TIFF Pixeladas

Para converter todas as páginas de um arquivo PDF para o formato TIFF Pixelado, use a opção Pixelated de IndexedConversionType

```php
// Crie um novo objeto TiffSettings
$tiffSettings = new devices_TiffSettings();

// Descomente as linhas a seguir para personalizar as configurações do TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);
// definir o brilho da imagem
$tiffSettings->setBrightness(0.5f);
// definir o tipo de conversão indexada, o valor padrão é simples
$tiffSettings->setIndexedConversionType(IndexedConversionType::Pixelated);


$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Defina a resolução para a imagem TIFF
$resolution = new devices_Resolution(300);

// Crie um novo objeto TiffDevice com a resolução e configurações especificadas
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Converta o documento PDF para TIFF usando o TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Crie um objeto de fluxo para salvar a imagem de saída
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


{{% alert color="success" %}}
**Tente converter PDF para TIFF online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF para TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão de PDF para TIFF com o Aplicativo Gratuito Aspose.PDF](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Converter PDF usando a classe ImageDevice

`ImageDevice` é o antecessor de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` e `EmfDevice`.

- A classe [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) permite que você converta páginas de PDF em imagens <abbr title="Arquivo de Imagem Bitmap">BMP</abbr>.
- A classe [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) permite que você converta páginas de PDF em imagens <abbr title="Arquivo de Meta Enriquecido">EMF</abbr>.

- A classe [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) permite que você converta páginas de PDF em imagens JPEG.
- A classe [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) permite que você converta páginas de PDF em imagens <abbr title="Portable Network Graphics">PNG</abbr>.
- A classe [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) permite que você converta páginas de PDF em imagens <abbr title="Graphics Interchange Format">GIF</abbr>.

Vamos dar uma olhada em como converter uma página de PDF em uma imagem.

A classe [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) fornece um método chamado [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) que permite converter uma página específica do arquivo PDF para o formato de imagem BMP. As outras classes têm o mesmo método. Portanto, se precisarmos converter uma página de PDF em uma imagem, basta instanciar a classe necessária.

O trecho de código a seguir mostra essa possibilidade:

```php
// Carregar o documento PDF
$document = new Document($inputFile);

// Obter a coleção de páginas no documento
$pages = $document->getPages();

// Obter o número total de páginas no documento
$count = $pages->size();

// Definir a resolução para as imagens PNG
$resolution = new devices_Resolution(300);

// Criar um novo dispositivo PNG com a resolução especificada
$imageDevice = new devices_PngDevice($resolution);

// Percorrer cada página no documento
for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {
    // Definir o nome do arquivo de imagem de saída para a página atual
    $imageFileName = $imageFileNameTemplate . $pageCount . '.png';

    // Obter a página atual da coleção
    $page = $document->getPages()->get_Item($pageCount);

    // Processar a página atual e salvá-la como uma imagem PNG
    $imageDevice->process($page, $imageFileName);
}
```


{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como um exemplo de como nossas aplicações gratuitas funcionam, por favor, verifique o próximo recurso.

Aspose.PDF para PHP apresenta a você a aplicação online gratuita ["PDF para PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Como converter PDF para PNG usando o Aplicativo Gratuito](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF usando a classe SaveOptions

Esta parte do artigo mostra como converter PDF para <abbr title="Scalable Vector Graphics">SVG</abbr> usando Java e a classe SaveOptions.

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF para PHP apresenta a você a aplicação online gratuita ["PDF para SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF PDF para SVG com Aplicativo Gratuito](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

As imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que eles podem ser pesquisados, indexados, programados e, se necessário, comprimidos. Como arquivos XML, as imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas é frequentemente mais conveniente criá-las com programas de desenho como o Inkscape.

### Converter páginas PDF em imagens SVG

Aspose.PDF para PHP suporta o recurso de converter arquivo PDF para o formato SVG.
 Para cumprir este requisito, a classe [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) foi introduzida no pacote com.aspose.pdf. Instancie um objeto de [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) e passe-o como segundo argumento para o método [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O trecho de código a seguir mostra as etapas para converter um arquivo PDF para o formato SVG.

```php
// Carregar o documento PDF
$document = new Document($inputFile);

// Criar uma instância da classe SvgSaveOptions
$saveOption = new SvgSaveOptions();

// Salvar o documento PDF como SVG
$document->save($outputFile, $saveOption);
```