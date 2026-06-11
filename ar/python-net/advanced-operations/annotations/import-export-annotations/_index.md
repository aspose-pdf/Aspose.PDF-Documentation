---
title: استيراد التعليقات التوضيحية وتصديرها باستخدام Python
linktitle: استيراد التعليقات التوضيحية وتصديرها
type: docs
weight: 80
url: /ar/python-net/import-export-annotations/
description: تعرف على كيفية استيراد التعليقات التوضيحية من ملف PDF واحد وتصديرها إلى مستند PDF جديد باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: نقل التعليقات التوضيحية لـ PDF بين المستندات في Python.
Abstract: تشرح هذه المقالة كيفية نسخ التعليقات التوضيحية من ملف PDF المصدر وتصديرها إلى مستند PDF جديد باستخدام Aspose.PDF لـ Python عبر .NET. تقسم الإرشادات العملية إلى خطوات صغيرة، بما في ذلك تحميل الملف المصدر وإنشاء مستند الوجهة وإضافة صفحة ونسخ التعليقات التوضيحية من الصفحة الأولى وحفظ النتيجة.
---

توضح هذه المقالة كيفية استيراد التعليقات التوضيحية من ملف PDF موجود وتصديرها إلى مستند PDF جديد باستخدام Aspose.PDF لـ Python عبر .NET.

يقرأ المثال التعليقات التوضيحية من الصفحة الأولى للملف المصدر، وينشئ PDF جديدًا، ويضيف صفحة فارغة، وينسخ كل تعليق توضيحي إلى تلك الصفحة الجديدة. يُعد هذا الأسلوب مفيدًا عندما تحتاج إلى نقل التعليقات أو الترميز أو ملاحظات المراجعة إلى مستند إخراج منفصل.

## قم بتحميل ملف PDF المصدر

قم بإنشاء `Document` كائن لملف الإدخال الذي يحتوي بالفعل على تعليقات توضيحية. يتيح هذا الكائن الوصول إلى مجموعة الصفحات والتعليقات التوضيحية المخزنة في كل صفحة.

```python
source_document = ap.Document(infile)
```

## قم بإنشاء ملف PDF الخاص بالوجهة

بعد ذلك، قم بإنشاء مستند PDF فارغ سيتلقى التعليقات التوضيحية المستوردة. في هذه المرحلة، لا تحتوي وثيقة الوجهة على أية صفحات.

```python
destination_document = ap.Document()
```

## إضافة صفحة للتعليقات التوضيحية المصدرة

ونظرًا لأن التعليقات التوضيحية يجب أن تنتمي إلى صفحة، قم بإضافة صفحة جديدة إلى المستند الوجهة قبل نسخ أي شيء.

```python
page = destination_document.pages.add()
```

## انسخ التعليقات التوضيحية من صفحة المصدر

قم بالتكرار من خلال مجموعة التعليقات التوضيحية على الصفحة الأولى من ملف PDF المصدر وأضف كل تعليق توضيحي إلى الصفحة الجديدة في مستند الوجهة.

الحجة الثانية في `page.annotations.add(annot, True)` يخبر Aspose.PDF بنسخ التعليق التوضيحي إلى صفحة الوجهة بدلاً من إعادة استخدام مرجع الكائن الموجود فقط.

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## احفظ مستند الإخراج

بعد نسخ جميع التعليقات التوضيحية، احفظ مستند الوجهة لإنشاء ملف PDF النهائي.

```python
destination_document.save(outfile)
```

## مثال كامل

تجمع التعليمة البرمجية التالية جميع الخطوات في وظيفة واحدة قابلة لإعادة الاستخدام:

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## موضوعات ذات صلة

- [التعليقات التوضيحية التفاعلية](/python-net/interactive-annotations/)
- [التعليقات التوضيحية للتوصيف](/python-net/markup-annotations/)
- [التعليقات التوضيحية لوسائل الإعلام](/python-net/media-annotations/)
- [التعليقات التوضيحية للأمان](/python-net/security-annotations/)
- [التعليقات التوضيحية للشكل](/python-net/shape-annotations/)
- [التعليقات التوضيحية المستندة إلى النص](/python-net/text-based-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/python-net/watermark-annotations/)
