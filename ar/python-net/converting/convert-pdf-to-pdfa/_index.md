---
title: تحويل PDF إلى تنسيقات PDF/A في بايثون
linktitle: تحويل PDF إلى تنسيقات PDF/A
type: docs
weight: 100
url: ar/python-net/convert-pdf-to-pdfa/
lastmod: "2022-12-23"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لبايثون لتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF لبايثون** يتيح لك تحويل ملف PDF إلى ملف PDF متوافق مع <abbr title="تنسيق المستند المحمول / أ">PDF/A</abbr>. قبل القيام بذلك، يجب التحقق من صحة الملف. يشرح هذا الموضوع كيفية القيام بذلك.

{{% alert color="primary" %}}

يرجى ملاحظة أننا نتبع Adobe Preflight للتحقق من التوافق مع PDF/A. جميع الأدوات في السوق لديها "تمثيلها" الخاص للتوافق مع PDF/A. يرجى مراجعة هذا المقال حول أدوات التحقق من PDF/A كمرجع. اخترنا منتجات Adobe للتحقق من كيفية إنتاج Aspose.PDF لملفات PDF لأن Adobe في مركز كل شيء متعلق بـ PDF.

{{% /alert %}}

قم بتحويل الملف باستخدام طريقة التحويل في فئة المستند.
 قبل تحويل ملف PDF إلى ملف متوافق مع PDF/A، قم بالتحقق من صحة ملف PDF باستخدام طريقة Validate. يتم تخزين نتيجة التحقق في ملف XML ثم يتم تمرير هذه النتيجة أيضًا إلى طريقة Convert. يمكنك أيضًا تحديد الإجراء للعناصر التي لا يمكن تحويلها باستخدام التعداد ConvertErrorAction.

{{% alert color="success" %}}
**حاول تحويل PDF إلى PDF/A عبر الإنترنت**

تقدم Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى PDF/A باستخدام التطبيق المجاني](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## تحويل ملف PDF إلى PDF/A-1b

يوضح مقتطف الشيفرة التالي كيفية تحويل ملفات PDF إلى ملفات متوافقة مع PDF/A-1b.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
    output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
    # فتح مستند PDF
    document = ap.Document(input_pdf)
    # التحويل إلى مستند متوافق مع PDF/A
    document.convert(output_log, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    # حفظ المستند الناتج
    document.save(output_pdf)
```