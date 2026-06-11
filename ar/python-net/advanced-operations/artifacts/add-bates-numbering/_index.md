---
title: إضافة ترقيم بيتس إلى PDF في بايثون
linktitle: إضافة ترقيم بيتس
type: docs
weight: 10
url: /ar/python-net/add-bates-numbering/
description: تعرف على كيفية إضافة وإزالة ترقيم Bates في مستندات PDF باستخدام Python مع Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة ترقيم بيتس عبر بايثون
Abstract: يعد ترقيم بيتس ميزة مهمة في عمليات سير عمل المستندات القانونية والطبية والتجارية، مما يضمن حصول كل صفحة في المجموعة على معرف فريد ومتسلسل للرجوع إليها بشكل موثوق. توضح هذه المقالة كيف يعمل Aspose.PDF لـ Python عبر .NET على تبسيط التشغيل الآلي لترقيم Bates من خلال واجهة برمجة التطبيقات المرنة الخاصة به. باستخدام فئة BateSnArtifact، يمكن للمطورين تكوين سلوك الترقيم - بما في ذلك عدد الأرقام والبادئات واللواحق والمحاذاة والهوامش - وتطبيقه برمجيًا عبر المستندات بأكملها. يتم تقديم أساليب متعددة، من تطبيق الأداة المباشرة إلى التكوين القائم على المندوبين، مما يوفر التحكم الثابت والديناميكي. بالإضافة إلى ذلك، تدعم واجهة برمجة التطبيقات الإزالة الكاملة لأرقام Bates من خلال استدعاء أحادي الأسلوب، مما يتيح إدارة دورة الحياة الكاملة لأشكال ترقيم الصفحات. توضح أمثلة التعليمات البرمجية الواضحة خطوة بخطوة كيفية إضافة ترقيم Bates وتخصيصه وحذفه، مما يجعل هذا الدليل موردًا عمليًا للمطورين الذين يسعون إلى تبسيط عمليات سير عمل معالجة المستندات.
---

يُستخدم ترقيم بيتس على نطاق واسع في عمليات سير العمل القانونية والطبية والتجارية لتعيين معرفات فريدة ومتسلسلة للصفحات داخل مجموعة المستندات. يقدم Aspose.PDF لـ Python عبر .NET واجهة برمجة تطبيقات بسيطة ومرنة لأتمتة هذه العملية، مما يتيح لك تطبيق أرقام Bates القياسية برمجيًا عبر أي ملف PDF.

استخدام [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) الفئة، يمكن للمطورين تخصيص سلوك الترقيم بالكامل - بما في ذلك رقم البداية وعدد الأرقام والبادئات واللواحق والمحاذاة والهوامش. بمجرد التهيئة، يمكن تطبيق الأداة على [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) من خلال `add_bates_numbering` الطريقة على [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) أو تمت إضافتها كجزء من قائمة [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) الكائنات. يدعم Aspose.PDF أيضًا نمط التكوين القائم على المندوبين، مما يسمح بالتحكم الديناميكي في إعدادات القطع الأثرية في وقت التشغيل.

بالإضافة إلى إنشاء أرقام Bates، توفر واجهة برمجة التطبيقات طريقة سهلة لإزالتها باستخدام `delete_bates_numbering`، مما يوفر مرونة كاملة في عمليات سير عمل معالجة المستندات.

تعرض هذه المقالة طرقًا متعددة لإضافة وإزالة ترقيم Bates في ملف PDF باستخدام Aspose.PDF لـ Python عبر .NET، مع أمثلة واضحة لتكوين القطع الأثرية وتطبيقها وإزالتها.

## إضافة أداة ترقيم بيتس

يوضح هذا المثال كيفية إضافة ترقيم Bates برمجيًا إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET. من خلال تكوين [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) باستخدام الإعدادات المطلوبة وتطبيقها على صفحات المستند، يمكنك أتمتة عملية إضافة معرفات موحدة إلى كل صفحة.

لإضافة قطعة أثرية بترقيم بيتس إلى [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)، اتصل بـ `AddBatesNumbering(BatesNArtifact)` طريقة التمديد على [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)، اجتياز [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) المثيل كمعامل:

```python
import sys
from os import path
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## إضافة ترقيم بيتس باستخدام مصنوعات ترقيم الصفحات

أضف ترقيم بيتس إلى ملف PDF باستخدام مجموعة عناصر ترقيم الصفحات في Aspose.PDF لـ Python:

1. قم بتحميل وثيقة PDF.
1. أدخل صفحات إضافية إذا لزم الأمر قبل تطبيق الترقيم.
1. قم بإنشاء قطعة أثرية من بيتس.
1. قم بتكوين خصائص الأداة.
1. أضف القطعة الأثرية إلى مجموعة ترقيم الصفحات.
1. قم بتطبيق ترقيم الصفحات على الصفحات.
1. احفظ المستند المحدث.

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## حذف ترقيم بيتس

لإزالة ترقيم بيتس من [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)، استخدم `delete_bates_numbering()` الطريقة على [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## موضوعات القطع الأثرية ذات الصلة

- [العمل مع مصنوعات PDF في بايثون](/pdf/ar/python-net/artifacts/)
- [أضف علامات مائية إلى PDF في Python](/pdf/ar/python-net/add-watermarks/)
- [إضافة خلفيات PDF في بايثون](/pdf/ar/python-net/add-backgrounds/)
- [عد أنواع القطع الأثرية في ملفات PDF](/pdf/ar/python-net/counting-artifacts/)