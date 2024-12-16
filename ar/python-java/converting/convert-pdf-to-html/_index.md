---
title: تحويل PDF إلى HTML في بايثون
linktitle: تحويل PDF إلى تنسيق HTML
type: docs
weight: 50
url: /ar/python-java/convert-pdf-to-html/
lastmod: "2021-11-01"
description: يوضح هذا الموضوع كيفية تحويل ملف PDF إلى تنسيق HTML باستخدام مكتبة Aspose.PDF لـ Python Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## نظرة عامة

تشرح هذه المقالة كيفية **تحويل PDF إلى HTML باستخدام بايثون**. تغطي هذه المواضيع.

_التنسيق_: **HTML**
- [بايثون PDF إلى HTML](#python-pdf-to-html)
- [بايثون تحويل PDF إلى HTML](#python-pdf-to-html)
- [بايثون كيفية تحويل ملف PDF إلى HTML](#python-pdf-to-html)


## تحويل PDF إلى HTML

يوفر **Aspose.PDF for Python عبر .NET** العديد من الميزات لتحويل صيغ الملفات المختلفة إلى مستندات PDF وتحويل ملفات PDF إلى صيغ إخراج متنوعة.
 هذه المقالة تناقش كيفية تحويل ملف PDF إلى <abbr title="لغة توصيف النص التشعبي">HTML</abbr>. يمكنك استخدام بضع سطور من كود Python لتحويل PDF إلى HTML. قد تحتاج إلى تحويل PDF إلى HTML إذا كنت تريد إنشاء موقع ويب أو إضافة محتوى إلى منتدى عبر الإنترنت. إحدى الطرق لتحويل PDF إلى HTML هي استخدام Python برمجيًا.

{{% alert color="success" %}}
**حاول تحويل PDF إلى HTML عبر الإنترنت**

تقدم Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>خطوات: تحويل PDF إلى HTML باستخدام Python</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) مع مستند PDF المصدر.
2. احفظه باستخدام [HtmlSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/htmlsaveoptions/) عن طريق استدعاء طريقة [Document.save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python
from asposepdf import Api

documentName = "../../testdata/source.pdf"
documentOutName = "../../testout/result.html"
# افتح مستند PDF
document = Api.Document(documentName)

# احفظ المستند بصيغة HTML
save_options = Api.HtmlSaveOptions()
document.save(documentOutName, save_options)
```

## انظر أيضا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما هو موضح أعلاه.

_تنسيق_: **HTML**
- [كود تحويل PDF إلى HTML في بايثون](#python-pdf-to-html)
- [API تحويل PDF إلى HTML في بايثون](#python-pdf-to-html)
- [تحويل PDF إلى HTML برمجياً في بايثون](#python-pdf-to-html)
- [مكتبة تحويل PDF إلى HTML في بايثون](#python-pdf-to-html)
- [حفظ PDF كـ HTML في بايثون](#python-pdf-to-html)
- [توليد HTML من PDF في بايثون](#python-pdf-to-html)
- [إنشاء HTML من PDF في بايثون](#python-pdf-to-html)

- [محول PDF إلى HTML في بايثون](#python-pdf-to-html)