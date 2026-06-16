---
title: العمل مع نماذج XFA
linktitle: نماذج XFA
type: docs
weight: 20
url: /ar/python-net/xfa-forms/
description: Aspose.PDF لبيثون عبر .NET API يتيح لك العمل مع حقول XFA و XFA Acroform في مستند PDF.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تحويل XFA إلى أكروفورم

{{% alert color="primary" %}}

جرب عبر الإنترنت
يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط: [المنتجات.aspose.app/pdf/xfa/أكروفورم](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

يوضح مقتطف الشفرة التالي كيفية تحويل نموذج XFA الديناميكي (بنية نماذج XML) إلى AcroForm قياسي.

**تتضمن الخطوات الرئيسية ما يلي: **

1. تحميل وثيقة PDF المدخلة.
1. تغيير نوع النموذج إلى STANDARD.
1. حفظ ملف PDF المحول إلى ملف جديد.

يسمح هذا التحويل بتوافق أفضل ومعالجة متسقة للنماذج عبر برامج قراءة وتطبيقات PDF المختلفة.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## استخدام عرض احتياجات التجاهل

يوضح هذا المثال كيفية تحويل نموذج XFA الديناميكي إلى AcroForm قياسي باستخدام Aspose.PDF لـ Python. يتحقق الكود مما إذا كان ملف PDF المُدخل يحتوي على نموذج XFA ويتجاوز العرض إذا لزم الأمر. ثم يقوم بتعيين نوع النموذج إلى STANDARD وحفظ ملف PDF المحدث.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```
