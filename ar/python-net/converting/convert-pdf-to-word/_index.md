---
title: تحويل PDF إلى Word في Python
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /ar/python-net/convert-pdf-to-word/
lastmod: "2026-06-05"
description: تعلم كيفية تحويل PDF إلى Word في Python، بما في ذلك PDF إلى DOC، PDF إلى DOCX، والتعرف المتقدم على التخطيط باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحويل PDF إلى DOC و DOCX في Python
Abstract: توضح هذه المقالة كيفية تحويل ملفات PDF إلى صيغ Microsoft Word باستخدام Aspose.PDF for Python via .NET. تغطي التحويل من PDF إلى DOC، ومن PDF إلى DOCX، وخيارات التعرف المتقدمة على التخطيط لإنشاء مستندات Word قابلة للتحرير من محتوى PDF.
---

توضح هذه الصفحة كيفية **تحويل PDF إلى Word في بايثون**. استخدم هذه الأمثلة عندما تحتاج إلى إخراج DOC أو DOCX قابل للتحرير من ملف PDF لأغراض المراجعة أو إعادة الاستخدام أو سير عمل المستندات المكتبية.

## تحويل PDF إلى DOC في بايثون

إحدى أكثر الميزات شهرة هي تحويل PDF إلى Microsoft Word DOC، مما يجعل إدارة المحتوى أسهل. **Aspose.PDF for Python via .NET** يتيح لك تحويل ملفات PDF ليس فقط إلى DOC بل أيضًا إلى صيغة DOCX، بسهولة وكفاءة.

استخدم تحويل Word عندما تحتاج إلى تعديل النص، وإعادة استخدام المحتوى في سير عمل المكتب، أو نقل محتوى PDF إلى مستندات DOC أو DOCX القابلة للتحرير.

ال [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) توفر الفئة العديد من الخصائص التي تحسن عملية تحويل ملفات PDF إلى تنسيق DOC. من بين هذه الخصائص، يتيح لك Mode تحديد وضع التعرف على محتوى PDF. يمكنك تحديد أي قيمة من تعداد RecognitionMode لهذه الخاصية. لكل من هذه القيم فوائد ومحددات محددة:

الخطوات: تحويل PDF إلى DOC في بايثون

1. قم بتحميل PDF إلى كائن 'ap.Document'.
1. إنشاء مثيل 'DocSaveOptions'.
1. عيّن خاصية format إلى 'DocFormat.DOC' لضمان أن يكون الإخراج بتنسيق .doc (تنسيق Word القديم).
1. احفظ ملف PDF كمستند Word باستخدام خيارات الحفظ المحددة.
1. اطبع رسالة تأكيد.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

Aspose.PDF for Python يقدم لك تطبيقًا عبر الإنترنت ["PDF إلى DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل PDF إلى DOC](/pdf/ar/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى DOCX في Python

تُتيح لك Aspose.PDF for Python API قراءة وتحويل مستندات PDF إلى DOCX باستخدام Python عبر .NET. يُعد DOCX تنسيقًا معروفًا لمستندات Microsoft Word التي تم تغيير هيكلها من ثنائي بسيط إلى مزيج من ملفات XML وملفات ثنائية. يمكن فتح ملفات DOCX باستخدام Word 2007 والإصدارات اللاحقة لكن ليس مع الإصدارات السابقة من MS Word التي تدعم امتدادات ملفات DOC.

المقتطف التالي من شفرة Python يوضح عملية تحويل ملف PDF إلى تنسيق DOCX.

الخطوات: تحويل PDF إلى DOCX في Python

1. حمّل ملف PDF المصدر باستخدام 'ap.Document'.
1. إنشاء نسخة من 'DocSaveOptions'.
1. عيّن خاصية format إلى 'DocFormat.DOC_X' لتوليد ملف .docx (صيغة Word الحديثة).
1. احفظ ملف PDF كملف DOCX باستخدام خيارات الحفظ المكوّنة.
1. اطبع رسالة تأكيد بعد التحويل.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## تحويل PDF إلى DOCX مع التعرف المتقدم على التخطيط

قم بتحويل مستند PDF إلى ملف DOCX (Word) باستخدام Python و Aspose.PDF مع إعدادات التعرف المتقدمة. يستخدم وضع التدفق المحسن للحفاظ على بنية المستند، مما يجعل الناتج أكثر قابلية للتحرير وأقرب إلى التنسيق الأصلي.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

ال [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) الصف يحتوي على خاصية تسمى Format التي توفر القدرة على تحديد تنسيق المستند الناتج، أي DOC أو DOCX. من أجل تحويل ملف PDF إلى تنسيق DOCX، يرجى تمرير القيمة Docx من تعداد DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

Aspose.PDF for Python يقدم لك تطبيقًا عبر الإنترنت ["PDF إلى Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF PDF إلى Word App](/pdf/ar/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## عمليات التحويل ذات الصلة

- [تحويل PDF إلى Excel](/pdf/ar/python-net/convert-pdf-to-excel/) للتصديرات الموجهة نحو الجداول.
- [تحويل PDF إلى PowerPoint](/pdf/ar/python-net/convert-pdf-to-powerpoint/) عندما تحتاج إلى شرائح عرض تقديمي بدلاً من مخرجات معالجة النصوص.
- [تحويل PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) لنشر الويب وتدفقات عمل المحتوى المستندة إلى المتصفح.
