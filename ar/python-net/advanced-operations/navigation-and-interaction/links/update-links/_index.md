---
title: تحديث روابط PDF في بايثون
linktitle: روابط التحديث
type: docs
weight: 20
url: /ar/python-net/update-links/
description: تعرف على كيفية تحديث مظهر رابط PDF والوجهات في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحديث الروابط في PDF
Abstract: دليل Aspose.PDF لـ Python عبر .NET حول تحديث الروابط يوجه المطورين خلال عملية تعديل سلوك الارتباط التشعبي داخل مستندات PDF باستخدام Python. يشرح كيفية تغيير وجهات الروابط للإشارة إلى صفحات معينة أو مواقع ويب خارجية أو حتى ملفات PDF أخرى. تغطي الوثائق أيضًا كيفية ضبط مظهر التعليقات التوضيحية للروابط، بما في ذلك لون النص، وتوفر أمثلة التعليمات البرمجية العملية لكل سيناريو. سواء كنت تقوم بتصحيح عناوين URL القديمة أو تحسين التنقل، يقدم هذا المورد نهجًا واضحًا وفعالًا لإدارة الروابط برمجيًا.
---

## تحديث لون نص التعليق على الرابط

يوضح هذا المثال كيفية اكتشاف جميع التعليقات التوضيحية للروابط على الصفحة الأولى من PDF باستخدام Aspose.PDF لـ Python، ثم تمييز النص بالقرب من كل رابط عن طريق تغيير لون الخط إلى اللون الأحمر. يستخدم TextFragmentAbsorber مع منطقة موسعة قليلاً حول كل مستطيل ارتباط للعثور على نص قريب وتعديله.

يمكن استخدام هذا من أجل:

- وضع علامات مرئية على الروابط في المستند
- تعزيز إمكانية الوصول من خلال التأكيد على المحتوى المرتبط
- المعالجة المسبقة لملفات PDF قبل المراجعة أو التصدير

بالنسبة لكل من هذه التعليقات التوضيحية للروابط، يسترجع النص البرمجي حدوده المستطيلة ويوسع تلك المنطقة قليلاً لتشمل نصًا قريبًا، مما يسمح بتحديد مرئي أوسع. ثم يقوم بتطبيق TextFragmentAbsorber على هذه المنطقة الموسعة لاستخراج أي أجزاء نصية موجودة داخلها. يتم تعديل هذه الأجزاء الملتقطة عن طريق تغيير لون الخط إلى اللون الأحمر، ووضع علامة فعالة على النص المحيط للتأكيد والمراجعة. بعد تطبيق كل هذه التحديثات، يتم حفظ المستند المعدل في مسار الإخراج، مع الحفاظ على التعليقات التوضيحية المميزة والنص المرتبط بها.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## تحديث الحدود

يركز البرنامج النصي على الصفحة الأولى من المستند ويقوم بتصفية جميع التعليقات التوضيحية، مع تحديد التعليقات التوضيحية فقط من نوع LINK - وهي عادةً ما تمثل عناصر تفاعلية، مثل الارتباطات التشعبية أو مشغلات التنقل. بالنسبة لكل من هذه التعليقات التوضيحية للروابط، ترسلها الشفرة إلى نوع LinkAnNotation وتقوم بتحديث خاصية اللون الخاصة بها إلى اللون الأحمر، مع إبرازها بصريًا لتبرز عن المحتوى الآخر. بعد تعديل جميع التعليقات التوضيحية للروابط، يتم حفظ المستند المحدث في موقع الإخراج المحدد، مع الحفاظ على النمط الجديد.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## تحديث وجهة الويب

بمجرد وضع المسارات، يتم تحميل المستند الأصلي باستخدام مكتبة Aspose.PDF، مما يجعل محتواه متاحًا للتعديل. ثم يركز البرنامج النصي على الصفحة الأولى من المستند، ويقوم بتصفية جميع التعليقات التوضيحية وتحديد تلك التي من نوع الارتباط فقط، والتي تمثل عادةً مناطق قابلة للنقر أو ارتباطات تشعبية. لتجنب أخطاء الكتابة وضمان المعالجة الآمنة، يتم فحص كل تعليق توضيحي باستخدام is_assignable ثم إرساله إلى نوع LinkAnNotation المناسب. إذا كان الرابط مرتبطًا بـ GoTouriAction، مما يعني أنه يشير إلى عنوان ويب، فإن البرنامج النصي يقوم بتحديث عنوان URI هذا لإعادة توجيه المستخدمين إلى»https://www.aspose.com". أخيرًا، بعد تطبيق جميع التغييرات المطلوبة، يتم حفظ المستند المعدل في مسار الإخراج المحدد.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## موضوعات الارتباط ذات الصلة

- [العمل مع روابط PDF في بايثون](/pdf/ar/python-net/links/)
- [إنشاء روابط PDF في بايثون](/pdf/ar/python-net/create-links/)
- [استخراج روابط PDF في بايثون](/pdf/ar/python-net/extract-links/)