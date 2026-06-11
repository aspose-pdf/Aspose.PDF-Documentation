---
title: العمل مع مشغلي PDF في بايثون
linktitle: العمل مع المشغلين
type: docs
weight: 90
url: /ar/python-net/working-with-operators/
description: تعرف على كيفية استخدام مشغلات PDF منخفضة المستوى في Python لمعالجة تدفق المحتوى بدقة والتحكم في الرسومات.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخدم مشغلات PDF منخفضة المستوى للتحكم في تدفق المحتوى في Python
Abstract: تشرح هذه المقالة كيفية العمل مع مشغلات PDF منخفضة المستوى في Aspose.PDF لـ Python عبر .NET. تعرف على كيفية التعامل مع تدفقات المحتوى مباشرة، ووضع الرسومات بدقة مع فئات المشغل، وإزالة الكائنات المرسومة من صفحات PDF في عمليات سير عمل Python.
---

## مقدمة لمشغلات PDF واستخداماتها

عامل التشغيل هو كلمة PDF تحدد بعض الإجراءات التي يجب تنفيذها، مثل رسم شكل رسومي على الصفحة. يتم تمييز الكلمة الأساسية للمشغل عن الكائن المسمى بغياب حرف صلب أولي (2Fh). تكون عوامل التشغيل ذات مغزى فقط داخل دفق المحتوى.

دفق المحتوى هو كائن دفق PDF تتكون بياناته من تعليمات تصف العناصر الرسومية التي سيتم رسمها على الصفحة. يمكن العثور على مزيد من التفاصيل حول مشغلات PDF في [مواصفات PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

استخدم هذه الصفحة عندما تحتاج إلى تحكم مباشر في تدفقات محتوى PDF في Python، مثل وضع الرسومات في الإحداثيات الدقيقة، أو تغليف تغييرات حالة الرسومات، أو إزالة عوامل رسم محددة من الصفحة.

## إضافة صور مع فئات المشغل

استخدم فئات المشغل ذات المستوى المنخفض عندما تحتاج إلى وضع محتوى الصورة بدقة شديدة في دفق صفحات PDF دون الاعتماد على تجريدات التخطيط ذات المستوى الأعلى.

توفر هذه الطريقة تحكمًا دقيقًا في موضع الصورة داخل PDF من خلال معالجة تدفق المحتوى مباشرةً باستخدام مشغلات الرسومات منخفضة المستوى. وهي مفيدة بشكل خاص عند الحاجة إلى تحديد المواقع بدقة وتحويل الصور، مثل:

- إضافة علامات مائية أو شعارات في مواقع محددة.
- تراكب الصور على المحتوى الحالي بمحاذاة دقيقة.
- تنفيذ تخطيطات مخصصة لا يمكن تحقيقها باستخدام التجريدات ذات المستوى الأعلى.

باستخدام عوامل تشغيل مثل gSave و ConcateMatrix و Do و GreStore، يمكن للمطورين ضمان عرض الصور بدقة وبدون آثار جانبية غير مقصودة على محتوى الصفحة الأخرى.

- ال [GSAVE](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) يقوم المشغل بحفظ الحالة الرسومية الحالية لملف PDF.
- ال [مصفوفة متسلسلة](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) يتم استخدام عامل التشغيل (مصفوفة متسلسلة) لتحديد كيفية وضع الصورة على صفحة PDF.
- ال [فعل](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) عامل التشغيل يرسم الصورة على الصفحة.
- ال [متجر GRESTORE](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) يستعيد المشغل الحالة الرسومية.

لإضافة صورة إلى ملف PDF:

1. افتح مستند PDF
1. تحديد إحداثيات موضع الصورة
1. الوصول إلى الصفحة المستهدفة
1. قم بتحميل الصورة إلى البث
1. احفظ حالة الرسومات الحالية
1. قم بإنشاء مستطيل ومصفوفة تحويل
1. قم بتطبيق مصفوفة التحويل
1. ارسم الصورة
1. استعادة حالة الرسومات السابقة
1. احفظ مستند PDF المعدل

يوضح مقتطف الشفرة التالي كيفية استخدام عوامل تشغيل PDF:

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## ارسم XForm على الصفحة باستخدام عوامل التشغيل

استخدم هذا المثال قوة XForms ومشغلي الرسومات لإعادة استخدام المحتوى الرسومي بكفاءة داخل PDF. من خلال تغليف الصورة في XForm، يمكن رسمها عدة مرات دون تكرار بيانات الصورة، مما يؤدي إلى أحجام ملفات أصغر وأداء محسن. هذا النهج مفيد بشكل خاص عندما:

- يجب أن تظهر نفس الصورة أو الرسم عدة مرات في المستند.

- مطلوب تحكم دقيق في وضع الرسومات وتحويلها.

- يعد تحسين ملف PDF للأداء والحجم أولوية.

من خلال إدارة حالة الرسومات باستخدام gSave و GreStore، واستخدام مصفوفات التحويل مع ConcateMatrix، تضمن هذه التقنية تقديم كل رسم بشكل صحيح ومستقل.

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## إزالة كائنات الرسومات باستخدام فئات المشغل

يوضح مقتطف الشفرة التالي كيفية إزالة الرسومات. يرجى ملاحظة أنه إذا كان ملف PDF يحتوي على تسميات نصية للرسومات، فقد تظل موجودة في ملف PDF، باستخدام هذا الأسلوب. لذلك ابحث في مشغلي الرسوم عن طريقة بديلة لحذف هذه الصور.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## موضوعات ذات صلة

- [عمليات PDF المتقدمة في بايثون](/pdf/ar/python-net/advanced-operations/)
- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [العمل مع الصور في PDF باستخدام Python](/pdf/ar/python-net/working-with-images/)
- [العمل مع الرسوم البيانية PDF في بايثون](/pdf/ar/python-net/working-with-graphs/)
