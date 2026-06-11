---
title: حذف عنصر القائمة
linktitle: حذف عنصر القائمة
type: docs
weight: 40
url: /ar/python-net/del-list-item/
description:
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة العناصر من حقول مربع قائمة PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إزالة عنصر من حقل نموذج مربع القائمة في مستند PDF باستخدام Aspose.PDF لـ Python. يفتح الكود ملف PDF موجود، ويحذف عنصرًا معينًا من حقل مربع القائمة، ويحفظ المستند المحدث.
---

تسمح حقول مربع القائمة في ملفات PDF للمستخدمين بتحديد خيار واحد أو عدة خيارات محددة مسبقًا. باستخدام Aspose.PDF لـ Python، يمكن للمطورين إزالة العناصر من هذه الحقول برمجيًا.

تشرح هذه المقالة كيفية حذف عنصر «المملكة المتحدة» من حقل مربع القائمة المسمى «البلد»، مع التأكد من أن الحقل يحتوي فقط على الخيارات المطلوبة.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) توفر الفئة طريقة «del_list_item» لإزالة عنصر معين من حقل مربع القائمة.

1. افتح نموذج PDF موجود.
1. قم بإنشاء كائن ForMeditor.
1. قم بربط وثيقة PDF إلى ForMeditor.
1. احذف عنصر «المملكة المتحدة» من حقل مربع قائمة «البلد».
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```

