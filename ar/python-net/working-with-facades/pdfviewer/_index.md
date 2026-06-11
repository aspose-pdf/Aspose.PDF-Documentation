---
title: فئة عارض ملفات PDF
linktitle: فئة عارض ملفات PDF
type: docs
weight: 135
url: /ar/python-net/pdfviewer-class/
description: تعرف على كيفية استخدام فئة PDFViewer في Aspose.PDF لـ Python عبر .NET لفك تشفير جميع صفحات PDF وفك شفرة صفحة معينة وفحص بيانات PDF الوصفية المتعلقة بالعارض.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بفك تشفير صفحات PDF وفحص بيانات المشاهد في Python باستخدام PDFViewer
Abstract: توضح هذه المقالة كيفية استخدام واجهة PDFViewer في Aspose.PDF لـ Python عبر .NET لفك تشفير الصفحة ومهام الفحص المتعلقة بالعارض. تعرف على كيفية فك تشفير جميع صفحات PDF، وعرض صفحة معينة، وفحص الخصائص مثل عدد الصفحات ونوع الإحداثيات والدقة.
---

يوفر Aspose.PDF لبيثون عبر .NET [عارض ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) واجهة للعمل مع سيناريوهات عرض PDF وفك تشفير الصفحة. إحدى حالات الاستخدام الشائعة هي تحويل صفحات PDF إلى كائنات صور يمكن حفظها بعد ذلك على القرص.

## قم بإنشاء مساعد PDFViewer قابل لإعادة الاستخدام

قبل فك تشفير الصفحات أو قراءة الخصائص المتعلقة بالمشاهد، قم بإنشاء مساعد صغير يقوم بتهيئة ملف `PdfViewer` مثال. هذا يحافظ على الأمثلة أدناه قائمة بذاتها ويوضح كيفية إنشاء كائن المشاهد قبل ربطه بمستند PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades


def _create_viewer() -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured for decoding examples."""
    viewer = pdf_facades.PdfViewer()
    viewer.coordinate_type = ap.PageCoordinateType.MEDIA_BOX
    viewer.resolution = 150
    viewer.scale_factor = 1.0
    viewer.show_hidden_areas = False
    return viewer
```

## فك شفرة جميع صفحات PDF

استخدم `decode_all_pages()` عندما تريد تحويل كل صفحة في PDF إلى صورة منفصلة. يمكن بعد ذلك حفظ صور الصفحة التي تم إرجاعها واحدة تلو الأخرى في دليل الإخراج.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close_pdf_file()
```

## فك شفرة صفحة PDF محددة

استخدم `decode_page()` عندما تحتاج إلى صفحة واحدة فقط من المستند. يكون هذا مفيدًا عند إنشاء معاينات أو صور مصغرة أو عمليات تصدير خاصة بالصفحة.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)

    finally:
        viewer.close()
```

## افحص بيانات PDF الوصفية

ال `inspect_pdf_metadata` توضح الوظيفة كيفية فتح مستند PDF واسترداد البيانات الوصفية الأساسية المتعلقة بالعارض باستخدام Aspose.PDF. وهي تركز على استخراج المعلومات التي تصف كيفية تفسير المستند وعرضه بدلاً من محتواه.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def inspect_pdf_metadata(infile: str) -> None:
    """Open a PDF and print page-count related viewer metadata."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        print(f"Page count: {viewer.page_count}")
        print(f"Coordinate type: {viewer.coordinate_type}")
        print(f"Resolution: {viewer.resolution}")
    finally:
        viewer.close_pdf_file()
```
