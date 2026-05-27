---
title: Rotacionar Texto PDF em Python
linktitle: Rotacionar Texto Dentro do PDF
type: docs
weight: 50
url: /pt/python-net/rotate-text-inside-pdf/
description: Aprenda como rotacionar fragmentos de texto e parágrafos dentro de documentos PDF em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotacione fragmentos de texto e parágrafos em documentos PDF com Python
Abstract: Este artigo explica como girar texto em documentos PDF usando Aspose.PDF for Python via .NET. Ele mostra como definir a propriedade `rotation` em `TextFragment`, criar conteúdo girado com `TextBuilder` e `TextParagraph`, e adicionar texto girado diretamente aos parágrafos da página para diferentes cenários de layout.
---

Gire fragmentos de texto em um documento PDF usando Aspose.PDF for Python via .NET. Esta página mostra como controlar a posição e a rotação do texto usando `TextFragment`, `TextState`, e `TextBuilder`. Ao ajustar ângulos de rotação, você pode criar layouts como cabeçalhos diagonais, rótulos verticais e anotações rotacionadas.

## Girar Fragmentos de Texto Usando TextBuilder em PDF

Cria um arquivo PDF chamado `rotated_fragments.pdf` contendo três fragmentos de texto alinhados horizontalmente:

- o primeiro texto não está rotacionado
- o segundo está rotacionado 45°
- o terceiro está rotacionado 90°

1. Crie um novo documento PDF.
1. Insira uma nova página para hospedar o texto rotacionado.
1. Crie o primeiro fragmento de texto (sem rotação).
1. Crie o segundo fragmento de texto (rotação de 45°).
1. Crie o terceiro fragmento de texto (rotação de 90°).
1. Adicionar fragmentos de texto usando `TextBuilder`.
1. Salvar o documento.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotacionar fragmentos de texto individuais dentro de um parágrafo no PDF

Gire fragmentos de texto individuais dentro de um parágrafo. Ele demonstra como criar um parágrafo de várias linhas (TextParagraph) contendo múltiplos fragmentos (TextFragment), cada um com seu próprio ângulo de rotação. Esta técnica é útil para criar documentos visualmente ricos que combinam texto orientado horizontalmente e diagonalmente — por exemplo, cabeçalhos estilizados, diagramas ou rótulos anotados.

Cria um PDF chamado `rotated_paragraph_fragments.pdf` contendo um parágrafo com três linhas de texto, cada linha rotacionada de forma diferente:

- a primeira linha está rotacionada 45°
- a segunda linha permanece horizontal (0°)
- a terceira linha está rotacionada -45°

1. Crie um novo documento PDF.
1. Adicione uma página em branco onde o texto girado aparecerá.
1. Criar um `TextParagraph`.
1. Crie e configure o primeiro fragmento de texto (rotação de +45°).
1. Crie o segundo fragmento de texto (sem rotação).
1. Crie o terceiro fragmento de texto (-45° rotação).
1. Anexe fragmentos de texto ao parágrafo.
1. Adicione o parágrafo à página usando `TextBuilder`.
1. Salvar o documento.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Rotacionar Texto Usando Parágrafos de Página no PDF

Esta seção demonstra um método simplificado para girar texto dentro de um PDF usando Aspose.PDF for Python via .NET.
Ao contrário de abordagens de nível inferior com `TextBuilder` ou `TextParagraph`, este método adiciona fragmentos de texto rotacionados diretamente à coleção de parágrafos da página (`page.paragraphs`). É ideal quando você precisa de rotação de texto básica, mas não requer posicionamento preciso ou estruturação de parágrafos.

Gera um arquivo chamado `simple_rotated_text.pdf` contendo:

- um fragmento de texto horizontal principal com rotação de 0°
- fragmento rotacionado 315°
- fragmento girado 270°

1. Inicialize um novo PDF Document.
1. Crie uma página onde o texto girado será colocado.
1. Crie o primeiro fragmento de texto (sem rotação).
1. Crie o segundo fragmento de texto (rotação de 315°).
1. Crie o terceiro fragmento de texto (rotação de 270°).
1. Adicione fragmentos de texto diretamente aos parágrafos da página.
1. Salve o documento PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotacionar parágrafos inteiros em um PDF

Este exemplo demonstra rotação avançada de texto em nível de parágrafo em um PDF. Ao contrário da rotação em nível de fragmento (onde cada trecho de texto é rotacionado individualmente), este método rotaciona parágrafos inteiros como blocos unificados em ângulos diferentes.
Cada parágrafo contém múltiplos fragmentos de texto estilizados, e o parágrafo completo é girado em ângulos específicos — permitindo transformações de layout complexas e consistentes.
Isso é ideal para layouts artísticos, marcas d'água ou PDFs com muito design, onde seções inteiras de texto precisam ser orientadas em várias direções.

Cria `rotated_paragraphs.pdf`, contendo quatro parágrafos totalmente estilizados e girados:

- cada um girado em um ângulo único (45°, 135°, 225° e 315°)
- cada parágrafo tem três linhas de texto com fundos coloridos, sublinhado e estilo consistente

1. Crie um novo documento PDF.
1. Adicione uma página em branco para conter os parágrafos girados.
1. Iterar para criar vários parágrafos.
1. Crie e posicione o parágrafo.
1. Crie fragmentos de texto com formatação.
1. Aplicar formatação de texto.
1. Adicionar fragmentos de texto ao parágrafo.
1. Anexe o parágrafo à página usando `TextBuilder`.
1. Repita para todas as quatro rotações.
1. Salve o documento PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Tópicos de Texto Relacionados

- [Trabalhar com texto em PDF usando Python](/pdf/pt/python-net/working-with-text/)
- [Adicionando texto ao PDF](/pdf/pt/python-net/add-text-to-pdf-file/)
- [Formatar texto PDF em Python](/pdf/pt/python-net/text-formatting-inside-pdf/)
- [Substituir texto em PDF com Python](/pdf/pt/python-net/replace-text-in-pdf/)