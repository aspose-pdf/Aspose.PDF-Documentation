---
title: إنشاء روابط PDF في بايثون
linktitle: إنشاء روابط
type: docs
weight: 10
url: /ar/python-net/create-links/
description: تعرف على كيفية إنشاء روابط PDF داخلية وخارجية وبعيدة في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إنشاء روابط في PDF
Abstract: يوفر دليل Aspose.PDF لـ Python عبر .NET حول إنشاء الروابط للمطورين تعليمات عملية لإضافة ارتباطات تشعبية تفاعلية إلى مستندات PDF باستخدام Python. ويغطي كيفية إنشاء أنواع مختلفة من الروابط، بما في ذلك تلك التي تطلق تطبيقات خارجية، أو تنتقل إلى صفحات محددة داخل نفس المستند، أو تفتح ملفات PDF أخرى. تشرح الوثائق كيفية استخدام كائنات LinkAnNotation، وتحديد المناطق القابلة للنقر باستخدام المستطيل، وتعيين إجراءات مثل LaunchAction أو GoToRemoteAction. من خلال أمثلة التعليمات البرمجية الواضحة والإرشادات خطوة بخطوة، يساعد هذا المورد المطورين على تحسين التنقل والتفاعل في ملفات PDF في تطبيقات Python الخاصة بهم.
---

## روابط في مستندات PDF

وفقًا لمواصفات PDF 1.7 (ISO 32000-1:2008)، يمكن أن يؤدي التعليق التوضيحي للرابط ** إلى تشغيل عدة أنواع من الإجراءات التي تحدد ما يحدث عند تنشيط التعليق التوضيحي. فيما يلي الإجراءات الأساسية المدعومة:

1. **GoTo** - ينتقل إلى وجهة داخل نفس المستند.
1. **GoTor** - ينتقل إلى وجهة في ملف PDF آخر (الانتقال عن بُعد).
1. **URI** - يفتح معرف مورد موحد، عادةً رابط ويب.
1. **إطلاق** - يقوم بتشغيل تطبيق أو فتح ملف (يعتمد على النظام الأساسي وغالبًا ما يكون مقيدًا للأمان).
1. **Named** - ينفذ إجراءً محددًا مسبقًا، مثل الانتقال إلى الصفحة التالية أو طباعة المستند.
1. **جافا سكريبت** - ينفذ شفرة جافا سكريبت المضمنة (تُستخدم بحذر بسبب مخاوف أمنية).
1. **submitForm** - يرسل بيانات النموذج إلى عنوان URL محدد.
1. **ResetForm** - يعيد تعيين حقول النموذج إلى قيمها الافتراضية.
1. ** ImportData** - استيراد البيانات إلى المستند من ملف خارجي.

من خلال إضافة رابط إلى تطبيق إلى مستند، يمكن الارتباط بالتطبيقات من مستند. يكون هذا مفيدًا عندما تريد من القراء اتخاذ إجراء معين في نقطة محددة في البرنامج التعليمي، على سبيل المثال، أو لإنشاء مستند غني بالميزات.

لإنشاء رابط تطبيق بـ «LaunchAction»:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## إنشاء رابط مستند PDF في ملف PDF

### استخدام «الانتقال إلى العمل عن بُعد»

يوضح مقتطف الشفرة هذا كيفية إضافة تعليق توضيحي للرابط إلى صفحة معينة من مستند PDF باستخدام مكتبة Python PDF.

1. افتح مستند PDF
1. حدد الصفحة الثانية من المستند (الفهرس 1)
1. إنشاء تعليق توضيحي للرابط:
1. تم وضعه عند الإحداثيات (10، 580، 120، 600)
1. أخضر ملون
1. روابط إلى 'sample.pdf' على صفحتها الأولى
1. أضف التعليق التوضيحي للرابط إلى الصفحة
1. احفظ المستند المعدل إلى مسار ملف الإخراج

لإنشاء رابط مستند PDF باستخدام «GoToreRemoteAction»:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### استخدام GoToAction

يوضح هذا الرمز كيفية إضافة تعليق توضيحي للرابط إلى صفحة معينة من مستند PDF باستخدام Aspose.PDF لـ Python. يظهر الارتباط كمستطيل أخضر ذو حدود متقطعة ويسمح للمستخدم بالانتقال إلى صفحة أخرى داخل نفس ملف PDF. لإنشاء رابط مستند PDF باستخدام «GoToAction»:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### تطبيق GoTouriAction

يوضح المثال التالي كيفية إضافة تعليق توضيحي للرابط إلى مستند PDF باستخدام Aspose.PDF لـ Python. يظهر الرابط كمنطقة خضراء قابلة للنقر على الصفحة الأولى، وعند النقر عليه، فإنه يفتح Aspose.PDF لوثائق Python في متصفح الويب عبر GoTouriAction.

هذه الوظيفة مفيدة لتضمين مراجع خارجية مفيدة أو وثائق أو روابط دعم مباشرة داخل ملفات PDF الخاصة بك.

1. قم بتحميل وثيقة PDF. افتح ملف PDF الموجود باستخدام AP.document.
1. قم بالوصول إلى الصفحة الأولى. استخدم document.pages [1] للوصول إلى الصفحة الأولى (يستخدم Aspose الفهرسة المستندة إلى 1).
1. قم بإنشاء تعليق توضيحي للرابط. قم بإنشاء كائن LinkAnNotation وحدد المنطقة المستطيلة القابلة للنقر باستخدام AP.Rectangle.
1. تعيين مظهر التعليق التوضيحي. قم بتعيين لون التعليق التوضيحي إلى اللون الأخضر باستخدام link.color = AP.color.green.
1. قم بتعيين إجراء URI. استخدم GoTouriAction لربط التعليق التوضيحي بعنوان URL خارجي.
1. أضف التعليق التوضيحي إلى الصفحة. قم بإلحاق التعليق التوضيحي للرابط الذي تم تكوينه بمجموعة التعليقات التوضيحية للصفحة الأولى.
1. احفظ المستند المعدل. احفظ مستند PDF المحدث إلى مسار الإخراج المحدد.

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## موضوعات الارتباط ذات الصلة

- [العمل مع روابط PDF في بايثون](/pdf/ar/python-net/links/)
- [استخراج الروابط من PDF في Python](/pdf/ar/python-net/extract-links/)
- [تحديث الروابط في PDF باستخدام Python](/pdf/ar/python-net/update-links/)