---
title: استخراج بيانات المتجهات من ملف PDF باستخدام بايثون
linktitle: استخراج بيانات المتجهات من PDF
type: docs
weight: 80
url: /ar/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF يجعل من السهل استخراج بيانات المتجهات من ملف PDF. يمكنك الحصول على بيانات المتجهات (المسار، المضلع، الخط المتعدد النقاط)، مثل الموقع، اللون، عرض الخط، إلخ.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## الوصول إلى بيانات المتجهات من مستند PDF

القطعة البرمجية التالية تستخدم فئة GraphicsAbsorber لتوضح كيفية استخراج عناصر الرسومات المتجهية من صفحة محددة في مستند PDF وفحص الخصائص مثل حدود المستطيل، المشغلات، والمواضع.

1. تحميل مستند PDF باستخدام 'ap.Document'.
1. تهيئة كائن 'GraphicsAbsorber'.
1. استدعاء 'gr_absorber.visit()' لفحص الصفحة الثانية.
1. استرجاع العناصر المستخرجة عبر 'gr_absorber.elements'.
1. تكرار عبر كل عنصر وتسجيل الخصائص - المستطيل، الموضع، وعدد المشغلات.
1. كتابة المعلومات إلى ملف نصي.
1. إغلاق المستند لتحرير الموارد.

```python

import os
import aspose.pdf as ap

def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)
    try:
        gr_absorber = ap.vector.GraphicsAbsorber()
        # Visit page 1 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])
        
        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n")
    finally:
        document.close()
```

## حفظ الرسومات المتجهية من صفحة إلى ملف SVG

تصدير الرسومات المتجهية من صفحة PDF إلى ملف SVG، مع الحفاظ على الأشكال والمسارات المتجهية:

1. تحميل مستند PDF.
1. الوصول إلى الصفحة المستهدفة().
1. استدعاء 'page.try_save_vector_graphics()' الذي يصدر مسارات المتجهات للصفحة إلى ملف SVG.
1. إغلاق المستند.

```python

import os
import aspose.pdf as ap

def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        # Try to save vector graphics into SVG
        page.try_save_vector_graphics(svg_outfile)
    finally:
        document.close()
```

### استخراج كل مسار فرعي إلى ملف SVG منفصل

استخراج كل مسار فرعي (مكوّن) من الرسومات المتجهية إلى ملفات SVG منفصلة باستخدام كائن خيارات الاستخراج.

1. تحميل ملف PDF.
1. إنشاء 'SvgExtractionOptions' وتعيين 'extract_every_subpath_to_svg'.
1. الوصول إلى الصفحة الأولى من المستند.
1. إنشاء مثيل 'SvgExtractor' باستخدام الخيارات.
1. استدعاء 'extractor.extract()' لإنتاج ملفات SVG منفصلة لكل مسار فرعي متجه.
1. إغلاق المستند.

```python

import os
import aspose.pdf as ap

def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    try:
        options = ap.vector.SvgExtractionOptions()
        options.extract_every_subpath_to_svg = True
        
        page = document.pages[1]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### استخراج قائمة العناصر إلى صورة واحدة

استخراج عناصر متجهية متعددة من صفحة PDF وحفظها كصورة SVG موحدة باستخدام Aspose.PDF للبايثون.
هذا مفيد عندما تريد الحفاظ على الهيكل البصري للأشكال أو الرسومات المجمعة، مثل المخططات أو تصديرات CAD.

1. فتح ملف PDF باستخدام 'Document'.
1. اختيار صفحة وإعداد قائمة بالعناصر المتجهية.
1. استخدام 'SvgExtractor' لدمج تلك العناصر في ملف SVG واحد.
1. حفظ ملف الإخراج.

```python

import os
import aspose.pdf as ap

def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        svg_extractor = ap.vector.SvgExtractor()
        elements = []  # Fill this list with specific graphic elements as needed
        svg_extractor.extract(elements, page, outfile)
    finally:
        document.close()
```

### استخراج عنصر واحد

استخراج عنصر متجهي محدد من ملف PDF وحفظه كملف SVG منفرد.
هذا مفيد لعزل وتصدير الشعارات، الأيقونات، أو الأشكال المنفردة من ملفات PDF المعتمدة على المتجهات المعقدة.

1. إنشاء 'GraphicsAbsorber' لالتقاط بيانات المتجهات.
1. زيارة صفحة محددة لجمع عناصر المتجهات الخاصة بها.
1. اختيار عنصر الهدف (مثال: 'XFormPlacement').
1. حفظ هذا العنصر الواحد إلى ملف SVG.

```python

import os
import aspose.pdf as ap

def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        graphics_absorber = ap.vector.GraphicsAbsorber()
        page = document.pages[1]
        graphics_absorber.visit(page)
        xform_placement = graphics_absorber.elements[1]
        if isinstance(xform_placement, ap.vector.XFormPlacement):
            xform_placement.elements[2].save_to_svg(outfile)
    finally:
        document.close()
```
