---
title: إضافة قطعة ترقيم Bates في بايثون عبر .NET
linktitle: إضافة ترقيم Bates
type: docs
weight: 10
url: /ar/python-net/add-bates-numbering/
description: Aspose.PDF for Python via .NET يسمح لك بإضافة ترقيم Bates إلى PDF.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة ترقيم Bates عبر بايثون
Abstract: يُعد ترقيم Bates ميزة حاسمة في سير عمل المستندات القانونية والطبية والتجارية، حيث يضمن أن يحصل كل صفحة في مجموعة على معرف فريد ومتسلسل لتسهيل الإشارة الموثوقة. يوضح هذا المقال كيف يبسط Aspose.PDF for Python عبر .NET أتمتة ترقيم Bates من خلال واجهته البرمجية المرنة. باستخدام فئة BatesNArtifact، يمكن للمطورين تكوين سلوك الترقيم — بما في ذلك عدد الأرقام، والبادئات، واللاحقات، والمحاذاة، والهوامش — وتطبيقه برمجياً على المستندات بأكملها. تُعرض نهج متعددة، بدءًا من تطبيق القطعة مباشرةً إلى التكوين القائم على التفويض، مما يوفر تحكمًا ثابتًا وديناميكيًا. بالإضافة إلى ذلك، تدعم الواجهة البرمجية إزالة ترقيم Bates بالكامل باستدعاء طريقة واحدة، مما يمكّن من إدارة دورة حياة قطع الترقيم بالكامل. توضح أمثلة الشيفرة الواضحة خطوة بخطوة كيفية إضافة وتخصيص وحذف ترقيم Bates، مما يجعل هذا الدليل مصدرًا عمليًا للمطورين الساعين لتبسيط سير عمل معالجة المستندات.
---

يُستخدم ترقيم Bates على نطاق واسع في سير العمل القانوني والطبي والتجاري لتعيين معرفات فريدة ومتسلسلة للصفحات داخل مجموعة المستندات. يوفر Aspose.PDF for Python عبر .NET واجهة برمجة تطبيقات بسيطة ومرنة لأتمتة هذه العملية، مما يتيح لك تطبيق أرقام Bates موحدة برمجيًا على أي ملف PDF.

باستخدام الفئة [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)، يمكن للمطورين تخصيص سلوك الترقيم بالكامل — بما في ذلك رقم البداية، عدد الأرقام، البادئات واللاحقات، المحاذاة، والهوامش. بمجرد تكوينه، يمكن تطبيق القطعة على الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) عبر طريقة `add_bates_numbering` في الـ[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) أو إضافتها كجزء من قائمة كائنات الـ[`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/). كما يدعم Aspose.PDF نمط تكوين قائم على التفويض، مما يسمح بالتحكم الديناميكي في إعدادات القطعة أثناء وقت التشغيل.

بالإضافة إلى إنشاء أرقام Bates، توفر الواجهة البرمجية طريقة سهلة لإزالتها باستخدام `delete_bates_numbering`، مما يمنح مرونة كاملة في سير عمل معالجة المستندات.

يظهر هذا المقال عدة طرق لإضافة وإزالة ترقيم Bates في ملف PDF باستخدام Aspose.PDF for Python عبر .NET، مع أمثلة واضحة لتكوين القطعة وتطبيقها وإزالتها.

## إضافة قطعة ترقيم Bates

يوضح هذا المثال كيفية إضافة ترقيم Bates برمجيًا إلى مستند PDF باستخدام Aspose.PDF for Python عبر .NET. من خلال تكوين [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) بالإعدادات المطلوبة وتطبيقه على صفحات المستند، يمكنك أتمتة عملية إضافة معرفات موحدة لكل صفحة.

لإضافة قطعة ترقيم Bates إلى الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)، استدعِ طريقة الامتداد `AddBatesNumbering(BatesNArtifact)` على الـ[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)، مع تمرير نسخة من الـ[`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) كمعامل:

```python

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

أو، يمكنك تمرير مجموعة من كائنات [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/):

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

إضافة قطعة ترقيم Bates باستخدام تفويض الإجراء:

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## حذف ترقيم Bates

لإزالة ترقيم Bates من الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)، استخدم طريقة `delete_bates_numbering()` على الـ[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```
