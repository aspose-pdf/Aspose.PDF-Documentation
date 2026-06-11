---
title: حذف الختم حسب المعرف
linktitle: حذف الختم حسب المعرف
type: docs
weight: 85
url: /ar/python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احذف الطوابع المطاطية بمعرفات مفردة أو متعددة في ملف PDF باستخدام PDFContentEditor
Abstract: يوضح هذا المثال كيفية إزالة التعليقات التوضيحية للختم المطاطي من ملف PDF استنادًا إلى معرفاتها الفريدة باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. ويغطي كلاً من حذف المعرف الفردي وحذف المعرفات المتعددة.
---

عند العمل مع ملفات PDF التي تحتوي على طوابع متعددة، غالبًا ما يكون من الضروري إزالة طوابع معينة دون التأثير على الآخرين. باستخدام الحذف المستند إلى المعرف، يمكنك التحكم بدقة في الطوابع التي تريد إزالتها:

- 'delete_stamp_by_id (stamp_id, page_number) '- يحذف طابعًا واحدًا بمعرفه على صفحة معينة
- 'delete_stamp_by_ids (page_number, stamp_ids) '- تحذف عدة طوابع بواسطة معرفاتها على صفحة معينة

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. أضف ختمين مطاطيين بمعرفات مميزة.
1. احذف الطوابع باستخدام أساليب حذف المعرف الفردي والمعرف المتعدد.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```

