---
title: Converter vários formatos de Imagens para PDF
linktitle: Converter Imagens para PDF
type: docs
weight: 60
url: /pt/php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: Este tópico mostra como a biblioteca Aspose.PDF para PHP permite converter vários formatos de imagens para PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF para PHP** permite converter diferentes formatos de imagens para arquivos PDF. Nossa biblioteca demonstra trechos de código para converter os formatos de imagem mais populares, como - BMP, CGM, DMF, JPG, PNG, SVG e TIFF.

## Converter BMP para PDF

Converter arquivos BMP para documento PDF usando a biblioteca **Aspose.PDF para PHP**.

Imagens <abbr title="Bitmap Image File">BMP</abbr> são arquivos com extensão .BMP que representam arquivos de imagem bitmap usados para armazenar imagens digitais bitmap. Estas imagens são independentes do adaptador gráfico e também são chamadas de formato de arquivo bitmap independente de dispositivo (DIB). Você pode converter BMP para PDF com a API Aspose.PDF para PHP.
 Portanto, você pode seguir os seguintes passos para converter imagens BMP:

1. Crie um novo objeto Document
1. Adicione uma nova página ao documento
1. Defina as margens da página para 0 (se necessário)
1. Crie um novo objeto Image e defina o arquivo BMP de entrada
1. Adicione a imagem à página
1. Salve o documento no arquivo PDF de saída

Assim, o seguinte trecho de código segue esses passos e mostra como converter BMP para PDF usando PHP:

```php
// Crie um novo objeto Document
$document = new Document();

// Adicione uma nova página ao documento
$page = $document->getPages()->add();

// Defina as margens da página para 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crie um novo objeto Image e defina o arquivo BMP de entrada
$image = new Image();
$image->setFile($inputFile);

// Adicione a imagem à página
$page->getParagraphs()->add($image);

// Salve o documento no arquivo PDF de saída
$document->save($outputFile);
```

## Converter CGM para PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> é um padrão ISO que fornece um formato de arquivo de imagem 2D baseado em vetor para o armazenamento e recuperação de informações gráficas. CGM é um formato independente de dispositivo. CGM é um formato de gráficos vetoriais que suporta três métodos diferentes de codificação: binário (melhor para velocidade de leitura do programa), baseado em caracteres (produz o menor tamanho de arquivo e permite transferências de dados mais rápidas) ou codificação de texto claro (permite que os usuários leiam e modifiquem o arquivo com um editor de texto)

O trecho de código a seguir mostra como converter arquivos CGM para o formato PDF usando Aspose.PDF para PHP.

1. Crie uma instância de [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) para especificar quaisquer opções específicas para carregar o arquivo CGM.
1. Crie uma instância da classe [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) com o nome do arquivo de origem mencionado e opções.
1. Salve o documento com o nome de arquivo desejado.

```php
$options = new CgmLoadOptions();

// Crie um objeto Document e carregue o arquivo CGM usando as opções especificadas
$document = new Document($inputFile, $options);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```


## Converter DICOM para PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> é um padrão para manuseio, armazenamento, impressão e transmissão de informações em imagens médicas. Ele inclui uma definição de formato de arquivo e um protocolo de comunicação em rede.

Aspose.PDF para PHP permite converter arquivos DICOM para o formato PDF, veja o próximo trecho de código:

1. Crie um novo objeto Document
1. Adicione uma nova página ao documento
1. Defina as margens da página para 0 (se necessário)
1. Crie um novo objeto Image e defina o arquivo BMP de entrada
1. Defina o arquivo DICOM como o arquivo de origem para a imagem
1. Defina o tipo de arquivo da imagem como DICOM
1. Adicione a imagem à página
1. Salve o documento no arquivo PDF de saída

```php
// Crie um novo objeto Document
$document = new Document();

// Adicione uma nova página ao documento
$page = $document->getPages()->add();

// Defina as margens da página para 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crie um novo objeto Image
$image = new Image();

// Defina o arquivo DICOM como o arquivo de origem para a imagem
$image->setFile($inputFile);

// Defina o tipo de arquivo da imagem como DICOM
$image->setFileType(ImageFileType::$Dicom);

// Adicione a imagem à página
$page->getParagraphs()->add($image);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**Tente converter DICOM para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["DICOM para PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), onde você pode experimentar a funcionalidade e a qualidade de seu funcionamento.

[![Aspose.PDF Conversão DICOM para PDF usando App Gratuito](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Converter EMF para PDF

O formato de metarquivo aprimorado (<abbr title="Enhanced metafile format">EMF</abbr>) armazena imagens gráficas de forma independente do dispositivo. Metarquivos de EMF são compostos por registros de comprimento variável em ordem cronológica que podem renderizar a imagem armazenada após o parsing em qualquer dispositivo de saída.

Temos várias abordagens para converter EMF em PDF.

## Usando a classe Image

Um documento PDF é composto por páginas e cada página contém um ou mais objetos parágrafo. Um parágrafo pode ser um texto, imagem, tabela, caixa flutuante, gráfico, título, campo de formulário ou um anexo.

Para converter um arquivo de imagem em formato PDF, envolva-o em um parágrafo.

É possível converter imagens em um local físico no disco rígido local, encontradas em uma URL da web ou em uma instância de Stream.

Para adicionar uma imagem:

1. Crie um objeto da classe com.aspose.pdf.Image.
1. Adicione a imagem a uma coleção de [Parágrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) de uma instância de página.
1. Especifique o caminho ou a fonte da Imagem.
    - Se uma imagem estiver em um local no disco rígido, especifique o local do caminho usando o método [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - Se uma imagem estiver colocada em um FileInputStream, passe o objeto contendo a imagem para o método [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

O trecho de código a seguir mostra como carregar um objeto de imagem, definir a margem da página, colocar a imagem na página e salvar o resultado como PDF.

```php
$inputFile = "sample.emf";

// Crie um novo objeto Document
$document = new Document();

// Adicione uma nova página ao documento
$page = $document->getPages()->add();

// Defina as margens da página como 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crie um novo objeto Image e defina o arquivo de entrada
$image = new Image();
$image->setFile($inputFile);

// Adicione a imagem à página
$page->getParagraphs()->add($image);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```


## Converter JPG para PDF

Não há necessidade de se perguntar como converter JPG para PDF, porque a biblioteca Apose.PDF para PHP tem a melhor solução.

Você pode converter facilmente imagens JPG para PDF com Aspose.PDF para PHP seguindo os passos:

1. Inicialize o objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Adicione uma nova página ao documento
1. Defina as margens da página como 0
1. Crie um novo objeto Image e defina o arquivo de entrada
1. Salve o PDF de saída

O trecho de código abaixo mostra como converter uma imagem JPG para PDF usando PHP:

```php
$inputFile = "sample.jpg";

// Crie um novo objeto Document
$document = new Document();

// Adicione uma nova página ao documento
$page = $document->getPages()->add();

// Defina as margens da página como 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crie um novo objeto Image e defina o arquivo de entrada
$image = new Image();
$image->setFile($inputFile);

// Adicione a imagem à página
$page->getParagraphs()->add($image);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**Tente converter JPG para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["JPG para PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade de seu funcionamento.

[![Aspose.PDF Conversão JPG para PDF usando App Gratuito](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Converter PNG para PDF

**Aspose.PDF para PHP** suporta a funcionalidade de converter imagens PNG para o formato PDF. Verifique o próximo trecho de código para realizar sua tarefa.

<abbr title="Portable Network Graphics">PNG</abbr> refere-se a um tipo de formato de arquivo de imagem raster que usa compressão sem perda, o que o torna popular entre seus usuários.

Você pode converter PNG para imagem PDF usando os passos abaixo:

1. Inicialize o objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Adicione uma nova página ao documento
1. Defina as margens da página para 0
1. Crie um novo objeto de Imagem e defina o arquivo de entrada
1. Salve o PDF de saída

Além disso, o trecho de código abaixo mostra como converter PNG para PDF em suas aplicações PHP:

```php
$inputFile = "sample.png";

// Crie um novo objeto Documento
$document = new Document();

// Adicione uma nova página ao documento
$page = $document->getPages()->add();

// Defina as margens da página para 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crie um novo objeto Imagem e defina o arquivo de entrada
$image = new Image();
$image->setFile($inputFile);

// Adicione a imagem à página
$page->getParagraphs()->add($image);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Tente converter PNG para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["PNG para PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF PNG para PDF usando Aplicativo Gratuito](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

{{% /alert %}}

## Converter SVG para PDF

Gráficos Vetoriais Escaláveis (SVG) é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que tem sido desenvolvido pelo World Wide Web Consortium (W3C) desde 1999.

Imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que eles podem ser pesquisados, indexados, scriptados e, se necessário, comprimidos. Como arquivos XML, imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas é frequentemente mais conveniente criá-las com programas de desenho, como o Inkscape.

## Como converter um arquivo SVG para o formato PDF

Para converter arquivos SVG para PDF, use a classe chamada [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) que é usada para inicializar o objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions).
 Mais tarde, este objeto é passado como um argumento durante a inicialização do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) e ajuda o mecanismo de renderização de PDF a determinar o formato de entrada do documento de origem.

O trecho de código a seguir mostra o processo de conversão de um arquivo SVG para o formato PDF.

```php
// Crie um novo objeto SvgLoadOptions
$loadOption = new SvgLoadOptions();

// Crie um novo objeto Document e carregue o arquivo SVG
$document = new Document($inputFile, $loadOption);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Tente converter o formato SVG para PDF online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF SVG para PDF com Aplicativo Gratuito](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Converter TIFF para PDF

**Aspose.PDF para PHP** formato de arquivo suportado, seja uma imagem <abbr title="Tag Image File Format">TIFF</abbr> de um único quadro ou de múltiplos quadros. Isso significa que você pode converter a imagem TIFF em PDF em suas aplicações Java.

TIFF ou TIF, Formato de Arquivo de Imagem Marcada, representa imagens raster que são destinadas ao uso em uma variedade de dispositivos que cumprem com este padrão de formato de arquivo. A imagem TIFF pode conter vários quadros com diferentes imagens. O formato de arquivo Aspose.PDF também é suportado, seja uma imagem TIFF de um único quadro ou de múltiplos quadros. Assim, você pode converter a imagem TIFF em PDF em suas aplicações Java. Portanto, consideraremos um exemplo de conversão de imagem TIFF de múltiplas páginas em documento PDF de múltiplas páginas com os passos abaixo:

1. Crie um novo objeto Document
1. Adicione uma nova página ao documento
1. Defina as margens da página para 0
1. Crie um novo objeto Image
1. Defina o caminho do arquivo da imagem TIFF de entrada
1. Adicione a imagem à página
1. Salve o documento como um arquivo PDF

Além disso, o seguinte trecho de código mostra como converter uma imagem TIFF de múltiplas páginas ou de múltiplos quadros em PDF:

```php
// Crie um novo objeto Documento
$document = new Document();

// Adicione uma nova página ao documento
$page = $document->getPages()->add();

// Defina as margens da página para 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Crie um novo objeto Imagem
$image = new Image();

// Defina o caminho do arquivo da imagem TIFF de entrada
$image->setFile($inputFile);

// Adicione a imagem à página
$page->getParagraphs()->add($image);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```