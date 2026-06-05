---
title: Converter PDF para Word em Python
linktitle: Converter PDF para Word
type: docs
weight: 10
url: /pt/python-net/convert-pdf-to-word/
lastmod: "2026-04-14"
description: Aprenda como converter PDF para Word em Python, incluindo PDF para DOC, PDF para DOCX e reconhecimento avançado de layout com Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Converter PDF para DOC e DOCX em Python
Abstract: Este artigo mostra como converter arquivos PDF para formatos Microsoft Word com Aspose.PDF for Python via .NET. Ele aborda PDF para DOC, PDF para DOCX e opções avançadas de reconhecimento de layout para criar documentos Word editáveis a partir do conteúdo PDF.
---

Esta página mostra como **converter PDF para Word em Python**. Use estes exemplos quando precisar de saída editável em DOC ou DOCX a partir de um arquivo PDF para revisão, reutilização ou fluxos de trabalho de documentos de escritório.

## Converter PDF para DOC em Python

Um dos recursos mais populares é a conversão de PDF para Microsoft Word DOC, que facilita a gestão de conteúdo. **Aspose.PDF for Python via .NET** permite converter arquivos PDF não apenas para DOC, mas também para o formato DOCX, de forma fácil e eficiente.

Use a conversão Word quando precisar revisar texto, reutilizar conteúdo em fluxos de trabalho de escritório ou mover conteúdo PDF para documentos editáveis DOC ou DOCX.

O [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) classe fornece diversas propriedades que aprimoram o processo de conversão de arquivos PDF para o formato DOC. Entre essas propriedades, Mode permite que você especifique o modo de reconhecimento para o conteúdo PDF. Você pode especificar qualquer valor da enumeração RecognitionMode para essa propriedade. Cada um desses valores tem benefícios e limitações específicas:

Etapas: Converter PDF para DOC em Python

1. Carregue o PDF em um objeto 'ap.Document'.
1. Crie uma instância 'DocSaveOptions'.
1. Defina a propriedade format como 'DocFormat.DOC' para garantir que a saída esteja no formato .doc (formato Word mais antigo).
1. Salve o PDF como um documento Word usando as opções de salvamento especificadas.
1. Imprima uma mensagem de confirmação.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF for Python apresenta-lhe um aplicativo online [“PDF para DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Converter PDF para DOC](/pdf/pt/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter PDF para DOCX em Python

Aspose.PDF for Python API permite ler e converter documentos PDF para DOCX usando Python via .NET. DOCX é um formato bem conhecido para documentos Microsoft Word cuja estrutura foi alterada de binário simples para uma combinação de arquivos XML e binários. Arquivos DOCX podem ser abertos com Word 2007 e versões laterais, mas não com as versões anteriores do MS Word que suportam extensões de arquivo DOC.

O trecho de código Python a seguir mostra o processo de conversão de um arquivo PDF para o formato DOCX.

Etapas: Converter PDF para DOCX em Python

1. Carregue o PDF de origem usando 'ap.Document'.
1. Crie uma instância de 'DocSaveOptions'.
1. Defina a propriedade format como 'DocFormat.DOC_X' para gerar um arquivo .docx (formato Word moderno).
1. Salve o PDF como um arquivo DOCX com as opções de salvamento configuradas.
1. Exiba uma mensagem de confirmação após a conversão.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## Convert PDF to DOCX with Advanced Layout Recognition

Converta um documento PDF em um arquivo DOCX (Word) usando Python e Aspose.PDF com configurações avançadas de reconhecimento. Ele utiliza o modo de fluxo aprimorado para preservar a estrutura do documento, tornando a saída mais editável e mais próxima do layout original.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

O [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) A classe tem uma propriedade chamada Format que fornece a capacidade de especificar o formato do documento resultante, isto é, DOC ou DOCX. Para converter um arquivo PDF para o formato DOCX, por favor passe o valor Docx da enumeração DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF for Python apresenta-lhe um aplicativo online ["PDF para Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para Word App](/pdf/pt/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Conversões relacionadas

- [Converter PDF para Excel](/pdf/pt/python-net/convert-pdf-to-excel/) para exportações orientadas a planilhas.
- [Converter PDF para PowerPoint](/pdf/pt/python-net/convert-pdf-to-powerpoint/) quando você precisa de slides de apresentação em vez de saída de processamento de texto.
- [Converter PDF para HTML](/pdf/pt/python-net/convert-pdf-to-html/) para publicação na web e fluxos de trabalho de conteúdo baseados em navegador.
