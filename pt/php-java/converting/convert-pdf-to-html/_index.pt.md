---
title: Converter arquivo PDF para formato HTML
linktitle: Converter arquivo PDF para formato HTML
type: docs
weight: 50
url: /php-java/convert-pdf-to-html/
lastmod: "2024-05-20"
description: Este tópico mostra como o Aspose.PDF permite converter arquivo PDF para formato HTML com a biblioteca PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF para PHP oferece muitos recursos para converter vários formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída. Este artigo discute como converter um arquivo PDF em formato HTML e salvar as imagens do arquivo PDF em uma pasta específica.

{{% alert color="success" %}}
**Tente converter PDF para HTML online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para HTML com Aplicativo Gratuito](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

Ao converter um arquivo PDF grande com várias páginas para o formato HTML, a saída aparece como uma única página HTML. Isso pode acabar sendo muito longo. Para controlar o tamanho da página, é possível dividir a saída em várias páginas durante a conversão de PDF para HTML.

## Converter páginas de PDF para HTML

Aspose.PDF para PHP oferece muitos recursos para converter vários formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída. Este artigo discute como converter um arquivo PDF para o formato HTML e salvar as imagens do arquivo PDF em uma pasta específica.

O trecho de código a seguir mostra todas as opções possíveis que você pode usar ao converter PDF para HTML.

```php
// Criar um novo objeto Document e carregar o arquivo PDF de entrada
$document = new Document($inputFile);

// Criar um novo objeto HtmlSaveOptions para salvar o documento como HTML
$saveOption = new HtmlSaveOptions();

// Salvar o documento como HTML usando as opções de salvamento especificadas
$document->save($outputFile, $saveOption);
```

## Converter PDF para HTML - Dividindo a saída em HTML de várias páginas

Aspose.PDF para PHP suporta a funcionalidade de converter documentos PDF para vários formatos de saída, incluindo HTML. No entanto, ao converter arquivos PDF grandes (compostos por várias páginas), pode haver a necessidade de salvar cada página PDF individual em um arquivo HTML separado.

Ao converter um arquivo PDF grande com várias páginas para o formato HTML, a saída aparece como uma única página HTML. Pode acabar sendo muito longa. Para controlar o tamanho da página, é possível dividir a saída em várias páginas durante a conversão de PDF para HTML. Por favor, tente usar o seguinte trecho de código.

```php
// Crie um novo objeto Document e carregue o arquivo PDF de entrada
$document = new Document($inputFile);

// Crie um novo objeto HtmlSaveOptions para salvar o documento como HTML
$saveOption = new HtmlSaveOptions();

// Especifique para dividir a saída em várias páginas
$saveOption->setSplitIntoPages(true);

// Salve o documento como HTML usando as opções de salvamento especificadas
$document->save($outputFile, $saveOption);
```

## Converter PDF para HTML - Evitar Salvar Imagens no Formato SVG


O formato de saída padrão para salvar imagens ao converter de PDF para HTML é SVG. Durante a conversão, algumas imagens do PDF são transformadas em imagens vetoriais SVG. Isso pode ser lento. Em vez disso, as imagens podem ser transformadas em PNG. Para permitir isso, o Aspose.PDF tem a opção de usar SVG para vetores ou criar PNGs.

Para remover completamente a renderização de imagens no formato SVG ao converter arquivos PDF para o formato HTML, tente usar o seguinte trecho de código.

```php
// Crie um novo objeto Documento e carregue o arquivo PDF de entrada
$document = new Document($inputFile);

// Crie um novo objeto HtmlSaveOptions para salvar o documento como HTML
$saveOption = new HtmlSaveOptions();

// Especifique a pasta onde as imagens SVG são salvas durante a conversão de PDF para HTML
$saveOption->setSpecialFolderForSvgImages(DATA_DIR);

// Salve o documento como HTML usando as opções de salvamento especificadas
$document->save($outputFile, $saveOption);
```

## Comprimindo Imagens SVG Durante a Conversão

Para comprimir imagens SVG durante a conversão de PDF para HTML, tente usar o seguinte código:

```php
// Crie um novo objeto Document e carregue o arquivo PDF de entrada
$document = new Document($inputFile);

// Crie um novo objeto HtmlSaveOptions para salvar o documento como HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions = setCompressSvgGraphicsIfAny(true);

// Salve o documento como HTML usando as opções de salvamento especificadas
$document->save($outputFile, $saveOptions);
```

## Converter PDF para HTML - Especificar Pasta de Imagens

Por padrão, ao converter um arquivo PDF para HTML, as imagens no PDF são salvas em uma pasta separada criada no mesmo diretório em que o HTML de saída é criado. Mas às vezes, é necessário especificar uma pasta diferente para salvar as imagens ao gerar arquivos HTML. Para realizar isso, introduzimos o [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions).

O método [setSpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForSvgImages-java.lang.String-) é usado para especificar a pasta de destino para armazenar imagens.


```php
// Crie um novo objeto Document e carregue o arquivo PDF de entrada
$document = new Document($inputFile);

// Crie um novo objeto HtmlSaveOptions para salvar o documento como HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSpecialFolderForAllImages(DATA_DIR);

// Salve o documento como HTML usando as opções de salvamento especificadas
$document->save($outputFile, $saveOptions);
```

## Renderização de Texto Transparente

Caso o arquivo PDF de origem/entrada contenha textos transparentes sombreado por imagens de primeiro plano, pode haver problemas de renderização de texto. Portanto, para atender a tais cenários, as propriedades SaveShadowedTextsAsTransparentTexts e SaveTransparentTexts podem ser usadas.

```php
// Crie um novo objeto Document e carregue o arquivo PDF de entrada
$document = new Document($inputFile);

// Crie um novo objeto HtmlSaveOptions para salvar o documento como HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSaveShadowedTextsAsTransparentTexts(true);
$saveOptions->setTransparentTexts(true);

// Salve o documento como HTML usando as opções de salvamento especificadas
$document->save($outputFile, $saveOptions);
```


## Renderização de camadas de documentos PDF

Podemos renderizar camadas de documentos PDF em elementos de tipo de camada separada durante a conversão de PDF para HTML:

```php
// Cria um novo objeto Document e carrega o arquivo PDF de entrada
$document = new Document($inputFile);

// Cria um novo objeto HtmlSaveOptions para salvar o documento como HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setConvertMarkedContentToLayers(true);

// Salva o documento como HTML usando as opções de salvamento especificadas
$document->save($outputFile, $saveOptions);
```

A conversão de PDF para HTML é uma das funcionalidades mais populares do Aspose.PDF porque torna possível visualizar o conteúdo de arquivos PDF em várias plataformas sem usar um visualizador de documentos PDF. O HTML de saída está de acordo com os padrões da WWW e pode ser facilmente exibido em todos os navegadores da web. Usando esse recurso, os arquivos PDF podem ser visualizados em dispositivos portáteis porque você não precisa instalar nenhum aplicativo de visualização de PDF, mas pode usar um simples navegador da web.