---
title: استخراج النص الأساسي باستخدام بايثون
linktitle: استخراج النص الأساسي
type: docs
weight: 10
url: /ar/python-net/basic-text-extraction/
description: يتضمن هذا القسم مقالات حول استخراج النص الأساسي من مستندات PDF باستخدام Aspose.PDF في بايثون.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

يُعلمك Aspose.PDF لبايثون كيفية استخراج النص من كل صفحة في مستند PDF. يستخدم فئة TextAbsorber لالتقاط جميع المحتوى النصي من المستند بالكامل ويحفظه في ملف نصي منفصل.
مثالي لتحويل ملفات PDF إلى نص قابل للبحث، وإجراء تحليل المحتوى، أو تصدير النص للفهرسة ومهام المعالجة.

1. تحميل ملف PDF.
1. إنشاء كائن 'TextAbsorber'.
1. استدعِ 'document.pages.accept(text_absorber)' لتقوم بمسح جميع الصفحات.
1. الحصول على النص الكامل عبر 'text_absorber.text'.
1. كتابة النتيجة في ملف نصي.

```python

import os
import aspose.pdf as ap

def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    try:
        # Create a TextAbsorber to extract text
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber for all pages
        document.pages.accept(text_absorber)
        # Get extracted text
        extracted_text = text_absorber.text
        # Write the text to an output file
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## استخراج النص من صفحة معينة

استخراج النص من صفحة واحدة من مستند PDF. عن طريق تطبيق TextAbsorber فقط على صفحة محددة، يمكنك عزل وحفظ النص من قسم معين من PDF متعدد الصفحات.

مفيد عندما تحتاج فقط إلى محتوى من صفحة واحدة — على سبيل المثال، استخراج النص من صفحة فاتورة، أو قسم تقرير، أو ملخص حقل نموذج.

1. فتح ملف PDF.
1. إنشاء TextAbsorber.
1. قبول الصفحة المحددة فقط (pages[page_number]).
1. استخراج النص وكتابته إلى ملف.

```python

import os
import aspose.pdf as ap

def extract_text_from_page(infile, page_number, outfile):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based page index to extract.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber on only the specified page
        document.pages[page_number].accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

