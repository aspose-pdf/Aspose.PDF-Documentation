---
title: Converter PDF para Documentos do Microsoft Word em Python
linktitle: Converter PDF para Word 2003/2019
type: docs
weight: 10
url: pt/python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: Aprenda como escrever código Python para conversão de formatos de PDF para Microsoft Word com Aspose.PDF para Python via .NET e ajuste a conversão de PDF para DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visão Geral

Este artigo explica como **converter PDF para Documentos do Microsoft Word usando Python**. Ele abrange os seguintes tópicos.

_Formato_: **DOC**
- [Python PDF para DOC](#python-pdf-to-doc)
- [Python Converter PDF para DOC](#python-pdf-to-doc)
- [Python Como converter arquivo PDF para DOC](#python-pdf-to-doc)

_Formato_: **DOCX**
- [Python PDF para DOCX](#python-pdf-to-docx)
- [Python Converter PDF para DOCX](#python-pdf-to-docx)
- [Python Como converter arquivo PDF para DOCX](#python-pdf-to-docx)

_Formato_: **Word**
- [Python PDF para Word](#python-pdf-to-docx)
- [Python Converter PDF para Word](#python-pdf-to-doc)

- [Python Como converter arquivo PDF para Word](#python-pdf-to-docx)

## Conversão de PDF para DOC e DOCX em Python

Uma das funcionalidades mais populares é a conversão de PDF para DOC do Microsoft Word, o que facilita a gestão de conteúdo. **Aspose.PDF para Python** permite converter arquivos PDF não apenas para DOC, mas também para o formato DOCX, de maneira fácil e eficiente.

## Converter PDF para arquivo DOC (Word 97-2003)

Converta arquivos PDF para o formato DOC com facilidade e total controle. Aspose.PDF para Python é flexível e suporta uma grande variedade de conversões. Converter páginas de documentos PDF para imagens, por exemplo, é uma funcionalidade muito popular.

Uma conversão que muitos dos nossos clientes solicitaram é de PDF para DOC: converter um arquivo PDF em um documento do Microsoft Word. Os clientes desejam isso porque os arquivos PDF não podem ser facilmente editados, enquanto os documentos do Word podem. Algumas empresas querem que seus usuários possam manipular texto, tabelas e imagens em arquivos que começaram como PDFs.

Mantendo viva a tradição de tornar as coisas simples e compreensíveis, Aspose.PDF para Python permite transformar um arquivo PDF de origem em um arquivo DOC com duas linhas de código.
 Para realizar este recurso, introduzimos uma enumeração chamada SaveFormat e seu valor .Doc permite que você salve o arquivo de origem no formato Microsoft Word.

O snippet de código Python a seguir mostra o processo de conversão de um arquivo PDF para o formato DOC.

<a name="csharp-pdf-to-doc"><strong>Passos: Converter PDF para DOC em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
2. Salve-o no formato [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) chamando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # Abrir documento PDF
    document = ap.Document(input_pdf)
    # Salvar o arquivo no formato de documento MS Word
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### Usando a Classe DocSaveOptions

A classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) fornece inúmeras propriedades que melhoram o processo de conversão de arquivos PDF para o formato DOC. Entre estas propriedades, Mode permite que você especifique o modo de reconhecimento para o conteúdo do PDF. Você pode especificar qualquer valor da enumeração RecognitionMode para esta propriedade. Cada um desses valores tem benefícios e limitações específicos:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # Definir o modo de reconhecimento como Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Definir a proximidade horizontal como 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Ativar o valor para reconhecer marcadores durante o processo de conversão
    save_options.recognize_bullets = True

    # Salvar o arquivo no formato de documento do MS Word
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**Tente converter PDF para DOC online**


Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter PDF para DOCX

Aspose.PDF para Python API permite que você leia e converta documentos PDF para DOCX usando Python via .NET. DOCX é um formato bem conhecido para documentos do Microsoft Word cuja estrutura foi alterada de binário simples para uma combinação de arquivos XML e binários. Arquivos Docx podem ser abertos com Word 2007 e versões posteriores, mas não com as versões anteriores do MS Word que suportam extensões de arquivo DOC.

O seguinte trecho de código Python mostra o processo de conversão de um arquivo PDF em formato DOCX.

<a name="csharp-pdf-to-docx"><strong>Passos: Converter PDF para DOCX em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.

2. Salve-o no formato [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) chamando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # Abra o documento PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # Defina o modo de reconhecimento como Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Defina a proximidade horizontal como 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Habilite o valor para reconhecer marcadores durante o processo de conversão
    save_options.recognize_bullets = True

    # Salve o arquivo no formato de documento do MS Word
    document.save(output_pdf, save_options)
```

A classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) tem uma propriedade chamada Format que fornece a capacidade de especificar o formato do documento resultante, ou seja, DOC ou DOCX.
 Para converter um arquivo PDF para o formato DOCX, por favor, passe o valor Docx da enumeração DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF para Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Word App Gratuito](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Veja Também

Este artigo também cobre esses tópicos. Os códigos são os mesmos que acima.

_Formato_: **Word**
- [Código Python PDF para Word](#python-pdf-to-docx)
- [API Python PDF para Word](#python-pdf-to-docx)
- [Python PDF para Word Programaticamente](#python-pdf-to-docx)
- [Biblioteca Python PDF para Word](#python-pdf-to-docx)
- [Salvar PDF como Word em Python](#python-pdf-to-docx)
- [Gerar Word a partir de PDF em Python](#python-pdf-to-docx)
- [Criar Word a partir de PDF em Python](#python-pdf-to-docx)

- [Conversor Python PDF para Word](#python-pdf-to-docx)
_Format_: **DOC**
- [Código Python PDF para DOC](#python-pdf-to-doc)
- [API Python PDF para DOC](#python-pdf-to-doc)
- [Python PDF para DOC Programaticamente](#python-pdf-to-doc)
- [Biblioteca Python PDF para DOC](#python-pdf-to-doc)
- [Python Salvar PDF como DOC](#python-pdf-to-doc)
- [Python Gerar DOC de PDF](#python-pdf-to-doc)
- [Python Criar DOC de PDF](#python-pdf-to-doc)
- [Conversor Python PDF para DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [Código Python PDF para DOCX](#python-pdf-to-docx)
- [API Python PDF para DOCX](#python-pdf-to-docx)
- [Python PDF para DOCX Programaticamente](#python-pdf-to-docx)
- [Biblioteca Python PDF para DOCX](#python-pdf-to-docx)
- [Python Salvar PDF como DOCX](#python-pdf-to-docx)
- [Python Gerar DOCX de PDF](#python-pdf-to-docx)
- [Python Criar DOCX de PDF](#python-pdf-to-docx)
- [Conversor Python PDF para DOCX](#python-pdf-to-docx)