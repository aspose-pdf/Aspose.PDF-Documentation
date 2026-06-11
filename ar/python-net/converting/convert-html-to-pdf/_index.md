---
title: تحويل HTML إلى PDF في بايثون
linktitle: تحويل HTML إلى ملف PDF
type: docs
weight: 40
url: /ar/python-net/convert-html-to-pdf/
lastmod: "2026-06-11"
description: تعرف على كيفية تحويل HTML و MHTML إلى PDF في Python باستخدام Aspose.PDF لـ Python عبر .NET، بما في ذلك إعدادات وسائط CSS والخطوط المضمنة وإخراج PDF الموسوم.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل HTML إلى PDF في بايثون باستخدام Aspose.PDF
Abstract: تشرح هذه المقالة كيفية تحويل ملفات HTML و MHTML إلى PDF باستخدام Aspose.PDF لبيثون عبر .NET. ويغطي سير العمل الأساسي من HTML إلى PDF ويوضح كيفية التحكم في العرض باستخدام أنواع الوسائط، وأولوية قاعدة صفحة CSS، والخطوط المضمنة، وإخراج الصفحة الواحدة، وإنشاء البنية المنطقية لملفات PDF ذات العلامات التي يمكن الوصول إليها.
---

## تحويل لغة بايثون من HTML إلى PDF

**Aspose.pdf لبايثون عبر .NET** يتيح لك تحويل مستندات HTML الحالية إلى PDF مع خيارات عرض مرنة. يمكنك ضبط كيفية إنشاء المخرجات لتتناسب مع متطلبات التخطيط والتصميم وإمكانية الوصول والأرشفة.

## تحويل HTML إلى PDF

يوضح مثال Python التالي سير العمل الأساسي لتحويل مستند HTML إلى PDF.

1. قم بإنشاء مثيل لـ [خيارات تحميل HTML](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) فئة.
1. قم بتهيئة ملف [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن مع ملف HTML المصدر.
1. احفظ مستند PDF الناتج عن طريق الاتصال `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## التحويلات ذات الصلة

- [تحويل ملفات PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) عندما تحتاج إلى إخراج جاهز للويب من ملفات PDF الموجودة.
- [تحويل تنسيقات الملفات الأخرى إلى PDF](/pdf/ar/python-net/convert-other-files-to-pdf/) لعمليات سير عمل تحويل EPUB وXPS والنص وPostScript.
- [تحويل الصور إلى PDF](/pdf/ar/python-net/convert-images-format-to-pdf/) عندما يكون محتوى المصدر الخاص بك قائمًا على الصور بدلاً من ترميز HTML.

{{% alert color="success" %}}
** حاول تحويل HTML إلى PDF عبر الإنترنت**

تقدم Aspose التطبيق عبر الإنترنت [«HTML إلى PDF»](https://products.aspose.app/html/en/conversion/html-to-pdf)، حيث يمكنك اختبار جودة التحويل والإخراج.

[![Aspose.PDF تحويل HTML إلى PDF باستخدام التطبيق](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## تحويل HTML إلى PDF باستخدام نوع الوسائط

يوضح هذا المثال كيفية تحويل ملف HTML إلى PDF باستخدام خيارات عرض محددة.

1. قم بإنشاء مثيل لـ [خيارات تحميل HTML ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) فئة.
1. مجموعة `html_media_type` لتطبيق قواعد CSS المخصصة لتخطيطات الشاشة أو الطباعة، مثل `HtmlMediaType.SCREEN` أو `HtmlMediaType.PRINT`.
1. قم بتحميل HTML إلى `ap.Document` باستخدام خيارات التحميل.
1. احفظ المستند كملف PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## حدد أولويات CSS `@page` القاعدة أثناء تحويل HTML إلى PDF

تستخدم بعض المستندات [ال `@page` قاعدة](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) لتخطيط الصفحة. إذا كانت هذه الأنماط تتعارض مع الإعدادات الأخرى، يمكنك التحكم في الأولوية باستخدام `is_priority_css_page_rule`.

1. قم بإنشاء مثيل لـ [خيارات تحميل HTML](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) فئة.
1. مجموعة `is_priority_css_page_rule = False` للسماح للأنماط الأخرى بالأسبقية `@page` قواعد.
1. قم بتحميل HTML إلى `ap.Document` مع الخيارات التي تم تكوينها.
1. احفظ المستند كملف PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## تحويل HTML إلى PDF باستخدام الخطوط المضمنة

يوضح هذا المثال كيفية تحويل ملف HTML إلى PDF أثناء تضمين الخطوط. إذا كنت بحاجة إلى ملف PDF الناتج للحفاظ على الطباعة الأصلية، فاضبط `is_embed_fonts` إلى `True`.

1. ابتكر `HtmlLoadOptions()` لتكوين تحويل HTML إلى PDF.
1. مجموعة `is_embed_fonts = True` لتضمين الخطوط المستخدمة في HTML مباشرة في PDF.
1. قم بتحميل HTML إلى `ap.Document` مع هذه الخيارات.
1. احفظ المستند كملف PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## عرض محتوى HTML على صفحة PDF واحدة

يوضح هذا المثال كيفية تحويل ملف HTML إلى ملف PDF من صفحة واحدة باستخدام Aspose.PDF لـ Python عبر .NET. استخدم `is_render_to_single_page` الخاصية عندما تريد عرض محتوى HTML الكامل على صفحة واحدة مستمرة.

1. قم بإنشاء مثيل لـ `HtmlLoadOptions()` لتكوين عملية التحويل.
1. تمكين `is_render_to_single_page` لعرض محتوى HTML الكامل على صفحة واحدة.
1. قم بتحميل المستند بالخيارات التي تم تكوينها في `ap.Document`.
1. احفظ النتيجة كملف PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## إنشاء بنية منطقية من علامات HTML

تحافظ البنية المنطقية، التي تسمى أيضًا PDF ذي العلامات، على التسلسل الهرمي الدلالي لـ HTML الأصلي، مثل العناوين والفقرات والقوائم. وهذا يجعل ملف PDF الناتج أكثر سهولة وقابلية للبحث ومناسبًا لعمليات سير عمل المستندات المنظمة.

من خلال تمكين البنية المنطقية أثناء التحويل، يتم تعيين HTML DOM في شجرة علامات PDF بدلاً من تقديمه كمحتوى مرئي فقط.

للوفاء بمتطلبات إمكانية الوصول، يجب أن يتضمن PDF عناصر البنية المنطقية التي تحدد ترتيب القراءة، وتوفر نصًا بديلاً لقارئات الشاشة، وتحافظ على التسلسل الهرمي للمحتوى.

> تعتمد جودة البنية المنطقية في ملف PDF الناتج بشكل مباشر على جودة ترميز HTML الأصلي. قد يؤدي HTML غير المنظم أو غير الصالح إلى وضع علامات غير كاملة أو غير دقيقة في ملف PDF المحول.

1. قم بإنشاء مثيل HTMLLoadOptions للتحكم في كيفية تحويل HTML.
1. قم بتنشيط العلامات الدلالية بحيث يحتوي PDF على عناصر منظمة.
1. افتح ملف HTML باستخدام الخيارات التي تم تكوينها.
1. احفظ ملف PDF المنظم.

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## تحويل ملفات MHTML إلى PDF

يوضح هذا المثال كيفية تحويل ملف MHT أو MHTML إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET بأبعاد صفحة محددة.

1. قم بإنشاء مثيل لـ `ap.MhtLoadOptions()` لتكوين معالجة ملفات MHTML.
1. قم بتعيين العديد من المعلمات، مثل حجم الصفحة.
1. قم بتهيئة المستند باستخدام ملف الإدخال وخيارات التحميل المهيأة.
1. احفظ المستند الناتج كملف PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
