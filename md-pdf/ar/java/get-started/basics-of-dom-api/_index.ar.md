---
title: أساسيات Aspose.PDF DOM API
linktitle: أساسيات DOM API
type: docs
weight: 110
url: /java/basics-of-dom-api/
description: يستخدم Aspose.PDF لـ Java أيضًا فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات. هنا يمكنك قراءة وصف هذا الهيكل.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مقدمة إلى DOM API

نموذج كائن المستند (DOM) هو شكل من أشكال تمثيل المستندات المنظمة كنموذج موجه للكائن. DOM هو المعيار الرسمي لاتحاد شبكة الويب العالمية (W3C) لتمثيل المستندات المنظمة بطريقة محايدة للمنصة واللغة.

بعبارات بسيطة، DOM هو شجرة من الكائنات التي تمثل هيكل بعض المستندات.
 Aspose.PDF for Java يستخدم أيضًا فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات. ومع ذلك، يتم التلاعب بجوانب DOM (مثل عناصره) داخل تركيب لغة البرمجة المستخدمة. يتم تحديد الواجهة العامة لـ DOM في واجهة برمجة التطبيقات الخاصة به (API).

### مقدمة إلى مستند PDF

تنسيق المستندات المحمولة (PDF) هو معيار مفتوح لتبادل المستندات. مستند PDF هو مزيج من النصوص والبيانات الثنائية. إذا فتحته في محرر نصوص، سترى الكائنات الأولية التي تحدد هيكل ومحتوى المستند.

الهيكل المنطقي لملف PDF هرمي ويحدد التسلسل الذي تقوم به تطبيقات العرض برسم صفحات المستند ومحتوياتها. يتكون PDF من أربعة مكونات: الكائنات وهيكل الملف وهيكل المستند وتيارات المحتوى.

### هيكل مستند PDF

نظرًا لأن هيكل ملف PDF هرمي، فإن Aspose.PDF for Java يصل أيضًا إلى العناصر بنفس الطريقة. يظهر التسلسل الهرمي التالي كيف يتم هيكلة مستند PDF منطقياً وكيف يقوم Aspose.PDF for Java DOM API ببنائه.

![هيكل مستند PDF](../images/structure.png)

### الوصول إلى عناصر مستند PDF

كائن المستند موجود في المستوى الجذري لنموذج الكائن. يتيح لك Aspose.PDF for Java DOM API إنشاء كائن مستند ثم الوصول إلى جميع الكائنات الأخرى في التسلسل الهرمي. يمكنك الوصول إما إلى أي من المجموعات مثل الصفحات أو العنصر الفردي مثل الصفحة وما إلى ذلك. يوفر DOM API نقاط دخول وخروج فردية للتعامل مع مستند PDF كما هو موضح أدناه:

- فتح مستند PDF
- الوصول إلى هيكل مستند PDF بأسلوب DOM
- تحديث البيانات في مستند PDF
- التحقق من صحة مستند PDF
- تصدير مستند PDF إلى صيغ مختلفة
- أخيراً، حفظ مستند PDF المحدث

## كيفية استخدام Aspose.PDF for Java API الجديد

سيشرح هذا الموضوع Aspose.PDF for Java API الجديد ويرشدك للبدء بسرعة وسهولة. يرجى ملاحظة أن التفاصيل المتعلقة باستخدام الميزات الخاصة ليست جزءًا من هذه المقالة.

يتكون Aspose.PDF for Java من جزأين:

- Aspose.PDF for Java DOM API
- Aspose.PDF.Facades

ستجد تفاصيل كل من هذه المجالات أدناه.

### Aspose.PDF for Java DOM API

يتوافق Aspose.PDF for Java DOM API الجديد مع هيكل مستندات PDF، مما يساعدك على العمل مع مستندات PDF ليس فقط على مستوى الملف والمستند، ولكن أيضًا على مستوى الكائن. لقد وفرنا مرونة أكبر للمطورين للوصول إلى جميع العناصر والكائنات في مستند PDF. باستخدام فئات Aspose.PDF DOM API، يمكنك الوصول برمجيًا إلى عناصر المستند والتنسيق. تتألف هذه الـ DOM API الجديدة من مساحات أسماء مختلفة كما هو موضح أدناه:

### com.aspose.pdf

يوفر مساحة الاسم هذه فئة Document التي تسمح لك بفتح وحفظ مستند PDF. The License class is also a part of this namespace. It also provides classes related to PDF pages, attachments, and bookmarks like com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, and com.aspose.pdf.OutlineCollection etc.

#### com.aspose.pdf.text

توفر مساحة الاسم هذه فئات تساعدك على العمل مع النص وجوانبه المختلفة، على سبيل المثال com.aspose.pdf.Font، com.aspose.pdf.FontCollection، com.aspose.pdf.FontRepository، com.aspose.pdf.FontStyles، com.aspose.pdf.TextAbsorber، com.aspose.pdf.TextFragment، com.aspose.pdf.TextFragmentAbsorber، com.aspose.pdf.TextFragmentCollection، com.aspose.pdf.TextFragmentState، com.aspose.pdf.TextSegment وcom.aspose.pdf.TextSegmentCollection إلخ.

#### com.aspose.pdf.TextOptions

توفر مساحة الاسم هذه فئات تتيح لك تعيين خيارات مختلفة للبحث أو تحرير أو استبدال النص، على سبيل المثال com.aspose.pdf.TextEditOptions، com.aspose.pdf.TextReplaceOptions، وcom.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

تحتوي هذه المساحة على فئات تساعدك في العمل مع الميزات التفاعلية لوثيقة PDF، على سبيل المثال العمل مع الوثيقة وغيرها من الإجراءات. تحتوي هذه المساحة على فئات مثل com.aspose.pdf.GoToAction، com.aspose.pdf.GoToRemoteAction وcom.aspose.pdf.GoToURIAction إلخ.

#### com.aspose.pdf.Annotation

التعليقات التوضيحية هي جزء من الميزات التفاعلية لوثيقة PDF. لقد خصصنا مساحة للتعليقات التوضيحية. تحتوي هذه المساحة على فئات تساعدك في العمل مع التعليقات التوضيحية، على سبيل المثال، com.aspose.pdf.Annotation، com.aspose.pdf.AnnotationCollection، com.aspose.pdf.CircleAnnotation وcom.aspose.pdf.LinkAnnotation إلخ.

#### com.aspose.pdf.Form

تحتوي هذه المساحة على فئات تساعدك في العمل مع النماذج وحقول النماذج في وثائق PDF، على سبيل المثال com.aspose.pdf.Form، com.aspose.pdf.Field، com.aspose.pdf.TextBoxField وcom.aspose.pdf.OptionCollection إلخ.

#### com.aspose.pdf.devices 

يمكننا تنفيذ عمليات متنوعة على وثائق PDF مثل تحويل وثيقة PDF إلى صيغ صور متنوعة.
  ومع ذلك، فإن مثل هذه العمليات لا تنتمي إلى كائن Document ولا يمكننا تمديد فئة Document لمثل هذه العمليات. لهذا السبب قمنا بإدخال مفهوم الجهاز في واجهة برمجة التطبيقات الجديدة لـ DOM.

##### com.aspose.pdf.facades

قبل Aspose.PDF لـ Java t.o.o، كنت بحاجة إلى Aspose.PDF.Kit لـ Java للتلاعب بملفات PDF الموجودة. لتنفيذ كود Aspose.PDF.Kit القديم، يمكن استخدام فضاء الأسماء com.aspose.pdf.facades.