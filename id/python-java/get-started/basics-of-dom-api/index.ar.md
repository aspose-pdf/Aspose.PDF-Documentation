---
title: أساسيات واجهة برمجة تطبيقات Aspose.PDF DOM
linktitle: أساسيات واجهة برمجة التطبيقات DOM
type: docs
weight: 110
url: id/python-java/basics-of-dom-api/
description: يستخدم Aspose.PDF لـ Java أيضًا فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات. هنا يمكنك قراءة وصف هذا الهيكل.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مقدمة إلى واجهة برمجة التطبيقات DOM

نموذج كائن المستند (DOM) هو شكل من أشكال تمثيل المستندات المهيكلة كنموذج موجه للكائنات. DOM هو المعيار الرسمي لاتحاد الشبكة العالمية (W3C) لتمثيل المستندات المهيكلة بطريقة محايدة للمنصة واللغة.

بعبارات بسيطة، DOM هو شجرة من الكائنات التي تمثل هيكل مستند ما.
 Aspose.PDF for Java يستخدم أيضًا فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات. ومع ذلك، يتم التلاعب بجوانب DOM (مثل عناصره) داخل بناء الجملة للغة البرمجة المستخدمة. يتم تحديد الواجهة العامة لـ DOM في واجهة برمجة التطبيقات الخاصة به (API).

### مقدمة إلى مستند PDF

تنسيق المستندات المحمولة (PDF) هو معيار مفتوح لتبادل المستندات. مستند PDF هو مزيج من النص والبيانات الثنائية. إذا قمت بفتحه في محرر نصوص، ستشاهد الكائنات الخام التي تحدد هيكل ومحتويات المستند.

الهيكل المنطقي لملف PDF هرمي ويحدد التسلسل الذي ترسم به تطبيقات العرض صفحات المستند ومحتوياتها. يتكون PDF من أربعة مكونات: الكائنات، هيكل الملف، هيكل المستند وتدفقات المحتوى.

### هيكل مستند PDF

نظرًا لأن هيكل ملف PDF هرمي، فإن Aspose.PDF for Java يصل أيضًا إلى العناصر بنفس الطريقة. يظهر التسلسل الهرمي التالي كيف يتم بناء مستند PDF منطقياً وكيف يقوم Aspose.PDF لـ Java DOM API بتكوينه.

![هيكل مستند PDF](../images/structure.png)

### الوصول إلى عناصر مستند PDF

كائن المستند موجود في المستوى الجذري لنموذج الكائنات. يتيح لك Aspose.PDF لـ Java DOM API إنشاء كائن مستند ثم الوصول إلى جميع الكائنات الأخرى في التسلسل الهرمي. يمكنك إما الوصول إلى أي من المجموعات مثل الصفحات أو العنصر الفردي مثل الصفحة وما إلى ذلك. يوفر DOM API نقاط دخول وخروج فردية للتلاعب بمستند PDF كما هو موضح أدناه:

- فتح مستند PDF
- الوصول إلى هيكل مستند PDF بأسلوب DOM
- تحديث البيانات في مستند PDF
- التحقق من صحة مستند PDF
- تصدير مستند PDF إلى تنسيقات مختلفة
- وأخيرًا، حفظ مستند PDF المحدث

## كيفية استخدام Aspose.PDF الجديد لـ Java API

سيشرح هذا الموضوع API الجديد لـ Aspose.PDF لـ Java ويوجهك للبدء بسرعة وسهولة. يرجى ملاحظة أن التفاصيل المتعلقة باستخدام الميزات الخاصة ليست جزءًا من هذه المقالة.

يتكون Aspose.PDF for Java من جزئين:

- Aspose.PDF for Java DOM API
- Aspose.PDF.Facades

ستجد تفاصيل كل من هذه المجالات أدناه.

### Aspose.PDF for Java DOM API

يتوافق Aspose.PDF for Java DOM API الجديد مع بنية مستند PDF، مما يساعدك على العمل مع مستندات PDF ليس فقط على مستوى الملف والمستند، ولكن أيضًا على مستوى الكائن. لقد وفرنا مزيدًا من المرونة للمطورين للوصول إلى جميع عناصر وكائنات مستند PDF. باستخدام فئات Aspose.PDF DOM API، يمكنك الحصول على الوصول البرمجي إلى عناصر المستند والتنسيق. يتألف هذا DOM API الجديد من عدة مساحات أسماء كما هو موضح أدناه:

### com.aspose.pdf

يوفر مساحة الاسم هذه فئة Document التي تتيح لك فتح وحفظ مستند PDF. The License class is also a part of this namespace. It also provides classes related to PDF pages, attachments, and bookmarks like com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, and com.aspose.pdf.OutlineCollection etc.

#### com.aspose.pdf.text

يوفر مساحة الاسم هذه الفئات التي تساعدك في العمل مع النص وجوانبه المختلفة، على سبيل المثال com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment و com.aspose.pdf.TextSegmentCollection إلخ.

#### com.aspose.pdf.TextOptions

يوفر مساحة الاسم هذه الفئات التي تتيح لك تحديد خيارات مختلفة للبحث أو تحرير أو استبدال النص، على سبيل المثال com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, و com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

هذه المساحة الاسمية تحتوي على فئات تساعدك في العمل مع الميزات التفاعلية لوثيقة PDF، على سبيل المثال، العمل مع الوثيقة وإجراءات أخرى. هذه المساحة الاسمية تحتوي على فئات مثل com.aspose.pdf.GoToAction، com.aspose.pdf.GoToRemoteAction وcom.aspose.pdf.GoToURIAction وغيرها.

#### com.aspose.pdf.Annotation

التعليقات التوضيحية هي جزء من الميزات التفاعلية لوثيقة PDF. لقد خصصنا مساحة اسمية للتعليقات التوضيحية. هذه المساحة الاسمية تحتوي على فئات تساعدك في العمل مع التعليقات التوضيحية، على سبيل المثال، com.aspose.pdf.Annotation، com.aspose.pdf.AnnotationCollection، com.aspose.pdf.CircleAnnotation وcom.aspose.pdf.LinkAnnotation وغيرها.

#### com.aspose.pdf.Form

هذه المساحة الاسمية تحتوي على فئات تساعدك في العمل مع نماذج PDF وحقول النماذج، على سبيل المثال، com.aspose.pdf.Form، com.aspose.pdf.Field، com.aspose.pdf.TextBoxField وcom.aspose.pdf.OptionCollection وغيرها.

#### com.aspose.pdf.devices

يمكننا تنفيذ عمليات متنوعة على وثائق PDF مثل تحويل وثيقة PDF إلى تنسيقات صور متنوعة.
 ومع ذلك، فإن مثل هذه العمليات لا تنتمي إلى كائن المستند ولا يمكننا تمديد فئة المستند لمثل هذه العمليات. لهذا السبب قمنا بإدخال مفهوم الجهاز في واجهة برمجة تطبيقات DOM الجديدة.

##### com.aspose.pdf.facades

قبل Aspose.PDF for Java t.o.o، كنت بحاجة إلى Aspose.PDF.Kit for Java لمعالجة ملفات PDF الموجودة. لتنفيذ كود Aspose.PDF.Kit القديم، يمكنك استخدام فضاء الأسماء com.aspose.pdf.facades.