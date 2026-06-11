---
title: استيراد بيانات XML
linktitle: استيراد بيانات XML
type: docs
weight: 40
url: /ar/python-net/import-xml-data/
description: يوضح هذا المثال كيفية استيراد بيانات النموذج من ملف XML إلى حقول نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF، وقراءة بيانات XML المهيكلة من خلال دفق الملفات، وتعبئة حقول النموذج المقابلة تلقائيًا.
lastmod: "2026-06-11"
---

يُستخدم XML بشكل شائع لتخزين بيانات النموذج المنظم، مما يجعله تنسيقًا عمليًا لنقل القيم بين الأنظمة. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يستخدم لتحميل نموذج PDF وتطبيق قيم الحقول مباشرة من ملف XML. بعد استيراد البيانات، يتم حفظ ملف PDF المحدث كمستند جديد.

1. قم بتهيئة PDF_facades.form () للتفاعل مع حقول نموذج PDF.
1. اتصل بـ «bind_pdf ()» لإرفاق قالب نموذج PDF.
1. استخدم 'FileIO () 'للوصول إلى ملف XML الذي يحتوي على بيانات النموذج.
1. اتصل بـ «import_xml ()» لملء حقول PDF بقيم من ملف XML.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
