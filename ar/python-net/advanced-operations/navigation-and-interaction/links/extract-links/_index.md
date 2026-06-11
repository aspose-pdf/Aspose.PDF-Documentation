---
title: استخراج روابط PDF في بايثون
linktitle: استخراج الروابط
type: docs
weight: 30
url: /ar/python-net/extract-links/
description: تعرف على كيفية استخراج التعليقات التوضيحية للارتباطات والارتباطات التشعبية من مستندات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الروابط من PDF
Abstract: يشرح دليل Aspose.PDF لـ Python عبر .NET حول استخراج الروابط كيفية استرداد التعليقات التوضيحية للارتباطات التشعبية برمجيًا من مستندات PDF باستخدام Python. تتضمن الوثائق أمثلة التعليمات البرمجية العملية وتسلط الضوء على كيفية استخدام هذه الوظيفة لمهام مثل تدقيق الروابط أو تحليل التنقل أو إنشاء ميزات المستندات التفاعلية. سواء كنت تعمل مع ملفات PDF ذات صفحة واحدة أو تعالج مجموعات كبيرة، يقدم هذا الدليل نهجًا واضحًا وفعالًا لاستخراج الارتباطات التشعبية.
---

## استخراج الروابط من ملف PDF

يوضح هذا المثال كيفية التكرار من خلال جميع التعليقات التوضيحية للروابط على الصفحة الأولى من PDF باستخدام Aspose.PDF لـ Python. يقوم بتصفية التعليقات التوضيحية لتحديد تلك من النوع LinkAnNotation، وينشرها بأمان، ثم يطبع فهرس الصفحة والموضع المستطيل على الصفحة.

يمكن استخدام هذا لتصحيح الأخطاء أو التحليلات أو التحديثات التلقائية للتعليقات التوضيحية للروابط الموجودة في PDF.

1. قم بتحميل وثيقة PDF. استخدم AP.document (path_infile) لفتح الملف.
1. يمكنك الوصول إلى التعليقات التوضيحية من الصفحة الأولى. استخدم document.pages [1] .التعليقات التوضيحية لاسترداد جميع التعليقات التوضيحية.
1. عامل تصفية لأنواع LinkAnNotation فقط. تحقق من نوع التعليق التوضيحي لكل تعليق توضيحي.
1. إرسال ملاحظات الارتباط ومعالجتها. استخدم is_assignable () و cast () لضمان الوصول الآمن إلى خصائص linkAnNotation.
1. طباعة تفاصيل التعليق التوضيحي. قم بإخراج فهرس الصفحة والمستطيل (الموقع) لكل رابط.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## استخراج الارتباطات التشعبية من ملف PDF

يوضح هذا الرمز كيفية استخراج جميع كائنات LinkAnNotation من الصفحة الأولى من مستند PDF باستخدام Aspose.PDF لـ Python، ثم تحديد تلك التي تحتوي على GoTouriAction. بالنسبة لكل رابط من هذا القبيل، فإنه يطبع فهرس الصفحة وURI الهدف.

هذا مفيد لمهام مثل:

- تدقيق الروابط الخارجية في PDF
- استخراج الوثائق أو عناوين URL للدعم
- اكتشاف الارتباطات التشعبية المعطلة أو القديمة

1. قم بتحميل وثيقة PDF. افتح الملف باستخدام AP.Document.
1. احصل على جميع التعليقات التوضيحية للروابط من الصفحة الأولى. قم بتصفية التعليقات التوضيحية لتشمل فقط تلك التي تحتوي على النوع AnnotationType.link.
1. تحقق من الكتابة ثم قم بالإرسال إلى LinkAnNotation. تأكد من أن كل تعليق توضيحي هو بالفعل LinkAnNotation قبل الوصول إلى خصائصه.
1. تحقق من نوع إجراء الارتباط. تصفية الروابط التي تستخدم GoTouriAction (أي الروابط إلى عنوان URL على الويب).
1. قم باستخراج وطباعة URI وفهرس الصفحة. استخدم .uri للحصول على الرابط الخارجي و.page_index للسياق.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
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
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## موضوعات الارتباط ذات الصلة

- [العمل مع روابط PDF في بايثون](/pdf/ar/python-net/links/)
- [إنشاء روابط PDF في بايثون](/pdf/ar/python-net/create-links/)
- [تحديث الروابط في PDF باستخدام Python](/pdf/ar/python-net/update-links/)