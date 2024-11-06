---
title: Converter arquivo PDF para outros formatos
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: pt/php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: Este tópico mostra como o Aspose.PDF permite converter arquivos PDF para outros formatos de arquivo.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter PDF para EPUB

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão de PDF para EPUB com Aplicativo Gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (abreviação de publicação eletrônica) é um padrão gratuito e aberto de e-book do Fórum Internacional de Publicação Digital (IDPF).
 Os arquivos têm a extensão .epub. EPUB é projetado para conteúdo redimensionável, o que significa que um leitor EPUB pode otimizar o texto para um dispositivo de exibição específico. EPUB também suporta conteúdo de layout fixo. O formato é destinado como um formato único que editoras e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

Aspose.PDF para PHP suporta o recurso de converter documentos PDF para o formato EPUB. Aspose.PDF para PHP tem uma classe chamada [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) que pode ser usada como o segundo argumento para o método [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-) para gerar um arquivo EPUB. Por favor, tente usar o seguinte trecho de código para realizar esse requisito.

```php
// Crie uma nova instância da classe Document e carregue o arquivo PDF de entrada
$document = new Document($inputFile);

// Crie uma nova instância da classe EpubSaveOptions
$saveOption = new EpubSaveOptions();

// Salve o documento no formato EPUB usando as opções de salvamento especificadas
$document->save($outputFile, $saveOption);
```

## Converter PDF para LaTeX/TeX

**Aspose.PDF para PHP** suporta a conversão de PDF para LaTeX/TeX. O formato de arquivo LaTeX é um formato de arquivo de texto com marcação especial e é usado no sistema de preparação de documentos baseado em TeX para composição tipográfica de alta qualidade.

Para converter arquivos PDF para TeX, Aspose.PDF possui a classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions) que fornece o método `setOutDirectoryPath` para salvar imagens temporárias durante o processo de conversão.

O trecho de código a seguir mostra o processo de conversão de arquivos PDF para o formato TEX com Java.

```php
// Crie um novo objeto Document e carregue o arquivo PDF de entrada
$document = new Document($inputFile);

// Crie um novo objeto LaTeXSaveOptions
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// Salve o documento como LaTeX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF para PHP apresenta a você a aplicação online gratuita ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode tentar investigar a funcionalidade e qualidade que oferece.

[![Aspose.PDF Conversão PDF para LaTeX/TeX com Aplicativo Gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Converter PDF para Texto

**Aspose.PDF para PHP** suporta a conversão de todo o documento PDF e de uma única página para um arquivo de Texto.

### Converter todo o documento PDF para um arquivo de Texto

Você pode converter um documento PDF para um arquivo TXT usando o método Visit da classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

O trecho de código a seguir explica como extrair os textos de todas as páginas.

```php
// Carregar o documento PDF
$document = new Document($inputFile);

// Criar um objeto TextAbsorber para extrair texto do documento
$textAbsorber = new TextAbsorber();

// Extrair o texto do documento
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// Salvar o texto extraído no arquivo de saída
file_put_contents($outputFile, $content);

// Obter o tamanho do arquivo do arquivo de saída
$fileSize = filesize($outputFile);
```


{{% alert color="success" %}}
**Tente converter Converter PDF para Texto online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode tentar investigar a funcionalidade e a qualidade de seu funcionamento.

[![Aspose.PDF Conversão PDF para Texto com Aplicativo Gratuito](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Converter página PDF para arquivo de texto

Você pode converter um documento PDF para um arquivo TXT com Aspose.PDF para PHP. Você deve usar o método Visit da classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) para resolver essa tarefa.

O trecho de código a seguir explica como extrair os textos das páginas específicas.

```php
// Carregar o documento PDF
$document = new Document($inputFile);

// Criar um objeto TextAbsorber para extrair texto do documento
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // Salvar o texto extraído no arquivo de saída
    file_put_contents($outputFile, $content);
}
```


## Converter PDF para XPS

**Aspose.PDF para PHP** oferece a possibilidade de converter arquivos PDF para o formato <abbr title="XML Paper Specification">XPS</abbr>. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com Java.

{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para XPS com Aplicativo Grátis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

O tipo de arquivo XPS está principalmente associado à Especificação de Papel XML pela Microsoft Corporation. A Especificação de Papel XML (XPS), anteriormente codinome Metro e subsumindo o conceito de marketing Caminho de Impressão de Próxima Geração (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos no sistema operacional Windows.

Para converter arquivos PDF para XPS, Aspose.PDF possui a classe [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) que é usada como o segundo argumento para o construtor Document.save(..) para gerar o arquivo XPS.
 O trecho de código a seguir mostra o processo de conversão de arquivos PDF para o formato XPS.

```php
// Crie um novo objeto Document e carregue o arquivo PDF de entrada
$document = new Document($inputFile);

// Crie um novo objeto XpsSaveOptions
$saveOption = new XpsSaveOptions();

// Salve o documento como XPS usando as opções de salvamento especificadas
$document->save($outputFile, $saveOption);
```