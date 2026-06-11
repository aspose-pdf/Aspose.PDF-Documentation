---
title: نسخ الحقل الداخلي
linktitle: نسخ الحقل الداخلي
type: docs
weight: 20
url: /ar/python-net/copy-inner-field/
description: انسخ حقول نموذج PDF إلى موضع جديد باستخدام Python باستخدام Aspose.PDF لبيثون.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: انسخ حقول نموذج PDF إلى موضع جديد باستخدام Python
Abstract: يوضح هذا المثال كيفية نسخ حقل نموذج موجود إلى موضع جديد في مستند PDF باستخدام Aspose.PDF لـ Python. يفتح الكود ملف PDF، ويكرر الحقل إلى صفحة محددة ويقوم بالإحداثيات، ويحفظ المستند المحدث.
---

غالبًا ما تتطلب نماذج PDF تكرار الحقول مع الحفاظ على التنسيق والسلوك الأصليين. باستخدام Aspose.PDF لـ Python، يمكن للمطورين نسخ حقل موجود إلى موضع جديد على نفس الصفحة أو صفحة أخرى برمجيًا.

تشرح هذه المقالة كيفية نسخ حقل باسم «الاسم الأول» إلى حقل جديد يسمى «نسخ الاسم الأول» في الصفحة 2 بإحداثيات محددة (x=200، y=600)، وإنتاج ملف PDF مع الحقل الذي تم وضعه حديثًا.

1. افتح نموذج PDF موجود.
1. قم بإنشاء كائن ForMeditor.
1. قم بربط وثيقة PDF إلى ForMeditor.
1. انسخ حقل «الاسم الأول» إلى حقل جديد «نسخ الاسم الأول» في الصفحة 2 عند الإحداثيات (200، 600).
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**يرجى ملاحظة ما يلي: **

يبدو توقيع الأسلوب «copy_inner_field» كما يلي:

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' - الحقل الذي تريد تكراره.
- 'new_field_name' — اسم الحقل الجديد.
- 'page_number' - الصفحة التي سيظهر عليها الحقل الجديد.
- x، y - الإحداثيات على تلك الصفحة.

من المتوقع أن يكون page_number عددًا صحيحًا موجبًا يتوافق مع صفحة موجودة في PDF (الفهرسة المستندة إلى 1).

إذا قمت بتمرير معامل سلبي، على سبيل المثال:

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

سيتم إعادة تعيين البرنامج بعد ذلك إلى المعلمات السابقة.
