---
title: Converter vários formatos de imagens para PDF em .NET
linktitle: Converter Imagens para PDF
type: docs
weight: 60
url: pt/net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: Converter vários formatos de imagens como BMP, CGM, JPEG, DICOM, PNG, TIFF, EMF e SVG para PDF usando C# .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Visão Geral

Este artigo explica como converter vários formatos de imagens para PDF usando C#. Ele abrange os seguintes tópicos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Formato_: **BMP**
- [C# BMP para PDF](#csharp-bmp-to-pdf)
- [C# Converter BMP para PDF](#csharp-bmp-to-pdf)
- [C# Como converter imagem BMP para PDF](#csharp-bmp-to-pdf)

_Formato_: **CGM**
- [C# CGM para PDF](#csharp-cgm-to-pdf)
- [C# Converter CGM para PDF](#csharp-cgm-to-pdf)
- [C# Como converter imagem CGM para PDF](#csharp-cgm-to-pdf)

_Formato_: **DICOM**
- [C# DICOM para PDF](#csharp-dicom-to-pdf)
- [C# Converter DICOM para PDF](#csharp-dicom-to-pdf)
- [C# Como converter imagem DICOM para PDF](#csharp-dicom-to-pdf)
- [C# Como converter imagem DICOM para PDF](#csharp-dicom-to-pdf)

_Formato_: **EMF**
- [C# EMF para PDF](#csharp-emf-to-pdf)
- [C# Converter EMF para PDF](#csharp-emf-to-pdf)
- [C# Como converter imagem EMF para PDF](#csharp-emf-to-pdf)

_Formato_: **GIF**
- [C# GIF para PDF](#csharp-gif-to-pdf)
- [C# Converter GIF para PDF](#csharp-gif-to-pdf)
- [C# Como converter imagem GIF para PDF](#csharp-gif-to-pdf)

_Formato_: **JPG**
- [C# JPG para PDF](#csharp-jpg-to-pdf)
- [C# Converter JPG para PDF](#csharp-jpg-to-pdf)
- [C# Como converter imagem JPG para PDF](#csharp-jpg-to-pdf)

_Formato_: **PNG**
- [C# PNG para PDF](#csharp-png-to-pdf)
- [C# Converter PNG para PDF](#csharp-png-to-pdf)
- [C# Como converter imagem PNG para PDF](#csharp-png-to-pdf)

_Formato_: **SVG**
- [C# SVG para PDF](#csharp-svg-to-pdf)
- [C# Converter SVG para PDF](#csharp-svg-to-pdf)
- [C# Como converter imagem SVG para PDF](#csharp-svg-to-pdf)

_Formato_: **TIFF**
- [C# TIFF para PDF](#csharp-tiff-to-pdf)
- [C# Converter TIFF para PDF](#csharp-tiff-to-pdf)
- [C# Como converter imagem TIFF para PDF](#csharp-tiff-to-pdf)
- [C# Como converter imagem TIFF para PDF](#csharp-tiff-to-pdf)

Outros tópicos abordados por este artigo
- [Veja Também](#see-also)


## C# Conversões de Imagens para PDF

**Aspose.PDF for .NET** permite converter diferentes formatos de imagens em arquivos PDF. Nossa biblioteca demonstra trechos de código para converter os formatos de imagem mais populares, como - BMP, CGM, DICOM, EMF, JPG, PNG, SVG e formatos TIFF.

## Converter BMP para PDF

Converta arquivos BMP para documento PDF usando a biblioteca **Aspose.PDF for .NET**.

<abbr title="Arquivo de Imagem Bitmap">BMP</abbr> são arquivos com extensão .BMP que representam arquivos de imagem Bitmap usados para armazenar imagens digitais bitmap. Essas imagens são independentes do adaptador gráfico e também são chamadas de formato de arquivo bitmap independente de dispositivo (DIB).
Você pode converter BMP para arquivos PDF com a API Aspose.PDF for .NET. Portanto, você pode seguir os seguintes passos para converter imagens BMP:

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>Passos: Converter BMP para PDF em C#</strong></a>

1.
1.
2. Carregar imagem **BMP** de entrada.
3. Finalmente, salvar o arquivo PDF de saída.

Então, o seguinte trecho de código segue esses passos e mostra como converter BMP para PDF usando C#:

```csharp
//Inicializar documento PDF vazio
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Carregar arquivo de imagem BMP de exemplo
    image.File = dataDir + "Sample.bmp";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Salvar documento PDF de saída
    pdfDocument.Save(dataDir + "BMPtoPDF.pdf");
}
```

{{% alert color="success" %}}
**Tente converter BMP para PDF online**

Aspose apresenta a você aplicação gratuita online ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de BMP para PDF usando Aplicativo Gratuito](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Converter CGM para PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> é uma extensão de arquivo para um formato de Metafile de Gráficos Computacionais comumente usado em aplicativos de CAD (desenho assistido por computador) e gráficos de apresentação.
<abbr title="Computer Graphics Metafile">CGM</abbr> é uma extensão de arquivo para um formato de Metafile de Gráficos Computacionais comumente usado em aplicativos de CAD (projeto auxiliado por computador) e gráficos de apresentação.

Confira o próximo trecho de código para converter arquivos CGM para o formato PDF.

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>Passos: Converter CGM para PDF em C#</strong></a>

1. Crie uma instância da classe [CgmLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/cgmloadoptions).
2. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o nome do arquivo fonte e opções mencionadas.
3. Salve o documento com o nome de arquivo desejado.

```csharp
public static void ConvertCGMtoPDF()
{
    CgmLoadOptions option = new CgmLoadOptions();
    Document pdfDocument= new Document(_dataDir+"corvette.cgm", option);
    pdfDocument.Save(_dataDir+"CGMtoPDF.pdf");
}
```

## Converter DICOM para PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> é o padrão da indústria médica para a criação, armazenamento, transmissão e visualização de imagens médicas digitais e documentos de pacientes examinados.
O formato <abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> é o padrão da indústria médica para a criação, armazenamento, transmissão e visualização de imagens médicas digitais e documentos de pacientes examinados.

**Aspsoe.PDF for .NET** permite converter imagens DICOM e SVG, mas por razões técnicas para adicionar imagens você precisa especificar o tipo de arquivo a ser adicionado ao PDF:

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>Passos: Converter DICOM para PDF em C#</strong></a>

1. Crie um objeto da classe Image.
2. Adicione a imagem à coleção Paragraphs de uma página.
3. Especifique a propriedade [FileType](https://reference.aspose.com/pdf/net/aspose.pdf/image/properties/filetype).
4. Especifique o caminho ou fonte do arquivo.
    - Se uma imagem está localizada em um disco rígido, especifique o local do caminho usando a propriedade Image.File.
    - Se uma imagem está colocada em um MemoryStream, passe o objeto que contém a imagem para a propriedade Image.ImageStream.

O seguinte trecho de código mostra como converter arquivos DICOM para o formato PDF com Aspose.PDF.
O seguinte trecho de código mostra como converter arquivos DICOM para o formato PDF com Aspose.PDF.

```csharp
private const string _dataDir = "..\\..\\..\\..\\Samples";
// Converter imagens DICOM para PDF usando a classe Image
public static void ConvertDICOMtoPDF()
{
    // Instanciar o Objeto Document
    Document pdfDocument = new Document();

    // Adicionar uma página à coleção de páginas do documento
    Page page = pdfDocument.Pages.Add();

    Image image = new Image
    {
        FileType = ImageFileType.Dicom,
        File = System.IO.Path.Combine(_dataDir,"bmode.dcm")
    };
    pdfDocument.Pages[1].Paragraphs.Add(image);
    // Salvar a saída como formato PDF
    pdfDocument.Save(System.IO.Path.Combine(_dataDir,"PDFWithDicomImage_out.pdf"));
}
```

{{% alert color="success" %}}
**Tente converter DICOM para PDF online**

Aspose apresenta a você a aplicação gratuita online ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), onde você pode explorar a funcionalidade e a qualidade com que funciona.
{{% /alert %}}

[![Aspose.PDF Conversão de DICOM para PDF usando App Gratuito](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
## Converter EMF para PDF

<abbr title="Formato de metaarquivo aprimorado">EMF</abbr>EMF armazena imagens gráficas de forma independente do dispositivo. Metaarquivos EMF consistem em registros de comprimento variável em ordem cronológica que podem renderizar a imagem armazenada após análise em qualquer dispositivo de saída. Além disso, você pode converter uma imagem EMF para PDF usando as etapas abaixo:

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>Passos: Converter EMF para PDF em C#</strong></a>

1. Primeiramente, inicialize o objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Carregue o arquivo de imagem **EMF**.
3. Adicione a imagem EMF carregada a uma Página.
4. Salve o documento PDF.

Além disso, o seguinte trecho de código mostra como converter um EMF para PDF com C# no seu trecho de código .NET:

```csharp
// Inicializa novo documento PDF
var doc = new Document();

// Especifique o caminho do arquivo de imagem EMF de entrada
var imageFile = dataDir + "drawing.emf";
var page = doc.Pages.Add();
string file = imageFile;
FileStream filestream = new FileStream(file, FileMode.Open, FileAccess.Read);
BinaryReader reader = new BinaryReader(filestream);
long numBytes = new FileInfo(file).Length;
byte[] bytearray = reader.ReadBytes((int)numBytes);
Stream stream = new MemoryStream(bytearray);
var b = new Bitmap(stream);

// Especifique as propriedades das dimensões da página
page.PageInfo.Margin.Bottom = 0;
page.PageInfo.Margin.Top = 0;
page.PageInfo.Margin.Left = 0;
page.PageInfo.Margin.Right = 0;
page.PageInfo.Width = b.Width;
page.PageInfo.Height = b.Height;
var image = new Aspose.Pdf.Image();
image.File = imageFile;
page.Paragraphs.Add(image);

// Salva o documento PDF de saída
doc.Save(dataDir + "EMFtoPDF.pdf");
```
{{% alert color="success" %}}
**Tente converter EMF para PDF online**

A Aspose apresenta a você uma aplicação gratuita online ["EMF para PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), onde você pode explorar a funcionalidade e a qualidade com que funciona.

[![Conversão de Aspose.PDF de EMF para PDF usando App Gratuito](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Converter GIF para PDF

Converta arquivos GIF para documento PDF usando a biblioteca **Aspose.PDF for .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> é capaz de armazenar dados comprimidos sem perda de qualidade em um formato de no máximo 256 cores. O formato GIF independente de hardware foi desenvolvido em 1987 (GIF87a) pela CompuServe para a transmissão de imagens bitmap em redes.
Você pode converter arquivos GIF para PDF com a API Aspose.PDF for .NET. Portanto, você pode seguir os seguintes passos para converter imagens GIF:

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>Passos: Converter GIF para PDF em C#</strong></a>

1.
1.
2. Carregue a imagem **GIF** de entrada.
3. Finalmente, salve o arquivo PDF de saída.

Portanto, o seguinte trecho de código segue esses passos e mostra como converter BMP para PDF usando C#:

```csharp
//Inicializa documento PDF vazio
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Carrega arquivo de imagem GIF de exemplo
    image.File = dataDir + "Sample.gif";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Salva o documento PDF de saída
    pdfDocument.Save(dataDir + "GIFtoPDF.pdf");
}
```

{{% alert color="success" %}}
**Tente converter GIF para PDF online**

A Aspose apresenta a aplicação gratuita online ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de GIF para PDF usando Aplicativo Gratuito](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Converter JPG para PDF

Não precisa se perguntar como converter JPG para PDF, porque a biblioteca **Apose.PDF for .NET** tem a melhor decisão.
Não há necessidade de se perguntar como converter JPG para PDF, pois a biblioteca **Apose.PDF for .NET** tem a melhor solução.

Você pode converter imagens JPG para PDF com o Aspose.PDF for .NET seguindo os passos:

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>Passos: Converter JPG para PDF em C#</strong></a>

1. Inicialize o objeto da classe [Document](https://reference.aspose.com/page/net/aspose.page/document).
2. Adicione uma nova página ao documento PDF.
3. Carregue a imagem **JPG** e adicione ao parágrafo.
4. Salve o PDF de saída.

O trecho de código abaixo mostra como converter uma imagem JPG para PDF usando C#:

```csharp
// Carrega o arquivo JPG de entrada
String path = dataDir + "Aspose.jpg";

// Inicializa novo documento PDF
Document doc = new Document();

// Adiciona página vazia no documento vazio
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Adiciona imagem na página
page.Paragraphs.Add(image);

// Salva o arquivo PDF de saída
doc.Save(dataDir + "ImagetoPDF.pdf");
```

Então, você pode ver como converter uma imagem para PDF com **a mesma altura e largura da página**.
Então você pode ver como converter uma imagem para PDF com a **mesma altura e largura da página**.

1. Carregar arquivo de imagem de entrada
1. Obter a altura e largura da imagem
1. Definir altura, largura e margens de uma página
1. Salvar o arquivo PDF de saída

O seguinte trecho de código mostra como converter uma Imagem para PDF com a mesma altura e largura da página usando C#:

```csharp
// Carregar arquivo de imagem JPG de entrada
String path = dataDir + "Aspose.jpg";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);

// Ler altura da imagem de entrada
int h = srcImage.Height;

// Ler largura da imagem de entrada
int w = srcImage.Width;

// Inicializar um novo documento PDF
Document doc = new Document();

// Adicionar uma página vazia
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Definir dimensões e margens da página
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Salvar arquivo PDF de saída
doc.Save(dataDir + "ImagetoPDF_HeightWidth.pdf");
```
{{% alert color="success" %}}
**Experimente converter JPG para PDF online**

A Aspose apresenta a você uma aplicação gratuita online ["JPG para PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), onde você pode explorar a funcionalidade e a qualidade com que funciona.

[![Conversão de Aspose.PDF de JPG para PDF usando Aplicativo Gratuito](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Converter PNG para PDF

**Aspose.PDF para .NET** suporta a funcionalidade de converter imagens PNG para o formato PDF. Confira o próximo trecho de código para realizar sua tarefa.

<abbr title="Portable Network Graphics">PNG</abbr> refere-se a um tipo de formato de arquivo de imagem raster que usa compressão sem perdas, o que o torna popular entre seus usuários.

Você pode converter imagens PNG para PDF usando os passos abaixo:

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>Passos: Converter PNG para PDF em C#</strong></a>

1. Carregue a imagem **PNG** de entrada.
2. Leia os valores de altura e largura.
3.
3.
4. Definir dimensões da página.
5. Salvar arquivo de saída.

Além disso, o trecho de código abaixo mostra como converter PNG para PDF com C# em suas aplicações .NET:

```csharp
// Carregar arquivo PNG de entrada
String path = dataDir + "Aspose.png";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);
int h = srcImage.Height;
int w = srcImage.Width;

// Inicializar novo Documento
Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Definir dimensões da página
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Salvar PDF de saída
doc.Save(dataDir + "ImagetoPDF.pdf");
```

{{% alert color="success" %}}
**Tente converter PNG para PDF online**

A Aspose apresenta a você a aplicação gratuita online ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), onde você pode experimentar investigar a funcionalidade e qualidade com que funciona.

Aspose apresenta a você a aplicação gratuita online ["PNG para PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Conversão de Aspose.PDF de PNG para PDF usando Aplicativo Gratuito](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Converter SVG para PDF

**Aspose.PDF para .NET** explica como converter imagens SVG para o formato PDF e como obter as dimensões do arquivo <abbr title="Gráficos Vetoriais Escaláveis">SVG</abbr> fonte.

Gráficos Vetoriais Escaláveis (SVG) é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

Imagens SVG e seus comportamentos são definidos em arquivos de texto XML.
Imagens SVG e seus comportamentos são definidos em arquivos de texto XML.

{{% alert color="success" %}}
**Tente converter o formato SVG para PDF online**

Aspose.PDF para .NET apresenta a você uma aplicação gratuita online ["SVG para PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão de Aspose.PDF de SVG para PDF com Aplicativo Gratuito](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Para converter arquivos SVG para PDF, use a classe chamada [SvgLoadOptions](https://reference.aspose.com/net/pdf/aspose.pdf/svgloadoptions) que é usada para inicializar o objeto [`LoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions). Posteriormente, esse objeto é passado como argumento durante a inicialização do objeto Documento e ajuda o motor de renderização de PDF a determinar o formato de entrada do documento fonte.

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>Passos: Converter SVG para PDF em C#</strong></a>

1.
1.
2. Crie uma instância da classe [`Document`](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o nome do arquivo de origem e opções mencionadas.
3. Salve o documento com o nome de arquivo desejado.

O seguinte trecho de código mostra o processo de conversão de um arquivo SVG em formato PDF com o Aspose.PDF para .NET.

```csharp
public static void ConvertSVGtoPDF()
{
    SvgLoadOptions option = new SvgLoadOptions();
    Document pdfDocument = new Document(_dataDir + "car.svg", option);
    pdfDocument.Save(_dataDir + "svgtest.pdf");
}
```

## Obter dimensões do SVG

Também é possível obter as dimensões do arquivo SVG de origem. Essa informação pode ser útil se quisermos que o SVG cubra toda a página do PDF de saída. A propriedade AdjustPageSize da classe ScgLoadOption cumpre esse requisito. O valor padrão desta propriedade é falso. Se o valor for definido como verdadeiro, o PDF de saída terá o mesmo tamanho (dimensões) que o SVG de origem.

O seguinte trecho de código mostra o processo de obter as dimensões do arquivo SVG de origem e gerar um arquivo PDF.

O seguinte trecho de código mostra o processo de obter as dimensões do arquivo SVG de origem e gerar um arquivo PDF.

```csharp
public static void ConvertSVGtoPDF_Advanced()
{
    // Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // O caminho para o diretório de documentos.
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var loadopt = new SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    var svgDoc = new Document(dataDir + "GetSVGDimensions.svg", loadopt);
    svgDoc.Pages[1].PageInfo.Margin.Top = 0;
    svgDoc.Pages[1].PageInfo.Margin.Left = 0;
    svgDoc.Pages[1].PageInfo.Margin.Bottom = 0;
    svgDoc.Pages[1].PageInfo.Margin.Right = 0;
    svgDoc.Save(dataDir + "GetSVGDimensions_out.pdf");
}
```

### Recursos SVG Suportados

<table>
    <thead>
        <tr>
            <th>
                <p>Tag SVG</p>
            </th>
            <th>
                <p>Exemplo de Uso</p>
            </th>
        </tr>
    </thead>
    <tbody>

<tbody>
    <tr>
        <td>
            <p>círculo</p>
        </td>
        <td>
            <code><pre>&lt;circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt;</pre></code>
        </td>
    </tr>
    <tr>
        <td>
            <p>defs</p>
        </td>
        <td>
            <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
                stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
                cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
                &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
                x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
                x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
                x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
        </td>
    </tr>
</tbody>
```

         </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Dados de caracteres referenciados&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
```
```
font-family="Verdana" font-size="100"
text-anchor="middle" >  
    Texto mascarado  
    </text>  
    <use xlink:href="#Text" fill="azul" />

</p>
</td>
</tr>
<tr>
<td>
    <p>elipse</p>
</td>
<td>
    <p><ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="vermelho" /></p>
</td>
</tr>
<tr>
<td>
    <p>g</p>
</td>
<td>
    <p><g fill="none" stroke="cinza escuro" stroke-width="1.5" >  
        <line x1="-7"
        y1="-7" x2="-3" y2="-3"/>  
        <line x1="7" y1="7" x2="3" y2="3"/>
   </g>
</p>
</td>
</tr>
```

&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
y2="3"/&gt;&nbsp; <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7" y1="7" x2="-3" y2="3"/&gt;&nbsp;
<br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="-7" x2="3" y2="-3"/&gt;&nbsp; <br
    class="atl-forced-newline"> &lt;/g&gt;&nbsp;</p>
</td>
</tr>
<tr>
<td>
    <p>imagem</p>
</td>
<td>
    <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"
        /&gt;&nbsp;</p>
</td>
</tr>
<tr>
<td>
    <p>linha</p>
</td>
<td>
    <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
```

<tr>
    <td>
        <p>linha</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>caminho</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>estilo</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>polígono</p>
    </td>
    <td>
        <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
            /&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>polilinha</p>
```

<p>polilinha</p>
</td>
<td>
    <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
        -3,1 -3,-5"/&gt;</p>
</td>
</tr>
<tr>
<td>
    <p>retângulo&nbsp;</p>
</td>
<td>
    <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
</td>
</tr>
<tr>
<td>
    <p>svg</p>
</td>
<td>
    <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
</td>
</tr>
<tr>
<td>
    <p>texto</p>
</td>
<td>
    <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
        y="30" pointer-events="none"&gt;Título do Mapa&lt;/text&gt;</p>
</td>
```

## Converter TIFF para PDF

**Aspose.PDF** suporta o formato de arquivo, seja uma única imagem ou uma imagem <abbr title="Tag Image File Format">TIFF</abbr> com múltiplos quadros. Isso significa que você pode converter a imagem TIFF para PDF em suas aplicações .NET.

TIFF ou TIF, Tagged Image File Format, representa imagens rasterizadas que são destinadas para uso em uma variedade de dispositivos que estão de acordo com esse padrão de formato de arquivo.
```
TIFF ou TIF, Formato de Arquivo de Imagem Marcada, representa imagens raster que são destinadas para uso em uma variedade de dispositivos que cumprem esse padrão de formato de arquivo.

Você pode converter TIFF para PDF da mesma maneira que os demais formatos de arquivo raster gráficos:

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>Passos: Converter TIFF para PDF em C#</strong></a>

1. Crie um novo objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) e adicione uma Página.
2. Carregue a imagem **TIFF** de entrada.
3. Salve o documento PDF.

```csharp
Inicialize o documento PDF vazio
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Carregar arquivo de imagem Tiff de exemplo
    image.File = dataDir + "sample.tiff";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Salvar o documento PDF de saída
    pdfDocument.Save(dataDir + "TIFFtoPDF.pdf");
}
```

Caso você precise converter uma imagem TIFF de várias páginas para um documento PDF de várias páginas e controlar alguns parâmetros, por exemplo,
Caso precise converter uma imagem TIFF de múltiplas páginas em um documento PDF de múltiplas páginas e controlar alguns parâmetros, por exemplo:

1. Instancie uma instância da classe Document
1. Carregue a imagem TIFF de entrada
1. Obtenha FrameDimension dos quadros
1. Adicione uma nova página para cada quadro
1. Finalmente, salve as imagens nas páginas do PDF

O seguinte trecho de código mostra como converter uma imagem TIFF de múltiplas páginas ou quadros em PDF com C#:

```csharp
public static void TiffToPDF2()
{
    // Inicializa novo Documento
    Document pdf = new Document();

    // Carrega imagem TIFF em stream
    Bitmap bitmap = new Bitmap(File.OpenRead(_dataDir+"multipage.tif"));
    // Converte TIFF de múltiplas páginas ou quadros para PDF
    FrameDimension dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
    int frameCount = bitmap.GetFrameCount(dimension);

    // Itera por cada quadro
    for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
    {
        Page page = pdf.Pages.Add();

        bitmap.SelectActiveFrame(dimension, frameIdx);

        MemoryStream currentImage = new MemoryStream();
        bitmap.Save(currentImage, ImageFormat.Tiff);

        Aspose.Pdf.Image imageht = new Aspose.Pdf.Image
        {
            ImageStream = currentImage,
            // Aplica outras opções
            // ImageScale = 0.5
        };
        page.Paragraphs.Add(imageht);
    }

    // Salva o arquivo PDF de saída
    pdf.Save(_dataDir + "TifftoPDF.pdf");
}
```
## Aplica-se a

|**Plataforma**|**Suportado**|**Comentários**|
| :- | :- |:- |
|Windows .NET Framework|2.0-4.6| |
|Windows .NET Core |2.0-3.1| |
|.NET 5 Windows| |
|Linux .NET Core|2.0-3.1 | |
|.NET 5 Linux | |

## Veja Também

Este artigo também aborda os seguintes tópicos. Os códigos são os mesmos mencionados acima.

_Formato_: **BMP**
- [Código C# BMP para PDF](#csharp-bmp-to-pdf)
- [API C# BMP para PDF](#csharp-bmp-to-pdf)
- [C# BMP para PDF Programaticamente](#csharp-bmp-to-pdf)
- [Biblioteca C# BMP para PDF](#csharp-bmp-to-pdf)
- [C# Salvar BMP como PDF](#csharp-bmp-to-pdf)
- [C# Gerar PDF a partir de BMP](#csharp-bmp-to-pdf)
- [C# Criar PDF a partir de BMP](#csharp-bmp-to-pdf)
- [Conversor C# BMP para PDF](#csharp-bmp-to-pdf)

_Formato_: **CGM**
- [Código C# CGM para PDF](#csharp-cgm-to-pdf)
- [API C# CGM para PDF](#csharp-cgm-to-pdf)
- [C# CGM para PDF Programaticamente](#csharp-cgm-to-pdf)
- [Biblioteca C# CGM para PDF](#csharp-cgm-to-pdf)
- [C# Salvar CGM como PDF](#csharp-cgm-to-pdf)
- [C# Gerar PDF a partir de CGM](#csharp-cgm-to-pdf)
- [C# Criar PDF a partir de CGM](#csharp-cgm-to-pdf)
- [Conversor C# CGM para PDF](#csharp-cgm-to-pdf)
- [C# CGM to PDF Converter](#csharp-cgm-to-pdf)

_Formato_: **DICOM**
- [C# DICOM para PDF Code](#csharp-dicom-to-pdf)
- [C# DICOM para PDF API](#csharp-dicom-to-pdf)
- [C# DICOM para PDF Programaticamente](#csharp-dicom-to-pdf)
- [C# DICOM para PDF Library](#csharp-dicom-to-pdf)
- [C# Salvar DICOM como PDF](#csharp-dicom-to-pdf)
- [C# Gerar PDF a partir de DICOM](#csharp-dicom-to-pdf)
- [C# Criar PDF a partir de DICOM](#csharp-dicom-to-pdf)
- [C# DICOM para PDF Converter](#csharp-dicom-to-pdf)

_Formato_: **EMF**
- [C# EMF para PDF Code](#csharp-emf-to-pdf)
- [C# EMF para PDF API](#csharp-emf-to-pdf)
- [C# EMF para PDF Programaticamente](#csharp-emf-to-pdf)
- [C# EMF para PDF Library](#csharp-emf-to-pdf)
- [C# Salvar EMF como PDF](#csharp-emf-to-pdf)
- [C# Gerar PDF a partir de EMF](#csharp-emf-to-pdf)
- [C# Criar PDF a partir de EMF](#csharp-emf-to-pdf)
- [C# EMF para PDF Converter](#csharp-emf-to-pdf)
