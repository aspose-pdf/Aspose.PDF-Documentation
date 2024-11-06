---
title: Converter PDF para Documentos Microsoft Word em Java
linktitle: Converter PDF para Word
type: docs
weight: 10
url: pt/java/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Converta arquivos PDF para o formato DOC e DOCX com facilidade e controle total com o Aspose.PDF para Java. Saiba mais sobre como ajustar a conversão de documentos PDF para Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visão Geral

Este artigo explica como converter PDF para Word usando Java. O código é muito simples, basta carregar o PDF na classe Document e salvá-lo como saída no formato Microsoft Word DOC ou DOCX. Ele cobre os seguintes tópicos

- [Java PDF para Word](#convert-pdf-to-doc)
- [Java PDF para DOC](#convert-pdf-to-doc)
- [Java PDF para DOCX](#convert-pdf-to-docx)
- [Java Converter PDF para Word](#convert-pdf-to-docx)
- [Java Converter PDF para DOC](#convert-pdf-to-doc)
- [Java Converter PDF para DOCX](#convert-pdf-to-docx)
- [Java Como converter arquivo PDF para Word DOC](#convert-pdf-to-doc) ou [Word DOCX](#convert-pdf-to-docx)

- [Java Biblioteca PDF para Word, API ou Código para Salvar, Gerar ou Criar Documentos Word Programaticamente a partir de PDF](#convert-pdf-to-docx)

## Converter PDF para DOC

Um dos recursos mais populares é a conversão de PDF para DOC do Microsoft Word, o que torna o conteúdo fácil de manipular. Aspose.PDF for Java permite que você converta arquivos PDF para DOC.

**Aspose.PDF for Java** pode criar documentos PDF do zero e é uma excelente ferramenta para atualizar, editar e manipular documentos PDF existentes. Uma característica importante é a capacidade de converter páginas e documentos PDF inteiros em imagens. Outro recurso popular é a conversão de PDF para DOC do Microsoft Word, o que torna o conteúdo fácil de manipular. (A maioria dos usuários não consegue editar documentos PDF, mas pode facilmente trabalhar com tabelas, texto e imagens no Microsoft Word.)

Para simplificar e tornar compreensível, Aspose.PDF for Java fornece um código de duas linhas para transformar um arquivo PDF de origem em um arquivo DOC.

O seguinte trecho de código Java mostra o processo de conversão de um arquivo PDF para o formato DOC.

1. Crie uma instância do objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document) com o documento PDF de origem.
2. Salve-o no formato **SaveFormat.Doc** chamando o método **Document.save()**.

```java
public static void convertPDFtoWord() {
    // Abra o documento PDF de origem
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Salve o arquivo no formato de documento MS
    document.save(DATA_DIR + "PDFToDOC_out.doc", SaveFormat.Doc);
    document.close();
}
```

## Usando a Classe DocSaveOptions

A [classe DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) fornece inúmeras propriedades que melhoram o processo de conversão de arquivos PDF para o formato DOC. Entre essas propriedades, Mode permite que você especifique o modo de reconhecimento para o conteúdo do PDF. Você pode especificar qualquer valor da enumeração RecognitionMode para esta propriedade. Cada um desses valores tem benefícios e limitações específicas:

- O modo [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) é rápido e bom para preservar a aparência original de um arquivo PDF, mas a editabilidade do documento resultante pode ser limitada.
 Cada bloco de texto visualmente agrupado no PDF original é convertido em uma caixa de texto no documento de saída. Isso atinge uma semelhança máxima com o original para que o documento de saída fique bom, mas consiste inteiramente em caixas de texto e isso pode tornar a edição no Microsoft Word difícil.

- O Flow é o modo de reconhecimento completo, onde o motor realiza agrupamento e análise multinível para restaurar o documento original conforme a intenção do autor, enquanto produz um documento facilmente editável. A limitação é que o documento de saída pode parecer diferente do original.

- A propriedade RelativeHorizontalProximity pode ser usada para controlar a proximidade relativa entre elementos textuais e significa que a distância é normatizada pelo tamanho da fonte. Fontes maiores podem ter distâncias maiores entre sílabas e ainda serem consideradas como um único todo. Ela é especificada como uma porcentagem do tamanho da fonte, por exemplo, 1 = 100%. Isso significa que dois caracteres de 12pt colocados a 12 pt de distância são proximais.

- RecognitionBullets é usado para ativar o reconhecimento de marcadores durante a conversão.
```java
public static void convertPDFtoWordDocAdvanced() {
    Path pdfFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.pdf");
    Path docFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.doc");
    Document document = new Document(pdfFile.toString());
    DocSaveOptions saveOptions = new DocSaveOptions();

    // Especificar o formato de saída como DOC
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    // Definir o modo de reconhecimento como Flow
    saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);

    // Definir a proximidade horizontal como 2.5
    saveOptions.setRelativeHorizontalProximity(2.5f);

    // Habilitar o valor para reconhecer marcadores durante o processo de conversão
    saveOptions.setRecognizeBullets(true);

    document.save(docFile.toString(), saveOptions);
    document.close();
}
```

{{% alert color="success" %}}
**Tente converter PDF para DOC online**


Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["PDF para Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Converter PDF para DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter PDF para DOCX

A enumeração DocFormat também oferece a opção de escolher DOCX como o formato de saída para documentos do Word. Para renderizar o arquivo PDF de origem para o formato DOCX, use o trecho de código especificado abaixo.

## Como converter PDF para DOCX

O trecho de código Java a seguir mostra o processo de conversão de um arquivo PDF para o formato DOCX.

1. Crie uma instância do objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document) com o documento PDF de origem.
2. Salve no formato **SaveFormat.DocX** chamando o método **Document.save()**.

```java
public static void convertPDFtoWord_DOCX_Format() {
    // Abra o documento PDF de origem
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Salve o arquivo DOC resultante
    document.save(DATA_DIR + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    document.close();
}
```

A classe [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) tem uma propriedade chamada Format que fornece a capacidade de especificar o formato do documento resultante, ou seja, DOC ou DOCX.
 A fim de converter um arquivo PDF para o formato DOCX, por favor passe o valor Docx da enumeração DocSaveOptions.DocFormat.

Por favor, veja o trecho de código a seguir que fornece a capacidade de converter um arquivo PDF para o formato DOCX com Java.

```java
public static void convertPDFtoWord_Advanced_DOCX_Format() {
    // Abra o documento PDF de origem
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");

    // Instanciar o objeto DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions();
    // Especificar o formato de saída como DOCX
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    // Definir outros parâmetros do DocSaveOptions
    // ....

    // Salvar documento no formato docx
    document.save("ConvertToDOCX_out.docx", saveOptions);
    document.close();
}
```

{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF para Java apresenta um aplicativo online gratuito ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.
[![Aspose.PDF Conversão PDF para DOCX App Gratuito](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}