---
title: Converter PDF para Microsoft Word
linktitle: Converter PDF para Word
type: docs
weight: 10
url: /php-java/convert-pdf-to-word/
lastmod: "2024-05-20"
description: Converta arquivo PDF para formato DOC e DOCX com facilidade e controle total com Aspose.PDF para PHP. Saiba mais sobre como ajustar a conversão de documentos PDF para Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visão Geral

Este artigo explica como converter PDF para Word usando PHP. O código é muito simples, basta carregar o PDF na classe Document e salvá-lo como saída no formato Microsoft Word DOC ou DOCX. Ele cobre os seguintes tópicos

- [PHP PDF para Word](#convert-pdf-to-doc)
- [PHP PDF para DOC](#convert-pdf-to-doc)
- [PHP PDF para DOCX](#convert-pdf-to-docx)
- [PHP Converter PDF para Word](#convert-pdf-to-docx)
- [PHP Converter PDF para DOC](#convert-pdf-to-doc)
- [PHP Converter PDF para DOCX](#convert-pdf-to-docx)
- [PHP Como converter arquivo PDF para Word DOC](#convert-pdf-to-doc) ou [Word DOCX](#convert-pdf-to-docx)

- [PHP Biblioteca PDF para Word, API ou Código para Salvar, Gerar ou Criar Documentos Word Programaticamente a partir de PDF](#convert-pdf-to-docx)

## Converter PDF para DOC

Uma das características mais populares é a conversão de PDF para DOC do Microsoft Word, o que torna o conteúdo fácil de manipular. Aspose.PDF para PHP permite que você converta arquivos PDF para DOC.

**Aspose.PDF para PHP** pode criar documentos PDF do zero e é um excelente kit de ferramentas para atualizar, editar e manipular documentos PDF existentes. Uma característica importante é a capacidade de converter páginas e documentos PDF inteiros em imagens. Outra característica popular é a conversão de PDF para DOC do Microsoft Word, o que torna o conteúdo fácil de manipular. (A maioria dos usuários não consegue editar documentos PDF, mas pode facilmente trabalhar com tabelas, texto e imagens no Microsoft Word.)

Para simplificar e tornar as coisas compreensíveis, Aspose.PDF para PHP fornece um código de duas linhas para transformar um arquivo PDF de origem em um arquivo DOC.

O trecho de código Java a seguir mostra o processo de conversão de um arquivo PDF para o formato DOC.

1. Crie uma instância do objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document) com o documento PDF de origem.

2. Salve-o no formato **SaveFormat.Doc** chamando o método **Document.save()**.

```php
// Carregar o documento PDF
$document = new Document($inputFile);

// Criar um novo objeto DocSaveOptions
$saveOption = new DocSaveOptions();

// Definir o formato de saída para DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// Salvar o documento como DOC
$document->save($outputFile, $saveOption);
```

## Usando a Classe DocSaveOptions

A [classe DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) fornece várias propriedades que melhoram o processo de conversão de arquivos PDF para o formato DOC. Entre essas propriedades, o modo permite que você especifique o modo de reconhecimento para o conteúdo do PDF. Você pode especificar qualquer valor da enumeração RecognitionMode para esta propriedade. Cada um desses valores tem benefícios e limitações específicos:

- O modo [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) é rápido e bom para preservar a aparência original de um arquivo PDF, mas a editabilidade do documento resultante pode ser limitada.
 Cada bloco de texto visualmente agrupado no PDF original é convertido em uma caixa de texto no documento de saída. Isso alcança uma semelhança máxima com o original, de modo que o documento de saída fique bom, mas consiste inteiramente de caixas de texto e isso pode tornar a edição no Microsoft Word difícil.

- Flow é o modo de reconhecimento completo, onde o mecanismo realiza agrupamento e análise multinível para restaurar o documento original conforme a intenção do autor, ao mesmo tempo em que produz um documento facilmente editável. A limitação é que o documento de saída pode parecer diferente do original.

- A propriedade RelativeHorizontalProximity pode ser usada para controlar a proximidade relativa entre elementos textuais e significa que a distância é normatizada pelo tamanho da fonte. Fontes maiores podem ter distâncias maiores entre sílabas e ainda serem consideradas um único todo. É especificado como uma porcentagem do tamanho da fonte, por exemplo, 1 = 100%. Isso significa que dois caracteres de 12pt colocados a 12 pt de distância são próximos.

- RecognitionBullets é usado para ativar o reconhecimento de marcadores durante a conversão.
```php
// Carregar o documento PDF
$document = new Document($inputFile);

// Criar um novo objeto DocSaveOptions
$saveOption = new DocSaveOptions();

// Definir o modo de reconhecimento para EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// Definir o formato de saída como DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// Definir o modo de reconhecimento como Flow
saveOptions->setMode(DocSaveOptions_RecognitionMode::$Flow);

// Definir a proximidade horizontal como 2.5
saveOptions->setRelativeHorizontalProximity(2.5f);

// Habilitar o valor para reconhecer marcadores durante o processo de conversão
saveOptions->setRecognizeBullets(true);

// Salvar o documento como DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF para Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.


[![Converter PDF para DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter PDF para DOCX

A enumeração DocFormat também oferece a opção de escolher DOCX como o formato de saída para documentos Word. Para renderizar o arquivo PDF de origem no formato DOCX, use o trecho de código especificado abaixo.

## Como converter PDF para DOCX

O seguinte trecho de código Java mostra o processo de conversão de um arquivo PDF para o formato DOCX.

1. Crie uma instância do objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document) com o documento PDF de origem.
2. Salve-o no formato **SaveFormat.DocX** chamando o método **Document.save()**.

```php
    // Carregar o documento PDF
    $document = new Document($inputFile);
    
    // Salvar o documento como DOCX
    $document->save($outputFile, SaveFormat::$DocX);
```

A classe [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) possui uma propriedade chamada Format que fornece a capacidade de especificar o formato do documento resultante, ou seja, DOC ou DOCX.
 Para converter um arquivo PDF para o formato DOCX, passe o valor Docx da enumeração DocSaveOptions.DocFormat.

Por favor, veja o seguinte trecho de código que fornece a capacidade de converter um arquivo PDF para o formato DOCX com Java.

```php
// Carregar o documento PDF
$document = new Document($inputFile);

// Criar um novo objeto DocSaveOptions
$saveOption = new DocSaveOptions();

// Definir o modo de reconhecimento para EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// Definir o formato de saída para DOCX
$saveOption->setFormat(DocSaveOptions_DocFormat::$DocX);

// Salvar o documento como DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.


[![Aspose.PDF Convertion PDF to DOCX Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)
{{% /alert %}}