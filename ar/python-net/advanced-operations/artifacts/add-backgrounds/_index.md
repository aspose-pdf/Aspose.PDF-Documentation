---
title: إضافة خلفيات PDF في بايثون
linktitle: إضافة خلفيات
type: docs
weight: 20
url: /ar/python-net/add-backgrounds/
description: تعلم كيفية إضافة صورة خلفية إلى صفحات PDF في بايثون باستخدام فئة BackgroundArtifact في Aspose.PDF لبيثون عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة خلفية إلى PDF باستخدام Python
Abstract: تتناول هذه المقالة استخدام صور الخلفية في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. إنه يسلط الضوء على القدرة على إضافة علامات مائية أو تصميمات دقيقة للمستندات من خلال استخدام فئة «BackgroundArtifact»، والتي تسمح بدمج صور الخلفية في كائنات الصفحات الفردية. تقدم المقالة مثالاً عمليًا على التعليمات البرمجية يوضح كيفية تنفيذ هذه الميزة. تتضمن العملية إنشاء مستند PDF جديد، وإضافة صفحة، وإنشاء كائن «BackgroundArtifact»، وإعداد صورة خلفية، وإلحاق قطعة الخلفية بمجموعة القطع الأثرية للصفحة. أخيرًا، يتم حفظ المستند المعدل كملف PDF. تسمح هذه التقنية بعرض مرئي محسن لمستندات PDF.
---

## إضافة صورة خلفية إلى PDF

يمكن استخدام صور الخلفية لإضافة علامة مائية أو أي تصميم دقيق آخر إلى المستندات. في Aspose.PDF لـ Python عبر .NET، كل مستند PDF عبارة عن مجموعة من الصفحات وتحتوي كل صفحة على مجموعة من القطع الأثرية. ال [قطعة أثرية في الخلفية](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) يمكن استخدام الفئة لإضافة صورة خلفية إلى كائن صفحة.

هذا الأسلوب مفيد عندما تحتاج إلى وضع صورة زخرفية خلف محتوى PDF الرئيسي دون تحويلها إلى نص مستند يمكن البحث فيه.

يوضح مقتطف الشفرة التالي كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact مع Python.

1. قم بتحميل وثيقة PDF.
1. قم بإنشاء قطعة أثرية في الخلفية.
1. قم بتحميل ملف الصورة.
1. أرفق القطعة الأثرية بصفحة.
1. احفظ المستند المحدث.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## أضف صورة خلفية ذات عتامة إلى PDF

أضف صورة خلفية شبه شفافة إلى صفحة PDF باستخدام Aspose.PDF لـ Python.

من خلال تطبيق التعتيم، تصبح صورة الخلفية شفافة جزئيًا، مما يسمح لمحتوى الصفحة الأصلية (النص والصور وما إلى ذلك) بالبقاء مرئيًا بوضوح. هذا مفيد بشكل خاص لـ:

- علامات مائية
- تراكبات العلامات التجارية
- تحسينات التصميم الدقيقة

تتم إضافة الخلفية كقطعة أثرية، مما يضمن بقائها خلف كل محتوى الصفحة.

1. قم بتحميل وثيقة PDF.
1. قم بإنشاء قطعة أثرية في الخلفية.
1. قم بتحميل ملف الصورة.
1. قم بتعيين مستوى العتامة.
1. أرفق القطعة الأثرية بصفحة.
1. احفظ المستند المحدث.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## إضافة لون خلفية إلى PDF

قم بتطبيق لون خلفية صلب على صفحة PDF باستخدام Aspose.PDF لـ Python.

1. قم بتحميل وثيقة PDF.
1. قم بإنشاء قطعة أثرية في الخلفية.
1. قم بتعيين لون الخلفية.
1. أرفق القطعة الأثرية بصفحة.
1. احفظ المستند المحدث.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## إزالة الخلفية من PDF

قم بإزالة عناصر الخلفية من صفحة PDF باستخدام Aspose.PDF لـ Python.
غالبًا ما يتم تخزين الخلفيات في ملفات PDF كعناصر أثرية، وهذه الطريقة تحدد وتزيل بشكل انتقائي فقط تلك القطع الأثرية المصنفة كعناصر خلفية.

1. قم بتحميل وثيقة PDF.
1. عناصر صفحة الوصول.
1. تصفية القطع الأثرية في الخلفية.
1. اجمع عناصر الخلفية.
1. احذف عناصر الخلفية.
1. احفظ المستند المحدث.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## موضوعات القطع الأثرية ذات الصلة

- [العمل مع مصنوعات PDF في بايثون](/pdf/ar/python-net/artifacts/)
- [أضف علامات مائية إلى PDF في Python](/pdf/ar/python-net/add-watermarks/)
- [إضافة ترقيم بيتس إلى PDF في بايثون](/pdf/ar/python-net/add-bates-numbering/)
- [عد أنواع القطع الأثرية في ملفات PDF](/pdf/ar/python-net/counting-artifacts/)