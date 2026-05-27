---
title: Converter outros formatos de arquivo para PDF em Python
linktitle: Converter outros formatos de arquivo para PDF
type: docs
weight: 80
url: /pt/python-net/convert-other-files-to-pdf/
lastmod: "2026-05-18"
description: Aprenda como converter arquivos EPUB, Markdown, PCL, XPS, PostScript, XML e LaTeX para PDF em Python com Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Como converter outros formatos de arquivo para PDF em Python
Abstract: Este artigo fornece um guia abrangente sobre a conversão de diversos formatos de arquivo para PDF usando Python, aproveitando os recursos do Aspose.PDF for Python via .NET. O documento descreve os processos de conversão para vários formatos, incluindo EPUB, Markdown, PCL, Text, XPS, PostScript, XML, XSL-FO e LaTeX/TeX. Cada seção oferece trechos de código específicos e instruções para implementar essas conversões. O artigo enfatiza a utilidade dos recursos do Aspose.PDF, como opções de carregamento personalizadas para cada tipo de arquivo, para garantir conversões precisas e eficientes. Além disso, destaca a disponibilidade de aplicações de conversão online para que os usuários explorem a funcionalidade diretamente. O guia serve como um recurso prático para desenvolvedores que desejam integrar capacidades de conversão para PDF em suas aplicações Python.
---

Este artigo explica como **converter vários outros tipos de formatos de arquivo para PDF usando Python**. Ele aborda os seguintes tópicos.

## Converter OFD para PDF

OFD significa Open Fixed-layout Document (também chamado de formato Open Fixed Document). É um padrão nacional chinês (GB/T 33190-2016) para documentos eletrônicos, introduzido como uma alternativa ao PDF.

Etapas para converter OFD em PDF em Python:

1. Configure as opções de carregamento OFD usando OfdLoadOptions().
1. Carregue o documento OFD.
1. Salvar como PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_OFD_to_PDF(infile, outfile):
    load_options = ap.OfdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Converter LaTeX/TeX para PDF

O formato de arquivo LaTeX é um formato de arquivo de texto com marcação na derivada LaTeX da família de linguagens TeX e o LaTeX é um formato derivado do sistema TeX. LaTeX (ˈleɪtɛk/lay-tek ou lah-tek) é um sistema de preparação de documentos e linguagem de marcação de documentos. É amplamente usado para a comunicação e publicação de documentos científicos em muitas áreas, incluindo matemática, física e ciência da computação. Também desempenha um papel fundamental na preparação e publicação de livros e artigos que contêm material multilíngue complexo, como coreano, japonês, caracteres chineses e árabe, incluindo edições especiais.

LaTeX usa o programa de composição tipográfica TeX para formatar sua saída, e ele próprio é escrito na linguagem de macros TeX.

{{% alert color="success" %}}
**Tente converter LaTeX/TeX para PDF online**

Aspose.PDF for Python via .NET apresenta a você um aplicativo online ["LaTex para PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão LaTeX/TeX para PDF com App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Passos para Converter TEX em PDF em Python:

1. Configure as opções de carregamento do LaTeX usando LatexLoadOptions().
1. Carregue o documento LaTeX.
1. Salvar como PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TEX_to_PDF(infile, outfile):
    load_options = ap.LatexLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Converter EPUB para PDF

**Aspose.PDF for Python via .NET** permite que você simplesmente converta arquivos EPUB para o formato PDF.

EPUB (abreviação de publicação eletrônica) é um padrão gratuito e aberto de e-book da International Digital Publishing Forum (IDPF). Os arquivos têm a extensão .epub. O EPUB foi projetado para conteúdo refluível, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico.

<abbr title="electronic publication">EPUB</abbr> também suporta conteúdo de layout fixo. O formato foi concebido como um único formato que editores e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook. A versão EPUB 3 também é endossada pelo Book Industry Study Group (BISG), uma associação líder do comércio de livros para práticas recomendadas padronizadas, pesquisa, informação e eventos, para o empacotamento de conteúdo.

{{% alert color="success" %}}
**Tente converter EPUB para PDF online**

Aspose.PDF for Python via .NET apresenta a você um aplicativo online ["EPUB para PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão de EPUB para PDF com App Aspose.PDF](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Etapas para Converter EPUB em PDF em Python:

1. Carregue o Documento EPUB com EpubLoadOptions().
1. Converter EPUB para PDF.
1. Imprimir Confirmação.

O próximo trecho de código mostra como converter arquivos EPUB para o formato PDF com Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_EPUB_to_PDF(infile, outfile):
    load_options = ap.EpubLoadOptions()
    document = ap.Document(infile, load_options)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Converter Markdown para PDF

**Este recurso é suportado a partir da versão 19.6 ou superior.**

{{% alert color="success" %}}
**Tente converter Markdown para PDF online**

Aspose.PDF for Python via .NET apresenta a você um aplicativo online ["Markdown para PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de Markdown para PDF com App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Este trecho de código da Aspose.PDF for Python via .NET ajuda a converter arquivos Markdown em PDFs, permitindo melhor compartilhamento de documentos, preservação de formatação e compatibilidade de impressão.o

O trecho de código a seguir mostra como usar esta funcionalidade com a biblioteca Aspose.PDF:

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_MD_to_PDF(infile, outfile):
    load_options = ap.MdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Converter PCL para PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) é uma linguagem de impressora da Hewlett-Packard desenvolvida para acessar recursos padrão de impressoras. Os níveis PCL 1 a 5e/5c são linguagens baseadas em comandos que utilizam sequências de controle processadas e interpretadas na ordem em que são recebidas. Em nível de consumidor, os fluxos de dados PCL são gerados por um driver de impressão. A saída PCL também pode ser facilmente gerada por aplicações personalizadas.

{{% alert color="success" %}}
**Tente converter PCL para PDF online**

Aspose.PDF for for .NET apresenta-lhe um aplicativo online ["PCL para PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PCL para PDF com App](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

Para permitir a conversão de PCL para PDF, Aspose.PDF tem a classe [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) que é usado para inicializar o objeto LoadOptions. Mais tarde, esse objeto é passado como argumento durante a inicialização do objeto Document e ajuda o mecanismo de renderização de PDF a determinar o formato de entrada do documento de origem.

O trecho de código a seguir mostra o processo de conversão de um arquivo PCL para o formato PDF.

Etapas Converter PCL para PDF em Python:

1. Opções de carregamento para PCL usando PclLoadOptions().
1. Carregue o documento.
1. Salvar como PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PCL_to_PDF(infile, outfile):
    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Converter texto pré-formatado para PDF

**Aspose.PDF for Python via .NET** suporta o recurso de converter texto simples e arquivos de texto pré-formatados para o formato PDF.

Converter texto para PDF significa adicionar fragmentos de texto à página PDF. Quanto a arquivos de texto, estamos lidando com 2 tipos de texto: pré-formatação (por exemplo, 25 linhas com 80 caracteres por linha) e texto não formatado (texto simples). Dependendo de nossas necessidades, podemos controlar essa adição nós mesmos ou confiá‑la aos algoritmos da biblioteca.

{{% alert color="success" %}}
**Tente converter TEXTO para PDF online**

Aspose.PDF for Python via .NET apresenta a você um aplicativo online ["Texto para PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de texto para PDF com App](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Passos para Converter TEXTO em PDF em Python:

1. Leia o arquivo de texto de entrada linha por linha.
1. Configure uma fonte monoespaçada (Courier New) para alinhamento consistente do texto.
1. Crie um novo PDF Document e adicione a primeira página com margens personalizadas e configurações de Font.
1. Iterar nas linhas do arquivo de texto Para simular Máquina de escrever, usamos a fonte \u0027monospace_font\u0027 com tamanho 12.
1. Limite a criação de páginas a 4 páginas.
1. Salve o PDF final no caminho especificado.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TXT_to_PDF(infile, outfile):
    with open(infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Converter PostScript para PDF

Este exemplo demonstra como converter um arquivo PostScript em um documento PDF usando Aspose.PDF for Python via .NET.

1. Crie uma instância de 'PsLoadOptions' para interpretar corretamente o arquivo PS.
1. Carregue o arquivo ‘PostScript’ em um objeto Document usando as opções de carregamento.
1. Salve o documento no formato PDF para o caminho de saída desejado.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Converter XPS para PDF

**Aspose.PDF for Python via .NET** suporta recurso de conversão <abbr title="XML Paper Specification">XPS</abbr> arquivos para o formato PDF. Consulte este artigo para resolver suas tarefas.

O tipo de arquivo XPS está principalmente associado à XML Paper Specification da Microsoft Corporation. A XML Paper Specification (XPS), anteriormente codinome Metro e que engloba o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos em seu sistema operacional Windows.

O seguinte trecho de código mostra o processo de conversão de arquivo XPS para formato PDF com Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XPS_to_PDF(infile, outfile):
    load_options = ap.XpsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter o formato XPS para PDF online**

Aspose.PDF for Python via .NET apresenta a você um aplicativo online ["XPS para PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de XPS para PDF com App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Converter XSL-FO para PDF

O trecho de código a seguir pode ser usado para converter um XSLFO para o formato PDF com Aspose.PDF for Python via .NET:

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## Converter XML com XSLT para PDF

Este exemplo demonstra como converter um arquivo XML em PDF, primeiro transformando-o em HTML usando um modelo XSLT e, em seguida, carregando o HTML no Aspose.PDF.

1. Crie uma instância de 'HtmlLoadOptions' para configurar a conversão de HTML para PDF.
1. Carregue o arquivo HTML transformado em um objeto Aspose.PDF Document.
1. Salve o documento como PDF no caminho de saída especificado.
1. Remova o arquivo HTML temporário após a conversão bem-sucedida.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## Conversões relacionadas

- [Converter HTML para PDF](/pdf/pt/python-net/convert-html-to-pdf/) para cenários de conversão de HTML e MHTML.
- [Converter formatos de imagem para PDF](/pdf/pt/python-net/convert-images-format-to-pdf/) quando suas entradas são PNG, JPEG, TIFF, SVG ou outras imagens.
- [Converter PDF para outros formatos](/pdf/pt/python-net/convert-pdf-to-other-files/) se você também precisar de conversões reversas, como PDF para EPUB, Markdown ou texto.
