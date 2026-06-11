---
title: تحقق من حدود الشكل في رسوم PDF باستخدام Python
linktitle: تحقق من حدود الشكل
type: docs
weight: 70
url: /ar/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: تعرف على كيفية التحقق من حدود الشكل في مجموعات رسومات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحقق من حدود شكل الرسم البياني في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية التحقق من حدود الشكل في مجموعات الرسم البياني باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي تكوين BoundScheckMode واكتشاف الأشكال خارج النطاق والتعامل مع استثناءات الحدود بأمان.
---

## تحقق من حدود الشكل في الرسم البياني

عند إضافة أشكال إلى [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)، يمكنك تمكين التحقق من الحدود للتأكد من أن كل شكل يناسب منطقة الرسم البياني.

استخدم [وضع التحقق من الحدود](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) لتحديد السلوك عندما يكون الشكل خارج النطاق. في هذا المثال، `THROW_EXCEPTION_IF_DOES_NOT_FIT` يتم استخدامه لرفع استثناء.

اتبع الخطوات أدناه:

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إضافة [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. قم بإنشاء [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. قم بإنشاء [المستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) يمتد خارج حدود الرسم البياني.
1. قم بتعيين وضع فحص الحدود إلى `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. أضف المستطيل وعالج الاستثناء.
1. احفظ المستند.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## ملاحظات

- استخدم `THROW_EXCEPTION_IF_DOES_NOT_FIT` عندما يكون التحقق الصارم من التخطيط مطلوبًا.
- بالنسبة للسلوك المتساهل، اختر سلوكًا آخر `BoundsCheckMode` خيار يعتمد على احتياجات التخطيط الخاصة بك.

## موضوعات الرسم البياني ذات الصلة

- [العمل مع الرسوم البيانية PDF في بايثون](/pdf/ar/python-net/working-with-graphs/)
- [إضافة أشكال مستطيلة إلى PDF في Python](/pdf/ar/python-net/add-rectangle/)
- [أضف أشكال الخطوط إلى PDF في Python](/pdf/ar/python-net/add-line/)
- [أضف الأشكال البيضاوية إلى PDF في Python](/pdf/ar/python-net/add-ellipse/)
