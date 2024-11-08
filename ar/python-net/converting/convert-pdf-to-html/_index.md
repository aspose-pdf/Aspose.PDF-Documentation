---
title: تحويل PDF إلى HTML في بايثون 
linktitle: تحويل PDF إلى تنسيق HTML
type: docs
weight: 50
url: /ar/python-net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: يوضح لك هذا الموضوع كيفية تحويل ملف PDF إلى تنسيق HTML باستخدام مكتبة Aspose.PDF لبايثون .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## نظرة عامة

توضح هذه المقالة كيفية **تحويل PDF إلى HTML باستخدام بايثون**. يغطي هذه المواضيع.

_التنسيق_: **HTML**
- [تحويل PDF إلى HTML باستخدام بايثون](#python-pdf-to-html)
- [بايثون تحويل PDF إلى HTML](#python-pdf-to-html)
- [بايثون كيفية تحويل ملف PDF إلى HTML](#python-pdf-to-html)

## تحويل PDF إلى HTML

يوفر **Aspose.PDF لبايثون عبر .NET** العديد من المزايا لتحويل تنسيقات الملفات المختلفة إلى مستندات PDF وتحويل ملفات PDF إلى تنسيقات إخراج متنوعة.
 هذه المقالة تناقش كيفية تحويل ملف PDF إلى <abbr title="لغة ترميز النص الفائق">HTML</abbr>. يمكنك استخدام بضع سطور من كود بايثون لتحويل PDF إلى HTML. قد تحتاج إلى تحويل PDF إلى HTML إذا كنت ترغب في إنشاء موقع ويب أو إضافة محتوى إلى منتدى على الإنترنت. إحدى الطرق لتحويل PDF إلى HTML هي استخدام بايثون برمجيًا.

{{% alert color="success" %}}
**حاول تحويل PDF إلى HTML عبر الإنترنت**

يقدم لك Aspose.PDF لبايثون تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)، حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى HTML مع تطبيق مجاني](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>الخطوات: تحويل PDF إلى HTML في بايثون</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع مستند PDF المصدر.
2. احفظه بـ [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) عن طريق استدعاء [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) الطريقة.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_html.html"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    # حفظ المستند بتنسيق HTML
    save_options = ap.HtmlSaveOptions()
    document.save(output_pdf, save_options)
```

## انظر أيضا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما في الأعلى.

_التنسيق_: **HTML**
- [كود Python لتحويل PDF إلى HTML](#python-pdf-to-html)
- [API Python لتحويل PDF إلى HTML](#python-pdf-to-html)
- [تحويل PDF إلى HTML برمجياً باستخدام Python](#python-pdf-to-html)
- [مكتبة Python لتحويل PDF إلى HTML](#python-pdf-to-html)
- [حفظ PDF كـ HTML باستخدام Python](#python-pdf-to-html)
- [توليد HTML من PDF باستخدام Python](#python-pdf-to-html)
- [إنشاء HTML من PDF باستخدام Python](#python-pdf-to-html)

- [محول Python لتحويل PDF إلى HTML](#python-pdf-to-html)