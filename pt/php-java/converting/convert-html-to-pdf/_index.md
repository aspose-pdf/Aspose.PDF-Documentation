---
title: Convert HTML to PDF
linktitle: Convert HTML to PDF
type: docs
weight: 40
url: /pt/php-java/convert-html-to-pdf/
lastmod: "2024-05-20"
description: Este tópico mostra como o Aspose.PDF permite converter formatos HTML e MHTML para arquivo PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Visão Geral

Este artigo explica como converter HTML em PDF usando PHP. O código é muito simples, basta carregar HTML na classe Document e salvá-lo como PDF de saída. Converter MHTML para PDF em Java também é similar. Ele cobre os seguintes tópicos

## Biblioteca Java para Conversão de HTML para PDF

**Aspose.PDF para PHP via Java** é uma API de manipulação de PDF que permite converter qualquer documento HTML existente em PDF de forma contínua.
O processo de conversão de HTML para PDF pode ser customizado de forma flexível.

## Converter HTML para PDF

O seguinte exemplo de código Java mostra como converter um documento HTML para PDF.

1. Crie uma instância da classe [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).

1. Inicialize o objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Salve o documento PDF de saída chamando o método [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-).

```php
    // Crie uma instância de HtmlLoadOptions para especificar as opções de carregamento para o arquivo HTML
    $loadOption = new HtmlLoadOptions();

    // Crie um novo objeto Document e carregue o arquivo HTML
    $document = new Document($inputFile, $loadOption);

    // Salve o documento como um arquivo PDF
    $document->save($outputFile);
```

## Conversão avançada de HTML para PDF

O mecanismo de conversão de HTML possui várias opções que nos permitem controlar o processo de conversão.

### Suporte a Media Queries

1. Crie um [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) HTML.
1. [Defina o modo Print ou Screen](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-).

1. Inicialize o [objeto Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Salve o documento PDF de saída.

Consultas de mídia são uma técnica popular para entregar uma folha de estilo personalizada para diferentes dispositivos. Podemos definir o tipo de dispositivo usando a classe [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```php

    // Crie uma instância de HtmlLoadOptions para especificar as opções de carregamento para o arquivo HTML
    $htmlMediaType = new HtmlMediaType();

    // Defina o modo de Impressão ou Tela
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // Crie um novo objeto Document e carregue o arquivo HTML
    $document = new Document($inputFile, $loadOption);

    // Salve o documento como um arquivo PDF
    $document->save($outputFile);
```

### Ativar (desativar) a incorporação de fontes

1. Adicione novas [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) Html.
1. Desative a incorporação de fontes.
1. Salve um novo Documento.

Páginas HTML frequentemente usam fontes (por exemplo.
 fontes da pasta local, Google Fonts, etc). Também podemos controlar a incorporação de fontes em um documento usando uma propriedade [setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-).

```php

    // Crie uma instância de HtmlLoadOptions para especificar as opções de carregamento para o arquivo HTML
    $loadOption = new HtmlLoadOptions();

    // Desabilitar a incorporação de fontes
    $loadOption->setEmbedFonts(true);

    // Crie um novo objeto Document e carregue o arquivo HTML
    $document = new Document($inputFile, $loadOption);

    // Salve o documento como um arquivo PDF
    $document->save($outputFile);
```

## Converter MHTML para PDF

<abbr title="Encapsulamento MIME de documentos HTML agregados">MHTML</abbr>, abreviação de MIME HTML, é um formato de arquivo de arquivamento de página da web usado para combinar recursos que geralmente são representados por links externos (como imagens, animações Flash, applets Java e arquivos de áudio) com código HTML em um único arquivo. O conteúdo de um arquivo MHTML é codificado como se fosse uma mensagem de email HTML, usando o tipo MIME multipart/related.

O próximo trecho de código mostra como converter arquivos MHTML para o formato PDF com Java:

```php

    // Crie uma nova instância da classe MhtLoadOptions.
    $loadOption = new MhtLoadOptions();

    // Crie uma nova instância da classe Document e carregue o arquivo MHTML.
    $document = new Document($inputFile, $loadOption);

    // Salve o documento como um arquivo PDF.
    $document->save($outputFile);
```