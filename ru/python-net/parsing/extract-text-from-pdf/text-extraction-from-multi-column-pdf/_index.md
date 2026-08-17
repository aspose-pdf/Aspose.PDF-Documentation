---
title: Улучшите извлечение текста из многоколоночных PDF
linktitle: Улучшите извлечение текста из многоколоночных PDF
type: docs
weight: 30
url: /ru/python-net/text-extraction-from-multi-column-pdf/
description: Узнайте о приёмах улучшения извлечения текста из многоколоночных макетов PDF с помощью Aspose.PDF for Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Уменьшите размер шрифта вручную перед извлечением

В некоторых многоколоночных макетах уменьшение размера шрифта текстовых фрагментов перед извлечением может улучшить порядок чтения и уменьшить проблемы с наложением. Этот приём помогает при работе с плотно оформленными документами, например журналами, научными статьями, брошюрами или отчётами с насыщенными текстовыми колонками.

1. Загрузите PDF.
1. Используйте [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), чтобы собрать текстовые фрагменты.
1. Уменьшите размер шрифта каждого фрагмента, затем сохраните и повторно откройте документ.
1. Используйте [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/), чтобы извлечь текст.
1. Запишите извлечённый текст в выходной файл.

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

## Извлеките текст с коэффициентом масштабирования

Ещё один вариант для извлечения из многоколоночных документов — настроить [TextExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) с коэффициентом масштабирования. Изменение `scale_factor` может улучшить интерпретацию плотно расположенных фрагментов и помочь сохранить более точный порядок чтения в насыщенных макетах, таблицах и документах с колонками.

1. Загрузите PDF.
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. Настройте `TextExtractionOptions.scale_factor`.
1. Присвойте параметры извлечения поглотителю.
1. Извлеките текст страницы и запишите результат в выходной файл.

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
