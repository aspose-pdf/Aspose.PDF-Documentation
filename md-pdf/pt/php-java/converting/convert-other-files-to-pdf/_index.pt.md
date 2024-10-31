---
title: Converter vários formatos de arquivo para PDF 
linktitle: Converter outros formatos de arquivo para PDF 
type: docs
weight: 80
url: /php-java/convert-other-files-to-pdf/
lastmod: "2024-05-20"
description: Este tópico mostra como Aspose.PDF permite converter outros formatos de arquivo para documento PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Converter EPUB para PDF

**Aspose.PDF para PHP** permite que você converta facilmente arquivos EPUB para o formato PDF.

<abbr title="publicação eletrônica">EPUB</abbr> é um padrão de e-book livre e aberto do Fórum Internacional de Publicação Digital (IDPF). Os arquivos têm a extensão .epub. O EPUB é projetado para conteúdo redimensionável, o que significa que um leitor EPUB pode otimizar o texto para um dispositivo de exibição específico.

Para converter arquivos EPUB para o formato PDF, Aspose.PDF para PHP possui uma classe chamada [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) que é usada para carregar o arquivo EPUB de origem.
 Após isso, o objeto é passado como um argumento para a inicialização do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), pois isso ajuda o mecanismo de renderização de PDF a determinar o formato de entrada do documento de origem.

O trecho de código a seguir mostra o processo de conversão de um arquivo EPUB para o formato PDF.

1. Crie um [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) EPUB.
1. Inicialize o objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
1. Salve o documento PDF de saída.

```php
// Crie uma nova instância de EpubLoadOptions
$loadOption = new EpubLoadOptions();

// Crie um novo objeto Document e carregue o arquivo EPUB
$document = new Document($inputFile, $loadOption);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Tente converter EPUB para PDF online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.
[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Converter Markdown para PDF

{{% alert color="success" %}}
**Tente converter Markdown para PDF online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["Markdown para PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Convertion Markdown to PDF with Free App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown é uma ferramenta de conversão de texto para HTML para autores da web. Markdown permite que você escreva em um formato de texto simples fácil de ler e escrever e depois o converta em XHTML (ou HTML) estruturalmente válido.

O snippet de código a seguir mostra como usar esta funcionalidade com Aspose.PDF para PHP:

```php
// Crie uma nova instância de MdLoadOptions
$loadOption = new MdLoadOptions();

// Crie uma nova instância de Document e carregue o arquivo Markdown de entrada
$document = new Document($inputFile, $loadOption);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```


## Converter PCL para PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) é uma linguagem de impressora da Hewlett-Packard desenvolvida para acessar recursos padrão de impressoras. Os níveis de PCL de 1 a 5e/5c são linguagens baseadas em comandos que usam sequências de controle processadas e interpretadas na ordem em que são recebidas. Em nível de consumidor, os fluxos de dados PCL são gerados por um driver de impressão. A saída PCL também pode ser facilmente gerada por aplicativos personalizados.

{{% alert color="success" %}}
**Tente converter PCL para PDF online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PCL para PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF PCL para PDF com Aplicativo Gratuito](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Atualmente, apenas PCL5 e versões anteriores são suportados.**

|**Conjuntos de Comandos**|**Suporte**|**Exceções**|**Descrição**|

| :- | :- | :- | :- |
|Comandos de controle de trabalho|+|Modo de impressão duplex|Controlar o processo de impressão: número de cópias, bandeja de saída, impressão simplex/duplex, deslocamentos à esquerda e no topo etc.|
|Comandos de controle de página|+|Comando de pular perfuração|Especificar um tamanho de página, margens, orientação da página entre -linhas, -distâncias de caracteres etc.|
|Comandos de posicionamento do cursor|+| |Especificar a posição do cursor e, portanto, as origens do texto, imagens raster ou vetoriais e detalhes.|

|Comandos de seleção de fonte|+|<p>1. Comando de Dados de Impressão Transparente.</p><p>2. Fontes incorporadas. Na versão atual, em vez de criar uma fonte incorporada, nossa biblioteca seleciona uma fonte adequada a partir das fontes TrueType "duras" existentes instaladas em uma máquina de destino. <br>A adequação é definida pela proporção largura/altura. <br>Esse recurso funciona apenas para fontes Bitmap e TrueType e não garante que o texto impresso com fonte incorporada será relevante para aquele em um arquivo de origem. <br>Porque os códigos de caracteres na fonte incorporada podem não corresponder aos padrões.</p><p>3. Conjuntos de Símbolos Definidos pelo Usuário.</p>|Permitir o carregamento de fontes incorporadas (embutidas) a partir do arquivo PCL e gerenciá-las na memória.|
|Comandos de gráficos rasterizados|+|Apenas preto e branco|Permitir o carregamento de imagens rasterizadas do arquivo PCL para a memória, especificar parâmetros rasterizados <br>como largura, altura, tipo de compressão, resolução, etc.|
|Comandos de cor|+| |Permitir coloração para todos os objetos imprimíveis.|
|Comandos do modelo de impressão|+| |Permitir o preenchimento de texto, imagens rasterizadas e áreas retangulares com padrões rasterizados pré-definidos e definidos pelo usuário, especificar o modo de transparência para padrões e imagem rasterizada de origem.
 <br>Padrões predefinidos são de hachura, hachura cruzada e sombreamento.|
|Comandos de preenchimento de área retangular|+| |Permitem a criação e o preenchimento de áreas retangulares com padrões.|
|Comandos de Gráficos Vetoriais HP-GL/2|+|Os comandos de Vetor com Tela (SV), Modo de Transparência (TR), Dados Transparentes (TD), RO (Rotacionar Sistema de Coordenadas), Fontes Escaláveis ou Bitmap (SB), Inclinação de Caracteres (SL) e Espaço Extra (ES) não estão implementados e os comandos DV (Definir Caminho de Texto Variável) são realizados na versão beta.|<p>- Permite o carregamento de imagens vetoriais HP-GL/2 do arquivo PCL na memória. A imagem vetorial tem uma origem no canto inferior esquerdo da área imprimível, pode ser escalada, transladada, rotacionada e recortada.</p><p>- Uma imagem vetorial pode conter texto, como rótulos, e figuras geométricas como retângulo, círculo, elipse, linha, arco, curva de bezier e figuras complexas compostas pelas simples.</p><p>- Figuras fechadas, incluindo letras de rótulos, podem ser preenchidas com preenchimento sólido ou padrão vetorial.</p><p>- O padrão pode ser hachura, hachura cruzada, sombreamento, definido pelo usuário raster, hachura ou hachura cruzada PCL e definido pelo usuário PCL. Os padrões PCL são raster. Os rótulos podem ser individualmente rotacionados, escalados e direcionados em quatro direções: para cima, para baixo, para a esquerda e para a direita. As direções Esquerda e Direita envolvem disposição de letras uma-atrás-da-outra. As direções Para Cima e Para Baixo envolvem disposição de letras uma-sob-a-outra.</p>|
|Macross|―| |Permite carregar uma sequência de comandos PCL na memória e usar essa sequência muitas vezes, por exemplo, para imprimir cabeçalho de página ou definir uma formatação para um conjunto de páginas.|
|Texto Unicode|―| |Permite imprimir caracteres não-ASCII. Não implementado devido à falta de arquivos de exemplo com texto Unicode<br>|
|PCL6 (PCL-XL)| |Realizado apenas na versão Beta por falta de arquivos de teste. Fontes incorporadas também não são suportadas. A extensão JetReady não é suportada porque é impossível ter a especificação JetReady.|Formato de arquivo binário.|

### Convertendo um arquivo PCL para o formato PDF

Para permitir a conversão de PCL para PDF, [Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java) possui a classe [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) que é usada para inicializar o objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Este objeto é então passado como argumento durante a inicialização do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) e ajuda o mecanismo de renderização de PDF a determinar o formato de entrada do documento de origem.

O snippet de código a seguir mostra o processo de conversão de um arquivo PCL para o formato PDF.

```php
// Criar uma nova instância de PclLoadOptions
$loadOption = new PclLoadOptions();

// Criar uma nova instância de Document e carregar o arquivo PCL
$document = new Document($inputFile, $loadOption);

// Salvar o documento como um arquivo PDF
$document->save($outputFile);
```

### Problemas Conhecidos

1. A origem das cadeias de texto e imagens pode diferir ligeiramente das de um arquivo PCL de origem se a direção da impressão não for 0º. O mesmo se aplica a imagens vetoriais se o sistema de coordenadas do gráfico vetorial estiver rotacionado (precedido pelo comando RO).
2. A origem das etiquetas em imagens vetoriais pode diferir das de um arquivo PCL de origem se as etiquetas forem influenciadas por uma sequência de comandos: Origem da Etiqueta (LO), Definir Caminho de Texto Variável (DV), Direção Absoluta (DI) ou Direção Relativa (DR).
3. Um texto pode ser lido incorretamente se precisar ser renderizado com fonte Bitmap ou TrueType soft (incorporada), porque atualmente essas fontes são suportadas apenas parcialmente (veja exceções na "tabela de recursos suportados"). Nessa situação, o texto pode ser lido corretamente apenas se os códigos de caracteres em uma fonte soft corresponderem aos padrões. O estilo do texto lido também pode diferir daquele no arquivo PCL de origem porque não é necessário definir o estilo no cabeçalho da fonte soft.

1. Se o arquivo PCL analisado contiver fontes Intellifont ou Universal soft, uma exceção será lançada, porque as fontes Intellifont e Universal não são suportadas de forma alguma.
1. Se o arquivo PCL analisado contiver comandos macros, o resultado da análise diferirá muito do arquivo de origem, porque os comandos macros não são suportados.

## Converter Texto para PDF

**Aspose.PDF para PHP** oferece a capacidade de converter arquivos de Texto para o formato PDF. Neste artigo, demonstramos como podemos converter de forma fácil e eficiente um arquivo de texto para PDF usando o Aspose.PDF.

Quando você precisa converter um arquivo de Texto para PDF, inicialmente leia o arquivo de texto de origem em algum leitor. Usamos StringBuilder para ler o conteúdo do arquivo de Texto. Instancie o objeto Document e adicione uma nova página na coleção Pages. Crie um novo objeto de TextFragment e passe o objeto StringBuilder para seu construtor. Adicione um novo parágrafo na coleção Paragraphs usando o objeto TextFragment e salve o arquivo PDF resultante usando o método Save da classe Document.
**Tente converter TEXTO para PDF online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["Texto para PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão de Aspose.PDF TEXTO para PDF com Aplicativo Gratuito](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Converter arquivo de texto simples para PDF

```php
// Crie um novo objeto Document.
$document = new Document();

// Adicione uma nova página ao documento.
$page = $document->getPages()->add();

// Leia o conteúdo do arquivo de texto de entrada.
$text = file_get_contents($inputFile);

// Crie um novo objeto FontRepository.
$fontRepository = new FontRepository();

// Encontre a fonte "Courier" no repositório.
$font = $fontRepository->findFont("Courier");

// Crie um novo objeto TextFragment com o texto de entrada.
$textFragment = new TextFragment($text);

// Defina a fonte do fragmento de texto para "Courier".
$textFragment->getTextState()->setFont($font);

// Adicione o fragmento de texto à página.
$page->getParagraphs()->add($textFragment);

// Salve o documento no arquivo de saída.
$document->save($outputFile);
```


## Converter XPS para PDF

**Aspose.PDF para PHP** suporta a funcionalidade de conversão de arquivos <abbr title="XML Paper Specification">XPS</abbr> para o formato PDF. Confira este artigo para resolver suas tarefas.

XPS, Especificação de Papel XML, é um formato de arquivo da Microsoft usado para integrar a criação e visualização de documentos no Windows. Com o Aspose.PDF para PHP, é possível converter arquivos XPS para PDF, o formato de arquivo portátil da Adobe.

O formato de arquivo é basicamente um arquivo XML compactado, usado principalmente para distribuição e armazenamento. É muito difícil de editar e implementado principalmente pela Microsoft.

Para converter um arquivo XPS para PDF usando [Aspose.PDF para PHP](https://products.aspose.com/pdf/php-java), use a classe [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Isso é usado para inicializar um objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Posteriormente, este objeto é passado como um argumento durante a inicialização do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) e ajuda o mecanismo de renderização de PDF a determinar o formato de entrada do documento de origem.

O trecho de código a seguir mostra o processo de conversão do arquivo XPS para o formato PDF.

```php
// Crie uma nova instância da classe XpsLoadOptions
$loadOption = new XpsLoadOptions();

// Crie uma nova instância da classe Document e carregue o arquivo XPS
$document = new Document($inputFile, $loadOption);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Tente converter o formato XPS para PDF online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que ele trabalha.


[![Conversão Aspose.PDF de XPS para PDF com Aplicativo Gratuito](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/){{% /alert %}}

## Converter PostScript para PDF

**Aspose.PDF para PHP** suporta recursos de conversão de arquivos PostScript para o formato PDF. Um dos recursos do Aspose.PDF é que você pode definir um conjunto de pastas de fontes a serem usadas durante a conversão.

Para converter um arquivo PostScript para o formato PDF, Aspose.PDF para PHP oferece a classe [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) que é usada para inicializar o objeto LoadOptions. Mais tarde, este objeto pode ser passado como um argumento para o construtor do objeto Document, o que ajudará o Mecanismo de Renderização de PDF a determinar o formato do documento de origem.

O seguinte trecho de código pode ser usado para converter um arquivo PostScript em formato PDF:

```php
// Crie um novo objeto PsLoadOptions.
$loadOption = new PsLoadOptions();

// Crie um novo objeto Document e carregue o arquivo PS de entrada.
$document = new Document($inputFile, $loadOption);

// Salve o documento como um arquivo PDF.
$document->save($outputFile);
```

## Converter XML para PDF

O formato XML é usado para armazenar dados estruturados.
 Existem várias maneiras de converter <abbr title="Extensible Markup Language">XML</abbr> para PDF no Aspose.PDF.

{{% alert color="success" %}}
**Tente converter XML para PDF online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["XML para PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de XML para PDF com Aplicativo Gratuito](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Considere a opção de usar um documento XML baseado no padrão XSL-FO.

### Converter XSL-FO para PDF

A conversão de arquivos XSL-FO para PDF pode ser implementada usando o objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) com [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```php
// Defina o caminho para os arquivos de exemplo
$dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
$inputFoFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xslt";
$inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xml";
$outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . 'result-xmlfo-to-pdf.pdf';

// Crie uma nova instância da classe XslFoLoadOptions e passe o caminho do arquivo XSL-FO de entrada
$loadOption = new XslFoLoadOptions($inputFoFile);

// Crie uma nova instância da classe Document e passe o arquivo XML de entrada e as opções de carregamento XSL-FO
$document = new Document($inputFile, $loadOption);

// Salve o documento PDF convertido no caminho do arquivo de saída
$document->save($outputFile);
```

## Converter LaTeX/TeX para PDF

O formato de arquivo LaTeX é um formato de arquivo de texto com marcação na derivação LaTeX da família de linguagens TeX e o LaTeX é um formato derivado do sistema TeX. LaTeX (ˈleɪtɛk/ lay-tek ou lah-tek) é um sistema de preparação de documentos e linguagem de marcação de documentos. É amplamente utilizado para a comunicação e publicação de documentos científicos em muitos campos, incluindo matemática, física e ciência da computação. Ele também tem um papel proeminente na preparação e publicação de livros e artigos que contêm materiais multilíngues complexos, como sânscrito e árabe, incluindo edições críticas. LaTeX utiliza o programa de composição tipográfica TeX para formatar sua saída e é escrito na linguagem de macro TeX.

**Aspose.PDF para PHP** suporta o recurso de converter arquivos TeX para o formato PDF e, para realizar essa tarefa, o pacote com.aspose.pdf possui uma classe chamada [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) que fornece as capacidades para carregar arquivos LaTeX e renderizar a saída em formato PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document).
 O trecho de código a seguir mostra o processo de conversão de um arquivo LaTex para o formato PDF.

```php
// Crie uma nova instância da classe LatexLoadOptions
$loadOption = new LatexLoadOptions();

// Crie uma nova instância da classe Document e carregue o arquivo TeX usando o TeXLoadOptions
$document = new Document($inputFile, $loadOption);

// Salve o documento como um arquivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Tente converter LaTeX/TeX para PDF online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade que ele oferece.

[![Conversão Aspose.PDF LaTeX/TeX para PDF com Aplicativo Gratuito](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}