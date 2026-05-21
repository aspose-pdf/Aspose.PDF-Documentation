---
title: Adicionar Números de Página ao PDF em Python
linktitle: Adicionando Número de Página
type: docs
weight: 30
url: /pt/python-net/add-page-number/
description: Aprenda como adicionar carimbos de número de página a documentos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar Número de Página ao PDF usando Python
Abstract: Este artigo discute a importância de adicionar números de página aos documentos para facilitar a navegação e apresenta a biblioteca Aspose.PDF for Python via .NET como uma ferramenta para alcançar isso em arquivos PDF. A biblioteca utiliza a classe PageNumberStamp, que oferece propriedades para personalizar o carimbo de número de página, incluindo formato, margens, alinhamentos e número inicial. O processo envolve criar um objeto Document e um objeto PageNumberStamp, configurar as propriedades desejadas e aplicar o carimbo às páginas PDF usando o método add_stamp(). O artigo fornece um exemplo de código Python demonstrando como configurar e aplicar carimbos de número de página com atributos de fonte personalizáveis.
---

Todos os documentos devem ter números de página. O número de página facilita ao leitor localizar diferentes partes do documento.

**Aspose.PDF for Python via .NET** permite que você adicione números de página com [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Adicionando carimbo de número de página a um PDF

Adicione carimbos de número de página dinâmicos a um PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF for Python. O [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) objeto permite exibir automaticamente o número da página atual junto com o número total de páginas. O exemplo mostra como criar um carimbo de número de página, personalizar sua aparência (fonte, tamanho, estilo, cor, alinhamento e margens) usando [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), e aplicá-lo a um específico [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) no PDF via o [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) método. Os valores de alinhamento vêm de [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) enum, e cor/fonte/estilo estão disponíveis através de [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) e [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (fontes descobertas via [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). Essa funcionalidade é útil para gerar documentos profissionais numerados e automatizar a paginação em fluxos de trabalho PDF.

1. Abra o documento PDF.
1. Crie um carimbo de número de página.
1. Defina as propriedades do carimbo.
1. Personalize o estilo do texto.
1. Aplicar o carimbo a uma página.
1. Salvar o PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

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
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Adicionando números de página em algarismos romanos a um PDF

Adicione números de página no formato de algarismos romanos a todas as páginas de um documento PDF. Os números de página são adicionados como marcas usando [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), com fonte, tamanho, estilo, cor e alinhamento personalizáveis. Use o [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) enum para escolher algarismos romanos ou outros esquemas de numeração. A numeração também pode começar a partir de qualquer valor especificado.

1. Abra o documento PDF.
1. Crie um carimbo de número de página.
1. Configurar propriedades do carimbo.
1. Definir a aparência do texto.
1. Aplicar o carimbo a todas as páginas.
1. Salvar o PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

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

## Exemplo ao Vivo

[Adicionar números de página ao PDF](https://products.aspose.app/pdf/page-number) é um aplicativo web gratuito online que permite investigar como funciona a funcionalidade de adicionar números de página.

[![Como adicionar número de página em PDF usando Python](page_number.png)](https://products.aspose.app/pdf/page-number)

## Tópicos Relacionados a Carimbos

- [Carimbar páginas de PDF em Python](/pdf/pt/python-net/stamping/)
- [Adicionar carimbos de página ao PDF em Python](/pdf/pt/python-net/page-stamps-in-the-pdf-file/)
- [Adicionar carimbos de imagem ao PDF em Python](/pdf/pt/python-net/image-stamps-in-pdf-page/)
- [Adicionar carimbos de texto ao PDF em Python](/pdf/pt/python-net/text-stamps-in-the-pdf-file/)