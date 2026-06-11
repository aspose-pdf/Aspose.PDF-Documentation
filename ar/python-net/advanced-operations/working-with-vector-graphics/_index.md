---
title: العمل مع الرسومات المتجهة في بايثون
linktitle: العمل مع الرسومات المتجهة
type: docs
weight: 100
url: /ar/python-net/working-with-vector-graphics/
description: تعرف على كيفية استخراج الرسومات المتجهة ونقلها وإزالتها ونسخها بين صفحات PDF باستخدام GraphicsAbsorber في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخدم GraphicsAbsorber لفحص الرسومات المتجهة لـ PDF ومعالجتها في Python
Abstract: تشرح هذه المقالة كيفية العمل مع الرسومات المتجهة في Aspose.PDF لـ Python عبر .NET باستخدام فئة GraphicsAbsorber. تعرف على كيفية استخراج العناصر المتجهة من صفحات PDF، ونقلها أو إزالتها، ونسخ الرسومات بين الصفحات ذات التحكم المنخفض المستوى في عمليات سير عمل Python.
---

[Aspose.PDF لبيثون عبر .NET](/pdf/ar/python-net/) يوفر [ممتص الرسومات](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) فئة للوصول إلى الرسومات المتجهة الموجودة بالفعل في صفحة PDF ومعالجتها. اتصل بها `visit` طريقة على أي صفحة لاستخراج المسارات والأشكال والعوامل الرسومية الأخرى، ثم نقل هذه العناصر أو إزالتها أو نسخها حسب الحاجة.

استخدم هذه الصفحة عندما تحتاج إلى فحص أو تعديل عناصر الرسم المتجه المضمنة في PDF موجود، بدلاً من رسم أشكال جديدة من البداية.

## استخراج الرسومات

الاستخراج هو نقطة البداية لجميع مهام الرسومات المتجهة. `GraphicsAbsorber` يقرأ تدفق محتوى الصفحة ويعرض كل عنصر رسومي بمرجع الصفحة والموضع وعوامل التشغيل الأولية.

1. افتح وثيقة PDF.
1. قم بإنشاء [ممتص الرسومات](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) مثال.
1. اتصل `visit` على الصفحة المستهدفة للتعبئة `elements`.
1. قم بتكرار الغطاء `elements` لفحص الموقع وعدد المشغلين.

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` هو جزء من `aspose.pdf.vector` مساحة الاسم وهي مصممة خصيصًا للتفاعل مع الرسومات المتجهة في تدفقات محتوى PDF.

## رسومات متحركة

بعد الاستخراج، قم بتعيين جديد `position` على كل عنصر لنقله على نفس الصفحة. قم بتغليف التحديثات في `suppress_update` / `resume_update` يتم إجراء المكالمات إلى تدفق المحتوى دفعة واحدة في عملية واحدة وتجنب عمليات إعادة الطلاء الزائدة عن الحاجة.

1. افتح وثيقة PDF.
1. قم بإنشاء `GraphicsAbsorber` واتصل `visit` على الصفحة المستهدفة.
1. اتصل `suppress_update` لإيقاف عمليات الكتابة في بث المحتوى مؤقتًا.
1. قم بتحديث `position` لكل عنصر.
1. اتصل `resume_update` لتنفيذ جميع التغييرات مرة واحدة.
1. احفظ المستند المعدل.

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## إزالة الرسومات

لحذف عناصر متجهة محددة من صفحة، قم بالتصفية حسب الموضع أو المستطيل المحيط ثم قم بإزالتها. يوفر Aspose.PDF for Python طريقتين اعتمادًا على ما إذا كنت تريد إزالة العناصر المضمنة أو جمعها أولاً.

### الطريقة الأولى: إزالة المضمن باستخدام حدود المستطيل

يتحقق هذا الأسلوب من موضع كل عنصر مقابل المستطيل ويستدعي `element.remove()` مباشرة داخل الحلقة. استخدمه عندما تريد رمزًا موجزًا ولا تحتاج إلى فحص المجموعة التي تمت إزالتها بعد ذلك.

1. افتح وثيقة PDF.
1. قم بإنشاء `GraphicsAbsorber` واتصل `visit` على الصفحة المستهدفة.
1. حدد الهدف [المستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. اتصل `suppress_update` لإيقاف عمليات الكتابة في بث المحتوى مؤقتًا.
1. كرر `elements`، الاتصال `remove()` على كل عنصر يقع موضعه داخل المستطيل.
1. اتصل `resume_update` لارتكاب عمليات الحذف.
1. احفظ المستند المعدل.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### الطريقة 2: جمع العناصر أولاً، ثم حذفها

يجمع هذا الأسلوب العناصر المطابقة في [مجموعة العناصر الرسومية](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) وتمرر المجموعة إلى `page.delete_graphics`. استخدمه عندما تحتاج إلى مراجعة أو تسجيل ما ستتم إزالته قبل تنفيذ الحذف.

1. افتح وثيقة PDF.
1. قم بإنشاء `GraphicsAbsorber` واتصل `visit` على الصفحة المستهدفة.
1. حدد المستطيل المستهدف.
1. كرر `elements` وأضف عناصر مطابقة إلى `GraphicElementCollection`.
1. اتصل `page.contents.suppress_update` لإيقاف عمليات الكتابة في بث المحتوى مؤقتًا.
1. اتصل `page.delete_graphics` مع المجموعة.
1. اتصل `page.contents.resume_update` لارتكاب عمليات الحذف.
1. احفظ المستند المعدل.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## إضافة رسومات إلى صفحة أخرى

يمكن وضع العناصر المتجهة المستخرجة من صفحة واحدة على أي صفحة أخرى في نفس المستند. تتوفر طريقتان: إضافة عناصر واحدة تلو الأخرى، أو تمرير المجموعة بأكملها في مكالمة واحدة.

### الطريقة الأولى: إضافة عناصر بشكل فردي

استخدم هذه الطريقة عندما تحتاج إلى التحكم في كل عنصر، مثل تصفية العناصر الفردية أو تحويلها قبل وضعها على صفحة الوجهة.

1. افتح وثيقة PDF.
1. قم بإنشاء `GraphicsAbsorber` واتصل `visit` على صفحة المصدر.
1. أضف صفحة وجهة جديدة إلى المستند.
1. اتصل `page_2.contents.suppress_update` لإيقاف عمليات الكتابة في بث المحتوى مؤقتًا.
1. اتصل `element.add_on_page(page_2)` لكل عنصر.
1. اتصل `page_2.contents.resume_update` لارتكاب جميع الإضافات.
1. احفظ المستند المعدل.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### الطريقة 2: إضافة المجموعة بأكملها مرة واحدة

استخدم هذه الطريقة عندما تريد نسخ جميع العناصر المستخرجة إلى صفحة في عملية واحدة دون التكرار يدويًا.

1. افتح وثيقة PDF.
1. قم بإنشاء `GraphicsAbsorber` واتصل `visit` على صفحة المصدر.
1. أضف صفحة وجهة جديدة إلى المستند.
1. اتصل `page_2.contents.suppress_update` لإيقاف عمليات الكتابة في بث المحتوى مؤقتًا.
1. اتصل `page_2.add_graphics` مع الكامل `elements` مجموعة.
1. اتصل `page_2.contents.resume_update` لارتكاب جميع الإضافات.
1. احفظ المستند المعدل.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## موضوعات ذات صلة

- [عمليات PDF المتقدمة في بايثون](/pdf/ar/python-net/advanced-operations/)
- [العمل مع الرسوم البيانية PDF في بايثون](/pdf/ar/python-net/working-with-graphs/)
- [العمل مع مشغلي PDF في بايثون](/pdf/ar/python-net/working-with-operators/)
- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
