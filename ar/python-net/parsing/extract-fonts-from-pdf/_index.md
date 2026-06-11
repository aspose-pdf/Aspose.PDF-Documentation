---
title: استخراج الخطوط من PDF عبر Python
linktitle: استخراج الخطوط من PDF
type: docs
weight: 30
url: /ar/python-net/extract-fonts-from-pdf/
description: استخدم مكتبة Aspose.PDF لـ Python لاستخراج جميع الخطوط المضمنة من مستند PDF الخاص بك.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الخطوط من PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية فحص الخطوط المستخدمة في مستند PDF باستخدام Aspose.PDF لـ Python. يوضح كيفية فتح ملف PDF مع فئة المستند، والاتصال بـ font_utilities.get_all_fonts () لاسترداد كائنات الخط المتاحة، وتكرار النتائج لقراءة أسماء الخطوط للتحليل أو التدقيق أو سير عمل معالجة المستندات.
---

استخدم [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) لفتح ملف PDF والاتصال `font_utilities.get_all_fonts()` لاسترداد كل ما هو متاح [الخط](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) الكائنات المشار إليها في المستند. يكون هذا مفيدًا عند تدقيق الخطوط المضمنة أو التحقق من توفر الخط قبل التحويل أو تحليل موارد المستند.

1. افتح ملف PDF المصدر كملف `Document`.
1. اتصل `document.font_utilities.get_all_fonts()` للحصول على مجموعة الخطوط.
1. قم بالتكرار من خلال ما تم إرجاعه `Font` الكائنات.
1. اقرأ واطبع كل منها `font.font_name` قيمة.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
