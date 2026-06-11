---
title: عد مصنوعات PDF في بايثون
linktitle: عد القطع الأثرية
type: docs
weight: 40
url: /ar/python-net/counting-artifacts/
description: تعرف على كيفية فحص عناصر ترقيم الصفحات وحسابها في مستندات PDF باستخدام Python مع Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: عد القطع الأثرية في PDF باستخدام Python
Abstract: تُستخدم عناصر ترقيم الصفحات مثل العلامات المائية والخلفيات والرؤوس والتذييلات بشكل شائع في مستندات PDF لتوفير البنية والعلامة التجارية والتعريف. يوضح هذا المثال كيفية فحص هذه القطع الأثرية وحسابها برمجيًا باستخدام Aspose.PDF لـ Python عبر .NET. من خلال تصفية العناصر الموجودة على الصفحة وتجميعها حسب النوع الفرعي، يمكن للمطورين تحليل تكوين المستند بسرعة والتحقق من وجود عناصر محددة. توضح التعليمات البرمجية المتوفرة كيفية فتح ملف PDF، واستخراج عناصر ترقيم الصفحات من الصفحة الأولى، وحساب كل نوع فرعي، وإخراج النتائج، مما يوفر نهجًا عمليًا لتدقيق المستندات والتحقق من صحتها.
---

## عد القطع الأثرية من نوع معين

فحص وإحصاء آثار ترقيم الصفحات في ملف PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام Aspose.PDF لبيثون عبر.NET. تتضمن عناصر ترقيم الصفحات عناصر مثل العلامات المائية والخلفيات والرؤوس والتذييلات التي يتم تطبيقها على الصفحات لأغراض التخطيط والتعريف. عن طريق التصفية [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) الكائنات الموجودة على [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) وتجميعها حسب النوع الفرعي (`Artifact.ArtifactSubtype`)، يمكن للمطورين تحليل بنية المستند بسرعة والتحقق من وجود عناصر محددة.

لحساب العدد الإجمالي للقطع الأثرية من نوع معين (على سبيل المثال، العدد الإجمالي للعلامات المائية)، استخدم التعليمة البرمجية التالية. يقوم المثال بتصفية الصفحات [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) مجموعة (و) [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) بواسطة [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) ثم يحسب الأنواع الفرعية (`Artifact.ArtifactSubtype`).

1. افتح وثيقة PDF (انظر [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. تصفية عناصر ترقيم الصفحات باستخدام الصفحة [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) مجموعة.
1. عد القطع الأثرية حسب النوع الفرعي (`Artifact.ArtifactSubtype`).
1. نتائج الطباعة.

```python

from os import path
from collections import Counter
import sys
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## موضوعات القطع الأثرية ذات الصلة

- [العمل مع مصنوعات PDF في بايثون](/pdf/ar/python-net/artifacts/)
- [أضف علامات مائية إلى PDF في Python](/pdf/ar/python-net/add-watermarks/)
- [إضافة خلفيات PDF في بايثون](/pdf/ar/python-net/add-backgrounds/)
- [إضافة ترقيم بيتس إلى PDF في بايثون](/pdf/ar/python-net/add-bates-numbering/)
