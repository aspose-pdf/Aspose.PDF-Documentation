---
title: Anotações e Texto Especial usando Python
linktitle: Anotações e Texto Especial
type: docs
weight: 40
url: /pt/python-net/annotation-and-special-text/
description: Esta seção contém artigos sobre anotação e extração de Texto especial de documentos PDF usando Aspose.PDF em Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Anotações de Carimbo

A biblioteca Aspose.PDF for Python permite extrair texto de uma anotação de carimbo (especificamente um StampAnnotation) em uma página PDF.

1. Abra o documento.
1. Acesse a anotação de carimbo a partir da coleção de anotações da página.
1. Obtenha o fluxo de aparência do carimbo (XForm).
1. Use um 'TextAbsorber' para extrair o texto incorporado daquela aparência.

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

O padrão PDF oferece a capacidade de realçar partes do texto em um documento. Para extrair esse conteúdo realçado, siga estas etapas:

1. Importe `aspose.pdf as ap` e quaisquer auxiliares que você use (`is_assignable`, `cast`).
2. Chame `ap.Document(infile)` para abrir o PDF.
3. Selecione a página desejada com `document.pages` (a coleção de páginas começa em 1).
4. Percorra `page.annotations` para examinar cada anotação nesta página.
5. Filtre as anotações para que apenas as anotações de destaque sejam processadas.
6. Converta a anotação para `HighlightAnnotation` e chame `get_marked_text()` para ler o texto realçado.
7. Imprima ou manipule de outra forma o texto retornado.

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

## Extrair Texto de Sobrescritos e Subscritos

**SubScripts e SuperScripts** são mais frequentemente usados em fórmulas, expressões matemáticas e especificações de compostos químicos. É difícil editá‑los quando pode haver muitos deles no mesmo trecho de texto.
Em uma das versões mais recentes, a biblioteca **Aspose.PDF for Python via .NET** adicionou suporte à extração de texto de Sobrescritos e Subscritos de PDFs. Extraia todo o texto (incluindo sobrescritos e subscritos) de uma página específica de um documento PDF usando 'TextFragmentAbsorber'.

1. Carregue o documento PDF.
1. Instancie um 'TextFragmentAbsorber()', que suporta a detecção de texto sobrescrito/subscrito conforme as capacidades da versão.
1. Chame 'document.pages[page_number].accept(absorber)' para escanear apenas a página especificada.
1. Recupere o texto extraído via 'absorber.text'.
1. Grave o texto no arquivo de saída usando I/O de arquivo padrão.
1. Feche o documento para liberar recursos.

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
        with open(outfile, "w", encoding="utf‑8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Iterar pelos TextFragments para Detectar Sobrescrito/Subscrito

Percorra cada fragmento de texto em uma página, verifique se ele é sobrescrito ou subscrito, e processe adequadamente.

1. Carregue o documento PDF.
1. Crie 'TextFragmentAbsorber()' e aceite‑o na página escolhida.
1. Acesse 'absorber.text_fragments', que retorna uma coleção de fragmentos encontrados naquela página.
1. Para cada fragmento:
- Recupere 'fragment.text'.
- Verifique 'fragment.text_state.superscript' e 'fragment.text_state.subscript'.
- Grave uma linha no arquivo de saída com o texto do fragmento e as marcas.
1. Feche o arquivo e o documento.

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

        with open(outfile, "w", encoding="utf‑8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript    # True if subscript
                f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")
    finally:
        document.close()
```
