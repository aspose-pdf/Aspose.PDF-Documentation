---
title: Hello World PHP via Java Exemplo
linktitle: Hello World Exemplo
type: docs
weight: 40
url: /php-java/hello-world-example/
description: Esta página mostra como usar programação simples para criar um documento PDF contendo o texto - Hello World usando Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hello World Exemplo

Um exemplo de “Hello World” é tipicamente usado para demonstrar os recursos básicos de uma linguagem de programação ou software com um caso de uso direto.

Aspose.PDF para PHP via Java API permite que os desenvolvedores criem, leiam, editem e manipulem arquivos PDF dentro de suas aplicações Java. Ele suporta a leitura e conversão de vários tipos de arquivos para e do formato PDF. Este artigo Hello World mostra como criar um arquivo PDF usando Aspose.PDF para PHP via Java API. Após [instalar o Aspose.PDF para PHP via Java](/pdf/php-java/installation/) em seu ambiente, você pode executar o exemplo de código abaixo para ver como a API Aspose.PDF funciona.

O snippet de código abaixo segue estas etapas:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Adicionar uma [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) ao objeto do documento
1. Criar um objeto [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Adicionar TextFragment à coleção [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) da página
1. Salvar o documento PDF resultante

O seguinte trecho de código é um programa Hello World para demonstrar o funcionamento do Aspose.PDF para PHP via Java API.

```php
    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```