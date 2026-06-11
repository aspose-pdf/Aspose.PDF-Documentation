---
title: احصل على مظهر ميداني
linktitle: احصل على مظهر ميداني
type: docs
weight: 20
url: /ar/python-net/get-field-appearance/
description: تشرح هذه المقالة كيفية فتح PDF والوصول إلى حقل النموذج واسترداد إعدادات المظهر الخاصة به وعرضها. يوضح المثال استرداد مظهر الحقل المسمى «الاسم الأخير».
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرجع مظهر حقل نموذج PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية استرداد خصائص المظهر المرئي لحقل النموذج في مستند PDF باستخدام Aspose.PDF لـ Python. يفتح الكود ملف PDF موجود، ويصل إلى حقل نموذج معين، ويطبع تفاصيل مظهره، بما في ذلك لون الخلفية ولون النص ولون الحدود والمحاذاة.
---

تحتوي حقول النموذج في مستندات PDF على خصائص مرئية مثل لون الخلفية ولون النص ولون الحدود والمحاذاة. باستخدام Aspose.PDF لـ Python، يمكن للمطورين فحص إعدادات المظهر هذه برمجيًا باستخدام [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) فئة.

1. افتح مستند PDF موجود.
1. قم بإنشاء كائن ForMeditor.
1. استرجع معلومات المظهر لحقل معين.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))
```
