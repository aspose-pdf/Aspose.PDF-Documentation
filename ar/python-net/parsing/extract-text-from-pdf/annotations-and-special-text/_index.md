---
title: التعليقات التوضيحية والنصوص الخاصة باستخدام بايثون
linktitle: التعليقات التوضيحية والنصوص الخاصة
type: docs
weight: 40
url: /ar/python-net/annotation-and-special-text/
description: يتضمن هذا القسم مقالات حول التعليقات التوضيحية واستخراج النصوص الخاصة من مستندات PDF باستخدام Aspose.PDF في بايثون.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من تعليقات الطوابع

تتيح لك مكتبة Aspose.PDF للبايثون استخراج النص من تعليق طابع (وتحديدًا StampAnnotation) على صفحة PDF.

1. افتح المستند.
1. الوصول إلى تعليق الطابع من مجموعة تعليقات الصفحة.
1. احصل على تدفق الظهور للطابع (XForm).
1. استخدم 'TextAbsorber' لاستخراج النص المضمّن من ذلك الظهور.

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

## استخراج النص المظلل

يوفر معيار PDF القدرة على تظليل أجزاء من النص في مستند. لاستخراج هذا المحتوى المظلل، اتبع الخطوات التالية:

1. استورد `aspose.pdf as ap` وأي مساعدات تستخدمها (`is_assignable`، `cast`).
2. استدعِ `ap.Document(infile)` لفتح ملف PDF.
3. اختر الصفحة المطلوبة باستخدام `document.pages` (مجموعة الصفحات تبدأ من 1).
4. حلق عبر `page.annotations` لفحص كل تعليق في تلك الصفحة.
5. صَفِّ التعليقات بحيث يتم معالجة تعليقات التظليل فقط.
6. حول التعليق إلى `HighlightAnnotation` واستدعِ `get_marked_text()` لقراءة النص المظلل.
7. اطبع النص أو عالجه بأي طريقة أخرى.

```python

import os
import aspose.pdf as ap

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

## استخراج نصوص الحروف العلوية والسفلية

**الحروف السفلية والعلوية** تُستخدم غالبًا في الصيغ، التعابير الرياضية، ومواصفات المركبات الكيميائية. من الصعب تعديلها عندما يكون هناك الكثير منها في نفس الفقرة النصية.
في أحد الإصدارات الأخيرة، أضافت مكتبة **Aspose.PDF للبايثون عبر .NET** دعمًا لاستخراج نصوص الحروف العلوية والسفلية من PDF. استخرج كل النص (بما في ذلك الحروف العلوية والسفلية) من صفحة محددة في مستند PDF باستخدام 'TextFragmentAbsorber'.

1. حمّل مستند PDF.
1. أنشئ مثيلًا لـ 'TextFragmentAbsorber()', والذي يدعم اكتشاف نصوص الحروف العلوية/السفلية حسب قدرات الإصدار.
1. استدعِ 'document.pages[page_number].accept(absorber)' لمسح الصفحة المحددة فقط.
1. استرجع النص المستخرج عبر 'absorber.text'.
1. اكتب النص في ملف الإخراج باستخدام إدخال/إخراج الملفات القياسي.
1. أغلق المستند لتحرير الموارد.

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

## التكرار عبر TextFragments لاكتشاف الحروف العلوية/السفلية

احلق عبر كل جزء نص في صفحة، وتحقق مما إذا كان حرفًا عُلويًا أو سفليًا، وتعامل معه وفقًا لذلك.

1. حمّل مستند PDF.
1. أنشئ 'TextFragmentAbsorber()' واقبلها على الصفحة المختارة.
1. وصول إلى 'absorber.text_fragments'، التي تُرجع مجموعة من الأجزاء الموجودة في تلك الصفحة.
1. لكل جزء:
- استرجِ 'fragment.text'.
- تحقق من 'fragment.text_state.superscript' و 'fragment.text_state.subscript'.
- اكتب سطرًا إلى ملف الإخراج يتضمن نص الجزء والعلامات.
1. أغلق الملف والمستند.

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
