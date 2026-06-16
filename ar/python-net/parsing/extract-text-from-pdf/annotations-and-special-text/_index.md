---
title: التعليقات التوضيحية والنص الخاص باستخدام Python
linktitle: التعليقات التوضيحية والنص الخاص
type: docs
weight: 40
url: /ar/python-net/annotation-and-special-text/
description: تعرف على كيفية استخراج النص من التعليقات التوضيحية للطوابع والنص المميز ومحتوى النص المرتفع/الفرعي في مستندات PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج نص من التعليقات التوضيحية للطوابع

استخدم [ممتص النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) لاستخراج نص مضمن في ملف [التعليق التوضيحي للطوابع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) تيار المظهر. يكون هذا مفيدًا عندما يتم عرض محتوى الختم كنموذج XObject بدلاً من تخزينه كنص عادي.

1. افتح [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. الوصول إلى التعليق التوضيحي المستهدف من `page.annotations`.
1. تحقق من أنها `StampAnnotation`، ثم استرجع مظهره العادي XForm.
1. قم بتمرير النموذج إلى `TextAbsorber.visit()` لاستخراج النص المضمن.

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

## استخراج النص المميز

قم بالتكرار على التعليقات التوضيحية للصفحة واستخدامها [قم بتمييز التعليق التوضيحي. get_marked_text ()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) لقراءة الامتدادات النصية التي يغطيها كل تمييز. تستند مجموعة التعليقات التوضيحية للصفحة إلى 1.

1. افتح [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) وحدد الصفحة المستهدفة.
1. قم بالمرور عبر حلقة `page.annotations`.
1. استخدم `is_assignable` للتصفية لـ [قم بتمييز التعليق التوضيحي](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) مثيلات.
1. أرسل التعليق التوضيحي واتصل `get_marked_text()` لاسترداد المحتوى المميز.

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

## استخراج النص العلوي والنص الفرعي

تظهر الحروف العلوية والرموز الفرعية بشكل متكرر في الصيغ والتعبيرات الرياضية وأسماء المركبات الكيميائية. Aspose.PDF لبيثون عبر .NET يدعم استخراج هذا المحتوى من خلال [ممتص أجزاء النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber)، الذي يكتشف البيانات الوصفية لتحديد المواقع على مستوى الحرف.

1. افتح [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. قم بإنشاء `TextFragmentAbsorber` مثال.
1. اتصل `document.pages[page_number].accept(absorber)` لمسح الصفحة المستهدفة.
1. استرجع النص الكامل المستخرج من `absorber.text`.
1. اكتب النتيجة إلى ملف وأغلق المستند.

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

## قم بالتكرار من خلال أجزاء النص لاكتشاف النص المرتفع/النص الفرعي

للفحص لكل جزء، قم بالتكرار `absorber.text_fragments` واقرأ `text_state.superscript` و `text_state.subscript` أعلام منطقية على كل منها [جزء من النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. افتح [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) وقم بإنشاء [ممتص أجزاء النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. اقبل أداة الامتصاص على الصفحة المستهدفة للتعبئة `absorber.text_fragments`.
1. لكل جزء، اقرأ `fragment.text`, `fragment.text_state.superscript`، و `fragment.text_state.subscript`.
1. اكتب النتائج إلى ملف الإخراج وأغلق المستند.

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
