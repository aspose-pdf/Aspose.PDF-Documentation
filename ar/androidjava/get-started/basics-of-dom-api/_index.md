---
title: أساسيات Aspose.PDF DOM API
linktitle: أساسيات DOM API
type: docs
weight: 10
url: /ar/androidjava/basics-of-dom-api/
description: تستخدم Aspose.PDF لنظام Android عبر Java أيضًا فكرة DOM لتمثيل بنية مستند PDF من حيث الكائنات. هنا يمكنك قراءة وصف هذه البنية.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مقدمة إلى DOM API

نموذج كائن المستند (DOM) هو شكل من أشكال تمثيل المستندات المهيكلة كنموذج كائني التوجيه. DOM هو المعيار الرسمي لمجموعة توصيات الويب العالمية (W3C) لتمثيل المستندات المهيكلة بطريقة محايدة عن النظام الأساسي واللغة.

بكلمات بسيطة، DOM هو شجرة من الكائنات التي تمثل بنية مستند ما. تستخدم Aspose.PDF لنظام Android عبر Java أيضًا فكرة DOM لتمثيل بنية مستند PDF من حيث الكائنات. ومع ذلك، يتم التلاعب بجوانب DOM (مثل العناصر الخاصة به) داخل بنية لغة البرمجة المستخدمة. الواجهة العامة لـ DOM محددة في واجهة برمجة التطبيقات (API) الخاصة به.

### مقدمة إلى مستند PDF

تنسيق المستندات القابل للنقل (PDF) هو معيار مفتوح لتبادل المستندات. مستند PDF هو مزيج من النص والبيانات الثنائية. إذا فتحته في محرر نصوص، سترى الكائنات الخام التي تحدد بنية ومحتوى المستند.

الهيكل المنطقي لملف PDF هرمي ويحدد التسلسل الذي يرسم به تطبيق العرض صفحات المستند ومحتوياتها. يتكون PDF من أربعة مكونات: الكائنات، بنية الملف، بنية المستند وتدفقات المحتوى.

### بنية مستند PDF

نظرًا لأن بنية ملف PDF هرمية، فإن Aspose.PDF for Java يحصل أيضًا على العناصر بنفس الطريقة. تُظهر التسلسل الهرمي التالي كيف يتم هيكلة مستند PDF منطقياً وكيف يبنيها Aspose.PDF for Java DOM API.

![بنية مستند PDF](https://docs.aspose.com/pdf/java/images/structure.png)

### الوصول إلى عناصر مستند PDF

كائن Document يقع في المستوى الجذري لنموذج الكائنات. يتيح لك Aspose.PDF for Android عبر Java DOM API إنشاء كائن Document ثم الوصول إلى جميع الكائنات الأخرى في التسلسل الهرمي. يمكنك إما الوصول إلى أي من المجموعات مثل Pages أو العنصر الفردي مثل Page إلخ. يوفر DOM API نقاط دخول وخروج واحدة للتلاعب بالمستند PDF كما هو موضح أدناه:

- فتح مستند PDF
- الوصول إلى بنية مستند PDF بنمط DOM
- تحديث البيانات في مستند PDF
- تحقق من صحة مستند PDF
- تصدير مستند PDF إلى صيغ مختلفة
- أخيرًا، احفظ مستند PDF المحدث

## كيفية استخدام Aspose.PDF الجديد لنظام Android عبر واجهة برمجة التطبيقات Java

ستشرح هذه الفقرة Aspose.PDF الجديد لنظام Android عبر واجهة برمجة التطبيقات Java وتوجهك للبدء بسرعة وسهولة. يرجى ملاحظة أن التفاصيل المتعلقة باستخدام الميزات المحددة ليست جزءًا من هذه المقالة.

يتكون Aspose.PDF لنظام Android عبر Java من جزأين:

- Aspose.PDF لنظام Android عبر Java DOM API
- Aspose.PDF.Facades 

ستجد تفاصيل كل من هذه المجالات أدناه.

### Aspose.PDF لنظام Android عبر Java DOM API

يتطابق Aspose.PDF الجديد لنظام Android عبر Java DOM API مع بنية مستند PDF، مما يساعدك على العمل مع مستندات PDF ليس فقط على مستوى الملف والمستند، بل أيضًا على مستوى الكائن. لقد وفرنا مزيدًا من المرونة للمطورين للوصول إلى جميع عناصر وكائنات مستند PDF. باستخدام فئات Aspose.PDF DOM API، يمكنك الحصول على وصول برمجي إلى عناصر المستند وتنسيقه. يتكون هذا الـ DOM API الجديد من عدة مساحات أسماء كما هو مبين أدناه:

### com.aspose.pdf

توفر هذه مساحة الأسماء فئة Document التي تسمح لك بفتح وحفظ مستند PDF. فئة License هي أيضًا جزء من هذه مساحة الأسماء. كما توفر فئات متعلقة بصفحات PDF والمرفقات وعلامات الكتاب مثل com.aspose.pdf.Page، com.aspose.pdf.PageCollection، com.aspose.pdf.FileSpecification، com.aspose.pdf.EmbeddedFileCollection، com.aspose.pdf.OutlineItemCollection، و com.aspose.pdf.OutlineCollection وغيرها.

#### com.aspose.pdf.text

تُوفر هذه المساحة الاسمية فئات تساعدك على العمل مع النص وجوانبه المختلفة، على سبيل المثال com.aspose.pdf.Font، com.aspose.pdf.FontCollection، com.aspose.pdf.FontRepository، com.aspose.pdf.FontStyles، com.aspose.pdf.TextAbsorber، com.aspose.pdf.TextFragment، com.aspose.pdf.TextFragmentAbsorber، com.aspose.pdf.TextFragmentCollection، com.aspose.pdf.TextFragmentState، com.aspose.pdf.TextSegment و com.aspose.pdf.TextSegmentCollection إلخ.

#### com.aspose.pdf.TextOptions

تُوفر هذه المساحة الاسمية فئات تتيح لك ضبط خيارات مختلفة للبحث أو التحرير أو استبدال النص، على سبيل المثال com.aspose.pdf.TextEditOptions، com.aspose.pdf.TextReplaceOptions، و com.aspose.pdf.TextSearchOptions.

#### com.aspose.pdf.PdfAction

تحتوي هذه المساحة الاسمية على فئات تساعدك على العمل مع الميزات التفاعلية لمستند PDF، على سبيل المثال التعامل مع المستند وإجراءات أخرى. تحتوي هذه المساحة الاسمية على فئات مثل com.aspose.pdf.GoToAction، com.aspose.pdf.GoToRemoteAction و com.aspose.pdf.GoToURIAction إلخ.

#### com.aspose.pdf.Annotation

التعليقات التوضيحية هي جزء من ميزات التفاعل في مستند PDF. لقد خصصنا مساحة أسماء للتعليقات التوضيحية. تحتوي مساحة الاسم هذه على فئات تساعدك في التعامل مع التعليقات التوضيحية، على سبيل المثال، com.aspose.pdf.Annotation، com.aspose.pdf.AnnotationCollection، com.aspose.pdf.CircleAnnotation و com.aspose.pdf.LinkAnnotation وما إلى ذلك.

#### com.aspose.pdf.Form

تحتوي مساحة الاسم هذه على فئات تساعدك في التعامل مع نماذج PDF وحقول النماذج، على سبيل المثال com.aspose.pdf.Form، com.aspose.pdf.Field، com.aspose.pdf.TextBoxField و com.aspose.pdf.OptionCollection وما إلى ذلك.

#### com.aspose.pdf.devices 

يمكننا تنفيذ عمليات مختلفة على مستندات PDF مثل تحويل مستند PDF إلى صيغ صور متعددة. ومع ذلك، لا تنتمي هذه العمليات إلى كائن Document ولا يمكننا توسيع فئة Document لهذه العمليات. لهذا السبب قدمنا مفهوم Device في واجهة برمجة التطبيقات DOM الجديدة.

##### com.aspose.pdf.facades

قبل Aspose.PDF for Java t.o.o، كنت تحتاج إلى Aspose.PDF.Kit for Java للتعامل مع ملفات PDF الموجودة. لتنفيذ كود Aspose.PDF.Kit القديم، يمكنك استخدام مساحة الاسم com.aspose.pdf.facades.

