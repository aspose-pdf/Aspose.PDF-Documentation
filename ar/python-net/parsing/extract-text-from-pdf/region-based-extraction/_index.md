---
title: الاستخراج المستند إلى المنطقة باستخدام Python
linktitle: الاستخراج المستند إلى المنطقة
type: docs
weight: 20
url: /ar/python-net/region-based-extraction/
description: تعرف على كيفية استخراج النص من منطقة صفحة معينة أو بنية فقرة في مستندات PDF باستخدام Aspose.PDF for Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج نص من منطقة معينة من الصفحة

استخدم [ممتص النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) جنبا إلى جنب مع [المستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) لقصر الاستخراج على منطقة معينة من الصفحة. يُعد هذا الأسلوب مفيدًا للاستخراج المستند إلى المنطقة من الرؤوس أو التذييلات أو خلايا الجدول أو حقول النموذج أو الفواتير أو مناطق التخطيط الثابت الأخرى حيث يكون موضع النص معروفًا مسبقًا.

1. افتح ملف PDF المصدر كملف [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. قم بإنشاء `TextAbsorber` مثال.
1. قم بالتهيئة `text_search_options` للحد من الاستخراج إلى مستطيل.
1. اقبل جهاز الامتصاص على الصفحة المستهدفة.
1. اكتب النص المستخرج إلى ملف الإخراج.

```python
import aspose.pdf as ap


def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
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

## استخراج الفقرات مع عرض المضلع المحيط

يمكنك أيضًا استخدام [ممتص الفقرة](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) لفحص هندسة الفقرة. بالإضافة إلى استخراج النص، يسجل هذا الأسلوب كل مستطيل مقطع ومضلع فقرة، وهو أمر مفيد لتخطيط التخطيط أو تحليل المستندات أو أدوات إمكانية الوصول أو المعالجة اللاحقة على دراية بالمنطقة.

1. افتح ملف PDF المصدر كملف [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. قم بإنشاء `ParagraphAbsorber` مثال.
1. قم بزيارة الصفحة المستهدفة.
1. اقرأ ترميز الصفحة من `absorber.page_markups`.
1. قم بالتكرار من خلال الأقسام والفقرات لالتقاط الهندسة والنص.
1. اكتب بيانات المستطيل والمضلع والنص إلى ملف الإخراج.

```python
import aspose.pdf as ap


def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf-8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```
