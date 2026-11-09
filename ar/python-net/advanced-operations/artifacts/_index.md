---
title: عناصر PDF باستخدام Python
linktitle: العمل مع عناصر PDF
type: docs
weight: 170
url: /ar/python-net/artifacts/
description: إضافة عناصر PDF وفحصها وإزالتها، بما فيها الخلفيات والعلامات المائية ورؤوس الصفحات وتذييلاتها وترقيم Bates باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: عناصر PDF في Python
Abstract: إضافة عناصر PDF وفحصها وإزالتها، بما فيها الخلفيات والعلامات المائية ورؤوس الصفحات وتذييلاتها وترقيم Bates. تتناول الأدلة أيضًا فحص تفاصيل العلامات المائية وعدّ عناصر الترقيم باستخدام Aspose.PDF for Python via .NET.
---

تميّز عناصر PDF أجزاء الصفحة مثل الخلفيات الزخرفية والرؤوس والتذييلات المتكررة والعلامات المائية. في ملفات PDF الموسومة، يمكن للتقنيات المساعدة تجاوز هذه العناصر والتركيز على محتوى المستند ذي المعنى.

## اختيار الدليل

### إضافة العناصر

- [إضافة الخلفيات](/pdf/ar/python-net/add-backgrounds/)
- [إضافة العلامات المائية](/pdf/ar/python-net/add-watermarks/)
- [إضافة ترقيم Bates](/pdf/ar/python-net/add-bates-numbering/)
- [إضافة الرؤوس والتذييلات](/pdf/ar/python-net/artifacts-header-footer/)

### فحص العناصر

- [عدّ عناصر الترقيم](/pdf/ar/python-net/counting-artifacts/)
- [استخراج تفاصيل العلامات المائية](/pdf/ar/python-net/extract-watermarks/)

### إزالة العناصر

- [إزالة الخلفيات](/pdf/ar/python-net/remove-backgrounds/)
- [إزالة العلامات المائية](/pdf/ar/python-net/remove-watermarks/)
- [إزالة ترقيم Bates](/pdf/ar/python-net/remove-bates-numbering/)
- [إزالة الرؤوس والتذييلات](/pdf/ar/python-net/remove-headers-footers/)

## واجهة برمجة التطبيقات للعناصر

تُعيد الخاصية `artifacts` مجموعة عناصر الصفحة [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/). وتوفّر الفئة [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) الخصائص المشتركة بين الفئات المتخصصة، مثل [`BackgroundArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)، و[`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)، و[`HeaderArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)، و[`FooterArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)، و[`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/).

| المهمة | الخصائص |
| --- | --- |
| تحديد العنصر | استخدم `type` و`subtype` للتصنيفات القياسية، و`custom_type` و`custom_subtype` للأسماء المخصّصة. |
| فحص المحتوى | استخدم `text` و`image` و`lines` للنصوص والصور، و`contents` و`form` لمعاملات PDF وكائن XForm المرتبط. |
| تحديد الموضع | استخدم `rectangle` لفحص حدود العنصر. اضبط `position` لتحديد الموضع صراحةً، أو استخدم `left_margin` و`right_margin` و`top_margin` و`bottom_margin` و`artifact_horizontal_alignment` و`artifact_vertical_alignment`. يتجاوز الموضع الصريح إعدادات الهوامش والمحاذاة. |
| ضبط المظهر | استخدم `rotation` و`opacity` (من 0 إلى 1) و`text_state`. اضبط `is_background` لوضع العنصر خلف محتوى الصفحة. |
