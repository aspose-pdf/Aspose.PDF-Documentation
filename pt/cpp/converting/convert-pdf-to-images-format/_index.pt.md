---
title: Converter PDF para formatos de Imagens 
linktitle: Converter PDF para Imagens
type: docs
weight: 70
url: /cpp/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter PDF para vários formatos de imagens. Converta páginas PDF para imagens PNG, JPEG, BMP com algumas linhas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** usa algumas abordagens para converter PDF em imagem. De modo geral, usamos duas abordagens: conversão usando a abordagem Device e conversão usando SaveOption. Esta seção mostrará como converter documentos PDF em formatos de imagem como BMP, JPEG, PNG, TIFF e SVG usando uma dessas abordagens.

Existem várias classes na biblioteca que permitem usar um dispositivo virtual para transformar imagens. DocumentDevice é orientado para a conversão de todo o documento, mas ImageDevice - para uma página específica.

## Converter PDF usando a classe DocumentDevice

**Aspose.PDF for C++** torna possível converter Páginas PDF em imagens TIFF.

O [TiffDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) (baseado em DocumentDevice) permite que você converta páginas de PDF em imagens TIFF. Esta classe fornece um método chamado [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device#a0790daa96125c5638a645647e9678f0c) que permite converter todas as páginas em um arquivo PDF em uma única imagem TIFF.

{{% alert color="success" %}}
**Tente converter PDF para TIFF online**

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão de PDF para TIFF com App Gratuito Aspose.PDF](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Converter Páginas de PDF em Uma Imagem TIFF

Aspose.PDF para С++ explica como converter todas as páginas em um arquivo PDF em uma única imagem TIFF:

1. Abra [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) com MakeObject.
1. Crie um objeto Resolution.
1. Crie um objeto [TIffSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_settings/).
1. Crie um [dispositivo Tiff](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) com atributos especificados.
1. Converta uma página específica e salve a imagem em um stream.

O trecho de código a seguir mostra como converter todas as páginas do PDF em uma única imagem TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTIFF()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("PageToTiff.pdf");
    String outfilename("PagesToTIFF_out.tif");

    // Abra o documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Crie um objeto Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Crie um objeto TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
    tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
    tiffSettings->set_SkipBlankPages(false);

    // Crie o dispositivo TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

    // Converta as páginas e salve a imagem no stream
    tiffDevice->Process(document, 1, 2, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
### Converter uma Página para Imagem TIFF

Aspose.PDF para C++ permite converter uma página específica em um arquivo PDF para uma imagem TIFF, utilizando uma versão sobrecarregada do método Process(..) que recebe um número de página como argumento para a conversão. O trecho de código a seguir mostra como converter a primeira página de um PDF para o formato TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo
    String infilename("PageToTiff.pdf");
    String outfilename("PageToTiff_out.tif");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Criar objeto de Resolução
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Criar dispositivo TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

    // Converter uma página específica e salvar a imagem no fluxo
    tiffDevice->Process(document, 1, 1, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Use o algoritmo Bradley durante a conversão

Aspose.PDF para C++ tem suportado o recurso de converter PDF para TIF usando compressão LZW e, em seguida, com o uso de AForge, a binarização pode ser aplicada. No entanto, um dos clientes solicitou que para algumas imagens, eles precisam obter o limiar usando Otsu, então eles também gostariam de usar Bradley.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffBradleyBinarization()
{
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PageToTIFF.pdf");

    String outputImageFile = _dataDir + u"resultant_out.tif";
    String outputBinImageFile = _dataDir + u"37116-bin_out.tif";

    // Criar objeto Resolution 
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Criar objeto TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::LZW);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format1bpp);

    // Criar dispositivo TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);
    auto imageStream = System::IO::File::OpenWrite(_dataDir + outputImageFile);

    // Converter uma página específica e salvar a imagem no stream
    tiffDevice->Process(pdfDocument, 1, 2, imageStream);

    imageStream->Close();

    auto inStream = System::IO::File::OpenRead(outputImageFile);
    auto outStream = System::IO::File::OpenWrite(outputBinImageFile);

    tiffDevice->BinarizeBradley(inStream, outStream, 0.1);
}
```

## Convert PDF usando a classe ImageDevice

`ImageDevice` é o antecessor de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` e `EmfDevice`.

- A classe [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device/) permite converter páginas de PDF para imagens <abbr title="Bitmap Image File">BMP</abbr>.
- A classe [EmfDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.emf_device/) permite converter páginas de PDF para imagens <abbr title="Enhanced Meta File">EMF</abbr>.
- A classe [JpegDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.jpeg_device/) permite converter páginas de PDF para imagens JPEG.
- A classe [PngDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.png_device/) permite converter páginas de PDF para imagens <abbr title="Portable Network Graphics">PNG</abbr>.

- A classe [GifDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.gif_device/) permite converter páginas de PDF para imagens <abbr title="Graphics Interchange Format">GIF</abbr>.

Vamos dar uma olhada em como converter uma página PDF em uma imagem.

A classe [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device) fornece um método chamado [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device#a22cefdb47b7c762320fa7973aa4f1f93) que permite converter uma página específica do arquivo PDF para o formato de imagem BMP. As outras classes têm o mesmo método. Portanto, se precisarmos converter uma página PDF em uma imagem, basta instanciar a classe necessária.

O trecho de código a seguir mostra essa possibilidade:

```cpp
void Convert_PDF_To_Images::ConvertPDFusingImageDevice()
{
    std::clog << __func__ << ": Início" << std::endl;

    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // Criar objeto de Resolução            
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300); //300 dpi

    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    bmpDevice = MakeObject<Aspose::Pdf::Devices::BmpDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    jpegDevice = MakeObject<Aspose::Pdf::Devices::JpegDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    gifDevice = MakeObject<Aspose::Pdf::Devices::GifDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    emfDevice = MakeObject<Aspose::Pdf::Devices::EmfDevice>(resolution);

    auto document = MakeObject<Document>(_dataDir + u"ConvertAllPagesToBmp.pdf");

    ConvertPDFtoImage(bmpDevice, u"bmp", document);
    ConvertPDFtoImage(jpegDevice, u"jpeg", document);
    ConvertPDFtoImage(gifDevice, u"gif", document);
    ConvertPDFtoImage(pngDevice, u"png", document);
    ConvertPDFtoImage(emfDevice, u"emf", document);

    std::clog << __func__ << ": Fim" << std::endl;

}

void Convert_PDF_To_Images::ConvertPDFtoImage(
 System::SmartPtr<Aspose::Pdf::Devices::ImageDevice> imageDevice,
 String ext, System::SmartPtr<Document> document)
{
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    for (int pageCount = 1; pageCount <= document->get_Pages()->get_Count(); pageCount++)
    {
    String outfilename = String::Format(u"{0}PageToBmp{1}_out.{2}",
    _dataDir, pageCount, ext);

    auto imageStream = System::IO::File::OpenWrite(outfilename);

    // Criar objeto de Resolução
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Converter uma página específica e salvar a imagem no stream
    imageDevice->Process(document->get_Pages()->idx_get(pageCount), imageStream);

    // Fechar stream
    imageStream->Close();
    }
}
```

{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como um exemplo de como nossos aplicativos gratuitos funcionam, por favor, confira a próxima funcionalidade.

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["PDF para PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Como converter PDF para PNG usando o aplicativo gratuito](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF usando a classe SaveOptions

Esta parte do artigo mostra como converter PDF para <abbr title="Gráficos Vetoriais Escaláveis">SVG</abbr> usando C++ e a classe SaveOptions.

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["PDF para SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão de PDF para SVG com o aplicativo gratuito da Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

Para converter PDF para SVG, o Aspose.PDF para CPP oferece o método [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Você precisa passar o caminho de saída e o enum SaveFormat:: svg para o método Save para converter PDF para SVG. O trecho de código a seguir mostra como converter PDF para SVG:

Este artigo ensina como converter PDF para <abbr title="Scalable Vector Graphics">SVG</abbr> usando C++.

**Gráficos Vetoriais Escaláveis (SVG)** é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

As imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que eles podem ser pesquisados, indexados, scriptados e, se necessário, comprimidos. Como arquivos XML, imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas geralmente é mais conveniente criá-las com programas de desenho, como o Inkscape.

Aspose.PDF para C++ suporta o recurso de converter imagem SVG para o formato PDF e também oferece a capacidade de converter arquivos PDF para o formato SVG. Para realizar essa exigência, a classe `SvgSaveOptions` foi introduzida no namespace Aspose.PDF. Instancie um objeto de SvgSaveOptions e passe-o como um segundo argumento para o método [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

O seguinte trecho de código mostra as etapas para converter um arquivo PDF para o formato SVG com C++.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoSvgSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("PageToSvg.pdf");
    String outfilename("PageToSvg_out.svg");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar um objeto de SvgSaveOptions
    auto saveOptions = MakeObject<SvgSaveOptions>();
    // Não comprimir imagem SVG para arquivo Zip
    saveOptions->CompressOutputToZipArchive = false;

    try {
    // Salvar a saída em arquivos SVG
    document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```