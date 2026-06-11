---
title: إعادة تسمية حقول النموذج
linktitle: إعادة تسمية حقول النموذج
type: docs
weight: 30
url: /ar/python-net/rename-form-fields/
description: يوضح هذا المثال كيفية إعادة تسمية حقول النموذج في مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط نموذج PDF وتحديث أسماء الحقول الموجودة برمجيًا وحفظ الملف المعدل. تساعد إعادة تسمية الحقول على توحيد هياكل النماذج وتحسين تخطيط البيانات وتبسيط التكامل مع عمليات سير العمل التلقائية أو الأنظمة الخارجية.
lastmod: "2026-06-11"
---

تعد إعادة تسمية حقول النموذج مفيدة عند محاذاة نماذج PDF مع اصطلاحات التسمية الداخلية أو إعداد المستندات لمعالجة البيانات المنظمة. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يتم استخدام الوحدة لربط ملف PDF المصدر وتطبيق رسم خرائط يستبدل أسماء الحقول القديمة بأسماء جديدة. بعد تحديث معرفات الحقول، يتم حفظ المستند بالتغييرات المطبقة.

1. قم بتهيئة PDF_facades.form () للتفاعل مع حقول نموذج PDF.
1. اتصل بـ «bind_pdf ()» لإرفاق مستند PDF.
1. قم بإنشاء قائمة من المجموعات التي تحتوي على أسماء الحقول القديمة والأسماء الجديدة المقابلة لها.
1. قم بالتكرار من خلال التعيين واستدعاء 'rename_field () 'لكل إدخال.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
