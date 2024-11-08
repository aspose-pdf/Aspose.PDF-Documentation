---
title: تحويل HTML إلى PDF في بايثون
linktitle: تحويل HTML إلى ملف PDF
type: docs
weight: 40
url: /ar/python-java/convert-html-to-pdf/
lastmod: "2023-04-06"
description: يوضح لك هذا الموضوع كيفية تحويل HTML إلى PDF وMHTML إلى PDF باستخدام Aspose.PDF. لبايثون.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## نظرة عامة 

Aspose.PDF لبايثون عبر جافا هو حل احترافي يسمح لك بإنشاء ملفات PDF من صفحات الويب والشفرات الخام لـ HTML في تطبيقاتك.

تشرح هذه المقالة كيفية **تحويل HTML إلى PDF باستخدام بايثون**. تغطي المواضيع التالية.

_التنسيق_: **HTML**
- [تحويل HTML إلى PDF في بايثون](#python-html-to-pdf)
- [تحويل HTML إلى PDF باستخدام بايثون](#python-html-to-pdf)
- [كيفية تحويل HTML إلى PDF في بايثون](#python-html-to-pdf)

## تحويل HTML إلى PDF في بايثون

**Aspose.PDF لبايثون** هو API للتلاعب بملفات PDF يتيح لك تحويل أي مستندات HTML موجودة إلى PDF بسهولة. يمكن تخصيص عملية تحويل HTML إلى PDF بمرونة.

## تحويل HTML إلى PDF

يوضح نموذج الكود بايثون التالي كيفية تحويل مستند HTML إلى PDF.


1. قم بإنشاء مثيل لفئة [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. قم بتهيئة كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. احفظ مستند PDF الناتج عن طريق استدعاء طريقة **Document.Save()**.

```python

from asposepdf import Api


# تهيئة الرخصة
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# التحويل من مصفوفة بايت
documentName = "input.html"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array, Api.LoadFormat.HTML)
documentOutName = "result_fromHtml.pdf"
doc.save(documentOutName)

# التحويل من ملف
documentName = "input.html"
doc = Api.Document(documentName, Api.LoadFormat.HTML)
documentOutName = "result2_fromHtml.pdf"
doc.save(documentOutName)
```

{{% alert color="success" %}}
**حاول تحويل HTML إلى PDF عبر الإنترنت**


تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF HTML إلى PDF باستخدام تطبيق مجاني](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}