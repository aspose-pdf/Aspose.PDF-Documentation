---
title: استخراج قائم على المنطقة باستخدام بايثون
linktitle: استخراج قائم على المنطقة
type: docs
weight: 20
url: /ar/python-net/region-based-extraction/
description: يتضمن هذا القسم مقالات حول استخراج قائم على المنطقة من مستندات PDF باستخدام Aspose.PDF في بايثون.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من منطقة محددة في صفحة

استخراج النص من منطقة مستطيلة معرفة في صفحة معينة من ملف PDF باستخدام Aspose.PDF للبايثون. من خلال تحديد الإحداثيات، يمكنك تركيز الاستخراج على منطقة محددة — مثل خلية جدول، أو كتلة فقرة، أو منطقة حقل نموذج.

مثالي لاستخراج النص القائم على المناطق، مثل سحب البيانات من رؤوس الصفحات، وتذييلات الصفحات، والفواتير، أو التقارير ذات التخطيط الثابت حيث يظهر النص في مواقع متوقعة.

1. افتح مستند PDF.
1. أنشئ كائن 'TextAbsorber'.
1. اضبط 'text_search_options' لتقييد المنطقة بالمستطيل.
1. طبق الامتصاص على الصفحة المحددة.
1. احفظ النص المستخرج.

```python

import os
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

## استخراج الفقرات عبر التكرار عليها

يمكننا الحصول على نص من مستند PDF من خلال البحث عن نص معين (باستخدام "نص عادي" أو "تعبيرات نمطية") في صفحة واحدة أو في المستند كله، أو يمكننا الحصول على النص الكامل لصفحة واحدة، أو مجموعة من الصفحات، أو المستند بالكامل. ومع ذلك، في بعض الحالات قد تحتاج إلى استخراج الفقرات من مستند PDF أو النص على شكل فقرات. لقد نفذنا وظيفة للبحث عن الأقسام والفقرات في نص صفحات مستند PDF. لقد قدمنا فئة ParagraphAbsorber (مثل TextFragmentAbsorber و TextAbsorber)، والتي يمكن استخدامها لاستخراج الفقرات من مستندات PDF.

تتيح لك مكتبة Aspose.PDF قراءة ملف PDF واستخراج كل نص الفقرات من كل صفحة باستخدام 'ParagraphAbsorber'. تقوم بتنظيم المخرجات حسب الصفحة والقسم والفقرة، وتكتب المحتوى المستخرج في ملف نصي عادي. هذا مفيد لتحليل النصوص، أو الأرشفة، أو تحويل محتوى PDF المهيكل إلى تنسيقات قابلة للقراءة.

1. افتح مستند PDF.
1. أنشئ كائن 'ParagraphAbsorber'.
1. استدعِ 'absorber.visit(document)' لفحص جميع الصفحات بحثًا عن الفقرات.
1. تجول في مجموعة 'page_markups' للامتصاص.
1. لكل 'page‑markup'، تجول في 'sections' الخاصة به، ثم كل 'paragraph' داخل القسم.
1. داخل كل فقرة، تجول في 'lines'، ثم كل 'fragment' في السطر، مع جمع 'fragment.text'.
1. احفظ كل فقرة (مع فهارس الصفحة/القسم/الفقرة) في ملف المخرجات.
1. أغلق المستند عند الانتهاء.

```python

import os
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

        with open(outfile, "w", encoding="utf‑8") as tw:
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
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## استخراج الفقرات مع رسم حدود متعددة الأضلاع

يستخرج هذا المقتطف البرمجي نص الفقرات ومعلومات التخطيط من صفحة محددة في PDF. يلتقط المستطيل الحدودي لكل فقرة وإحداثيات المضلع، إلى جانب محتوى النص الفعلي، ويكتب النتائج إلى ملف نصي. هذا مفيد لتحليل هيكل المستند، ورسم خريطة التخطيط، أو إعداد البيانات لإمكانية الوصول ومهام استخراج المحتوى.

1. افتح ملف PDF وحمّل المستند.
1. أنشئ كائن 'ParagraphAbsorber'.
1. استدعِ 'absorber.visit(page)' للصفحة المحددة التي تريدها.
1. احصل على أول 'page_markup' من 'absorber.page_markups'.
1. لكل قسم في ذلك التخطيط:
- استرجع 'rectangle' الخاص به.
1. لكل فقرة في القسم:
- احصل على 'points' (المضلع).
- استخرج النص بتكرار 'paragraph.lines' - 'fragment.text'.
1. احفظ معلومات الهندسة والنص إلى ملف المخرجات.
1. أغلق المستند.

```python

import os
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
        with open(outfile, "w", encoding="utf‑8") as tw:
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

