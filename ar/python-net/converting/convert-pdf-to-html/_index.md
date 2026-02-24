---
title: تحويل PDF إلى HTML في بايثون
linktitle: تحويل PDF إلى تنسيق HTML
type: docs
weight: 50
url: /ar/python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: يُظهر لك هذا الموضوع كيفية تحويل ملف PDF إلى تنسيق HTML باستخدام مكتبة Aspose.PDF لبايثون عبر .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى HTML في بايثون
Abstract: يقدم هذا المقال دليلًا شاملاً حول تحويل ملفات PDF إلى HTML باستخدام بايثون، وتحديدًا عبر مكتبة Aspose.PDF لبايثون عبر .NET. يوضح الخطوات اللازمة لتحقيق هذا التحويل برمجيًا، مع التركيز على إنشاء كائن `Document` من ملف PDF المصدر واستخدام `HtmlSaveOptions` لحفظ المستند بتنسيق HTML. يتضمن المقال مقتطفًا موجزًا من كود بايثون يوضح عملية التحويل. بالإضافة إلى ذلك، يُعرف بأداة عبر الإنترنت، تطبيق Aspose.PDF "PDF to HTML"، لتمكين المستخدمين من استكشاف وظيفة وجودة التحويل. تم هيكلة المقال لتغطية مواضيع ذات صلة مختلفة، لضمان فهم شامل لاستخدام بايثون في تحويل PDF إلى HTML.
---

## تحويل PDF إلى HTML

**Aspose.PDF لبايثون عبر .NET** يوفر العديد من الميزات لتحويل صيغ الملفات المختلفة إلى مستندات PDF وتحويل ملفات PDF إلى صيغ إخراج متعددة. يناقش هذا المقال كيفية تحويل ملف PDF إلى <abbr title="HyperText Markup Language">HTML</abbr>. يمكنك استخدام بضع أسطر من كود بايثون لتحويل PDF إلى HTML. قد تحتاج إلى تحويل PDF إلى HTML إذا كنت تريد إنشاء موقع ويب أو إضافة محتوى إلى منتدى على الإنترنت. إحدى طرق تحويل PDF إلى HTML هي الاستخدام البرمجي لبايثون.

{{% alert color="success" %}}
**حاول تحويل PDF إلى HTML عبر الإنترنت**

Aspose.PDF لبايثون يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)، حيث يمكنك تجربة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى HTML مع تطبيق مجاني](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

الخطوات: تحويل PDF إلى HTML في بايثون

1. إنشاء نسخة من كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام ملف PDF المصدر.
1. احفظه باستخدام [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) عبر استدعاء طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML مع حفظ الصور في المجلد المحدد

تقوم هذه الدالة بتحويل ملف PDF إلى تنسيق HTML باستخدام Aspose.PDF لبايثون عبر .NET. تُحفظ جميع الصور المستخرجة في مجلد محدد بدلاً من تضمينها في ملف HTML.

1. إعداد خيارات حفظ HTML.
1. حفظ كـ HTML مع صور خارجية.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_all_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML متعدد الصفحات

تقوم هذه الدالة بتحويل ملف PDF إلى HTML متعدد الصفحات، حيث يتم تصدير كل صفحة PDF كملف HTML منفصل. هذا يجعل التنقل في الناتج أسهل ويقلل من وقت التحميل لملفات PDF الكبيرة.

1. تحميل ملف PDF المصدر باستخدام 'ap.Document'.
1. إنشاء 'HtmlSaveOptions' وتعيين 'split_into_pages'.
1. حفظ المستند كـ HTML مع تقسيم الصفحات إلى ملفات منفصلة.
1. طباعة رسالة تأكيد.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML مع حفظ صور SVG في المجلد المحدد

تقوم هذه الدالة بتحويل PDF إلى تنسيق HTML مع تخزين جميع الصور كملفات SVG في مجلد محدد، بدلاً من تضمينها مباشرة في HTML.

1. تحميل ملف PDF المصدر باستخدام 'ap.Document'.
1. إنشاء 'HtmlSaveOptions' وتعيين 'special_folder_for_svg_images' إلى المجلد المستهدف.
1. حفظ المستند كـ HTML مع صور SVG خارجية.
1. طباعة رسالة تأكيد.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML وحفظ صور SVG مضغوطة

يقوم هذا المقتطف بتحويل PDF إلى تنسيق HTML، مع تخزين جميع الصور كملفات SVG في مجلد محدد وضغطها لتقليل حجم الملف.

1. تحميل مستند PDF باستخدام 'ap.Document'.
1. إنشاء 'HtmlSaveOptions' و:
- تعيين 'special_folder_for_svg_images' لتخزين صور SVG خارجيًا.
- تمكين 'compress_svg_graphics_if_any' لضغط صور SVG.
1. حفظ المستند كـ HTML مع صور SVG مضغوطة خارجية.
1. طباعة رسالة تأكيد.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    save_options.compress_svg_graphics_if_any = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML مع التحكم في الصور النقطية المضمنة

يقوم هذا المقتطف بتحويل PDF إلى تنسيق HTML، مع تضمين الصور النقطية كخلفيات صفحات PNG. يحافظ هذا الأسلوب على جودة الصورة وتخطيط الصفحة داخل HTML.

1. تحميل مستند PDF باستخدام 'ap.Document'.
1. إنشاء 'HtmlSaveOptions' وضبط 'raster_images_saving_mode' إلى 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. حفظ المستند كـ HTML مع صور نقطية مدمجة.
1. طباعة رسالة تأكيد.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى صفحة HTML بمحتوى جسم فقط

هذه الدالة تحول ملف PDF إلى تنسيق HTML، وتولّد محتوى 'body-only' بدون وسوم 'html' أو 'head' إضافية، وتقسم الناتج إلى صفحات منفصلة.

1. تحميل مستند PDF باستخدام 'ap.Document'.
1. إنشاء 'HtmlSaveOptions' وتكوينها:
- 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' لتوليد محتوى 'body' فقط.
- 'split_into_pages' لإنشاء ملفات HTML منفصلة لكل صفحة PDF.
1. حفظ المستند كـ HTML باستخدام الخيارات المحددة.
1. طباعة رسالة تأكيد.

```python

from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML مع عرض النص الشفاف

هذه الدالة تحول ملف PDF إلى تنسيق HTML، وتظهر جميع النصوص شفافًا، بما في ذلك النصوص الظلية، مما يحافظ على الدقة البصرية بينما يتيح تنسيقًا مرنًا في HTML الناتج.

1. تحميل مستند PDF باستخدام 'ap.Document'.
1. إنشاء 'HtmlSaveOptions' وتكوينها:
- 'save_transparent_texts' لعرض النص العادي بشكل شفاف.
- 'save_shadowed_texts_as_transparent_texts' لعرض النص الظلي بشكل شفاف.
1. حفظ المستند كـ HTML مع عرض النص الشفاف.
1. طباعة رسالة تأكيد.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML مع عرض طبقات المستند

هذه الدالة تحول ملف PDF إلى تنسيق HTML، وتحافظ على طبقات المستند عن طريق تحويل المحتوى المميز إلى طبقات منفصلة في HTML الناتج. يتيح هذا عرض العناصر ذات الطبقات (مثل التعليقات التوضيحية، الخلفيات، والطبقات الفوقية) بدقة.

1. تحميل مستند PDF باستخدام 'ap.Document'.
1. إنشاء 'HtmlSaveOptions' وتفعيل 'convert_marked_content_to_layers' للحفاظ على الطبقات.
1. حفظ المستند كـ HTML بمحتوى طبقي.
1. طباعة رسالة تأكيد.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


