---
title: مثال Hello World باستخدام بايثون
linktitle: مثال Hello World
type: docs
weight: 20
url: /ar/python-net/hello-world-example/
description: يوضح هذا المثال كيفية إنشاء مستند PDF بسيط يحتوي على نص Hello World باستخدام Aspose.PDF for Python عبر .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: مثال Hello World عبر بايثون
Abstract: توفر هذه المقالة مثال Hello World باستخدام مكتبة Aspose.PDF for Python عبر .NET لإنشاء مستند PDF. يوضح المثال الخطوات الأساسية لاستخدام Aspose.PDF API من خلال إنشاء PDF يحتوي على النص "Hello World!". تتضمن العملية إنشاء كائن `Document`، إضافة `Page`، إنشاء كائن `TextFragment`، ضبط خصائص النص مثل حجم الخط واللون، واستخدام `TextBuilder` لإضافة النص إلى الصفحة. يتم بعد ذلك حفظ ملف PDF الناتج باسم "HelloWorld_out.pdf". تتضمن المقالة مقتطف كود كامل بايثون يوضح هذه الخطوات، ويعمل كدليل تمهيدي لاستخدام المكتبة.
---

يوضح مثال "Hello World" أبسط صياغة وأبسط برنامج في أي لغة برمجة. يتعرف المطورون على صيغ اللغة الأساسية من خلال تعلم كيفية طباعة "Hello World" على شاشة الجهاز. لذلك، نبدأ عادةً تعارفنا مع مكتبتنا من هذا المثال.

في هذه المقالة، نقوم بإنشاء مستند PDF يحتوي على النص "Hello World!". بعد تثبيت **Aspose.PDF for Python عبر .NET** في بيئتك، يمكنك تشغيل عينة الكود أدناه لرؤية كيفية عمل Aspose.PDF API.

يتبع مقتطف الكود أدناه هذه الخطوات:

1. إنشاء كائن [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. إضافة [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى كائن المستند
1. إنشاء كائن [مقتطف نص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. ضبط ألوان النص
1. إنشاء مُنشئ النص
1. إضافة [مقتطف نص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) إلى الصفحة
1. حفظ المستند الناتج باستخدام [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)

مقتطف الكود التالي هو برنامج "Hello World" يوضح وظائف Aspose.PDF for Python عبر .NET API.

```python

from datetime import timedelta
import aspose.pdf as ap

def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
