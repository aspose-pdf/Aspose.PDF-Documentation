---
title: نسخ الحقل الخارجي
linktitle: نسخ الحقل الخارجي
type: docs
weight: 30
url: /ar/python-net/copy-outer-field/
description: يوضح هذا المثال كيفية نسخ حقل نموذج من مستند PDF إلى آخر باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: انسخ حقول نموذج PDF من مستند آخر باستخدام Python
Abstract: توضح هذه المقالة كيفية إنشاء مستند PDF جديد، ونسخ حقل «الاسم الأول» من ملف PDF المصدر إلى الصفحة 1 عند الإحداثيات (200، 600)، وحفظ المستند الهدف المحدث.
---

في بعض الأحيان، تتطلب نماذج PDF إعادة استخدام الحقول من مستند إلى آخر. باستخدام Aspose.PDF لـ Python، يمكن للمطورين نسخ حقول النموذج برمجيًا من PDF المصدر إلى PDF الهدف.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) توفر الفئة طريقة «copy_outer_field»، التي تنسخ حقلاً من مستند مصدر إلى مستند هدف في صفحة وإحداثيات محددة.

يقوم الكود بإنشاء PDF جديد (هدف) وإضافة صفحة ثم نسخ حقل من PDF موجود (المصدر) إلى المستند الهدف بإحداثيات محددة.

1. قم بإنشاء مستند PDF مستهدف جديد.
1. أضف صفحة واحدة على الأقل إلى PDF الهدف.
1. احفظ المستند الهدف الفارغ.
1. قم بإنشاء كائن ForMeditor واربطه بملف PDF الهدف.
1. انسخ حقل «الاسم الأول» من ملف PDF المصدر إلى الصفحة 1 على (200، 600).
1. احفظ ملف PDF الهدف المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**يرجى ملاحظة ما يلي: **

يبدو توقيع الأسلوب «copy_outer_field» كما يلي:

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' - الحقل الذي تريد تكراره.
- 'new_field_name' — اسم الحقل الجديد.
- 'page_number' - الصفحة التي سيظهر عليها الحقل الجديد.
- x، y - الإحداثيات على تلك الصفحة.

من المتوقع أن يكون page_number عددًا صحيحًا موجبًا يتوافق مع صفحة موجودة في PDF (الفهرسة المستندة إلى 1).

إذا قمت بتمرير معامل سلبي، على سبيل المثال:

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

سيتم إعادة تعيين البرنامج بعد ذلك إلى المعلمات السابقة.
