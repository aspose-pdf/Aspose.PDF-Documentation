---
title: احفظ مستند PDF برمجيًا
linktitle: احفظ ملف PDF
type: docs
weight: 30
url: /ar/python-net/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF في بايثون Aspose.PDF لبيثون عبر مكتبة.NET. احفظ مستند PDF في نظام الملفات والبث وفي تطبيقات الويب.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حفظ مستندات PDF باستخدام مكتبة Aspose.PDF في Python
Abstract: توفر المقالة إرشادات حول حفظ مستندات PDF باستخدام مكتبة Aspose.PDF في Python. وهي تحدد ثلاث طرق أساسية لحفظ ملفات PDF - إلى نظام الملفات، وإلى البث، وبتنسيقات محددة مثل PDF/A أو PDF/X. تعتبر طريقة `save () `لفئة `Document` أساسية لهذه العمليات. لحفظ PDF في نظام الملفات، يمكن إنشاء مستند أو معالجته، مثل إضافة صفحة جديدة، ثم حفظه مباشرة في المسار. للحفظ في البث، تسمح الأحمال الزائدة لطريقة «الحفظ» بكتابة مستند إلى كائن البث. بالإضافة إلى ذلك، توضح المقالة كيفية حفظ المستندات بتنسيقات PDF/A أو PDF/X، وهي معايير للأرشفة طويلة الأجل وتبادل الرسومات، على التوالي. تتطلب هذه العملية إعداد المستند باستخدام طريقة «التحويل» قبل حفظه. توضح مقتطفات شفرة Python المقدمة كل نهج، مما يوضح التطبيق العملي لهذه الأساليب.
---

## حفظ مستند PDF إلى نظام الملفات

يمكنك حفظ مستند PDF الذي تم إنشاؤه أو معالجته في نظام الملفات باستخدام [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.

```python
import aspose.pdf as ap

def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)
```

## احفظ مستند PDF للبث

يمكنك أيضًا حفظ مستند PDF الذي تم إنشاؤه أو معالجته للبث باستخدام التحميل الزائد لـ `Save` أساليب.

```python
import aspose.pdf as ap
import io

def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, 'w') as stream:
        document.save(stream)
```

## حفظ صيغة PDF/A أو PDF/X

يمكنك بسهولة حفظ مستند في إصدار محدد من PDF، مثل PDF/A أو PDF/X. في هذه الحالة، نحتاج إلى استدعاء طريقة التحويل قبل حفظ المستند.

PDF/A هو إصدار معياري ISO من تنسيق المستندات المحمولة (PDF) للاستخدام في أرشفة المستندات الإلكترونية وحفظها على المدى الطويل.
يختلف PDF/A عن PDF في أنه يحظر الميزات غير المناسبة للأرشفة طويلة المدى، مثل ربط الخطوط (على عكس تضمين الخط) والتشفير. تتضمن متطلبات ISO لمشاهدي PDF/A إرشادات إدارة الألوان ودعم الخط المضمن وواجهة مستخدم لقراءة التعليقات التوضيحية المضمنة.

PDF/X هي مجموعة فرعية من معيار PDF ISO. الغرض من PDF/X هو تسهيل تبادل الرسومات، وبالتالي فإنه يحتوي على سلسلة من المتطلبات المتعلقة بالطباعة والتي لا تنطبق على ملفات PDF القياسية.

في كلتا الحالتين، [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) يتم استخدام الطريقة لتخزين المستندات، بينما يجب إعداد المستندات باستخدام [تحول](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

```python
import aspose.pdf as ap
import io


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
