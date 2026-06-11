---
title: تحسين استخراج النص من ملفات PDF متعددة الأعمدة
linktitle: استخراج النص من ملفات PDF متعددة الأعمدة
type: docs
weight: 30
url: /ar/python-net/text-extraction-from-multi-column-pdf/
description: تعلم تقنيات لتحسين استخراج النص من تخطيطات PDF متعددة الأعمدة باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## قم بتقليل حجم الخط يدويًا ثم استخرجه

في بعض التخطيطات متعددة الأعمدة، يمكن أن يؤدي تقليل حجم خط أجزاء النص قبل الاستخراج إلى تحسين ترتيب القراءة وتقليل مشكلات التداخل. يمكن أن تساعد هذه التقنية في المستندات المنسقة بإحكام مثل المجلات أو الأوراق البحثية أو الكتيبات أو التقارير ذات الأعمدة النصية الكثيفة.

1. قم بتحميل ملف PDF.
1. استخدم [ممتص أجزاء النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) لجمع أجزاء النص.
1. قم بتقليل حجم الخط لكل جزء، ثم احفظ المستند وأعد فتحه.
1. استخدم [ممتص النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) لاستخراج النص.
1. اكتب النص المستخرج إلى ملف الإخراج.

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

## استخراج النص باستخدام عامل القياس

هناك خيار آخر للاستخراج متعدد الأعمدة وهو التكوين [خيارات استخراج النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) مع عامل الحجم. يمكن أن يؤدي ضبط عامل القياس إلى تحسين تفسير الأجزاء المعبأة بإحكام والمساعدة في الحفاظ على ترتيب قراءة أكثر دقة في التخطيطات الكثيفة أو الجداول أو المستندات المستندة إلى الأعمدة.

1. قم بتحميل ملف PDF.
1. قم بإنشاء [ممتص النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. قم بالتهيئة `TextExtractionOptions.scale_factor`.
1. قم بتعيين خيارات الاستخراج للممتص.
1. استخرج نص الصفحة واكتب النتيجة إلى ملف الإخراج.

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
