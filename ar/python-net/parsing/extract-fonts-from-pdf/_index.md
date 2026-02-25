---
title: استخراج الخطوط من PDF باستخدام بايثون
linktitle: استخراج الخطوط من PDF
type: docs
weight: 30
url: /ar/python-net/extract-fonts-from-pdf/
description: استخدم مكتبة Aspose.PDF لبايثون لاستخراج جميع الخطوط المدمجة من مستند PDF الخاص بك.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الخطوط من PDF باستخدام بايثون
Abstract: يقدم هذا المقال إرشادات حول استخراج جميع الخطوط من مستند PDF باستخدام طريقة محددة من مكتبة Aspose.PDF. يُعرِّف الطريقة `font_utilities.get_all_fonts()` المتاحة في الفئة `Document`، والتي تُسهِّل استرجاع معلومات الخط. يتضمن المقال مقطع كود بايثون يوضح العملية، والذي يشمل استيراد الوحدات اللازمة، فتح مستند PDF، والتكرار عبر الخطوط لطباعة اسم كل خط. هذا النهج مفيد للمطورين الذين يحتاجون إلى تحليل أو تعديل بيانات الخط داخل ملفات PDF.
---

في حال رغبتك في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام طريقة 'font_utilities.get_all_fonts()' المتوفرة في فئة Document. يرجى مراجعة مقطع الكود التالي للحصول على جميع الخطوط من مستند PDF موجود:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

