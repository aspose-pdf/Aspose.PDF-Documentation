---
title: Melhorando a Extração de Texto de PDFs Multi‑Coluna
linktitle: Extração de Texto de PDFs Multi‑Coluna
type: docs
weight: 30
url: /pt/python-net/text-extraction-from-multi‑column-pdf/
description: Esta seção contém artigos sobre formatação e dimensionamento de texto usando Aspose.PDF em Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

## Reduza o tamanho da fonte manualmente e então extraia

A precisão da extração em PDFs multi‑coluna é alcançada primeiro reduzindo o tamanho da fonte de todos os fragmentos de texto antes da extração. O processo ajuda a prevenir problemas de texto sobreposto que podem ocorrer em layouts estreitamente formatados ou multi‑coluna.
É útil para extrair texto de layouts complexos — como revistas, artigos acadêmicos ou folhetos — onde redimensionar o texto melhora a clareza do layout e os resultados da extração.

1. Carregue o PDF.
1. Reduza o tamanho da fonte dos fragmentos de texto existentes, salve e reabra o documento.
1. Use 'TextAbsorber' para extrair texto das páginas.
1. Grave o texto extraído.

```python

import io
import aspose.pdf as ap

def extract_text_reduce_font(infile, outfile, reduce_ratio=0.7):
    """
    Extract text from a multi-column PDF by first reducing font size of all text fragments.
    Args:
        infile (str): Path to input PDF.
        outfile (str): Output text file.
        reduce_ratio (float): Ratio to reduce font size (e.g., 0.7 = 70%).
    """
    doc = ap.Document(infile)
    try:
        frag_absorber = ap.text.TextFragmentAbsorber()
        doc.pages.accept(frag_absorber)
        for frag in frag_absorber.text_fragments:
            frag.text_state.font_size = frag.text_state.font_size * reduce_ratio
        # Save to memory stream and reopen (to apply changes)
        ms = io.BytesIO()
        doc.save(ms)
        ms.seek(0)
        doc2 = ap.Document(ms)
        text_absorber = ap.text.TextAbsorber()
        doc2.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```

## Extraia texto com fator de escala

Extraia texto de PDFs com layouts multi‑coluna aplicando um fator de escala ao documento. Ajustar o fator de escala garante que os fragmentos de texto sejam interpretados corretamente, reduzindo sobreposição ou desalinhamento durante a extração.
É útil para PDFs com colunas, tabelas ou layouts densos, onde o dimensionamento ajuda a manter a ordem de leitura e a estrutura corretas no texto extraído.

1. Carregue o PDF.
1. Configure 'TextExtractionOptions.ScaleFactor'.
1. Use 'TextAbsorber' para extrair texto das páginas.
1. Grave o texto extraído.

```python

import aspose.pdf as ap

def extract_text_with_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        ext_opts = ap.text.TextExtractionOptions(ap.text.TextExtractionOptions.TextFormattingMode.PURE)
        ext_opts.scale_factor = scale_factor
        text_absorber.extraction_options = ext_opts
        doc.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```
