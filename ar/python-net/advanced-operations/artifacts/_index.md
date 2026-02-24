---
title: العمل مع العناصر في بايثون عبر .NET
linktitle: العمل مع العناصر
type: docs
weight: 170
url: /ar/python-net/artifacts/
description: Aspose.PDF for Python via .NET يتيح لك إضافة صورة خلفية إلى صفحات PDF، والحصول على كل علامة مائية باستخدام فئة Artifact.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة العناصر إلى PDF باستخدام بايثون
Abstract: هذا المقال يستكشف مفهوم وتطبيق العناصر في مستندات PDF، مع التركيز بشكل خاص على دورها في تحسين إمكانية الوصول والأداء. العناصر هي عناصر غير محتوى، مثل المكونات الزخرفية أو مكونات التخطيط، التي لا تنقل معنى المستند. يبرز المقال استخدام فئة `Artifact` في مكتبة Aspose.PDF for Python via .NET لإدارة هذه العناصر، مقدماً خصائص مثل `custom_type` و`contents` و`opacity` للتخصيص التفصيلي. كما يقدم الفئات المرتبطة للتعامل مع أنواع معينة من العناصر. توضح الأمثلة العملية عمليات مثل استرجاع العلامات المائية، إضافة صور خلفية، عد أنواع العناصر، وتطبيق ترقيم Bates.
---

العناصر في PDF هي كائنات رسومية أو عناصر أخرى لا تشكل جزءاً من المحتوى الفعلي للمستند. عادةً ما تُستخدم للزينة أو التخطيط أو الخلفية. تشمل أمثلة العناصر رؤوس الصفحات، تذييلات الصفحات، الفواصل، أو الصور التي لا تنقل أي معنى.

الغرض من العناصر في PDF هو السماح بالتمييز بين المحتوى والعناصر غير المحتوى. هذا مهم لإمكانية الوصول، حيث يمكن لقراء الشاشة وغيرها من تقنيات المساعدة تجاهل العناصر والتركيز على المحتوى ذي الصلة. يمكن للعناصر أيضاً تحسين أداء وجودة مستندات PDF، حيث يمكن حذفها من الطباعة أو البحث أو النسخ.

لإنشاء عنصر كعنصر في PDF، تحتاج إلى استخدام فئة [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/).
تحتوي على الخصائص المفيدة التالية:

- **custom_type** - يحصل على اسم نوع العنصر. قد يُستخدم إذا كان نوع العنصر غير قياسي.
- **custom_subtype** - يحصل على اسم النوع الفرعي للعنصر. قد يُستخدم إذا كان النوع الفرعي للعنصر غير قياسي.
- **type** - يحصل على نوع العنصر.
- **subtype** - يحصل على النوع الفرعي للعنصر. إذا كان للعنصر نوع فرعي غير قياسي، يمكن قراءة اسم النوع الفرعي عبر CustomSubtype.
- **contents** - يحصل على مجموعة من المشغلات الداخلية للعنصر.
- **form** - يحصل على XForm للعنصر (إذا تم استخدام XForm).
- **rectangle** - يحصل على المستطيل الخاص بالعنصر.
- **position** - يحصل على أو يحدد موضع العنصر. إذا تم تحديد هذه الخاصية، يتم تجاهل الهوامش والمحاذاة.
- **right_margin** - الهامش الأيمن للعنصر. إذا تم تحديد الموضع صراحةً (في خاصية Position) يتم تجاهل هذه القيمة.
- **left_margin** - الهامش الأيسر للعنصر. إذا تم تحديد الموضع صراحةً (في خاصية Position) يتم تجاهل هذه القيمة.
- **top_margin** - الهامش العلوي للعنصر. إذا تم تحديد الموضع صراحةً (في خاصية Position) يتم تجاهل هذه القيمة.
- **bottom_margin** - الهامش السفلي للعنصر. إذا تم تحديد الموضع صراحةً (في خاصية Position) يتم تجاهل هذه القيمة.
- **artifact_horizontal_alignment** - المحاذاة الأفقية للعنصر. إذا تم تحديد الموضع صراحةً (في خاصية Position) يتم تجاهل هذه القيمة.
- **artifact_vertical_alignment** - المحاذاة العمودية للعنصر. إذا تم تحديد الموضع صراحةً (في خاصية Position) يتم تجاهل هذه القيمة.
- **rotation** - يحصل على أو يحدد زاوية دوران العنصر.
- **text** - يحصل على نص العنصر.
- **image** - يحصل على صورة العنصر (إذا كانت موجودة).
- **opacity** - يحصل على أو يحدد شفافية العنصر. القيم الممكنة في النطاق 0..1.
- **lines** - أسطر نص العنصر متعدد السطر.
- **text_state** - حالة النص لنص العنصر.
- **is_background** - إذا كان صحيحاً، يتم وضع العنصر خلف محتويات الصفحة.

الفئات التالية قد تكون مفيدة أيضاً للعمل مع العناصر:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [ترقيم Bates](https://reference.aspose.com/pdf/python-net/aspose.pdf/)

يرجى مراجعة الأقسام التالية من المقال:

- [إضافة خلفيات](/pdf/python-net/add-backgrounds/) - إضافة صورة خلفية إلى ملف PDF الخاص بك باستخدام بايثون.
- [إضافة ترقيم Bates](/pdf/python-net/add-bates-numbering/) - إضافة ترقيم Bates إلى PDF.
- [إضافة علامة مائية](/pdf/python-net/add-watermarks/) - كيفية إضافة علامة مائية إلى PDF باستخدام بايثون.
- [عد العناصر](/pdf/python-net/counting-artifacts/) - عد العناصر في PDF باستخدام بايثون.

