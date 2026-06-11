---
title: استخراج البيانات المتجهة من ملف PDF باستخدام Python
linktitle: استخراج بيانات المتجهات من PDF
type: docs
weight: 80
url: /ar/python-net/extract-vector-data-from-pdf/
description: يجعل Aspose.PDF من السهل استخراج البيانات المتجهة من ملف PDF. يمكنك الحصول على بيانات المتجه (المسار، المضلع، الخطوط المتعددة)، مثل الموضع واللون وعرض الخط وما إلى ذلك.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الوصول إلى بيانات المتجهات من مستند PDF

استخدم [ممتص الرسومات](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) لفحص عناصر الرسوم المتجهة على صفحة من [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). بعد زيارة الصفحة الهدف، قم بتكرار العناصر المستخرجة لفحص الخصائص مثل حدود المستطيل والمواضع وعوامل الرسم.

1. افتح ملف PDF المصدر كملف `Document`.
1. قم بإنشاء `GraphicsAbsorber` مثال.
1. اتصل `gr_absorber.visit(page)` على الصفحة المستهدفة.
1. اقرأ العناصر المستخرجة من `gr_absorber.elements`.
1. قم بتكرار العناصر واكتب خصائصها إلى ملف الإخراج.

```python
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
        # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])

        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(
                    f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n"
                )
    finally:
        document.close()
```

## حفظ الرسومات المتجهة من صفحة إلى ملف SVG

قم بتصدير الرسومات المتجهة من صفحة PDF إلى SVG للحفاظ على المسارات والأشكال القابلة للتطوير خارج PDF الأصلي. هذه الطريقة مفيدة لإعادة استخدام العمل الفني المتجه في عمليات سير عمل الويب أو التصميم أو النشر.

1. قم بتحميل وثيقة PDF.
1. قم بالوصول إلى الصفحة المستهدفة.
1. اتصل `page.try_save_vector_graphics()` لتصدير المسارات المتجهة للصفحة إلى SVG.
1. أغلق المستند.

```python
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

### استخرج كل مسار فرعي إلى SVG منفصل

عندما تحتوي الصفحة على مسارات متجهية مستقلة متعددة، استخدم [خيارات استخراج SVG](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractionoptions/) مع [مستخرج SVG](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) لكتابة كل مسار فرعي إلى ملف SVG منفصل.

1. قم بتحميل ملف PDF.
1. ابتكر `SvgExtractionOptions` ومجموعة `extract_every_subpath_to_svg`.
1. قم بالوصول إلى الصفحة الأولى من المستند.
1. إنشاء مثيل `SvgExtractor` مع الخيارات.
1. اتصل `extractor.extract()` لكتابة ملفات SVG منفصلة لكل مسار فرعي متجه.
1. أغلق المستند.

```python
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

### استخرج قائمة العناصر إلى صورة واحدة

قم باستخراج عناصر متجهة متعددة من صفحة PDF وحفظها كصورة SVG مدمجة واحدة. يكون هذا مفيدًا عندما تريد الحفاظ على العلاقة المرئية بين الأشكال المجمعة أو الرسوم التخطيطية أو أجزاء الرسم.

1. افتح ملف PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. حدد صفحة وقم بإعداد قائمة بالعناصر المتجهة.
1. استخدم [مستخرج SVG](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) لدمج هذه العناصر في SVG واحد.
1. احفظ ملف الإخراج.

```python
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

قم باستخراج عنصر متجه محدد من PDF وحفظه كملف SVG فردي. يُعد هذا مفيدًا لعزل الشعارات أو الرموز أو الأشكال المستقلة عن الصفحات الأكثر تعقيدًا القائمة على المتجهات.

1. قم بإنشاء [ممتص الرسومات](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) لالتقاط بيانات المتجهات.
1. قم بزيارة صفحة معينة لتجميع عناصر المتجهات الخاصة بها.
1. حدد عنصرًا مستهدفًا، مثل [وضع نموذج X](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/xformplacement/).
1. احفظ هذا العنصر الفردي في ملف SVG.

```python
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
