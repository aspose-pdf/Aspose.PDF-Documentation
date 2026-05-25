---
title: Converter PDF para HTML em Python
linktitle: Converter PDF para formato HTML
type: docs
weight: 50
url: /pt/python-net/convert-pdf-to-html/
lastmod: "2026-05-21"
description: Aprenda como converter PDF para HTML em Python com Aspose.PDF for Python via .NET, incluindo saída de múltiplas páginas, imagens externas, manipulação de SVG e renderização de HTML em camadas.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF para HTML em Python
Abstract: Este artigo fornece um guia abrangente sobre como converter arquivos PDF para HTML usando Python, especificamente através da biblioteca Aspose.PDF for Python via .NET. Ele descreve as etapas necessárias para realizar essa conversão programaticamente, destacando a criação de um objeto `Document` a partir do PDF fonte e a utilização do `HtmlSaveOptions` para salvar o documento no formato HTML. O artigo inclui um trecho conciso de código Python que demonstra o processo de conversão. Além disso, apresenta uma ferramenta online, o aplicativo "PDF to HTML" da Aspose.PDF, para que os usuários explorem a funcionalidade e a qualidade da conversão. O artigo está estruturado para atender a vários tópicos relacionados, garantindo uma compreensão completa do uso de Python para a conversão de PDF para HTML.
---

## Converter PDF para HTML

**Aspose.PDF for Python via .NET** oferece muitos recursos para converter vários formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída. Este artigo discute como converter um arquivo PDF em <abbr title="HyperText Markup Language">HTML</abbr>. Você pode usar apenas algumas linhas de código Python para converter PDF em HTML. Você pode precisar converter PDF em HTML se quiser criar um site ou adicionar conteúdo a um fórum online. Uma maneira de converter PDF em HTML é usar Python programaticamente.

{{% alert color="success" %}}
**Tente converter PDF para HTML online**

Aspose.PDF for Python apresenta a você aplicação online ["PDF para HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para HTML com App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Etapas: Converter PDF para HTML em Python

1. Criar uma instância de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto com o documento PDF de origem.
1. Salvar em [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) chamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Conversões relacionadas

- [Converter HTML em PDF](/pdf/pt/python-net/convert-html-to-pdf/) quando precisar do fluxo de trabalho reverso web-para-documento.
- [Converter PDF para Word](/pdf/pt/python-net/convert-pdf-to-word/) se a saída de documento editável for mais útil do que HTML.
- [Converter PDF para formatos de imagem](/pdf/pt/python-net/convert-pdf-to-images-format/) para cenários de exportação raster.

### Converter PDF para HTML salvando imagens na pasta especificada

Esta função converte um arquivo PDF para o formato HTML usando Aspose.PDF for Python via .NET. Todas as imagens extraídas são armazenadas em uma pasta especificada em vez de serem incorporadas no arquivo HTML.

1. Configure as opções de salvamento HTML.
1. Salvar como HTML com imagens externas.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_images(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "images")
    save_options.special_folder_for_all_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML de várias páginas

Esta função converte um arquivo PDF em HTML multipáginas, onde cada página PDF é exportada como um arquivo HTML separado. Isso torna a saída mais fácil de navegar e reduz o tempo de carregamento para PDFs grandes.

1. Carregue o PDF de origem usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e defina `split_into_pages`.
1. Salve o documento como HTML com as páginas divididas em arquivos separados.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_multi_page(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML salvando imagens SVG em pasta especificada

Esta função converte um PDF para o formato HTML enquanto armazena todas as imagens como arquivos SVG em uma pasta especificada, em vez de incorporá‑las diretamente no HTML.

1. Carregue o PDF de origem usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e defina `special_folder_for_svg_images` para a pasta de destino.
1. Salve o documento como HTML com imagens SVG externas.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML e salvar imagens SVG compactadas

Este trecho converte um PDF para o formato HTML, armazenando todas as imagens como arquivos SVG em uma pasta especificada e comprimindo-os para reduzir o tamanho do arquivo.

1. Carregue o documento PDF usando 'ap.Document'.
1. Criar 'HtmlSaveOptions' e:
   - Defina 'special_folder_for_svg_images' para armazenar imagens SVG externamente.
   - Habilite 'compress_svg_graphics_if_any' para compactar imagens SVG.
1. Salve o documento como HTML com imagens SVG externas compactadas.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_compress_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    save_options.compress_svg_graphics_if_any = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML com controle de Imagens Raster Incorporadas

Este trecho converte um PDF para o formato HTML, incorporando imagens raster como fundos de página PNG. Essa abordagem preserva a qualidade da imagem e o layout da página no HTML.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e 'set raster_images_saving_mode' para 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Salve o documento como HTML com imagens raster incorporadas.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_PNG_background(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para página HTML contendo apenas o corpo

Esta função converte um PDF para o formato HTML, gerando conteúdo 'body-only' sem tags extras 'html' ou 'head', e divide a saída em páginas separadas.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e configure:
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' para gerar apenas o conteúdo 'body'.
   - 'split_into_pages' para criar arquivos HTML separados para cada página de PDF.
1. Salvar o documento como HTML com as opções especificadas.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_body_content(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.html_markup_generation_mode = (
        ap.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    )
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML com Renderização de Texto Transparente

Esta função converte um PDF para o formato HTML, renderizando todo o texto como transparente, incluindo textos com sombreamento, o que preserva a fidelidade visual ao mesmo tempo em que permite estilização flexível no HTML de saída.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e configure:
    - 'save_transparent_texts' para renderizar texto normal como transparente.
    - 'save_shadowed_texts_as_transparent_texts' para renderizar texto sombreado como transparente.
1. Salve o documento como HTML com renderização de texto transparente.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_transparent_text_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML com Renderização de Camadas de Documento

Esta função converte um PDF para o formato HTML, preservando as camadas do documento ao transformar o conteúdo marcado em camadas separadas no HTML de saída. Isso permite que os elementos em camadas (como anotações, fundos e sobreposições) sejam renderizados com precisão.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e habilite 'convert_marked_content_to_layers' para preservar camadas.
1. Salve o documento como HTML com conteúdo em camadas.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_document_layers_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

