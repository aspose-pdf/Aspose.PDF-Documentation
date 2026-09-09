---
title: استخراج النص الأساسي باستخدام Python
linktitle: استخراج النص الأساسي
type: docs
weight: 10
url: /ar/python-net/basic-text-extraction/
description: تعرف على كيفية استخراج النص من مستندات PDF باستخدام Aspose.PDF لـ Python - من جميع الصفحات مرة واحدة أو من صفحة معينة.
lastmod: "2026-08-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج النص من جميع صفحات وثيقة PDF

استخدم [ممتص النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) لالتقاط كل النص من كل صفحة من وثيقة PDF وكتابته إلى ملف نصي. هذا الأسلوب مناسب تمامًا لتحويل ملفات PDF إلى نص يمكن البحث فيه أو تشغيل تحليل المحتوى أو إعداد النص للفهرسة والمعالجة النهائية.

1. افتح مستند PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. قم بإنشاء `TextAbsorber` مثال.
1. اتصل `document.pages.accept(text_absorber)` لمسح جميع الصفحات.
1. استرجع النص المستخرج من `text_absorber.text`.
1. اكتب النتيجة إلى ملف نصي الإخراج.

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
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## استخراج نص من صفحة معينة

تقدم بطلبك [ممتص النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) إلى صفحة واحدة لعزل النص وحفظه من هذا القسم من مستند متعدد الصفحات. يكون هذا مفيدًا عندما تحتاج إلى محتوى من صفحة واحدة فقط - على سبيل المثال، فاتورة أو قسم تقرير أو ملخص نموذج.

1. افتح مستند PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. قم بإنشاء `TextAbsorber` مثال.
1. اتصل `accept` على الصفحة المستهدفة: `document.pages[page_number].accept(text_absorber)`.
1. استرجع النص المستخرج واكتبه في ملف.

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## استخرج الفقرات عن طريق التكرار من خلالها

استخدم [ممتص الفقرة](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) عندما تحتاج إلى الاستخراج مع مراعاة الفقرة بدلاً من نص الصفحة العادية. على عكس [ممتص النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) أو [ممتص أجزاء النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/)، تقوم واجهة برمجة التطبيقات هذه بتنظيم الإخراج حسب الصفحة والقسم والفقرة، وهو أمر مفيد لتحليل النص والتصدير المنظم والمعالجة الحساسة للتخطيط.

1. افتح ملف PDF المصدر كملف [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. قم بإنشاء `ParagraphAbsorber` مثال.
1. اتصل `absorber.visit(document)` لتحليل جميع الصفحات.
1. قم بالتكرار من خلال `page_markups`، ثم من خلال كل قسم وفقرة.
1. اقرأ أجزاء النص من كل فقرة واكتب النتيجة إلى ملف.

```python
import aspose.pdf as ap


def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf-8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```