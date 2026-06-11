---
title: تحويل PDF إلى HTML في بايثون
linktitle: تحويل PDF إلى صيغة HTML
type: docs
weight: 50
url: /ar/python-net/convert-pdf-to-html/
lastmod: "2026-06-11"
description: تعرف على كيفية تحويل PDF إلى HTML في Python باستخدام Aspose.PDF لـ Python عبر .NET، بما في ذلك الإخراج متعدد الصفحات والصور الخارجية ومعالجة SVG وعرض HTML متعدد الطبقات.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى HTML في بايثون
Abstract: توفر هذه المقالة دليلًا شاملاً حول تحويل ملفات PDF إلى HTML باستخدام Python، وتحديدًا من خلال Aspose.PDF لـ Python عبر مكتبة.NET. ويحدد الخطوات اللازمة لتحقيق هذا التحويل برمجيًا، ويسلط الضوء على إنشاء كائن «المستند» من ملف PDF المصدر واستخدام «HTMLSaveOptions» لحفظ المستند بتنسيق HTML. تتضمن المقالة مقتطفًا موجزًا من شفرة Python يوضح عملية التحويل. بالإضافة إلى ذلك، فإنه يقدم أداة عبر الإنترنت، وهي تطبيق Aspose.PDF «PDF to HTML»، للمستخدمين لاستكشاف وظائف وجودة التحويل. تم تصميم المقالة لتلبية مختلف الموضوعات ذات الصلة، مما يضمن فهمًا شاملاً لاستخدام Python لتحويل PDF إلى HTML.
---

## تحويل ملفات PDF إلى HTML

**Aspose.pdf لـ Python عبر .NET** يوفر العديد من الميزات لتحويل تنسيقات الملفات المختلفة إلى مستندات PDF وتحويل ملفات PDF إلى تنسيقات إخراج مختلفة. تتناول هذه المقالة كيفية تحويل ملف PDF إلى <abbr title="HyperText Markup Language">أتش تي أم أل</abbr>. يمكنك استخدام سطرين فقط من كود Python لتحويل PDF إلى HTML. قد تحتاج إلى تحويل PDF إلى HTML إذا كنت ترغب في إنشاء موقع ويب أو إضافة محتوى إلى منتدى عبر الإنترنت. طريقة واحدة لتحويل PDF إلى HTML هي استخدام Python برمجيًا.

{{% alert color="success" %}}
** حاول تحويل PDF إلى HTML عبر الإنترنت**

Aspose.PDF لبيثون يقدم لك التطبيق عبر الإنترنت [«PDF إلى HTML»](https://products.aspose.app/pdf/conversion/pdf-to-html)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF تحويل ملفات PDF إلى HTML مع التطبيق](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

الخطوات: تحويل PDF إلى HTML في بايثون

1. قم بإنشاء مثيل لـ [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن مع مستند PDF المصدر.
1. احفظه إلى [خيارات حفظ HTML](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) عن طريق الاتصال [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## التحويلات ذات الصلة

- [تحويل HTML إلى PDF](/pdf/ar/python-net/convert-html-to-pdf/) عندما تحتاج إلى سير العمل العكسي من الويب إلى المستند.
- [تحويل ملفات PDF إلى وورد](/pdf/ar/python-net/convert-pdf-to-word/) إذا كان إخراج المستند القابل للتحرير أكثر فائدة من HTML.
- [تحويل PDF إلى تنسيقات صور](/pdf/ar/python-net/convert-pdf-to-images-format/) لسيناريوهات تصدير البيانات النقطية.

### تحويل PDF إلى HTML مع حفظ الصور في المجلد المحدد

تقوم هذه الوظيفة بتحويل ملف PDF إلى تنسيق HTML باستخدام Aspose.PDF لبيثون عبر .NET. يتم تخزين جميع الصور المستخرجة في مجلد محدد بدلاً من تضمينها في ملف HTML.

1. قم بتكوين خيارات حفظ HTML.
1. احفظ بصيغة HTML مع صور خارجية.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_images(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "images")
    save_options.special_folder_for_all_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML متعدد الصفحات

تقوم هذه الوظيفة بتحويل ملف PDF إلى HTML متعدد الصفحات، حيث يتم تصدير كل صفحة PDF كملف HTML منفصل. هذا يجعل الإخراج أسهل للتنقل ويقلل من وقت التحميل لملفات PDF الكبيرة.

1. قم بتحميل ملف PDF المصدر باستخدام «AP.document».
1. قم بإنشاء «خيارات حفظ HTML» وتعيين «split_into_pages».
1. احفظ المستند بصيغة HTML مع تقسيم الصفحات إلى ملفات منفصلة.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_multi_page(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML مع حفظ صور SVG في مجلد محدد

تقوم هذه الوظيفة بتحويل PDF إلى تنسيق HTML أثناء تخزين جميع الصور كملفات SVG في مجلد محدد، بدلاً من تضمينها مباشرة في HTML.

1. قم بتحميل ملف PDF المصدر باستخدام «AP.document».
1. قم بإنشاء «HTMLSaveOptions» وقم بتعيين «special_folder_for_svg_images» إلى المجلد الهدف.
1. احفظ المستند بصيغة HTML مع صور SVG خارجية.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML وحفظ صور SVG المضغوطة

يقوم هذا المقتطف بتحويل PDF إلى تنسيق HTML، وتخزين جميع الصور كملفات SVG في مجلد محدد وضغطها لتقليل حجم الملف.

1. قم بتحميل مستند PDF باستخدام «AP.document».
1. قم بإنشاء «خيارات حفظ HTML» و:
   - قم بتعيين 'special_folder_for_svg_images' لتخزين صور SVG خارجيًا.
   - قم بتمكين 'compress_svg_graphics_if_any' لضغط صور SVG.
1. احفظ المستند بصيغة HTML مع صور SVG خارجية مضغوطة.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_compress_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    save_options.compress_svg_graphics_if_any = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML مع التحكم في الصور النقطية المضمنة

يقوم هذا المقتطف بتحويل PDF إلى تنسيق HTML، مع تضمين الصور النقطية كخلفيات لصفحات PNG. يحافظ هذا الأسلوب على جودة الصورة وتخطيط الصفحة داخل HTML.

1. قم بتحميل مستند PDF باستخدام «AP.document».
1. قم بإنشاء «خيارات حفظ HTML» و «تعيين وضع حفظ الصور النقطية» إلى «AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND».
1. احفظ المستند بصيغة HTML مع الصور النقطية المضمنة.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_PNG_background(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى صفحة HTML لمحتوى الجسم فقط

تعمل هذه الوظيفة على تحويل ملف PDF إلى تنسيق HTML، وإنشاء محتوى «للجسم فقط» بدون علامات «html» أو «head» إضافية، وتقسيم الإخراج إلى صفحات منفصلة.

1. قم بتحميل مستند PDF باستخدام «AP.document».
1. قم بإنشاء «HTMLSaveOptions» وقم بتكوين:
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT» لإنشاء المحتوى «الأساسي» فقط.
   - 'split_into_pages 'لإنشاء ملفات HTML منفصلة لكل صفحة PDF.
1. احفظ المستند بصيغة HTML مع الخيارات المحددة.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_body_content(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.html_markup_generation_mode = (
        ap.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    )
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML مع عرض نص شفاف

تقوم هذه الوظيفة بتحويل PDF إلى تنسيق HTML، مما يجعل كل النص شفافًا، بما في ذلك النصوص المظللة، والتي تحافظ على الدقة المرئية مع السماح بالتصميم المرن في HTML الناتج.

1. قم بتحميل مستند PDF باستخدام «AP.document».
1. قم بإنشاء «HTMLSaveOptions» وقم بتكوين:
    - «save_transparent_texts» لعرض النص العادي على أنه شفاف.
    - 'save_shadowed_texts_as_transparent_texts' لجعل النص المظلل شفافًا.
1. احفظ المستند بصيغة HTML مع عرض نص شفاف.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_transparent_text_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى HTML مع عرض طبقات المستند

تقوم هذه الوظيفة بتحويل PDF إلى تنسيق HTML، مع الحفاظ على طبقات المستند عن طريق تحويل المحتوى المحدد إلى طبقات منفصلة في HTML الناتج. يسمح هذا بعرض العناصر ذات الطبقات (مثل التعليقات التوضيحية والخلفيات والتراكبات) بدقة.

1. قم بتحميل مستند PDF باستخدام «AP.document».
1. قم بإنشاء «HTMLSaveOptions» وتمكين «convert_marked_content_to_layers» للحفاظ على الطبقات.
1. احفظ المستند بصيغة HTML مع محتوى متعدد الطبقات.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_document_layers_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

