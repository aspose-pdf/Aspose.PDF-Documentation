---
title: مثال على هالو وورلد باستخدام بايثون
linktitle: مثال مرحبا بالعالم
type: docs
weight: 20
url: /ar/python-net/hello-world-example/
description: يوضح هذا النموذج كيفية إنشاء مستند PDF بسيط بنص Hello World باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: مثال مرحبا بالعالم عبر بايثون
Abstract: تقدم هذه المقالة مثالاً على Hello World باستخدام Aspose.PDF لـ Python عبر مكتبة.NET لإنشاء مستند PDF. يوضح المثال الخطوات الأساسية لاستخدام واجهة برمجة تطبيقات Aspose.PDF عن طريق إنشاء ملف PDF بالنص «Hello World!». تتضمن العملية إنشاء كائن «مستند»، وإضافة «صفحة»، وإنشاء كائن «TextFragment»، وتعيين خصائص النص مثل حجم الخط ولونه، واستخدام «TextBuilder» لإضافة النص إلى الصفحة. ثم يتم حفظ ملف PDF الناتج باسم "HelloWorld_out.pdf». تتضمن المقالة مقتطفًا كاملاً من شفرة Python يوضح هذه الخطوات، ويعمل كدليل تمهيدي لاستخدام المكتبة.
---

يعرض مثال «Hello World» أبسط صيغة وأبسط برنامج في أي لغة برمجة معينة. يتم تعريف المطورين بصيغة لغة البرمجة الأساسية من خلال تعلم كيفية طباعة «Hello World» على شاشة الجهاز. لذلك، سنبدأ تقليديًا بالتعرف على مكتبتنا منها.

في هذه المقالة، نقوم بإنشاء مستند PDF يحتوي على نص «Hello World!». بعد تثبيت **Aspose.pdf لـ Python عبر .NET** في بيئتك، يمكنك تنفيذ نموذج التعليمات البرمجية أدناه لمعرفة كيفية عمل واجهة برمجة تطبيقات Aspose.PDF.

يتبع مقتطف الشفرة أدناه الخطوات التالية:

1. قم بإنشاء مثيل [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) موضوع
1. إضافة [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى كائن المستند
1. قم بإنشاء [جزء من النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) موضوع
1. تعيين ألوان النص
1. قم بإنشاء أداة إنشاء نصوص
1. أضِف [جزء من النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) إلى الصفحة
1. [حفظ المستند ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) وثيقة PDF الناتجة

مقتطف الشفرة التالي هو برنامج «Hello World» الذي يوضح وظائف Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات .NET.

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
    textFragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
