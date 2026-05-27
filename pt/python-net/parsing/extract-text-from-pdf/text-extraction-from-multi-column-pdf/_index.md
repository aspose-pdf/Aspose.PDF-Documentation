---
title: Melhorando a Extração de Texto de PDFs Multi‑Coluna
linktitle: Extração de Texto de PDFs Multi‑Coluna
type: docs
weight: 30
url: /pt/python-net/text-extraction-from-multi-column-pdf/
description: Aprenda técnicas para melhorar a extração de texto de layouts de PDF de múltiplas colunas com Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Reduza o tamanho da fonte manualmente e então extraia

Em alguns layouts de múltiplas colunas, reduzir o tamanho da fonte dos fragmentos de texto antes da extração pode melhorar a ordem de leitura e reduzir problemas de sobreposição. Essa técnica pode ajudar em documentos com formatação apertada, como revistas, artigos de pesquisa, brochuras ou relatórios com colunas de texto densas.

1. Carregue o PDF.
1. Usar [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) para coletar os fragmentos de texto.
1. Reduza o tamanho da fonte de cada fragmento, então salve e reabra o documento.
1. Usar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) para extrair o texto.
1. Escreva o texto extraído em um arquivo de saída.

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
```

## Extrair texto com fator de escala

Outra opção para extração de múltiplas colunas é configurar [TextExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) com um fator de escala. Ajustar o fator de escala pode melhorar a interpretação de fragmentos densamente compactados e ajudar a preservar uma ordem de leitura mais precisa em layouts densos, tabelas ou documentos baseados em colunas.

1. Carregue o PDF.
1. Criar um [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. Configurar `TextExtractionOptions.scale_factor`.
1. Atribua as opções de extração ao absorvedor.
1. Extraia o texto da página e escreva o resultado em um arquivo de saída.

```python
import aspose.pdf as ap


def extract_text_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    ext_opts = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    ext_opts.scale_factor = scale_factor
    text_absorber.extraction_options = ext_opts
    doc.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
