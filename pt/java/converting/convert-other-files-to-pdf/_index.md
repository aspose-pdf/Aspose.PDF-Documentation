---
title: Converter vários formatos de arquivo para PDF 
linktitle: Converter outros formatos de arquivo para PDF 
type: docs
weight: 80
url: pt/java/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter outros formatos de arquivo para documento PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Converter EPUB para PDF

**Aspose.PDF para Java** permite que você converta arquivos EPUB para o formato PDF de maneira simples.

<abbr title="publicação eletrônica">EPUB</abbr> (abreviação de publicação eletrônica) é um padrão de e-book livre e aberto do Fórum Internacional de Publicação Digital (IDPF). Os arquivos têm a extensão .epub. O EPUB é projetado para conteúdo refluível, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico.

Para converter arquivos EPUB para o formato PDF, o Aspose.PDF para Java possui uma classe chamada [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) que é usada para carregar o arquivo EPUB de origem.
 Após isso, o objeto é passado como um argumento para a inicialização do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), pois isso ajuda o mecanismo de renderização do PDF a determinar o formato de entrada do documento de origem.

O snippet de código a seguir mostra o processo de conversão de um arquivo EPUB para o formato PDF.

1. Crie um [`LoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions) EPUB.
1. Inicialize o objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
1. Salve o documento PDF de saída.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Crie um LoadOptions EPUB
        EpubLoadOptions options = new EpubLoadOptions();

        // Inicialize o objeto document
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // Salve o documento PDF de saída
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Tente converter EPUB para PDF online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["EPUB para PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF EPUB para PDF com Aplicativo Gratuito](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Converter Markdown para PDF

**Este recurso é suportado pela versão 19.6 ou superior.**

{{% alert color="success" %}}
**Tente converter Markdown para PDF online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["Markdown para PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF Markdown para PDF com Aplicativo Gratuito](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown é uma ferramenta de conversão de texto para HTML para autores da web.
 Markdown permite que você escreva em um formato de texto simples fácil de ler e escrever e depois converta-o em XHTML estruturalmente válido (ou HTML).

O trecho de código a seguir mostra como usar essa funcionalidade com Aspose.PDF para Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Instanciar objeto de opção de carga do Latex
        MdLoadOptions options = new MdLoadOptions();
        
        // Criar objeto de Documento
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // Salvar documento PDF de saída
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}

```

## Converter PCL para PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) é uma linguagem de impressora da Hewlett-Packard desenvolvida para acessar recursos padrão de impressoras. Os níveis PCL de 1 a 5e/5c são linguagens baseadas em comandos que usam sequências de controle processadas e interpretadas na ordem em que são recebidas. Em nível de consumidor, fluxos de dados PCL são gerados por um driver de impressão. A saída PCL também pode ser facilmente gerada por aplicações personalizadas.

{{% alert color="success" %}}
**Tente converter PCL para PDF online**

Aspose.PDF para Java apresenta a você um aplicativo online gratuito ["PCL para PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PCL para PDF com Aplicativo Gratuito](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Atualmente, apenas PCL5 e versões mais antigas são suportadas.**

|**Conjuntos de Comandos**|**Suporte**|**Exceções**|**Descrição**|

| :- | :- | :- | :- |
|Comandos de controle de trabalho|+|Modo de impressão duplex|Controlar o processo de impressão: número de cópias, bandeja de saída, impressão simplex/duplex, deslocamentos à esquerda e no topo, etc.|
|Comandos de controle de página|+|Comando de Pular Perforação|Especificar um tamanho de página, margens, orientação da página, distâncias entre linhas, entre caracteres, etc.|
|Comandos de Posicionamento do Cursor|+| |Especificar a posição do cursor e, portanto, as origens do texto, imagens raster ou vetoriais e detalhes.|

|Comandos de seleção de fonte|+|<p>1. Comando de Impressão de Dados Transparente.</p><p>2. Fontes soft incorporadas. Na versão atual, em vez de criar fonte soft, nossa biblioteca seleciona a fonte adequada a partir das fontes TrueType "duras" existentes instaladas em uma máquina alvo. <br>   A adequação é definida pela proporção largura/altura. <br>   Este recurso funciona apenas para fontes Bitmap e TrueType e não garante que o texto impresso com a fonte soft será relevante para o do arquivo fonte. <br>   Porque códigos de caracteres na fonte soft podem não corresponder aos padrões.</p><p>3. Conjuntos de Símbolos Definidos pelo Usuário.</p>|Permite carregar fontes soft (incorporadas) do arquivo PCL e gerenciá-las na memória.|
|Comandos de gráficos rasterizados|+|Apenas preto e branco|Permite carregar imagens rasterizadas do arquivo PCL para a memória, especificar parâmetros rasterizados <br>como largura, altura, tipo de compressão, resolução, etc.|
|Comandos de cor|+| |Permite colorir todos os objetos imprimíveis.|
|Comandos do Modelo de Impressão|+| |Permite preencher texto, imagens rasterizadas e áreas retangulares com padrões rasterizados pré-definidos e definidos pelo usuário, especificar modo de transparência para padrões e imagem rasterizada de origem.
 <br>Padrões predefinidos são hachuras, hachuras cruzadas e sombreamento.|
|Comandos de preenchimento de área retangular|+| |Permitem a criação e preenchimento de áreas retangulares com padrões.|
|Comandos de Gráficos Vetoriais HP-GL/2|+|O Comando Vetorial com Tela (SV), Comando de Modo de Transparência (TR), Comando de Dados Transparentes (TD), RO (Rotacionar Sistema de Coordenadas), Comando de Fontes Escaláveis ou Bitmap (SB), Comando de Inclinação de Caracteres (SL) e Espaço Extra (ES) não são implementados e os comandos DV (Definir Caminho de Texto Variável) são realizados em versão beta.|<p>- Permitem carregar imagens vetoriais HP-GL/2 do arquivo PCL na memória. A imagem vetorial tem uma origem no canto inferior esquerdo da área imprimível, pode ser escalada, transladada, rotacionada e recortada.</p><p>- Uma imagem vetorial pode conter texto, como rótulos, e figuras geométricas como retângulo, círculo, elipse, linha, arco, curva de bezier e figuras complexas compostas pelas simples.</p><p>- Figuras fechadas, incluindo letras de rótulos, podem ser preenchidas com preenchimento sólido ou padrão vetorial.</p><p>- O padrão pode ser hachura, hachura cruzada, sombreamento, raster definido pelo usuário, hachura PCL ou hachura cruzada PCL e definido pelo usuário PCL. Os padrões PCL são raster. Rótulos podem ser individualmente rotacionados, escalados e direcionados em quatro direções: para cima, para baixo, para esquerda e para direita. As direções Esquerda e Direita envolvem arranjo de letras uma após a outra. As direções Cima e Baixo envolvem arranjo de letras uma sob a outra.</p>|
|Macross|―| |Permite carregar uma sequência de comandos PCL na memória e usar essa sequência várias vezes, por exemplo, para imprimir cabeçalho de página ou definir uma formatação para um conjunto de páginas.|
|Texto Unicode|―| |Permite a impressão de caracteres não ASCII. Não implementado devido à falta de arquivos de exemplo com texto Unicode|
|PCL6 (PCL-XL)| |Realizado apenas na versão Beta devido à falta de arquivos de teste. Fontes incorporadas também não são suportadas. A extensão JetReady não é suportada porque é impossível ter a especificação JetReady.|Formato de arquivo binário.|

### Convertendo um arquivo PCL em formato PDF

Para permitir a conversão de PCL para PDF, [Aspose.PDF for Java](https://products.aspose.com/pdf/java) possui a classe [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) que é usada para inicializar o objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Este objeto é então passado como argumento durante a inicialização do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) e ajuda o mecanismo de renderização de PDF a determinar o formato de entrada do documento de origem.

O snippet de código a seguir mostra o processo de conversão de um arquivo PCL em formato PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPCLtoPDF {

    private ConvertPCLtoPDF() {
        
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {        
        ConvertPCLtoPDF_Simple();
        ConvertPCLtoPDF_Advanced();
    }

    public static void ConvertPCLtoPDF_Simple() {
        PclLoadOptions options = new PclLoadOptions();
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        pdfDocument.save(_dataDir + "epub_test.pdf");        
    }

    public static void ConvertPCLtoPDF_Advanced() {
        PclLoadOptions options = new PclLoadOptions();
        options.SupressErrors=true;
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        if (options.Exceptions!=null)
            for (Exception ex : options.Exceptions)
            {
                System.out.println(ex.getMessage());
            }
        pdfDocument.save(_dataDir + "pcl_test.pdf");        
    }
}
```

### Problemas Conhecidos

1. A origem das cadeias de texto e imagens pode diferir ligeiramente das de um arquivo PCL de origem se a direção de impressão não for 0º. O mesmo se refere a imagens vetoriais se o sistema de coordenadas do gráfico vetorial for rotacionado (comando RO precedido).
2. A origem das etiquetas em imagens vetoriais pode diferir das de um arquivo PCL de origem se as etiquetas forem influenciadas por uma sequência de comandos: Origem da Etiqueta (LO), Definir Caminho de Texto Variável (DV), Direção Absoluta (DI) ou Direção Relativa (DR).
3. Um texto pode ser lido incorretamente se tiver que ser renderizado com fonte Bitmap ou TrueType soft (embutida), porque atualmente essas fontes são apenas parcialmente suportadas (veja exceções na "Tabela de características suportadas"). Nessa situação, o texto pode ser lido corretamente apenas se os códigos de caracteres em uma fonte soft corresponderem aos padrões. Um estilo do texto lido também pode diferir daquele no arquivo PCL de origem porque não é necessário definir estilo no cabeçalho da fonte soft.

1. Se o arquivo PCL analisado contiver fontes Intellifont ou Universal, uma exceção será lançada, porque as fontes Intellifont e Universal não são suportadas de forma alguma.
1. Se o arquivo PCL analisado contiver comandos de macros, o resultado da análise será muito diferente do arquivo de origem, porque os comandos de macros não são suportados.

## Converter Texto para PDF
{{% alert color="success" %}}

**Aspose.PDF para Java** fornece a capacidade de converter arquivos de texto para o formato PDF. Neste artigo, demonstramos como podemos converter de forma fácil e eficiente um arquivo de texto para PDF usando Aspose.PDF.

Quando você precisa converter um arquivo de texto para PDF, inicialmente leia o arquivo de texto de origem em algum leitor. Usamos StringBuilder para ler o conteúdo do arquivo de texto. Instancie o objeto Document e adicione uma nova página na coleção Pages. Crie um novo objeto de TextFragment e passe o objeto StringBuilder para seu construtor. Adicione um novo parágrafo na coleção Paragraphs usando o objeto TextFragment e salve o arquivo PDF resultante usando o método Save da classe Document.
**Tente converter TEXTO para PDF online**

Aspose.PDF para Java apresenta a você a aplicação online gratuita ["Texto para PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), onde você pode tentar investigar a funcionalidade e qualidade com que ela funciona.

[![Conversão Aspose.PDF TEXTO para PDF com Aplicativo Gratuito](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Converter arquivo de texto simples para PDF

```java
package com.aspose.pdf.examples;
/**
 * Converter TXT para PDF
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // Inicializar objeto de documento

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // Instanciar um objeto Document chamando seu construtor vazio
        Document pdfDocument = new Document();

        // Adicionar uma nova página na coleção Pages do Document
        Page page = pdfDocument.getPages().add();

        // Criar uma instância de TextFragment e passar o texto do objeto leitor para o seu
        // construtor como argumento
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // Adicionar um novo parágrafo de texto na coleção de parágrafos e passar o objeto
        // TextFragment
        page.getParagraphs().add(text);

        // Salvar arquivo PDF resultante
        pdfDocument.save(pdfDocumentFileName);
    }
```


### Converter arquivo de texto pré-formatado para PDF

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // Ler o arquivo de texto como um array de string
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // Instanciar um objeto Document chamando seu construtor vazio
        Document pdfDocument = new Document();

        // Adicionar uma nova página na coleção Pages do Document
        Page page = pdfDocument.getPages().add();

        // Definir margens esquerda e direita para melhor apresentação
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // verificar se a linha contém o caractere "form feed"
            // veja https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Criar uma instância de TextFragment e
                // passar a linha para seu
                // construtor como argumento
                TextFragment text = new TextFragment(line);

                // Adicionar um novo parágrafo de texto na coleção de parágrafos e passar o objeto TextFragment
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}
```


## Converter XPS para PDF

**Aspose.PDF para Java** suporta a funcionalidade de conversão de arquivos <abbr title="XML Paper Specification">XPS</abbr> para o formato PDF. Consulte este artigo para resolver suas tarefas.

XPS, XML Paper Specification, é um formato de arquivo da Microsoft usado para integrar a criação e visualização de documentos no Windows. Com o Aspose.PDF para Java, é possível converter arquivos XPS para PDF, o formato de arquivo portátil da Adobe.

O formato de arquivo é basicamente um arquivo XML compactado, usado principalmente para distribuição e armazenamento. É muito difícil de editar e implementado principalmente pela Microsoft.

Para converter um arquivo XPS para PDF usando [Aspose.PDF para Java](https://products.aspose.com/pdf/java), use a classe [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Este é usado para inicializar um objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Mais tarde, este objeto é passado como um argumento durante a inicialização do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) e ajuda o mecanismo de renderização de PDF a determinar o formato de entrada do documento de origem.

Tanto no XP quanto no Windows 7, você deve encontrar uma Impressora XPS pré-instalada se você procurar no Painel de Controle e depois em Impressoras. Para criar arquivos XPS, você pode usar essa impressora como o dispositivo de saída. No Windows 7, você deve ser capaz de simplesmente dar um duplo clique no arquivo para abri-lo em um visualizador XPS. Você também pode baixar o [visualizador XPS](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer) do site da Microsoft.

O seguinte trecho de código mostra o processo de conversão do arquivo XPS para o formato PDF.

```java
public final class ConvertXPStoPDF {

    private ConvertXPStoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Inicializar objeto de documento

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();

        // Instanciar objeto LoadOption usando opção de carga XPS
        LoadOptions options = new XpsLoadOptions();

        // Instanciar um objeto Document chamando seu construtor vazio
        Document pdfDocument = new Document(xpsDocumentFileName, options);

        // Salvar arquivo PDF resultante
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

{{% alert color="success" %}}
**Tente converter o formato XPS para PDF online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), onde você pode experimentar a funcionalidade e qualidade de seu funcionamento.

[![Aspose.PDF Converção XPS para PDF com Aplicativo Gratuito](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Converter PostScript para PDF

**Aspose.PDF para Java** suporta recursos de conversão de arquivos PostScript para o formato PDF. Um dos recursos do Aspose.PDF é que você pode definir um conjunto de pastas de fontes a serem usadas durante a conversão.

Para converter um arquivo PostScript para o formato PDF, o Aspose.PDF para Java oferece a classe [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) que é usada para inicializar o objeto LoadOptions. Posteriormente, este objeto pode ser passado como um argumento para o construtor do objeto Document, o que ajudará o Motor de Renderização de PDF a determinar o formato do documento de origem.


O seguinte trecho de código pode ser usado para converter um arquivo PostScript em formato PDF:

```java
public static void ConvertPostScriptToPDF_Simple(){
        // Inicializar objeto de documento

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // Criar objeto Documento
        Document document = new Document(psDocumentFileName, options);

        // Salvar documento PDF de saída
        document.save(pdfDocumentFileName);
    }
```

Além disso, você pode definir um conjunto de pastas de fontes que serão usadas durante a conversão:

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // Criar objeto Documento
        Document document = new Document(psDocumentFileName, options);

        // Salvar documento PDF de saída
        document.save(pdfDocumentFileName);
    }
```


## Converter XML para PDF

O formato XML é usado para armazenar dados estruturados. Existem várias maneiras de converter <abbr title="Extensible Markup Language">XML</abbr> para PDF no Aspose.PDF.

{{% alert color="success" %}}
**Tente converter XML para PDF online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["XML para PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF XML para PDF com App Gratuito](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Considere a opção de usar o documento XML baseado no padrão XSL-FO.

### Converter XSL-FO para PDF

A conversão de arquivos XSL-FO para PDF pode ser implementada usando o objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) com [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```java
package com.aspose.pdf.examples;
/**
 * Converter XML para PDF
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Inicializar objeto documento

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // Instanciar um objeto Document chamando seu construtor vazio
        Document pdfDocument = new Document(xmlDocumentFileName, options);

        // Salvar arquivo PDF resultante
        pdfDocument.save(pdfDocumentFileName);
    }
}
```


### Converter XSL-FO para PDF com estratégia de tratamento de erros definida

```java
// Inicializar objeto de documento

String documentFileName = Paths.get(DATA_DIR.toString(), "demo_txt.pdf").toString();
String xmlDocumentFileName = Paths.get(DATA_DIR.toString(), "demo.xml").toString();
String xsltDocumentFileName = Paths.get(DATA_DIR.toString(), "employees.xslt").toString();

XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

// Definir estratégia de tratamento de erros
options.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);

// Instanciar um objeto Document chamando seu construtor vazio
Document document = new Document(xmlDocumentFileName, options);

// Salvar arquivo PDF resultante
document.save(documentFileName);
document.close();
```

## Converter LaTeX/TeX para PDF

O formato de arquivo LaTeX é um formato de arquivo de texto com marcação na derivação LaTeX da família de linguagens TeX, e o LaTeX é um formato derivado do sistema TeX.
 LaTeX (ˈleɪtɛk/ lay-tek ou lah-tek) é um sistema de preparação de documentos e uma linguagem de marcação de documentos. É amplamente utilizado para a comunicação e publicação de documentos científicos em muitos campos, incluindo matemática, física e ciência da computação. Também tem um papel proeminente na preparação e publicação de livros e artigos que contêm materiais multilíngues complexos, como sânscrito e árabe, incluindo edições críticas. LaTeX usa o programa de composição tipográfica TeX para formatar sua saída e é escrito na própria linguagem de macro TeX.

**Aspose.PDF for Java** suporta o recurso de converter arquivos TeX para o formato PDF e, para realizar esse requisito, o pacote com.aspose.pdf possui uma classe chamada [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) que fornece as capacidades para carregar arquivos LaTex e renderizar a saída em formato PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). O trecho de código a seguir mostra o processo de conversão de um arquivo LaTex para o formato PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Instanciar objeto de opção de carregamento Latex
        TeXLoadOptions options = new TeXLoadOptions();
        
        // Criar objeto Documento
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // Salvar documento PDF de saída
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Tente converter LaTeX/TeX para PDF online**

Aspose.PDF for Java apresenta a você o aplicativo online gratuito ["LaTex para PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade do funcionamento.
[![Conversão Aspose.PDF LaTeX/TeX para PDF com Aplicativo Gratuito](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}