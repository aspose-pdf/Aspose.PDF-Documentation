---
title: Converter PDF para EPUB, Texto, XPS e Mais em Python
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /pt/python-net/convert-pdf-to-other-files/
lastmod: "2026-05-21"
description: Aprenda como converter arquivos PDF para EPUB, LaTeX, Markdown, texto, XPS e MobiXML em Python com Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF para outros formatos em Python
Abstract: O artigo fornece um guia abrangente sobre como converter arquivos PDF em vários formatos usando Aspose.PDF for Python. Ele cobre a conversão de PDFs para os formatos EPUB, LaTeX/TeX, Texto, XPS e XML. Cada seção começa com um convite para experimentar as aplicações online fornecidas pela Aspose para converter PDFs nos formatos correspondentes, destacando a facilidade de uso e a qualidade dessas ferramentas.
---

## Converter PDF para EPUB

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF for Python apresenta a você um aplicativo online ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para EPUB com App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> é um padrão de e-book gratuito e aberto do International Digital Publishing Forum (IDPF). Os arquivos têm a extensão .epub.
EPUB foi projetado para conteúdo refluível, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico. EPUB também suporta conteúdo de layout fixo. O formato destina‑se a ser um único formato que editores e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

Aspose.PDF for Python também oferece o recurso de converter documentos PDF para o formato EPUB. Aspose.PDF for Python tem uma classe chamada 'EpubSaveOptions' que pode ser usada como o segundo argumento para [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método, para gerar um arquivo EPUB.
Por favor, tente usar o trecho de código a seguir para atender a esse requisito com Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Conversões relacionadas

- [Converter PDF para Word](/pdf/pt/python-net/convert-pdf-to-word/) para saída de documento do Office editável.
- [Converter PDF para HTML](/pdf/pt/python-net/convert-pdf-to-html/) para saída orientada ao navegador.
- [Converter PDF para PDF/A, PDF/E e PDF/X](/pdf/pt/python-net/convert-pdf-to-pdf_x/) para fluxos de trabalho de arquivamento e conversão compatíveis com padrões.

## Converter PDF para LaTeX/TeX

**Aspose.PDF for Python via .NET** suporta a conversão de PDF para LaTeX/TeX.
O formato de arquivo LaTeX é um formato de arquivo de texto com a marcação especial e usado em sistemas de preparação de documentos baseados em TeX para tipografia de alta qualidade.

{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF for Python apresenta a você um aplicativo online ["PDF para LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para LaTeX/TeX com App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para converter arquivos PDF para TeX, o Aspose.PDF tem a classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) que fornece a propriedade OutDirectoryPath para salvar imagens temporárias durante o processo de conversão.

O trecho de código a seguir mostra o processo de conversão de arquivos PDF para o formato TEX com Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para Texto

**Aspose.PDF for Python** suporta a conversão de todo o documento PDF e de uma única página para um arquivo de texto. Você pode converter um documento PDF em um arquivo TXT usando a classe 'TextDevice'. O trecho de código a seguir explica como extrair os textos de todas as páginas.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter PDF para Texto online**

Aspose.PDF for Python apresenta a você um aplicativo online ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para Texto com App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Converter PDF para XPS

**Aspose.PDF for Python** oferece a possibilidade de converter arquivos PDF para o formato XPS. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com Python.

{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF for Python apresenta a você um aplicativo online ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para XPS com App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

O tipo de arquivo XPS está principalmente associado à XML Paper Specification da Microsoft Corporation. A XML Paper Specification (XPS), anteriormente com o codinome Metro e que incorpora o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos no sistema operacional Windows.

Para converter arquivos PDF para XPS, o Aspose.PDF possui a classe [OpçõesDeSalvamentoXps](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) que é usado como o segundo argumento para o [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método para gerar o arquivo XPS.

O trecho de código a seguir mostra o processo de conversão de arquivo PDF para formato XPS.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para MD

Aspose.PDF tem a classe 'MarkdownSaveOptions()', que converte um documento PDF para o formato Markdown (MD) preservando imagens e recursos.

1. Carregue o PDF de origem usando 'ap.Document'.
1. Crie uma instância de 'MarkdownSaveOptions'.
1. Defina 'resources_directory_name' como 'images' – as imagens extraídas serão armazenadas nesta pasta.
1. Salve o documento Markdown convertido usando as opções configuradas.
1. Imprima uma mensagem de confirmação após a conversão.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

Um arquivo Markdown com texto e imagens vinculadas armazenadas na pasta de imagens especificada.

## Converter PDF para MobiXML

Este método converte um documento PDF para o formato MOBI (MobiXML), que é comumente usado para eBooks em dispositivos Kindle.

1. Carregue o documento PDF de origem usando 'ap.Document'.
1. Salve o documento com o formato 'ap.SaveFormat.MOBI_XML'.
1. Imprima uma mensagem de confirmação assim que a conversão for concluída.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
