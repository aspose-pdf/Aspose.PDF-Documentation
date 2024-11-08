---
title: تحويل HTML إلى PDF في بايثون
linktitle: تحويل ملف HTML إلى PDF
type: docs
weight: 40
url: /ar/python-net/convert-html-to-pdf/
lastmod: "2022-12-22"
description: يوضح هذا الموضوع كيفية تحويل HTML إلى PDF وMHTML إلى PDF باستخدام Aspose.PDF لبايثون.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## نظرة عامة 

Aspose.PDF لبايثون عبر .NET هو حل احترافي يسمح لك بإنشاء ملفات PDF من صفحات الويب وكود HTML الخام في تطبيقاتك.

توضح هذه المقالة كيفية **تحويل HTML إلى PDF باستخدام بايثون**. وهي تغطي المواضيع التالية.

_التنسيق_: **HTML**
- [تحويل HTML إلى PDF باستخدام بايثون](#python-html-to-pdf)
- [بايثون تحويل HTML إلى PDF](#python-html-to-pdf)
- [بايثون كيفية تحويل HTML إلى PDF](#python-html-to-pdf)

## تحويل HTML إلى PDF باستخدام بايثون

**Aspose.PDF لبايثون** هو واجهة برمجة تطبيقات لمعالجة PDF تتيح لك تحويل أي مستندات HTML موجودة إلى PDF بسلاسة. يمكن تخصيص عملية تحويل HTML إلى PDF بشكل مرن.

## تحويل HTML إلى PDF

يوضح نموذج كود بايثون التالي كيفية تحويل مستند HTML إلى PDF.

1. قم بإنشاء مثيل لفئة [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. قم بتهيئة كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. احفظ مستند PDF الناتج عن طريق استدعاء طريقة **Document.Save()**.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "little_html.html"
    output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
    options = ap.HtmlLoadOptions()
    document = ap.Document(input_pdf, options)
    document.save(output_pdf)
```

{{% alert color="success" %}}
**حاول تحويل HTML إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيق مجاني عبر الإنترنت ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}