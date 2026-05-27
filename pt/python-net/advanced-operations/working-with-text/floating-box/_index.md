---
title: Usar FloatingBox para Layout de PDF em Python
linktitle: Usando FloatingBox
type: docs
weight: 30
url: /pt/python-net/floating-box/
description: Aprenda a usar FloatingBox para layout de texto, conteúdo em várias colunas e posicionamento preciso em documentos PDF com Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Crie e posicione containers FloatingBox estilizados em PDF com Python.
Abstract: Este artigo explica como usar FloatingBox no Aspose.PDF for Python via .NET. Aprenda como colocar texto e outros conteúdos em contêineres flutuantes estilizados, controlar layout, bordas, alinhamento e recorte, e criar designs de página PDF mais estruturados em Python.
---

## Uso Básico do FloatingBox

O [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) classe é um contêiner para colocar texto e outro conteúdo em uma página PDF. Ele oferece controle mais forte sobre layout, bordas e estilo do que parágrafos de texto regulares. Se o conteúdo exceder o tamanho da caixa, o comportamento de recorte é controlado pelas configurações da caixa.

Use esta página quando precisar de contêineres de texto estruturados, layouts de múltiplas colunas e posicionamento preciso em documentos PDF com Aspose.PDF for Python via .NET.

1. Criar um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Adicionar um [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para o documento.
1. Criar um [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Defina a borda da caixa usando [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) e [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Repetição da caixa de controle com o [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) propriedade.
1. Adicionar conteúdo de texto usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Adicionar o `FloatingBox` para o [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Salve o documento PDF final usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap

def create_and_add_floating_box(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```

No exemplo acima, o `FloatingBox` é criado com uma largura de 400 pt e uma altura de 30 pt.
O texto intencionalmente excede a altura disponível, portanto parte dele é cortada.

![Imagem 1](image01.png)

O [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) propriedade com um valor de `False` limita a renderização de texto a uma única página.

Se você definir esta propriedade como `True`, o texto flui para as páginas subsequentes na mesma posição.

![Imagem 2](image02.png)

## Recursos Avançados de FloatingBox

### Suporte a múltiplas colunas

#### Layout de várias colunas (caso simples)

`FloatingBox` suporta layout de várias colunas. Para criar esse layout, você deve definir os valores de [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) propriedades.

* `column_widths` é uma cadeia de caracteres que define a largura de cada coluna em pontos.
* `column_spacing` é uma string que define a largura do espaço entre colunas.
* `column_count` é o número de colunas.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

O exemplo gera parágrafos de amostra e os coloca em três colunas. O conteúdo continua em páginas adicionais até que todos os parágrafos sejam renderizados.

#### Layout de múltiplas colunas com início de coluna forçado

Este exemplo usa a mesma configuração de múltiplas colunas, mas força cada parágrafo adicionado a começar em uma nova coluna. Para fazer isso, defina `is_first_paragraph_in_column = True` em cada `TextFragment` antes de adicioná-lo ao `FloatingBox`.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Suporte de fundo

Aplicar uma cor de fundo a um `FloatingBox` em um documento PDF usando Aspose.PDF for Python via .NET.
Ao atribuir um [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) para `background_color`, você pode destacar conteúdo para cabeçalhos, chamadas ou seções estilizadas.

Este trecho de código mostra como criar uma caixa de texto verde-clara simples com conteúdo de exemplo.

```python
import sys
import aspose.pdf as ap
from os import path

def background_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Suporte de posicionamento

A posição de um `FloatingBox` na página é controlado por `positioning_mode`, `left`, e `top`.
Quando `positioning_mode` é:

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (padrão)

A localização depende dos elementos adicionados anteriormente. Adicionar um novo parágrafo afeta o fluxo dos elementos subsequentes. Se [`left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) ou [`top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) são diferentes de zero, eles também são aplicados.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

A localização é definida por `left` e `top`; não depende de elementos anteriores e não afeta o fluxo dos posteriores.

```python
import sys
import aspose.pdf as ap
from os import path

def offset_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### Alinhar Caixas Flutuantes com Alinhamento Vertical e Horizontal em PDF

Alinhar `FloatingBox` elementos em uma página PDF usando [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) e [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) no Aspose.PDF for Python via .NET. Isso ajuda você a posicionar contêineres flutuantes nas posições superior, central ou inferior para layouts de página, blocos de cabeçalho/rodapé ou notas laterais.

1. Crie um novo documento PDF.
1. Adicione uma página ao documento.
1. Adicione o primeiro `FloatingBox` com alinhamento inferior direito.
1. Adicionar o segundo `FloatingBox` com alinhamento à direita central.
1. Adicionar o terceiro `FloatingBox` com alinhamento superior direito.
1. Salve o documento.

```python
import sys
import aspose.pdf as ap
from os import path

def align_text_to_float(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```

## Tópicos de Texto Relacionados

* [Trabalhe com texto em PDF usando Python](/pdf/pt/python-net/working-with-text/)
* [Adicionar texto ao PDF](/pdf/pt/python-net/add-text-to-pdf-file/)
* [Formatar texto PDF em Python](/pdf/pt/python-net/text-formatting-inside-pdf/)
* [Adicionar dicas de ferramenta ao texto PDF em Python](/pdf/pt/python-net/pdf-tooltip/)
