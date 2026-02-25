---
title: Extração Baseada em Região usando Python
linktitle: Extração Baseada em Região
type: docs
weight: 20
url: /pt/python-net/region-based-extraction/
description: Esta seção contém artigos sobre extração baseada em região de documentos PDF usando Aspose.PDF em Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Extrair texto de uma região específica de uma página

Extrair texto de uma região retangular definida em uma página específica de um PDF usando Aspose.PDF para Python. Ao especificar coordenadas, você pode concentrar a extração em uma área específica — como uma célula de tabela, bloco de parágrafo ou região de campo de formulário.

Ideal para extração de texto baseada em zona, como a obtenção de dados de cabeçalhos, rodapés, faturas ou relatórios de layout fixo onde o texto aparece em posições previsíveis.

1. Abra o documento PDF.
1. Crie um 'TextAbsorber'.
1. Configure 'text_search_options' para restringir à região retangular.
1. Aplique o absorvedor na página específica.
1. Grave o texto extraído.

```python

import os
import aspose.pdf as ap

def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Extrair Parágrafos iterando sobre eles

Podemos obter texto de um documento PDF pesquisando um texto específico (usando "texto simples" ou "expressões regulares") em uma única página ou em todo o documento, ou podemos obter o texto completo de uma única página, intervalo de páginas ou documento completo. No entanto, em alguns casos, é necessário extrair parágrafos de um documento PDF ou texto na forma de Parágrafos. Implementamos funcionalidade para pesquisar seções e parágrafos no texto das páginas de documentos PDF. Introduzimos a classe ParagraphAbsorber (como TextFragmentAbsorber e TextAbsorber), que pode ser usada para extrair parágrafos de documentos PDF.

A biblioteca Aspose.PDF permite ler um arquivo PDF e extrair todo o texto de parágrafos de cada página usando 'ParagraphAbsorber'. Ela organiza a saída por página, seção e parágrafo, e grava o conteúdo extraído em um arquivo de texto simples. Isso é útil para análise de texto, arquivamento ou conversão de conteúdo PDF estruturado em formatos legíveis.

1. Abra o documento PDF.
1. Instancie um 'ParagraphAbsorber'.
1. Chame 'absorber.visit(document)' para analisar todas as páginas em busca de parágrafos.
1. Percorra a coleção 'page_markups' do absorvedor.
1. Para cada page‑markup, percorra suas 'sections', então cada 'paragraph' na seção.
1. Dentro de cada parágrafo, percorra 'lines', então cada 'fragment' na linha, acumulando 'fragment.text'.
1. Grave cada parágrafo (com índices de página/seção/parágrafo) no arquivo de saída.
1. Feche o documento ao terminar.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf‑8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Extrair Parágrafos com renderização de polígono delimitador

Este trecho de código extrai texto e informações de layout ao nível de parágrafo de uma página específica em um PDF. Ele captura o retângulo delimitador e as coordenadas do polígono de cada parágrafo, juntamente com o conteúdo real do texto, e grava os resultados em um arquivo de texto. Isso é útil para analisar a estrutura do documento, mapear layout ou preparar dados para tarefas de acessibilidade e extração de conteúdo.

1. Abra o PDF e carregue o documento.
1. Instancie 'ParagraphAbsorber'.
1. Chame 'absorber.visit(page)' para a página específica desejada.
1. Obtenha o primeiro 'page_markup' de 'absorber.page_markups'.
1. Para cada seção nesse markup:
- Recupere seu 'rectangle'.
1. Para cada parágrafo na seção:
- Obtenha seus 'points' (polígono).
- Extraia o texto percorrendo 'paragraph.lines' - 'fragment.text'.
1. Grave as informações de geometria e texto no arquivo de saída.
1. Feche o documento.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf‑8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```

