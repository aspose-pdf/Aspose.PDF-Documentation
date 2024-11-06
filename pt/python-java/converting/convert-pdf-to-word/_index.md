---
title: Converter PDF para Documentos Microsoft Word em Python
linktitle: Converter PDF para Word 2003/2019
type: docs
weight: 10
url: pt/python-java/convert-pdf-to-word/
lastmod: "2023-04-06"
description: Aprenda a escrever código Python para conversão de formatos PDF para Microsoft Word com Aspose.PDF para Python via .NET. e ajuste a conversão de PDF para DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visão Geral

Este artigo explica como **converter PDF para Documentos Microsoft Word usando Python**. Ele cobre esses tópicos.

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

Um dos recursos mais populares é a conversão de PDF para DOC do Microsoft Word, que facilita o gerenciamento de conteúdo. **Aspose.PDF for Python** permite converter arquivos PDF não apenas para DOC, mas também para o formato DOCX, de maneira fácil e eficiente.

## Converter PDF para arquivo DOC (Word 97-2003)

Converta arquivos PDF para o formato DOC com facilidade e controle total. Aspose.PDF for Python é flexível e suporta uma ampla variedade de conversões. Converter páginas de documentos PDF em imagens, por exemplo, é um recurso muito popular.

Uma conversão que muitos de nossos clientes solicitaram é de PDF para DOC: converter um arquivo PDF em um documento do Microsoft Word. Os clientes querem isso porque os arquivos PDF não podem ser facilmente editados, enquanto os documentos do Word podem. Algumas empresas desejam que seus usuários possam manipular texto, tabelas e imagens em arquivos que começaram como PDFs.

Mantendo viva a tradição de tornar as coisas simples e compreensíveis, o Aspose.PDF for Python permite transformar um arquivo PDF de origem em um arquivo DOC com duas linhas de código.
 Para realizar esse recurso, introduzimos uma enumeração chamada SaveFormat e seu valor .Doc permite salvar o arquivo de origem no formato Microsoft Word.

O seguinte trecho de código Python mostra o processo de conversão de um arquivo PDF para o formato DOC.

<a name="csharp-pdf-to-doc"><strong>Passos: Converter PDF para DOC em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) com o documento PDF de origem.
2. Salve-o no formato [SaveFormat.Doc](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) chamando o método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python

from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/out.doc"
doc.save(documentOutName, Api.SaveFormat.Doc)
```

### Usando a Classe DocSaveOptions

A classe [DocSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/docsaveoptions/) fornece várias propriedades que melhoram o processo de conversão de arquivos PDF para o formato DOC. Entre essas propriedades, o Modo permite que você especifique o modo de reconhecimento para o conteúdo do PDF. Você pode especificar qualquer valor da enumeração RecognitionMode para esta propriedade. Cada um desses valores tem benefícios e limitações específicos:

```python

from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
# Abrir documento PDF
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Doc
# Definir o modo de reconhecimento como Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# Definir a proximidade horizontal como 2.5
save_options.relative_horizontal_proximity = 2.5
# Ativar o valor para reconhecer marcadores durante o processo de conversão
save_options.recognize_bullets = True

# Salvar o arquivo no formato de documento do MS Word
document.save(output_pdf, save_options)

```

{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF para Python apresenta a você a aplicação online gratuita ["PDF para DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.
[![Converter PDF para DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## Converter PDF para DOCX

Aspose.PDF para Python API permite ler e converter documentos PDF para DOCX usando Python via .NET. DOCX é um formato conhecido para documentos do Microsoft Word cuja estrutura foi alterada de binário simples para uma combinação de arquivos XML e binários. Arquivos Docx podem ser abertos com o Word 2007 e versões posteriores, mas não com as versões anteriores do MS Word que suportam extensões de arquivos DOC.

O seguinte trecho de código Python mostra o processo de conversão de um arquivo PDF para o formato DOCX.

<a name="csharp-pdf-to-docx"><strong>Etapas: Converter PDF para DOCX em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) com o documento PDF de origem.

2. Salve-o no formato [SaveFormat.DocX](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) chamando o método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.docx"
# Abrir documento PDF
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Docx
# Definir o modo de reconhecimento como Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# Definir a proximidade horizontal como 2.5
save_options.relative_horizontal_proximity = 2.5
# Habilitar o valor para reconhecer marcadores durante o processo de conversão
save_options.recognize_bullets = True

# Salvar o arquivo no formato de documento do MS Word
document.save(output_pdf, save_options)
```

A classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) tem uma propriedade chamada Format, que fornece a capacidade de especificar o formato do documento resultante, ou seja, DOC ou DOCX.
 Para converter um arquivo PDF para o formato DOCX, por favor, passe o valor Docx da enumeração DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF para Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aplicativo Gratuito de Conversão de PDF para Word Aspose.PDF](/pdf/java/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Veja Também 

Este artigo também aborda estes tópicos. Os códigos são os mesmos acima.

_Formato_: **Word**
- [Código Python PDF para Word](#python-pdf-to-docx)
- [API Python PDF para Word](#python-pdf-to-docx)
- [PDF para Word Programaticamente em Python](#python-pdf-to-docx)
- [Biblioteca Python PDF para Word](#python-pdf-to-docx)
- [Salvar PDF como Word em Python](#python-pdf-to-docx)
- [Gerar Word a partir de PDF em Python](#python-pdf-to-docx)
- [Criar Word a partir de PDF em Python](#python-pdf-to-docx)

- [Conversor Python PDF para Word](#python-pdf-to-docx)
_Format_: **DOC**
- [Código Python PDF para DOC](#python-pdf-to-doc)
- [API Python PDF para DOC](#python-pdf-to-doc)
- [Programar Python PDF para DOC](#python-pdf-to-doc)
- [Biblioteca Python PDF para DOC](#python-pdf-to-doc)
- [Salvar PDF como DOC em Python](#python-pdf-to-doc)
- [Gerar DOC a partir de PDF em Python](#python-pdf-to-doc)
- [Criar DOC a partir de PDF em Python](#python-pdf-to-doc)
- [Conversor de PDF para DOC em Python](#python-pdf-to-doc)

_Format_: **DOCX**
- [Código Python PDF para DOCX](#python-pdf-to-docx)
- [API Python PDF para DOCX](#python-pdf-to-docx)
- [Programar Python PDF para DOCX](#python-pdf-to-docx)
- [Biblioteca Python PDF para DOCX](#python-pdf-to-docx)
- [Salvar PDF como DOCX em Python](#python-pdf-to-docx)
- [Gerar DOCX a partir de PDF em Python](#python-pdf-to-docx)
- [Criar DOCX a partir de PDF em Python](#python-pdf-to-docx)
- [Conversor de PDF para DOCX em Python](#python-pdf-to-docx)