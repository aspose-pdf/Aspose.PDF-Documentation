---
title: تحويل PDF إلى وورد في بايثون
linktitle: تحويل ملفات PDF إلى وورد
type: docs
weight: 10
url: /ar/python-net/convert-pdf-to-word/
lastmod: "2026-06-11"
description: تعرف على كيفية تحويل PDF إلى Word في Python، بما في ذلك PDF إلى DOC، وPDF إلى DOCX، والتعرف المتقدم على التخطيط باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحويل PDF إلى DOC و DOCX في بايثون
Abstract: توضح هذه المقالة كيفية تحويل ملفات PDF إلى تنسيقات ميكروسوفت ورد باستخدام Aspose.PDF لبيثون عبر .NET. ويغطي خيارات PDF إلى DOC و PDF إلى DOCX وخيارات التعرف على التخطيط المتقدمة لإنشاء مستندات Word قابلة للتحرير من محتوى PDF.
---

تعرض هذه الصفحة كيفية **تحويل PDF إلى Word في Python**. استخدم هذه الأمثلة عندما تحتاج إلى إخراج DOC أو DOCX قابل للتحرير من ملف PDF للمراجعة أو إعادة الاستخدام أو عمليات سير عمل المستندات المكتبية.

## تحويل PDF إلى DOC في بايثون

واحدة من أكثر الميزات شيوعًا هي تحويل PDF إلى Microsoft Word DOC، مما يجعل إدارة المحتوى أسهل. **Aspose.pdf لبايثون عبر .NET** يسمح لك بتحويل ملفات PDF ليس فقط إلى DOC ولكن أيضًا إلى تنسيق DOCX بسهولة وكفاءة.

استخدم تحويل Word عندما تحتاج إلى مراجعة النص أو إعادة استخدام المحتوى في عمليات سير عمل المكتب أو نقل محتوى PDF إلى مستندات DOC أو DOCX القابلة للتحرير.

ال [خيارات حفظ المستندات](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) توفر الفئة العديد من الخصائص التي تعمل على تحسين عملية تحويل ملفات PDF إلى تنسيق DOC. من بين هذه الخصائص، يتيح لك الوضع تحديد وضع التعرف على محتوى PDF. يمكنك تحديد أي قيمة من تعداد RecognitionMode لهذه الخاصية. لكل من هذه القيم مزايا وقيود محددة:

الخطوات: تحويل PDF إلى DOC في بايثون

1. قم بتحميل ملف PDF إلى كائن «AP.Document».
1. قم بإنشاء مثيل «DocSaveOptions».
1. قم بتعيين خاصية التنسيق إلى 'DocFormat.DOC' للتأكد من أن الإخراج بتنسيق.doc (تنسيق Word الأقدم).
1. احفظ PDF كمستند Word باستخدام خيارات الحفظ المحددة.
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
** حاول تحويل PDF إلى DOC عبر الإنترنت**

Aspose.PDF لبيثون يقدم لك التطبيق عبر الإنترنت [«PDF إلى DOC»](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![تحويل ملفات PDF إلى DOC](/pdf/ar/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى DOCX في بايثون

يتيح لك Aspose.PDF لواجهة برمجة تطبيقات Python قراءة مستندات PDF وتحويلها إلى DOCX باستخدام Python عبر .NET. DOCX هو تنسيق معروف لمستندات Microsoft Word التي تم تغيير هيكلها من ثنائي عادي إلى مزيج من ملفات XML والملفات الثنائية. يمكن فتح ملفات Docx باستخدام Word 2007 والإصدارات الجانبية ولكن ليس مع الإصدارات السابقة من MS Word التي تدعم امتدادات ملفات DOC.

يعرض مقتطف شفرة Python التالي عملية تحويل ملف PDF إلى تنسيق DOCX.

الخطوات: تحويل PDF إلى DOCX في بايثون

1. قم بتحميل ملف PDF المصدر باستخدام «AP.document».
1. قم بإنشاء مثيل لـ «DocSaveOptions».
1. قم بتعيين خاصية التنسيق إلى «docformat.doc_x» لإنشاء ملف.docx (تنسيق Word الحديث).
1. احفظ PDF كملف DOCX مع خيارات الحفظ المهيأة.
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

## تحويل PDF إلى DOCX باستخدام التعرف المتقدم على التخطيط

قم بتحويل مستند PDF إلى ملف DOCX (Word) باستخدام Python و Aspose.PDF مع إعدادات التعرف المتقدمة. يستخدم وضع التدفق المحسن للحفاظ على بنية المستند، مما يجعل الإخراج أكثر قابلية للتحرير وأقرب إلى التخطيط الأصلي.

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

ال [خيارات حفظ المستندات](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) تحتوي الفئة على خاصية تسمى Format والتي توفر القدرة على تحديد تنسيق المستند الناتج، أي DOC أو DOCX. من أجل تحويل ملف PDF إلى صيغة DOCX، يرجى تمرير قيمة Docx من تعداد DocSaveOptions.docFormat.

{{% alert color="warning" %}}
** حاول تحويل PDF إلى DOCX عبر الإنترنت**

Aspose.PDF لبيثون يقدم لك التطبيق عبر الإنترنت [«تحويل ملف PDF إلى وورد»](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![تحويل ملف Aspose.PDF إلى تطبيق وورد](/pdf/ar/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## التحويلات ذات الصلة

- [تحويل ملفات PDF إلى إكسيل](/pdf/ar/python-net/convert-pdf-to-excel/) للصادرات الموجهة نحو جداول البيانات.
- [تحويل PDF إلى بوربوينت](/pdf/ar/python-net/convert-pdf-to-powerpoint/) عندما تحتاج إلى شرائح العرض التقديمي بدلاً من مخرجات معالجة الكلمات.
- [تحويل ملفات PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) للنشر على الويب وسير عمل المحتوى المستند إلى المتصفح.
