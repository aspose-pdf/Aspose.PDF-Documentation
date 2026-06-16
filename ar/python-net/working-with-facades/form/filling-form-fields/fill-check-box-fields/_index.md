---
title: تعبئة حقول خانة الاختيار
linktitle: تعبئة حقول خانة الاختيار
type: docs
weight: 20
url: /ar/python-net/fill-check-box-fields/
description: يوضح هذا المثال كيفية ملء حقول مربعات الاختيار برمجيًا في نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF وتحديث قيم مربعات الاختيار حسب اسم الحقل وحفظ الملف المعدل.
lastmod: "2026-06-11"
---

يُستخدم مربع الاختيار بشكل شائع في نماذج PDF لتمثيل الخيارات الثنائية مثل الاشتراكات أو تأكيدات الاتفاقية. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يتم استخدامه للوصول إلى حقول النموذج وتعيين قيمها إلى الحالة المحددة. بعد تحديث خانات الاختيار، يتم حفظ ملف PDF المعبأ كمستند جديد.

1. قم بتهيئة 'PDF_facades.form () 'لإدارة تفاعلات حقل النموذج.
1. استخدم 'bind_pdf () 'لإرفاق ملف PDF المصدر الذي يحتوي على حقول مربعات الاختيار.
1. اتصل بـ «fill_field ()» لوضع علامة على حقول مثل «subscribe_newsletter» و «accept_terms» على النحو المحدد.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```
