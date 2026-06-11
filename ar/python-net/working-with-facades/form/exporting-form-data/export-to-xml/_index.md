---
title: تصدير إلى XML
linktitle: تصدير إلى XML
type: docs
weight: 40
url: /ar/python-net/export-to-xml/
description: يوضح هذا المثال كيفية تصدير بيانات نموذج PDF إلى ملف XML باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية تحميل مستند PDF، والوصول إلى حقول النموذج الخاصة به من خلال واجهة النموذج، وحفظ البيانات المستخرجة كملف XML منظم باستخدام Form Class.
lastmod: "2026-06-11"
---

يسمح تصدير بيانات النموذج للمطورين بإعادة استخدام المعلومات المخزنة في PDF AcroForms دون نسخ قيم الحقول يدويًا. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) يتم إنشاء الكائن من aspose.pdf. في وحدة الواجهات، يكون ملف PDF المصدر مرتبطًا به، وتتم كتابة بيانات النموذج إلى دفق XML.

1. قم بإنشاء كائن نموذج. قم بتهيئة PDF_facades.form () للوصول إلى حقول النموذج وإدارتها.
1. استخدم 'bind_pdf () 'لإرفاق مستند PDF المصدر بمثيل النموذج.
1. قم بإنشاء دفق ملف قابل للكتابة باستخدام 'FileIO () '.
1. اتصل بـ «export_xml ()» لاستخراج جميع قيم حقول النموذج وكتابتها في ملف XML.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```
