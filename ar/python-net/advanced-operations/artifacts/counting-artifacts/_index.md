---
title: عدّ العناصر الفنية من نوع معين في بايثون عبر .NET
linktitle: عدّ العناصر الفنية
type: docs
weight: 40
url: /ar/python-net/counting-artifacts/
description: توضح هذه المقالة كيفية فحص عناصر ترقيم الصفحات في مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: عدّ العناصر الفنية في PDF باستخدام بايثون
Abstract: تُستخدم عناصر ترقيم الصفحات مثل العلامات المائية، الخلفيات، رؤوس الصفحات وتذييلات الصفحات بشكل شائع في مستندات PDF لتوفير هيكلية، العلامة التجارية، والهوية. يوضح هذا المثال كيفية فحص هذه العناصر وعدّها برمجيًا باستخدام Aspose.PDF للبايثون عبر .NET. من خلال تصفية العناصر على صفحة واحدة وتجميعها حسب النوع الفرعي، يمكن للمطورين تحليل تركيبة المستند بسرعة والتحقق من وجود عناصر معينة. يوضح الشيفرة المقدمة كيفية فتح ملف PDF، استخراج عناصر ترقيم الصفحات من الصفحة الأولى، عدّ كل نوع فرعي، وإخراج النتائج، مما يوفر نهجًا عمليًا لتدقيق المستندات والتحقق من صحتها.
---

## عدّ العناصر الفنية من نوع معين

قم بفحص وعدّ عناصر ترقيم الصفحات في PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام Aspose.PDF للبايثون عبر .NET. تشمل عناصر ترقيم الصفحات عناصر مثل العلامات المائية، الخلفيات، رؤوس الصفحات وتذييلات الصفحات التي تُطبّق على الصفحات لأغراض التخطيط والتعريف. من خلال تصفية كائنات [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) على [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) وتجميعها حسب النوع الفرعي (`Artifact.ArtifactSubtype`)، يمكن للمطورين تحليل بنية المستند بسرعة والتحقق من وجود عناصر معينة.

لحساب العدد الإجمالي للعناصر من نوع معين (على سبيل المثال، إجمالي عدد العلامات المائية)، استخدم الشيفرة التالية. يقوم المثال بتصفية مجموعة [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) الخاصة بالصفحة (وهي [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) حسب [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) ثم يحصِّي الأنواع الفرعية (`Artifact.ArtifactSubtype`).

1. افتح مستند PDF (انظر [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. صَفِّ عناصر ترقيم الصفحات باستخدام مجموعة [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) الخاصة بالصفحة.
1. عدّ العناصر حسب النوع الفرعي (`Artifact.ArtifactSubtype`).
1. طباعة النتائج.

```python

import aspose.pdf as ap

def count_pagination_artifacts(path_infile):
    # Open the PDF document
    with ap.Document(path_infile) as document:
        
        # Extract pagination artifacts from the first page
        pagination_artifacts = [
            artifact for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        # Count artifacts by subtype
        watermarks = sum(1 for artifact in pagination_artifacts 
                         if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK)
        backgrounds = sum(1 for artifact in pagination_artifacts 
                          if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND)
        headers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER)
        footers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER)

        # Display results
        print(f"Watermarks: {watermarks}")
        print(f"Backgrounds: {backgrounds}")
        print(f"Headers: {headers}")
        print(f"Footers: {footers}")
```

