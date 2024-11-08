---
title: تحويل PDF إلى تنسيقات PDF/A في بايثون
linktitle: تحويل PDF إلى تنسيقات PDF/A
type: docs
weight: 100
url: /ar/python-java/convert-pdf-to-pdfa/
lastmod: "2023-04-06"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لبايثون عبر بايثون لتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF لبايثون** يسمح لك بتحويل ملف PDF إلى ملف PDF متوافق مع <abbr title="تنسيق المستند المحمول / أ">PDF/A</abbr>. قبل القيام بذلك، يجب التحقق من صحة الملف. يشرح هذا الموضوع كيفية القيام بذلك.

{{% alert color="primary" %}}

يرجى ملاحظة أننا نتبع Adobe Preflight للتحقق من مطابقة PDF/A. جميع الأدوات في السوق لها "تمثيل" خاص بها لمطابقة PDF/A. يرجى مراجعة هذه المقالة حول أدوات التحقق من PDF/A كمرجع. اخترنا منتجات Adobe للتحقق من كيفية إنتاج Aspose.PDF لملفات PDF لأن Adobe في مركز كل ما يتعلق بـ PDF.

{{% /alert %}}

قم بتحويل الملف باستخدام طريقة Convert للفئة Document.
 قبل تحويل ملف PDF إلى ملف متوافق مع PDF/A، قم بالتحقق من صحة ملف PDF باستخدام طريقة Validate. يتم تخزين نتيجة التحقق في ملف XML ثم يتم تمرير هذه النتيجة أيضًا إلى طريقة Convert. يمكنك أيضًا تحديد الإجراء للعناصر التي لا يمكن تحويلها باستخدام التعداد ConvertErrorAction.

{{% alert color="success" %}}
**حاول تحويل PDF إلى PDF/A عبر الإنترنت**

تقدم Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)، حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي تعمل بها.

[![تحويل Aspose.PDF من PDF إلى PDF/A باستخدام التطبيق المجاني](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## تحويل ملف PDF إلى PDF/A-1b

يظهر مقطع الكود التالي كيفية تحويل ملفات PDF إلى PDF متوافق مع PDF/A-1b.

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
# افتح مستند PDF
document = Api.Document(input_pdf)
# تحويل إلى مستند متوافق مع PDF/A
document.convert(output_log, Api.PdfFormat.PDF_A_1B, Api.ConvertErrorAction.Delete)
# حفظ المستند الناتج
document.save(output_pdf)
```