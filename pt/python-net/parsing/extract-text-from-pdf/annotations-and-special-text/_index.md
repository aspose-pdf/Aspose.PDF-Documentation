---
title: Anotações e Texto Especial usando Python
linktitle: Anotações e Texto Especial
type: docs
weight: 40
url: /pt/python-net/annotation-and-special-text/
description: Aprenda como extrair texto de anotações de selo, texto destacado e conteúdo de sobrescrito/subscrito em documentos PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair Texto de Anotações de Selo

Usar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) para extrair texto incorporado em um [StampAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) fluxo de aparência. Isso é útil quando o conteúdo do carimbo é renderizado como um XObject de formulário em vez de ser armazenado como texto simples.

1. Abra o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Acesse a anotação de destino a partir de `page.annotations`.
1. Verifique se é um `StampAnnotation`, então recupere sua aparência normal XForm.
1. Passe o XForm para `TextAbsorber.visit()` para extrair o texto incorporado.

```python
import os
import aspose.pdf as ap


def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```

## Extrair Texto Realçado

Iterar sobre as anotações de uma página e usar [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) para ler os trechos de texto cobertos por cada realce. A coleção de anotações da página usa indexação a partir de 1.

1. Abra o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) e selecione a página de destino.
1. Percorrer `page.annotations`.
1. Usar `is_assignable` para filtrar [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) instâncias.
1. Faça o cast da anotação e chame `get_marked_text()` para recuperar o conteúdo destacado.

```python
def extract_highlight_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```

## Extrair texto sobrescrito e subscrito

Sobrescritos e subscritos aparecem com frequência em fórmulas, expressões matemáticas e nomes de compostos químicos. Aspose.PDF for Python via .NET suporta a extração desse conteúdo através de [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber), que detecta metadados de posicionamento ao nível de caracteres.

1. Abra o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Criar um `TextFragmentAbsorber` instância.
1. Chamar `document.pages[page_number].accept(absorber)` para digitalizar a página de destino.
1. Recupere o texto extraído completo de `absorber.text`.
1. Escreva o resultado em um arquivo e feche o documento.

```python
import os
import aspose.pdf as ap


def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Iterar pelos Fragmentos de Texto para Detectar Sobrescrito/Subscrito

Para inspeção por fragmento, itere sobre `absorber.text_fragments` e leia o `text_state.superscript` e `text_state.subscript` bandeiras booleanas em cada [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. Abra o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) e criar um [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Aceite o absorvedor na página de destino para preencher `absorber.text_fragments`.
1. Para cada fragmento, leia `fragment.text`, `fragment.text_state.superscript`, e `fragment.text_state.subscript`.
1. Escreva os resultados no arquivo de saída e feche o documento.

```python
import os
import aspose.pdf as ap


def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf-8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript  # True if subscript
                f.write(
                    f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n"
                )
    finally:
        document.close()
```
