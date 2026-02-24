---
title: Улучшение извлечения текста из многоколоночных PDF
linktitle: Извлечение текста из многоколоночных PDF
type: docs
weight: 30
url: /ru/python-net/text-extraction-from-multi‑column-pdf/
description: Этот раздел содержит статьи о форматировании текста и масштабировании с использованием Aspose.PDF в Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

## Сократите размер шрифта вручную, а затем извлеките

Точность извлечения в многоколоночных PDF достигается за счёт предварительного уменьшения размера шрифта всех текстовых фрагментов перед извлечением. Этот процесс помогает избежать проблем с наложением текста, которые могут возникать в плотно отформатированных или многоколоночных макетах.
Это помогает при извлечении текста из сложных макетов — таких как журналы, научные статьи или брошюры — где изменение размера текста улучшает ясность макета и результаты извлечения.

1. Загрузите PDF.
1. Уменьшите размер шрифта существующих текстовых фрагментов, сохраните и заново откройте документ.
1. Используйте 'TextAbsorber' для извлечения текста со страниц.
1. Запишите извлечённый текст.

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

## Извлечение текста с коэффициентом масштабирования

Извлеките текст из PDF с многоколоночными макетами, применяя к документу коэффициент масштабирования. Регулировка коэффициента масштабирования гарантирует правильную интерпретацию текстовых фрагментов, уменьшая наложения или смещения при извлечении.
Это полезно для PDF с колонками, таблицами или плотными макетами, где масштабирование помогает сохранить правильный порядок чтения и структуру в извлечённом тексте.

1. Загрузите PDF.
1. Настройте 'TextExtractionOptions.ScaleFactor'.
1. Используйте 'TextAbsorber' для извлечения текста со страниц.
1. Запишите извлечённый текст.

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
