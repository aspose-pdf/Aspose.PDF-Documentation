---
title: Converter vários formatos de Imagens para PDF 
linktitle: Converter Imagens para PDF
type: docs
weight: 60
url: pt/cpp/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Este tópico mostra como a biblioteca Aspose.PDF para C++ permite converter vários formatos de imagens para PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF para C++** permite converter diferentes formatos de imagens para arquivos PDF. Nossa biblioteca demonstra trechos de código para converter os formatos de imagem mais populares, como - formatos BMP, DICOM, EMF, JPG, PNG, SVG e TIFF.

## Converter BMP para PDF

Converta arquivos BMP para documento PDF usando a biblioteca **Aspose.PDF para C++**.

Imagens <abbr title="Arquivo de Imagem Bitmap">BMP</abbr> são arquivos com extensão. BMP representam arquivos de Imagem Bitmap que são usados para armazenar imagens digitais bitmap. Essas imagens são independentes do adaptador gráfico e também são chamadas de formato de arquivo bitmap independente de dispositivo (DIB).
Você pode converter arquivos BMP para PDF com a API Aspose.PDF para C++. Portanto, você pode seguir os seguintes passos para converter imagens BMP:

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para o nome do caminho e o nome do arquivo.
1. Uma instância de um novo objeto Document é criada.
1. Adicione uma nova [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) a este [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Um novo Aspose.Pdf BMP é criado.
1. O objeto Aspose.PDF BMP é inicializado usando o arquivo de entrada.
1. Aspose.PDF BMP é adicionado à Página como um Parágrafo.
1. Finalmente, salve o arquivo PDF de saída

Portanto, o trecho de código a seguir segue essas etapas e mostra como converter BMP para PDF usando C++:

```cpp
void ConvertBMPtoPDF() 
{
    std::clog << "BMP to PDF convert: Start" << std::endl;

    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo de entrada
    String infilename("sample.bmp");

    // String para o nome do arquivo de saída
    String outfilename("ImageToPDF-BMP.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    // Adicionar página vazia no documento vazio
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Adicionar imagem em uma página
    page->get_Paragraphs()->Add(image);

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);

    std::clog << "BMP to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Tente converter BMP para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["BMP para PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão BMP para PDF usando Aplicativo Gratuito](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Converter DICOM para PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> é o padrão da indústria médica para a criação, armazenamento, transmissão e visualização de imagens médicas digitais e documentos de pacientes examinados.

**Aspose.PDF para C++** permite converter imagens DICOM e SVG, mas por razões técnicas para adicionar imagens, você precisa especificar o tipo de arquivo a ser adicionado ao PDF:

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para o nome do caminho e o nome do arquivo.
1. Instantiate [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) Objeto.
1. Adicione uma [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à coleção de páginas do documento.
1. Aspose.PDF TDicom é adicionado à Página como um Parágrafo.
1. Carregue e [Salve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) o arquivo de imagem de entrada.

O código a seguir mostra como converter arquivos DICOM para o formato PDF com Aspose.PDF. Você deve carregar a imagem DICOM, colocar a imagem em uma página em um arquivo PDF e salvar a saída como PDF.

```cpp
void ConvertDICOMtoPDF()
{
    std::clog << "DICOM para PDF conversão: Iniciar" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("CR_Anno.dcm");
    String outfilename("PDFWithDicomImage_out.pdf");

    // Instanciar Objeto Documento
    auto document = MakeObject<Document>();

    // Adicionar uma página à coleção de páginas do documento
    auto page = document->get_Pages()->Add();

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);
    image->set_FileType(Aspose::Pdf::ImageFileType::Dicom);

    page->get_Paragraphs()->Add(image);

    // Salvar a saída como formato PDF
    document->Save(_dataDir + outfilename);
    std::clog << "DICOM para PDF conversão: Terminar" << std::endl;
}
```
{{% alert color="success" %}}
**Tente converter DICOM para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["DICOM para PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão DICOM para PDF usando Aplicativo Gratuito](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Converter EMF para PDF

<abbr title="Formato de metarquivo aprimorado">EMF</abbr>EMF armazena imagens gráficas de forma independente do dispositivo. Metarquivos EMF são compostos por registros de comprimento variável em ordem cronológica que podem renderizar a imagem armazenada após a análise em qualquer dispositivo de saída. Além disso, você pode converter EMF em uma imagem PDF usando as etapas abaixo:

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para o nome do caminho e o nome do arquivo.
1. Uma instância de um novo objeto Documento é criada.
1. Adicione uma nova Página a este [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Um novo Aspose.Pdf TIFF é criado.
1. O objeto Aspose.PDF TIFF é inicializado usando o arquivo de entrada.
1. O Aspose.PDF TIFF é adicionado à Página como um Parágrafo.
1. Carregar e [Salvar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) o arquivo de imagem de entrada.

Além disso, o trecho de código a seguir mostra como converter um EMF para PDF com C++ no seu trecho de código:

```cpp
void ConvertEMFtoPDF() 
{
    std::clog << "EMF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.emf");
    String outfilename("ImageToPDF_emf.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "EMF to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Tente converter EMF para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["EMF para PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão EMF para PDF usando aplicativo gratuito](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Converter JPG para PDF

Não há necessidade de se perguntar como converter JPG para PDF, porque a biblioteca **Aspose.PDF para C++** tem a melhor decisão.

Você pode converter facilmente imagens JPG para PDF com Aspose.PDF para C++ seguindo os passos:

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para o nome do caminho e o nome do arquivo.
1. Uma instância de um novo objeto Document é criada.
1. Adicione uma nova Página a este [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Uma nova Aspose::Pdf::Image é criada.
1. O objeto Aspose.PDF Image é inicializado usando o arquivo de entrada.
1. Aspose.PDF Imagem é adicionada à Página como um Parágrafo.  
1. Carregue e salve o arquivo de imagem de entrada.

O trecho de código abaixo mostra como converter uma imagem JPG para PDF usando C++:

```cpp
void ConvertJPEGtoPDF() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.jpg");

    // String para nome do arquivo de saída
    String outfilename("ImageToPDF-JPEG.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    // Adicionar página vazia em documento vazio
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Adicionar imagem em uma página
    page->get_Paragraphs()->Add(image);

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

Então você pode ver como converter uma imagem para PDF com a **mesma altura e largura da página**. Nós obteremos as dimensões da imagem e, conforme isso, definiremos as dimensões da página do documento PDF com as etapas abaixo:

1. Carregar o arquivo de imagem de entrada
1. Obter a altura e a largura da imagem
1. Definir altura, largura e margens de uma página
1. Salvar o arquivo PDF de saída

O trecho de código a seguir mostra como converter uma imagem em PDF com a mesma altura e largura de página usando C++:

```cpp
void ConvertJPGtoPDF_fitsize() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo de entrada
    String infilename("sample.jpg");

    // String para o nome do arquivo de saída
    String outfilename("ImageToPDF-JPG.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    // Adicionar página vazia no documento vazio
    auto page = document->get_Pages()->Add();
    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Adicionar imagem em uma página
    page->get_Paragraphs()->Add(image);

    // Definir dimensões e margens da página
    page->get_PageInfo()->set_Height(bitMap->get_Height());
    page->get_PageInfo()->set_Width(bitMap->get_Width());
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_Paragraphs()->Add(image);

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Tente converter JPG para PDF online**

A Aspose apresenta a você o aplicativo online gratuito ["JPG para PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF JPG para PDF usando Aplicativo Gratuito](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Converter PNG para PDF

**Aspose.PDF for C++** suporta o recurso de converter imagens PNG para o formato PDF. Confira o próximo trecho de código para realizar sua tarefa.

<abbr title="Portable Network Graphics">PNG</abbr> refere-se a um tipo de formato de arquivo de imagem raster que usa compressão sem perdas, o que o torna popular entre seus usuários.

Você pode converter PNG para imagem PDF usando as etapas abaixo:

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para nome do caminho e nome do arquivo.
1. Uma instância de um novo objeto Documento é criada.
1. Adicione uma nova Página a este [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Um novo Aspose.Pdf PNG é criado.
1. O objeto Aspose.PDF PNG é inicializado usando o arquivo de entrada.
1. Aspose.PDF PNG é adicionado à Página como um Parágrafo.
1. Carregue e salve o arquivo de imagem de entrada.

Além disso, o trecho de código abaixo mostra como converter PNG para PDF em suas aplicações C++:

```cpp
void ConvertPNGtoPDF() 
{
    std::clog << "PNG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.png");

    // String for input file name
    String outfilename("ImageToPDF-PNG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "PNG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Tente converter PNG para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PNG para PDF usando Aplicativo Gratuito](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Converter SVG para PDF

**Aspose.PDF para C++** explica como converter imagens SVG para o formato PDF e como obter as dimensões do arquivo <abbr title="Scalable Vector Graphics">SVG</abbr> de origem.

Gráficos Vetoriais Escaláveis (SVG) é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

Imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que eles podem ser pesquisados, indexados, scriptados e, se necessário, comprimidos. Como arquivos XML, imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas é frequentemente mais conveniente criá-las com programas de desenho, como o Inkscape.

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para o nome do caminho e o nome do arquivo.
1. Crie uma instância da classe [`SvgLoadOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options).
1. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o nome do arquivo de origem mencionado e opções.
1. Salve o documento com o nome de arquivo desejado.

O trecho de código a seguir mostra o processo de conversão de um arquivo SVG para o formato PDF com Aspose.PDF para C++.

```cpp
void ConvertSVGtoPDF() 
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```
Сonsiderar um exemplo com recursos avançados:

```cpp
void ConvertSVGtoPDF_Advanced()
{
    std::clog << "Conversão de SVG para PDF: Início" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("Sweden-Royal-flag-grand-coa.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    options->set_AdjustPageSize(true);
    options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }

    std::clog << "Conversão de SVG para PDF: Final" << std::endl;
}
```

{{% alert color="success" %}}
**Tente converter o formato SVG para PDF online**


Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["SVG para PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Converter TIFF para PDF

O formato de arquivo **Aspose.PDF** é suportado, seja uma imagem <abbr title="Tag Image File Format">TIFF</abbr> de um único quadro ou de vários quadros. Isso significa que você pode converter a imagem TIFF para PDF em suas aplicações C++.

TIFF ou TIF, Tagged Image File Format, representa imagens raster que são destinadas ao uso em uma variedade de dispositivos que cumprem com este padrão de formato de arquivo. A imagem TIFF pode conter vários quadros com imagens diferentes. O formato de arquivo Aspose.PDF também é suportado, seja uma imagem TIFF de um único quadro ou de vários quadros. Assim, você pode converter a imagem TIFF para PDF em suas aplicações C++. Portanto, consideraremos um exemplo de conversão de uma imagem TIFF de várias páginas para um documento PDF de várias páginas com os passos abaixo:

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para nome do caminho e nome do arquivo.
1. Um instance de um novo objeto Document é criado.
1. Adicione uma nova Página a este [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Um novo Aspose.Pdf TIFF é criado.
1. O objeto Aspose.PDF TIFF é inicializado usando o arquivo de entrada.
1. Aspose.PDF TIFF é adicionado à Página como um Parágrafo.
1. Carregue e salve o arquivo de imagem de entrada.

Além disso, o trecho de código a seguir mostra como converter uma imagem TIFF de várias páginas ou quadros para PDF com C++:

```cpp
void ConvertTIFFtoPDF() 
{
    std::clog << "TIFF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.tiff");
    String outfilename("ImageToPDF-TIFF.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "TIFF to PDF convert: Finish" << std::endl;
}
```