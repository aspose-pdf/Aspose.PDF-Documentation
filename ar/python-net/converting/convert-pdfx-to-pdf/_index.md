---
title: تحويل PDF/A و PDF/UA إلى PDF في بايثون
linktitle: تحويل ملفات PDF/A وPDF/UA إلى PDF
type: docs
weight: 120
url: /ar/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-06-11"
description: تعرف على كيفية إزالة توافق PDF/A و PDF/UA من ملفات PDF في Python باستخدام Aspose.PDF لـ Python عبر .NET وحفظها كمستندات PDF قياسية.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF/A و PDF/UA إلى PDF القياسي في بايثون
Abstract: تشرح هذه المقالة كيفية إزالة توافق PDF/A و PDF/UA من مستندات PDF المستندة إلى المعايير باستخدام Aspose.PDF لـ Python عبر .NET. وهو يغطي السيناريوهات التي قد تحتاج فيها إلى PDF قياسي بدلاً من ملف أرشيفي أو ملف مقيد الوصول، ويعرض كيفية حفظ النتيجة بعد إزالة البيانات الوصفية للامتثال والقيود.
---

استخدم هذه الصفحة عندما تحتاج إلى تحويل ملف PDF قائم على المعايير، مثل PDF/A أو PDF/UA، مرة أخرى إلى مستند PDF عادي للتحرير النهائي أو المعالجة أو إعادة التوزيع.

تعد ملفات PDF المتوافقة مع المعايير مفيدة لعمليات سير عمل الأرشفة والطباعة وإمكانية الوصول، ولكن في بعض الحالات قد تحتاج إلى إزالة هذا التوافق قبل دمج الملف في أنظمة أو خطوط أنابيب أخرى. يتيح لك Aspose.PDF لـ Python عبر .NET القيام بذلك برمجيًا ثم حفظ النتيجة كملف PDF قياسي.

## تحويل ملفات PDF/A إلى PDF

يزيل هذا المثال البيانات الوصفية للتوافق مع PDF/A والقيود من PDF بحيث يمكن حفظ المستند كملف PDF عادي مرة أخرى.

1. قم بتحميل مستند PDF باستخدام «AP.document».
1. اتصل بـ «remove_pdfa_compliance ()» لتجريد جميع إعدادات الامتثال والبيانات الوصفية المتعلقة بـ PDF/A.
1. احفظ ملف PDF الناتج إلى مسار الإخراج.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)
```

## إزالة التوافق مع PDF/UA

يوضح هذا المثال كيفية إزالة التوافق المرتبط بـ PDF/UAA بحيث يمكن حفظ المستند كملف PDF قياسي لعمليات سير العمل الخاصة بعدم إمكانية الوصول.

1. قم بتحميل مستند PDF باستخدام «AP.document ()».
1. اتصل بـ 'document.remove_pdfa_compliance () 'لإزالة أي قيود على PDF/A أو إعدادات التوافق.
1. احفظ ملف PDF المعدل إلى «path_outfile».

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFUA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)
```

## متى تستخدم سير العمل هذا

- قم بإزالة إعدادات التوافق قبل إرسال مستند إلى سلسلة أدوات لا تتطلب قيود PDF/A أو PDF/UA.
- قم بتبسيط معالجة المستندات النهائية عندما لا تكون هناك حاجة إلى البيانات الوصفية للأرشفة أو إمكانية الوصول.
- قم بتطبيع ملفات PDF المدخلة قبل تصديرها إلى تنسيقات أخرى.

## التحويلات ذات الصلة

- [تحويل ملفات PDF إلى ملفات PDF/A وPDF/E وPDF/X](/pdf/ar/python-net/convert-pdf-to-pdf_x/) إذا كنت بحاجة إلى سير العمل المعاكس وتريد إنشاء ملفات PDF متوافقة مع المعايير.
- [تحويل ملفات PDF إلى وورد](/pdf/ar/python-net/convert-pdf-to-word/) لإخراج مستند قابل للتحرير بعد إزالة قيود التوافق.
- [تحويل ملفات PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) للحصول على مخرجات سهلة للمتصفح من ملفات PDF القياسية.
