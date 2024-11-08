---
title: أساسيات Aspose.PDF DOM API
linktitle: أساسيات DOM API
type: docs
weight: 120
url: /ar/cpp/basics-of-dom-api/
description: يستخدم Aspose.PDF for C++ أيضًا فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات. هنا يمكنك قراءة وصف هذا الهيكل.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مقدمة إلى DOM API

نموذج كائن المستند (DOM) هو شكل من أشكال تمثيل المستندات المهيكلة كنموذج موجه للكائنات. DOM هو معيار اتحاد شبكة الويب العالمية (W3C) الرسمي لتمثيل المستندات المهيكلة بطريقة محايدة للمنصة واللغة.

بعبارات بسيطة، DOM هو شجرة من الكائنات التي تمثل هيكل بعض المستندات. Aspose.PDF for C++ تستخدم أيضاً فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات. ومع ذلك، يتم التلاعب بجوانب DOM (مثل عناصره) ضمن نحو لغة البرمجة المستخدمة. يتم تحديد الواجهة العامة لدوم في واجهة برمجة التطبيقات الخاصة به (API).

### مقدمة إلى مستندات PDF

تنسيق المستندات المحمولة (PDF) هو معيار مفتوح لتبادل المستندات. مستند PDF هو مزيج من النص والبيانات الثنائية. إذا قمت بفتحه في محرر نصوص، سترى الكائنات الأولية التي تحدد هيكل ومحتوى المستند.

الهيكل المنطقي لملف PDF هو هرمي ويحدد التسلسل الذي تقوم به تطبيقات العرض برسم صفحات المستند ومحتوياتها. يتكون PDF من أربعة مكونات: الكائنات، هيكل الملف، هيكل المستند وتيارات المحتوى.

### هيكل مستند PDF

نظرًا لأن هيكل ملف PDF هو هرمي، فإن Aspose.PDF for C++ يصل أيضًا إلى العناصر بنفس الطريقة. يُظهر التسلسل الهرمي التالي كيفية تنظيم مستند PDF بشكل منطقي وكيفية بنائه باستخدام Aspose.PDF لـ C++ DOM API.

![هيكل مستند PDF](../images/structure.png)

### الوصول إلى عناصر مستند PDF

كائن الوثيقة هو في المستوى الجذري لنموذج الكائنات. يسمح لك Aspose.PDF لـ C++ DOM API بإنشاء كائن وثيقة ثم الوصول إلى جميع الكائنات الأخرى في التسلسل الهرمي. يمكنك الوصول إلى أي من المجموعات مثل الصفحات أو عنصر فردي مثل الصفحة وما إلى ذلك. يوفر DOM API نقاط دخول وخروج فردية للتعامل مع مستند PDF كما هو موضح أدناه:

- فتح مستند PDF
- الوصول إلى هيكل مستند PDF بأسلوب DOM
- تحديث البيانات في مستند PDF
- التحقق من صحة مستند PDF
- تصدير مستند PDF إلى تنسيقات مختلفة
- وأخيراً، حفظ مستند PDF المحدث

## كيفية استخدام Aspose.PDF الجديد لـ C++ API

ستشرح هذه الموضوع الجديد في Aspose.PDF لـ C++ API وتوجهك للبدء بسرعة وسهولة. يرجى ملاحظة أن التفاصيل المتعلقة باستخدام الميزات الخاصة ليست جزءًا من هذه المقالة.

يتكون Aspose.PDF لـ C++ من جزئين:

- Aspose.PDF لـ C++ DOM API
- Aspose.PDF.Facades

ستجد تفاصيل كل من هذه المجالات أدناه.

### Aspose.PDF لـ C++ DOM API

يتعلق Aspose.PDF لـ C++ DOM API ببنية مستند PDF، مما يساعدك على العمل مع مستندات PDF ليس فقط على مستوى الملف والمستند، ولكن أيضًا على مستوى الكائنات. لقد وفرنا المزيد من المرونة للمطورين للوصول إلى جميع عناصر وكائنات مستند PDF. باستخدام فئات Aspose.PDF DOM API، يمكنك الوصول البرمجي إلى عناصر المستند والتنسيق. يتكون هذا DOM API الجديد من مساحات الأسماء المختلفة كما يلي:

### مرجع مساحة الأسماء Aspose::Pdf

تقدم مساحة الأسماء هذه فئة Document التي تسمح لك بفتح وحفظ مستند PDF.

#### مرجع مساحة الأسماء Aspose::Pdf::Text

تقدم مساحة الأسماء هذه فئات تساعدك في العمل مع النص وجوانبه المختلفة، على سبيل المثال Font، FontCollection، FontRepository، FontSource، TextAbsorber، TextFragment، TextFragmentAbsorber، TextFragmentCollection، TextFragmentState، TextSegment و TextSegmentCollection إلخ.
#### Aspose::Pdf::Collections Namespace Reference

يوفر مساحة الاسم هذه الفئة AsposeHashDictionary.

#### Aspose::Pdf::CommonData Namespace Reference

#### Aspose::Pdf::Diagnostics Namespace Reference

#### Aspose::Pdf::Drawing Namespace Reference

توفر مساحة الاسم هذه الفئات: Curve, Circle, Arc, Rectangle, Graph وغيرها، لإضافة عناصر رسومية إلى ملف PDF الخاص بك.

#### Aspose::Pdf::Engine Namespace Reference

توفر مساحة الاسم هذه الفئات: Addressing، Interactive، Security، CommonData، IO، Presentation.

#### Aspose::Pdf::GroupProcessor Namespace Reference

توفر مساحة الاسم هذه الفئات: ExtractorFactory - تمثل مصنع لإنشاء كائنات IPdfTypeExtractor، وفئات IDocumentPageTextExtractor، وIDocumentTextExtractor، وIPdfTypeExtractor - تمثل واجهة للتفاعل مع المستخرج.

#### Aspose::Pdf::Interchange Namespace Reference

#### Aspose::Pdf::LogicalStructure Namespace Reference

توفر مساحة الاسم هذه الفئات: AnnotationElement، AttributeOwnerStandard، CaptionElement، DocumentElement، FormElement، GroupingElement، ILSTextElement، PrivateElement، WarichuWTElement، وغيرها.

#### Aspose::Pdf::Operators Namespace Reference

يوفر فضاء الأسماء هذا فئات للمشغلين التاليين: BasicSetColorAndPatternOperator، BlockTextOperator، SetCharWidthBoundingBox، SetColorStroke، SetHorizontalTextScaling، SetTextRenderingMode، TextShowOperator، إلخ.

#### Aspose::Pdf::Optimization Namespace Reference

يوفر فضاء الأسماء هذا فئتين - ImageCompressionOptions و OptimizationOptions.

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

يوفر فضاء الأسماء هذا فئتين: FontEmbeddingOptions - يتطلب معيار PDF/A أن يتم تضمين جميع الخطوط في المستند. تتضمن هذه الفئة إشارات لحالات عندما لا يمكن تضمين بعض الخطوط بسبب غيابها على جهاز الكمبيوتر الوجهة. ToUnicodeProcessingRules - تصف هذه الفئة القواعد التي يمكن استخدامها لحل خطأ Adobe Preflight "لا يمكن تعيين النص إلى Unicode".

#### Aspose::Pdf::Sanitization Namespace Reference

يوفر فضاء الأسماء هذا فئتين: Details_SanitizationException و IRecovery.

#### Aspose::Pdf::Tagged Namespace Reference

يوفر مساحة الاسم هذه فئات Details_TaggedException - تمثل استثناءً لمحتوى TaggedPDF الخاص بالمستند. ITaggedContent - تمثل واجهة للعمل مع محتوى TaggedPdf الخاص بالمستند؟ و TaggedPdfExceptionCode.

#### Aspose::Pdf::Validation Namespace Reference

#### Aspose::Pdf::XfaConverter Namespace Reference

يوفر مساحة الاسم هذه فئة XfaParserOptions - فئة للتعامل مع تغليف البيانات ذات الصلة.

#### Aspose::Pdf::Annotations Namespace Reference

التعليقات التوضيحية هي جزء من الميزات التفاعلية لمستند PDF. لقد خصصنا مساحة اسم للتعليقات التوضيحية. تحتوي مساحة الاسم هذه على فئات تساعدك على العمل مع التعليقات التوضيحية، على سبيل المثال، Annotation، AnnotationCollection، CircleAnnotation و LinkAnnotation إلخ.

#### Aspose::Pdf::Forms Namespace Reference

تحتوي مساحة الاسم هذه على فئات تساعدك على العمل مع نماذج PDF وحقول النماذج، على سبيل المثال Form، Field، TextBoxField و OptionCollection إلخ.

#### Aspose::Pdf::Devices Namespace Reference

```
يمكننا إجراء عمليات مختلفة على مستندات PDF مثل تحويل مستند PDF إلى تنسيقات صور مختلفة. ومع ذلك، فإن مثل هذه العمليات لا تنتمي إلى كائن المستند ولا يمكننا تمديد فئة المستند لمثل هذه العمليات. لهذا السبب قمنا بتقديم مفهوم الجهاز في واجهة برمجة التطبيقات الجديدة للـ DOM.

##### Aspose::Pdf::Facades مرجع الفضاء الاسمي

يمكنك استخدام فضاء الاسم Aspose.PDF.Facades. يوفر هذا الفضاء الاسمي فئات مثل AutoFiller - يمثل فئة لاستقبال البيانات من قاعدة بيانات أو مصدر بيانات آخر. Bookmark, Form, Stamp, PdfConverter والمزيد من الفئات.
```