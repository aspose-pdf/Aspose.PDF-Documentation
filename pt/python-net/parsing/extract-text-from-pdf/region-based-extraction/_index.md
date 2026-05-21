---
title: Extração baseada em região usando Python
linktitle: Extração baseada em região
type: docs
weight: 20
url: /pt/python-net/region-based-extraction/
description: Aprenda como extrair texto de uma região específica da página ou da estrutura de parágrafos em documentos PDF com Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair texto de uma região específica de uma página

Usar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) juntamente com um [Retângulo](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) para limitar a extração a uma área específica de uma página. Esta abordagem é útil para extração baseada em zonas de cabeçalhos, rodapés, células de tabela, campos de formulário, faturas ou outras regiões de layout fixo onde a posição do texto é conhecida antecipadamente.

1. Abra o PDF de origem como um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Criar um `TextAbsorber` instância.
1. Configurar `text_search_options` para limitar a extração a um retângulo.
1. Aceite o absorvedor na página de destino.
1. Escreva o texto extraído em um arquivo de saída.

```python
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

## Extrair parágrafos iterando sobre eles

Usar [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) quando você precisa de extração consciente de parágrafos em vez de texto de página simples. Ao contrário [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) ou [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), esta API organiza a saída por página, seção e parágrafo, o que é útil para análise de texto, exportação estruturada e processamento sensível ao layout.

1. Abra o PDF de origem como um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Criar um `ParagraphAbsorber` instância.
1. Chamar `absorber.visit(document)` para analisar todas as páginas.
1. Iterar através `page_markups`, então através de cada seção e parágrafo.
1. Leia os fragmentos de texto de cada parágrafo e escreva o resultado em um arquivo.

```python
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

        with open(outfile, "w", encoding="utf-8") as tw:
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
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Extrair Parágrafos com renderização de polígono delimitador

Você também pode usar [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) para inspecionar a geometria do parágrafo. Além de extrair texto, esta abordagem registra o retângulo de cada seção e o polígono do parágrafo, o que é útil para mapeamento de layout, análise de documentos, ferramentas de acessibilidade ou pós-processamento sensível à região.

1. Abra o PDF de origem como um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Criar um `ParagraphAbsorber` instância.
1. Visite a página de destino.
1. Ler a marcação da página de `absorber.page_markups`.
1. Itere pelas seções e parágrafos para capturar geometria e texto.
1. Escreva os dados de retângulo, polígono e texto no arquivo de saída.

```python
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
        with open(outfile, "w", encoding="utf-8") as tw:
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
