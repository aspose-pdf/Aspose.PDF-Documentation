---
title: تدوير صفحات PDF في بايثون
linktitle: تدوير صفحات PDF
type: docs
weight: 110
url: /ar/python-net/rotate-pages/
description: تعرف على كيفية تدوير صفحات PDF وتغيير اتجاه الصفحة في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تدوير الصفحات في PDF باستخدام Python
Abstract: توفر هذه المقالة دليلًا حول كيفية تحديث أو تغيير اتجاه صفحة الصفحات برمجيًا في ملف PDF موجود باستخدام Python. باستخدام Aspose.PDF لـ Python عبر .NET، يمكن للمستخدمين التبديل بسهولة بين الاتجاهات الأفقية والعمودية عن طريق ضبط خصائص MediaBox الخاصة بالصفحة. تتضمن المقالة مقتطفًا من شفرة Python يوضح كيفية التكرار عبر الصفحات في مستند PDF، وتعديل أبعاد ومواضع MediaBox الخاصة بها، وضبط CropBox إذا لزم الأمر. بالإضافة إلى ذلك، يشرح كيفية ضبط زاوية دوران الصفحات باستخدام طريقة «التدوير» لتحقيق الاتجاه المطلوب. تنتهي العملية بحفظ ملف PDF المحدث.
---

يصف هذا الموضوع كيفية تحديث أو تغيير اتجاه الصفحة للصفحات في ملف PDF موجود برمجيًا باستخدام Python.

استخدم هذه الصفحة عندما تحتاج إلى تبديل الصفحات بين الاتجاه الرأسي والأفقي أو تطبيق زوايا التدوير على محتوى PDF الحالي.

## تغيير اتجاه الصفحة

تقوم هذه الوظيفة بتدوير كل صفحة من صفحات PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 درجة في اتجاه عقارب الساعة باستخدام Aspose.PDF لبيثون.
وهي مفيدة لتصحيح مشكلات اتجاه الصفحة، مثل المستندات الممسوحة ضوئيًا والتي تكون جانبية. يظل ملف PDF الأصلي بدون تغيير، ويتم حفظ النسخة التي تم تدويرها كملف جديد.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## موضوعات الصفحة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [تغيير حجم صفحة PDF في Python](/pdf/ar/python-net/change-page-size/)
- [قص صفحات PDF في بايثون](/pdf/ar/python-net/crop-pages/)
- [الحصول على خصائص صفحة PDF وتعيينها في Python](/pdf/ar/python-net/get-and-set-page-properties/)