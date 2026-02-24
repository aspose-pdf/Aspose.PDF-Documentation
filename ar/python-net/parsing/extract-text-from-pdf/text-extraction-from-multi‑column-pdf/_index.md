---
title: تحسين استخراج النص من ملفات PDF متعددة الأعمدة
linktitle: استخراج النص من ملفات PDF متعددة الأعمدة
type: docs
weight: 30
url: /ar/python-net/text-extraction-from-multi‑column-pdf/
description: يتضمن هذا القسم مقالات حول تنسيق النص وتكبيره باستخدام Aspose.PDF في بايثون.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

## تقليل حجم الخط يدويًا ثم الاستخراج

تحقق دقة الاستخراج في ملفات PDF متعددة الأعمدة عن طريق تقليل حجم الخط لجميع أجزاء النص قبل الاستخراج. يساعد هذا الإجراء على منع مشكلات تداخل النص التي قد تحدث في تنسيقات ضيقة أو تخطيطات متعددة الأعمدة.
يساعد ذلك في استخراج النص من تخطيطات معقدة—مثل المجلات، الأوراق الأكاديمية، أو الكتيبات—حيث يؤدي تعديل حجم النص إلى تحسين وضوح التخطيط ونتائج الاستخراج.

1. تحميل ملف PDF.
1. تقليل حجم الخط لأجزاء النص الحالية، ثم حفظ وإعادة فتح المستند.
1. استخدم 'TextAbsorber' لاستخراج النص من الصفحات.
1. كتابة النص المستخرج.

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

## استخراج النص باستخدام عامل مقياس

استخراج النص من ملفات PDF ذات التخطيطات متعددة الأعمدة عن طريق تطبيق عامل مقياس على المستند. يضمن ضبط عامل المقياس تفسير أجزاء النص بشكل صحيح، مما يقلل من التداخل أو الخطأ في المحاذاة أثناء الاستخراج.
يكون ذلك مفيدًا لملفات PDF ذات الأعمدة أو الجداول أو التخطيطات الكثيفة، حيث يساعد التكبير على الحفاظ على ترتيب القراءة الصحيح والهيكل في النص المستخرج.

1. تحميل ملف PDF.
1. ضبط 'TextExtractionOptions.ScaleFactor'.
1. استخدم 'TextAbsorber' لاستخراج النص من الصفحات.
1. كتابة النص المستخرج.

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
