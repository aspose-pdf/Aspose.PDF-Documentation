---
title: Adicionando Número de Página ao PDF com Python
linktitle: Adicionando Número de Página
type: docs
weight: 30
url: /pt/python-net/add-page-number/
description: Aspose.PDF for Python via .NET permite que você adicione um carimbo de número de página ao seu arquivo PDF usando a classe PageNumberStamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar número de página ao PDF usando Python
Abstract: Este artigo discute a importância de adicionar números de página aos documentos para facilitar a navegação e apresenta a biblioteca Aspose.PDF for Python via .NET como uma ferramenta para alcançar isso em arquivos PDF. A biblioteca utiliza a classe PageNumberStamp, que oferece propriedades para personalizar o carimbo de número de página, incluindo formato, margens, alinhamentos e número inicial. O processo envolve criar um objeto Document e um objeto PageNumberStamp, configurar as propriedades desejadas e aplicar o carimbo às páginas do PDF usando o método add_stamp(). O artigo fornece um exemplo de código Python que demonstra como configurar e aplicar carimbos de número de página com atributos de fonte personalizáveis.
---

Todos os documentos devem ter números de página. O número de página facilita ao leitor localizar diferentes partes do documento.

**Aspose.PDF for Python via .NET** permite que você adicione números de página com [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Adicionando Carimbo de Número de Página a um PDF

Adicione carimbos de número de página dinâmicos a um PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF for Python. O objeto [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) permite exibir automaticamente o número da página atual juntamente com o número total de páginas. O exemplo mostra como criar um carimbo de número de página, personalizar sua aparência (fonte, tamanho, estilo, cor, alinhamento e margens) usando [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), e aplicá-lo a uma [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) específica no PDF via o método [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods). Os valores de alinhamento vêm do enum [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/), e cor/fonte/estilo estão disponíveis através de [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) e [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (fontes descobertas via [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). Esta funcionalidade é útil para gerar documentos profissionais numerados e automatizar a paginação em fluxos de trabalho de PDF.

1. Abra o documento PDF.
1. Crie um carimbo de número de página.
1. Defina as propriedades do carimbo.
1. Personalize o estilo do texto.
1. Aplique o carimbo a uma página.
1. Salve o PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Adicionando Números de Página em Numerais Romanos a um PDF

Adicione números de página em formato de numerais romanos a todas as páginas de um documento PDF. Os números de página são adicionados como carimbos usando [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), com fonte, tamanho, estilo, cor e alinhamento personalizáveis. Use o enum [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) para escolher numerais romanos ou outros esquemas de numeração. A numeração também pode iniciar a partir de qualquer valor especificado.

1. Abra o documento PDF.
1. Crie um carimbo de número de página.
1. Configure as propriedades do carimbo.
1. Defina a aparência do texto.
1. Aplique o carimbo a todas as páginas.
1. Salve o PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Exemplo Ao Vivo

[Adicionar números de página ao PDF](https://products.aspose.app/pdf/page-number) é um aplicativo web gratuito online que permite investigar como a funcionalidade de adicionar números de página funciona.

[![Como adicionar número de página em pdf usando Python](page_number.png)](https://products.aspose.app/pdf/page-number)


