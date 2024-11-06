---
title: أساسيات Aspose.PDF DOM API
linktitle: أساسيات DOM API
type: docs
weight: 10
url: ar/androidjava/basics-of-dom-api/
description: يستخدم Aspose.PDF لنظام Android عبر Java أيضًا فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات. هنا يمكنك قراءة وصف لهذا الهيكل.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مقدمة إلى DOM API

نموذج كائن المستند (DOM) هو شكل من أشكال تمثيل المستندات المهيكلة كنموذج موجه للكائنات. DOM هو معيار رسمي من اتحاد شبكة الويب العالمية (W3C) لتمثيل المستندات المهيكلة بطريقة محايدة للنظام الأساسي واللغة.

بعبارات بسيطة، DOM هو شجرة من الكائنات التي تمثل هيكل بعض المستندات.
 Aspose.PDF for Android عبر Java يستخدم أيضًا فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات. ومع ذلك، يتم التلاعب بجوانب DOM (مثل عناصره) داخل بناء لغة البرمجة المستخدمة. يتم تحديد الواجهة العامة لـ DOM في واجهة برمجة التطبيقات الخاصة به (API).

### مقدمة إلى مستند PDF

تنسيق المستند المحمول (PDF) هو معيار مفتوح لتبادل المستندات. مستند PDF هو مزيج من النص والبيانات الثنائية. إذا فتحته في محرر نصوص، سترى الكائنات الخام التي تحدد هيكل ومحتويات المستند.

الهيكل المنطقي لملف PDF هرمي ويحدد التسلسل الذي تقوم به تطبيقات العرض برسم صفحات المستند ومحتوياتها. يتكون PDF من أربعة مكونات: الكائنات، هيكل الملف، هيكل المستند وتدفقات المحتوى.

### هيكل مستند PDF

نظرًا لأن هيكل ملف PDF هرمي، فإن Aspose.PDF for Java يصل أيضًا إلى العناصر بنفس الطريقة. يظهر التسلسل الهرمي التالي كيف يتم تنظيم مستند PDF بشكل منطقي وكيف يقوم Aspose.PDF لـ Java DOM API ببنائه.

![هيكل مستند PDF](https://docs.aspose.com/pdf/java/images/structure.png)

### الوصول إلى عناصر مستند PDF

كائن المستند موجود في المستوى الجذري لنموذج الكائن. يتيح لك Aspose.PDF لنظام Android عبر Java DOM API إنشاء كائن Document ثم الوصول إلى جميع الكائنات الأخرى في التسلسل الهرمي. يمكنك إما الوصول إلى أي من المجموعات مثل Pages أو العنصر الفردي مثل Page إلخ. يوفر DOM API نقاط دخول وخروج واحدة للتلاعب بمستند PDF كما هو موضح أدناه:

- فتح مستند PDF
- الوصول إلى هيكل مستند PDF بأسلوب DOM
- تحديث البيانات في مستند PDF
- التحقق من صحة مستند PDF
- تصدير مستند PDF إلى تنسيقات مختلفة
- وأخيراً، حفظ مستند PDF المحدث

## كيفية استخدام Aspose.PDF الجديد لنظام Android عبر Java API

سيشرح هذا الموضوع Aspose.PDF الجديد لنظام Android عبر Java API ويوجهك لبدء العمل بسرعة وسهولة. يرجى ملاحظة أن التفاصيل المتعلقة باستخدام الميزات المعينة ليست جزءًا من هذه المقالة.

يتكون Aspose.PDF for Android عبر Java من جزئين:

- Aspose.PDF for Android عبر Java DOM API
- Aspose.PDF.Facades

ستجد تفاصيل كل من هذه المناطق أدناه.

### Aspose.PDF for Android عبر Java DOM API

يتوافق API الجديد Aspose.PDF for Android عبر Java DOM مع هيكل مستندات PDF، مما يساعدك في العمل مع مستندات PDF ليس فقط على مستوى الملف والمستند، ولكن أيضًا على مستوى الكائن. لقد وفرنا مرونة أكبر للمطورين للوصول إلى جميع العناصر والكائنات في مستند PDF. باستخدام فئات Aspose.PDF DOM API، يمكنك الوصول البرمجي إلى عناصر المستند والتنسيق. يتألف هذا API الجديد من عدة مساحات اسم كما هو موضح أدناه:

### com.aspose.pdf

توفر مساحة الاسم هذه الفئة Document التي تتيح لك فتح وحفظ مستند PDF. The License class is also a part of this namespace. It also provides classes related to PDF pages, attachments, and bookmarks like com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, and com.aspose.pdf.OutlineCollection etc.

#### com.aspose.pdf.text

يوفر فضاء الأسماء هذا فئات تساعدك في العمل مع النص وجوانبه المختلفة، على سبيل المثال com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment و com.aspose.pdf.TextSegmentCollection إلخ.

#### com.aspose.pdf.TextOptions

يوفر فضاء الأسماء هذا فئات تتيح لك تعيين خيارات مختلفة للبحث، التحرير أو استبدال النص، على سبيل المثال com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, و com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

تحتوي مساحة الأسماء هذه على الفئات التي تساعدك على العمل مع الميزات التفاعلية لوثيقة PDF، على سبيل المثال العمل مع الوثيقة والإجراءات الأخرى. تحتوي مساحة الأسماء هذه على فئات مثل com.aspose.pdf.GoToAction، وcom.aspose.pdf.GoToRemoteAction وcom.aspose.pdf.GoToURIAction إلخ.

#### com.aspose.pdf.Annotation

التعليقات التوضيحية هي جزء من الميزات التفاعلية لوثيقة PDF. لقد خصصنا مساحة أسماء للتعليقات التوضيحية. تحتوي مساحة الأسماء هذه على فئات تساعدك على العمل مع التعليقات التوضيحية، على سبيل المثال، com.aspose.pdf.Annotation، وcom.aspose.pdf.AnnotationCollection، وcom.aspose.pdf.CircleAnnotation وcom.aspose.pdf.LinkAnnotation إلخ.

#### com.aspose.pdf.Form

تحتوي مساحة الأسماء هذه على الفئات التي تساعدك على العمل مع نماذج PDF وحقول النماذج، على سبيل المثال com.aspose.pdf.Form، وcom.aspose.pdf.Field، وcom.aspose.pdf.TextBoxField وcom.aspose.pdf.OptionCollection إلخ.

#### com.aspose.pdf.devices 

يمكننا تنفيذ عمليات متنوعة على وثائق PDF مثل تحويل وثيقة PDF إلى تنسيقات صور مختلفة.
 ومع ذلك، فإن مثل هذه العمليات لا تنتمي إلى كائن Document ولا يمكننا توسيع فئة Document لمثل هذه العمليات. لهذا السبب قمنا بإدخال مفهوم الجهاز في واجهة برمجة التطبيقات الجديدة لـ DOM.

##### com.aspose.pdf.facades

قبل Aspose.PDF لـ Java t.o.o، كنت بحاجة إلى Aspose.PDF.Kit لـ Java للتلاعب بملفات PDF الموجودة. لتنفيذ كود Aspose.PDF.Kit القديم، يمكن استخدام فضاء الأسماء com.aspose.pdf.facades.