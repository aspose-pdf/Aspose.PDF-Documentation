---
title: تحويل HTML إلى PDF باستخدام بايثون
linktitle: تحويل ملف HTML إلى PDF
type: docs
weight: 40
url: /ar/python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
description: تعرف على كيفية تحويل محتوى HTML إلى مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل HTML إلى PDF باستخدام Aspose.PDF للبايثون
Abstract: يقدم Aspose.PDF للبايثون عبر .NET حلاً قوياً لإنشاء ملفات PDF من صفحات الويب ورمز HTML الخام داخل التطبيقات. يقدم هذا المقال دليلًا حول تحويل HTML إلى PDF باستخدام بايثون، موضحًا استخدام Aspose.PDF للبايثون، وهو API لمعالجة PDF يتيح تحويل مستندات HTML إلى تنسيق PDF بسلاسة. يمكن تخصيص عملية التحويل حسب الحاجة. يتضمن المقال مثالًا على شفرة بايثون يوضح عملية التحويل، والتي تتضمن إنشاء مثال من فئة HtmlLoadOptions، وت初始化 كائن Document، وحفظ مستند PDF الناتج باستخدام طريقة Document.Save(). بالإضافة إلى ذلك، يوفر Aspose أداةً عبر الإنترنت لتحويل HTML إلى PDF، مما يتيح للمستخدمين استكشاف وظائف وجودة عملية التحويل.
---

## تحويل HTML إلى PDF باستخدام بايثون

**Aspose.PDF للبايثون** هو API لمعالجة PDF يتيح لك تحويل أي مستندات HTML موجودة إلى PDF بسلاسة. يمكن تخصيص عملية تحويل HTML إلى PDF بمرونة.

## تحويل HTML إلى PDF

العينة البرمجية التالية للبايثون توضح كيفية تحويل مستند HTML إلى PDF.

1. إنشاء مثال من فئة [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. تهيئة كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. حفظ مستند PDF الناتج عن طريق استدعاء طريقة **document.save()**.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**جرب تحويل HTML إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا على الإنترنت ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF HTML إلى PDF باستخدام التطبيق المجاني](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## تحويل HTML إلى PDF باستخدام نوع الوسائط

يوضح هذا المثال كيفية تحويل ملف HTML إلى PDF باستخدام Aspose.PDF للبايثون عبر .NET مع خيارات تصيير محددة.

1. إنشاء مثال من فئة [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/). تُطبق الخاصية 'html_media_type' قواعد CSS المصممة للعرض على الشاشة. يمكن أن تحتوي خاصية 'html_media_type' على قيم متعددة. يمكنك تعيينها إلى HtmlMediaType.SCREEN أو HtmlMediaType.PRINT.
1. تحميل HTML إلى ap.Document باستخدام خيارات التحميل.
1. حفظ المستند كملف PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## تحويل HTML إلى PDF مع قاعدة CSS للصفحة ذات الأولوية

قد تحتوي بعض المستندات على إعدادات تخطيط تستخدم [قاعدة الصفحة](https://developer.mozilla.org/en-US/docs/Web/CSS/@page)، والتي قد تُنشئ غموضًا عند إنشاء التخطيط. يمكنك التحكم بالأولوية باستخدام خاصية 'is_priority_css_page_rule'. إذا تم ضبط هذه الخاصية على 'True'، تُطبق قاعدة CSS أولًا.

1. إنشاء مثال من فئة [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. ضبط 'is_priority_css_page_rule = False' لتعطيل إعطاء أولوية لقواعد CSS @page، مما يسمح للأنماط الأخرى أن تتفوق.
1. تحميل HTML إلى ap.Document مع الخيارات المكوَّنة.
1. حفظ المستند كملف PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## تحويل HTML إلى PDF مع الخطوط المدمجة

يوضح هذا المثال كيفية تحويل ملف HTML إلى PDF مع دمج الخطوط. إذا كنت بحاجة إلى مستند PDF يحتوي على خطوط مدمجة، يجب ضبط 'is_embed_fonts' إلى True.

1. إنشاء 'HtmlLoadOptions()' لتكوين تحويل HTML إلى PDF.
1. ضبط 'is_embed_fonts = True' لضمان دمج جميع الخطوط المستخدمة في HTML مباشرةً في PDF، مع الحفاظ على الدقة البصرية.
1. تحميل HTML إلى ap.Document باستخدام هذه الخيارات.
1. حفظ المستند كملف PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## عرض المحتوى على صفحة واحدة أثناء تحويل HTML إلى PDF

يوضح هذا المثال كيفية تحويل ملف HTML إلى PDF صفحة واحدة باستخدام Aspose.PDF للبايثون.
يمكنك عرض كل المحتوى على صفحة واحدة باستخدام خاصية 'is_render_to_single_page'.

1. إنشاء مثال من 'HtmlLoadOptions()' لتكوين عملية التحويل.
1. تمكين 'is_render_to_single_page' لتصوير كامل محتوى HTML على صفحة PDF واحدة متواصلة.
1. تحميل المستند مع الخيارات المكوَّنة إلى 'ap.Document'.
1. حفظ النتيجة كملف PDF.

```python
    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## تحويل MHTML إلى PDF

هذا المثال يوضح كيفية تحويل ملف MHT (MHTML) إلى مستند PDF باستخدام Aspose.PDF للبايثون مع أبعاد صفحات محددة.

1. قم بإنشاء نسخة من ap.MhtLoadOptions() لتكوين معالجة ملف MHT.
1. ضبط مختلف المعلمات، مثل حجم الصفحة.
1. تهيئة المستند بملف الإدخال وخيارات التحميل المكوّنة.
1. حفظ المستند الناتج كملف PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
