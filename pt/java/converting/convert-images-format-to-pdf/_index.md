---
title: Converter vários formatos de imagens para PDF 
linktitle: Converter Imagens para PDF
type: docs
weight: 60
url: /pt/java/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Este tópico mostra como a biblioteca Aspose.PDF para Java permite converter vários formatos de imagens para PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF para Java** permite que você converta diferentes formatos de imagens em arquivos PDF. Nossa biblioteca demonstra trechos de código para converter os formatos de imagem mais populares, como - BMP, CGM, DICOM, EMF, JPG, PNG, SVG e TIFF.

## Converter BMP para PDF

Converta arquivos BMP para documento PDF usando a biblioteca **Aspose.PDF para Java**.

Imagens <abbr title="Bitmap Image File">BMP</abbr> são arquivos com extensão .BMP que representam arquivos de imagem Bitmap usados para armazenar imagens digitais bitmap. Essas imagens são independentes do adaptador gráfico e também são chamadas de formato de arquivo bitmap independente de dispositivo (DIB).
Você pode converter BMP para PDF com a API Aspose.PDF para Java.
 Portanto, você pode seguir os seguintes passos para converter imagens BMP:

1. Inicialize um novo Documento
1. Carregue o arquivo de imagem BMP de exemplo
1. Finalmente, salve o arquivo PDF de saída

Então, o trecho de código a seguir segue essas etapas e mostra como converter BMP para PDF usando Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // Inicialize o objeto do documento
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // Carregue o arquivo de imagem BMP de exemplo
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // Salve o documento PDF de saída
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Tente converter BMP para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["BMP para PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão BMP para PDF usando Aplicativo Gratuito](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Converter CGM para PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> é um padrão ISO que fornece um formato de arquivo de imagem 2D baseado em vetor para o armazenamento e recuperação de informações gráficas. CGM é um formato independente de dispositivo. CGM é um formato de gráficos vetoriais que suporta três métodos diferentes de codificação: binário (melhor para velocidade de leitura do programa), baseado em caracteres (produz o menor tamanho de arquivo e permite transferências de dados mais rápidas) ou codificação em texto claro (permite que os usuários leiam e modifiquem o arquivo com um editor de texto)

O trecho de código a seguir mostra como converter arquivos CGM para o formato PDF usando o Aspose.PDF para Java.

1. Crie uma classe [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/).
1. Crie uma instância da classe [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) com o nome do arquivo fonte mencionado e opções.
1. Salve o documento com o nome de arquivo desejado.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Crie um CGM LoadOptions
        CgmLoadOptions options = new CgmLoadOptions();

        // Inicialize o objeto do documento
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // Salve o documento PDF de saída
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


## Converter DICOM para PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> é um padrão para manuseio, armazenamento, impressão e transmissão de informações em imagens médicas. Ele inclui uma definição de formato de arquivo e um protocolo de comunicações de rede.

Aspose.PDF para Java permite converter arquivos DICOM para o formato PDF, confira o próximo trecho de código:

1. Carregar imagem no fluxo
1. Inicializar [objeto Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Carregar arquivo de imagem DICOM de exemplo
1. Salvar documento PDF de saída

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Carregar imagem no fluxo
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // Inicializar objeto documento
        Document document = new Document();
        document.getPages().add();
        
        // Carregar arquivo de imagem DICOM de exemplo
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // Salvar documento PDF de saída
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Tente converter DICOM para PDF online**

Aspose apresenta a você uma aplicação online gratuita ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF DICOM para PDF usando App Gratuito](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Converter EMF para PDF

O formato de metarquivo aprimorado (<abbr title="Enhanced metafile format">EMF</abbr>) armazena imagens gráficas de forma independente do dispositivo. Metarquivos EMF são compostos por registros de comprimento variável em ordem cronológica que podem renderizar a imagem armazenada após a análise em qualquer dispositivo de saída.

Temos várias abordagens para converter EMF em PDF.

## Usando a classe Image

Um documento PDF é composto por páginas e cada página contém um ou mais objetos de parágrafo. Um parágrafo pode ser um texto, imagem, tabela, caixa flutuante, gráfico, título, campo de formulário ou um anexo.

Para converter um arquivo de imagem em formato PDF, envolva-o em um parágrafo.

É possível converter imagens em um local físico no disco rígido local, encontrado em uma URL da web ou em uma instância de Stream.

Para adicionar uma imagem:

1. Crie um objeto da classe com.aspose.pdf.Image.
1. Adicione a imagem a uma coleção de [Parágrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) de uma instância de página.
1. Especifique o caminho ou a fonte da Imagem.
    - Se uma imagem estiver em um local no disco rígido, especifique o local do caminho usando o método [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - Se uma imagem estiver colocada em um FileInputStream, passe o objeto que contém a imagem para o método [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

O snippet de código a seguir mostra como carregar um objeto de imagem, definir a margem da página, colocar a imagem na página e salvar a saída como PDF.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * Converter EMF para PDF
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // Instanciar Objeto Documento
        Document doc = new Document();
        // Adicionar uma página à coleção de páginas do documento
        Page page = doc.getPages().add();
        // Carregar o arquivo de imagem de origem para o objeto Stream
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // Definir margens para que a imagem se encaixe, etc.
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // Criar um objeto de imagem
        Image image1 = new Image();
        // Adicionar a imagem na coleção de parágrafos da seção
        page.getParagraphs().add(image1);
        // Definir o fluxo de arquivo de imagem
        image1.setImageStream(fs);
        // Salvar o arquivo PDF resultante
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // veja o código abaixo
    } 
}
```


### Adicionar imagem a partir de BufferedImage

Aspose.PDF para Java também oferece o recurso de carregar imagem a partir de uma instância de Stream onde uma imagem pode ser carregada para um objeto BufferedImage e pode ser colocada dentro da coleção de parágrafos do arquivo Pdf.

```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // adiciona uma página à coleção de páginas do arquivo Pdf
    Page page = doc.getPages().add();
    // cria instância de imagem
    Image image1 = new Image();
    // cria instância de BufferedImage
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // escreve a imagem em buffer para a instância de OutputStream
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // adiciona imagem à coleção de parágrafos da primeira página
    page.getParagraphs().add(image1);
    // define o stream da imagem como OutputStream contendo a imagem em buffer
    image1.setImageStream(bais);
    // salva o arquivo PDF resultante
    doc.save("BufferedImage.pdf");
}
```


## Adicionar Imagem usando Operadores de PDF

Cada objeto de página de PDF contém os métodos [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) e [getContents()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getContents--). Recursos podem ser imagens e formulários, por exemplo, enquanto o conteúdo é representado por um conjunto de operadores de PDF. Cada operador tem seu próprio nome e argumento.

Este exemplo usa operadores para adicionar uma imagem a um arquivo PDF.

Para adicionar uma imagem a um arquivo PDF existente:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e abra o documento PDF de entrada.
1. Obtenha a página à qual você deseja adicionar uma imagem.
1. Adicione a imagem à coleção [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) da página.
1. Use operadores para colocar a imagem na página:
   1. Use o operador GSave para salvar o estado gráfico atual.
   1. Use o operador ConcatenateMatrix para especificar onde a imagem será colocada.

1. Use o operador Do para desenhar a imagem na página.
1. Finalmente, use o operador GRestore para salvar o estado gráfico atualizado.
1. Salve o arquivo.

O trecho de código a seguir mostra como adicionar uma imagem a um documento PDF.

```java
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.Pdf-for-Java
// Abra um documento
Document pdfDocument1 = new Document("input.pdf");

// Defina as coordenadas
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Obtenha a página na qual você deseja adicionar a imagem
Page page = pdfDocument1.getPages().get_Item(1);

// Carregue a imagem em um fluxo
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// Adicione uma imagem à coleção de imagens dos recursos da página
page.getResources().getImages().add(imageStream);

// Usando o operador GSave: este operador salva o estado gráfico atual
page.getContents().add(new Operator.GSave());

// Crie objetos Rectangle e Matrix
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// Usando o operador ConcatenateMatrix (concatenar matriz): define como a imagem deve ser posicionada
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// Usando o operador Do: este operador desenha a imagem
page.getContents().add(new Operator.Do(ximage.getName()));

// Usando o operador GRestore: este operador restaura o estado gráfico
page.getContents().add(new Operator.GRestore());

// Salve o novo PDF
pdfDocument1.save("Updated_document.pdf");

// Feche o fluxo de imagem
imageStream.close();
```


{{% alert color="success" %}}
**Tente converter EMF para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão EMF para PDF usando Aplicativo Gratuito](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Converter JPG para PDF

Não precisa se perguntar como converter JPG para PDF, pois a biblioteca Apose.PDF para Java tem a melhor solução.

Você pode converter facilmente imagens JPG para PDF com o Aspose.PDF para Java seguindo os passos:

1. Inicialize o objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Carregue a imagem JPG e adicione ao parágrafo
1. Salve o PDF de saída

O trecho de código abaixo mostra como converter uma imagem JPG para PDF usando Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

    private static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Inicializar objeto de documento
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Carregar arquivo de imagem JPEG de exemplo
        image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
        page.getParagraphs().add(image);

        // Salvar documento PDF de saída
        document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Tente converter JPG para PDF online**

Aspose apresenta a você o aplicativo online gratuito ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Convertion JPG to PDF using Free App](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Converter PNG para PDF

**Aspose.PDF para Java** suporta o recurso de converter imagens PNG para o formato PDF. Confira o próximo trecho de código para realizar sua tarefa.

<abbr title="Portable Network Graphics">PNG</abbr> refere-se a um tipo de formato de arquivo de imagem raster que usa compressão sem perdas, o que o torna popular entre seus usuários.

Você pode converter PNG para imagem PDF usando as etapas abaixo:

1. Carregar imagem PNG de entrada
1. Ler valores de altura e largura
1. Criar novo documento e adicionar Página
1. Definir dimensões da página
1. Salvar arquivo de saída

Além disso, o trecho de código abaixo mostra como converter PNG para PDF em suas aplicações Java:

```java
package com.aspose.pdf.examples;

/**
 * Converter PNG para PDF
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Inicializar objeto do documento
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Carregar arquivo de imagem BMP de exemplo
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());


        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight (0);
        page.getPageInfo().getMargin().setLeft (0);
        page.getParagraphs().add(image);

        // Salvar documento PDF de saída
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Tente converter PNG para PDF online**

A Aspose apresenta a você o aplicativo online gratuito ["PNG para PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PNG para PDF usando Aplicativo Gratuito](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Converter SVG para PDF

Gráficos Vetoriais Escaláveis (SVG) é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo Consórcio World Wide Web (W3C) desde 1999.

Imagens SVG e seus comportamentos são definidos em arquivos de texto XML.
 Isso significa que eles podem ser pesquisados, indexados, scriptados e, se necessário, comprimidos. Como arquivos XML, as imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas muitas vezes é mais conveniente criá-las com programas de desenho, como o Inkscape.

## Como converter arquivo SVG para formato PDF

Para converter arquivos SVG para PDF, use a classe chamada [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) que é usada para inicializar o objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Posteriormente, este objeto é passado como um argumento durante a inicialização do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) e ajuda o motor de renderização de PDF a determinar o formato de entrada do documento fonte.

O trecho de código a seguir mostra o processo de conversão de arquivo SVG para o formato PDF.

```java
// Inicializar objeto de documento

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();

SvgLoadOptions option = new SvgLoadOptions();
Document pdfDocument = new Document(svgDocumentFileName, option);
pdfDocument.save(pdfDocumentFileName);
```

{{% alert color="success" %}}
**Tente converter o formato SVG para PDF online**

Aspose.PDF para Java apresenta a você a aplicação online gratuita ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade de seu funcionamento.

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Converter TIFF para PDF

**Aspose.PDF para Java** suporta o formato de arquivo, seja uma imagem <abbr title="Tag Image File Format">TIFF</abbr> de um único quadro ou de múltiplos quadros. Isso significa que você pode converter a imagem TIFF para PDF em suas aplicações Java.

TIFF ou TIF, Tagged Image File Format, representa imagens rasterizadas que são destinadas ao uso em uma variedade de dispositivos que estão em conformidade com este padrão de formato de arquivo.
 A imagem TIFF pode conter várias frames com imagens diferentes. O formato de arquivo Aspose.PDF também é suportado, seja uma imagem TIFF de um único frame ou de múltiplos frames. Assim, você pode converter a imagem TIFF para PDF em suas aplicações Java. Portanto, consideraremos um exemplo de conversão de imagem TIFF de múltiplas páginas para documento PDF de múltiplas páginas com os passos abaixo:

1. Instanciar uma instância da classe Document
1. Carregar a imagem TIFF de entrada
1. Finalmente, salvar a imagem como página PDF

Além disso, o seguinte trecho de código mostra como converter uma imagem TIFF de múltiplas páginas ou múltiplos frames para PDF:

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Image;
import com.aspose.pdf.Page;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Converter TIFF para PDF.
 */
public final class ConvertTIFFtoPDF {

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertTIFFtoPDF() {
    }

    public static void run() throws IOException {
        // Inicializar objeto de documento
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        image.setFile(Paths.get(DATA_DIR.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // Salvar documento PDF de saída
        document.save(Paths.get(DATA_DIR.toString(), "TIFFtoPDF.pdf").toString());
        document.close();
    }    
}
```