---
title: تحويل ملفات PDF إلى مستندات Microsoft Word في .NET
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: ar/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: تعلم كيفية كتابة كود C# لتحويل PDF إلى صيغ Microsoft Word باستخدام Aspose.PDF لـ .NET. وضبط تحويل PDF إلى DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## نظرة عامة

يشرح هذا المقال كيفية **تحويل PDF إلى مستندات Microsoft Word باستخدام C#**. يغطي المواضيع التالية.

_الصيغة_: **DOC**

- [C# PDF إلى DOC](#csharp-pdf-to-doc)
- [C# تحويل PDF إلى DOC](#csharp-pdf-to-doc)
- [C# كيفية تحويل ملف PDF إلى DOC](#csharp-pdf-to-doc)

_الصيغة_: **DOCX**

- [C# PDF إلى DOCX](#csharp-pdf-to-docx)
- [C# تحويل PDF إلى DOCX](#csharp-pdf-to-docx)
- [C# كيفية تحويل ملف PDF إلى DOCX](#csharp-pdf-to-docx)

_الصيغة_: **Word**

- [C# PDF إلى Word](#csharp-pdf-to-docx)
- [C# تحويل PDF إلى Word](#csharp-pdf-to-doc)
- [C# كيفية تحويل ملف PDF إلى Word](#csharp-pdf-to-docx)

يعمل الشفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).
## تحويل PDF إلى ملفات DOC و DOCX

إحدى الميزات الأكثر شعبية هي تحويل PDF إلى مستند Microsoft Word DOC، مما يجعل إدارة المحتوى أكثر سهولة. **Aspose.PDF لـ .NET** يتيح لك تحويل ملفات PDF إلى تنسيق DOC و DOCX بسرعة وكفاءة.

## تحويل PDF إلى ملف DOC (Microsoft Word 97-2003)

قم بتحويل ملفات PDF إلى تنسيق DOC بكل سهولة وتحكم كامل. Aspose.PDF لـ .NET مرن ويدعم مجموعة واسعة من التحويلات. على سبيل المثال، تحويل صفحات من مستندات PDF إلى صور هو ميزة شائعة جدًا.

لقد طلب العديد من عملائنا تحويلًا من PDF إلى DOC: تحويل ملف PDF إلى مستند Microsoft Word. العملاء يريدون هذا لأن ملفات PDF لا يمكن تحريرها بسهولة، بينما يمكن تحرير مستندات Word. بعض الشركات تريد أن يتمكن مستخدموها من التعامل مع النصوص والجداول والصور في الملفات التي بدأت كملفات PDF.

مواصلة تقليد جعل الأمور بسيطة ومفهومة، يتيح لك Aspose.PDF لـ .NET تحويل ملف PDF مصدر إلى ملف DOC بسطرين من الكود.
الحفاظ على تقليد تبسيط الأشياء وجعلها مفهومة، يتيح لك Aspose.PDF لـ .NET تحويل ملف PDF مصدر إلى ملف DOC بسطرين من الكود فقط.

الشفرة التالية بلغة C# تُظهر تحويل ملف PDF إلى صيغة DOC.

<a name="csharp-pdf-to-doc"><strong>الخطوات: تحويل PDF إلى DOC في C#</strong></a>

1. إنشاء مثيل من كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) بالمستند PDF المصدر.
2. حفظه إلى صيغة **SaveFormat.Doc** بواسطة استدعاء طريقة **Document.Save()**.

```csharp
public static void ConvertPDFtoWord()
{
    // فتح مستند PDF المصدر
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // حفظ الملف بصيغة مستند MS
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

}
```

### استخدام فئة DocSaveOptions

توفر فئة [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) العديد من الخصائص التي تحسن من تحويل ملفات PDF إلى صيغة DOC.

فئة [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) توفر العديد من الخصائص التي تحسن تحويل ملفات PDF إلى تنسيق DOC.

- وضع [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) سريع وجيد للحفاظ على المظهر الأصلي لملف PDF، ولكن قابلية تحرير الوثيقة الناتجة قد تكون محدودة. يتم تحويل كل كتلة نصية مجمعة بصرياً في PDF الأصلي إلى مربع نص في الوثيقة الناتجة. هذا يحقق أقصى تشابه مع الأصل، لذا تبدو الوثيقة الناتجة جيدة، ولكنها تتكون بالكامل من مربعات نصية، والتي قد تكون تحريرها في Microsoft Word تحديًا.
- وضع [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) هو وضع التعرف الكامل، حيث يقوم المحرك بالتجميع والتحليل متعدد المستويات لاستعادة الوثيقة الأصلية كما قصدها المؤلف مع إنتاج وثيقة قابلة للتحرير بسهولة.
```
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) هو وضع التعرف الكامل، حيث يقوم المحرك بتجميع وتحليل متعدد المستويات لاستعادة الوثيقة الأصلية كما قصد المؤلف بينما ينتج وثيقة قابلة للتحرير بسهولة.

خاصية [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) يمكن استخدامها للتحكم في القرب النسبي بين العناصر النصية. وهذا يعني أن المسافة معيارية بحجم الخط. قد تحتوي الخطوط الأكبر على مسافات أكبر بين المقاطع ولا تزال تعتبر ككل واحد. يحدد كنسبة مئوية من حجم الخط؛ على سبيل المثال، 1 = 100%. هذا يعني أن حرفين بحجم 12 نقطة موضوعين على بعد 12 نقطة يعتبران قريبين.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) يستخدم لتفعيل التعرف على الرصاصات أثناء التحويل.

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // تعيين وضع التعرف كـ Flow
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // تعيين القرب الأفقي كـ 2.5
        RelativeHorizontalProximity = 2.5f,
        // تفعيل الخيار للتعرف على الرصاصات أثناء عملية التحويل
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```
{{% alert color="success" %}}
**جرب تحويل PDF إلى DOC عبر الإنترنت**

يقدم لك Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل PDF إلى DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى ملف DOCX (Microsoft Word 2007-2021)

يتيح لك API Aspose.PDF لـ .NET قراءة وتحويل مستندات PDF إلى DOCX باستخدام C# وأي لغة .NET. DOCX هو تنسيق معروف لمستندات Microsoft Word تم تغيير هيكله من الثنائي العادي إلى مزيج من ملفات XML والثنائية. يمكن فتح ملفات Docx بواسطة Word 2007 والإصدارات الأحدث ولكن ليس بواسطة الإصدارات السابقة من MS Word، التي تدعم امتدادات ملفات DOC.

الكود التالي بلغة C# يظهر تحويل ملف PDF إلى تنسيق DOCX.

<a name="csharp-pdf-to-docx"><strong>الخطوات: تحويل PDF إلى DOCX بلغة C#</strong></a>

1.
1.
2. احفظه بتنسيق **SaveFormat.DocX** بواسطة استدعاء طريقة **Document.Save()**.

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // فتح مستند PDF المصدر
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // حفظ الملف DOC الناتج
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### تحويل PDF إلى DOCX بالوضع المحسن

للحصول على نتائج أفضل لتحويل PDF إلى DOCX، يمكنك استخدام وضع `EnhancedFlow`.
الفرق الرئيسي بين الوضع العادي والوضع المحسن هو أن الجداول (سواء كانت مع حدود أو بدون) تتعرف كجداول حقيقية، وليس كنص مع صورة في الخلفية.
هناك أيضا التعرف على القوائم المرقمة والعديد من الأمور الصغيرة الأخرى.

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // فتح مستند PDF المصدر
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // إنشاء كائن DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // تحديد تنسيق الإخراج كـ DOCX
        Format = DocSaveOptions.DocFormat.DocX
        // تعيين معاملات DocSaveOptions الأخرى
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // حفظ المستند بتنسيق docx
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

يقدم لك Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى تطبيق Word المجاني](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## انظر أيضا

هذا المقال يغطي أيضا هذه المواضيع. الأكواد هي نفسها كما في الأعلى.

_التنسيق_: **Word**

- [C# كود PDF إلى Word](#csharp-pdf-to-docx)
- [C# واجهة برمجة تطبيقات PDF إلى Word](#csharp-pdf-to-docx)
- [C# PDF إلى Word برمجيًا](#csharp-pdf-to-docx)
- [C# مكتبة PDF إلى Word](#csharp-pdf-to-docx)
- [C# حفظ PDF كـ Word](#csharp-pdf-to-docx)
- [C# توليد Word من PDF](#csharp-pdf-to-docx)
- [C# إنشاء Word من PDF](#csharp-pdf-to-docx)
- [C# محول PDF إلى Word](#csharp-pdf-to-docx)

_التنسيق_: **DOC**

- [C# كود PDF إلى DOC](#csharp-pdf-to-doc)
- [C# واجهة برمجة تطبيقات PDF إلى DOC](#csharp-pdf-to-doc)
- [واجهة برمجة التطبيقات لتحويل PDF إلى DOC بلغة C#](#csharp-pdf-to-doc)
- [برمجة تحويل PDF إلى DOC بلغة C#](#csharp-pdf-to-doc)
- [مكتبة C# لتحويل PDF إلى DOC](#csharp-pdf-to-doc)
- [حفظ PDF كـ DOC بلغة C#](#csharp-pdf-to-doc)
- [توليد DOC من PDF بلغة C#](#csharp-pdf-to-doc)
- [إنشاء DOC من PDF بلغة C#](#csharp-pdf-to-doc)
- [محول PDF إلى DOC بلغة C#](#csharp-pdf-to-doc)

_Format_: **DOCX**

- [كود C# لتحويل PDF إلى DOCX](#csharp-pdf-to-docx)
- [واجهة برمجة التطبيقات لتحويل PDF إلى DOCX بلغة C#](#csharp-pdf-to-docx)
- [برمجة تحويل PDF إلى DOCX بلغة C#](#csharp-pdf-to-docx)
- [مكتبة C# لتحويل PDF إلى DOCX](#csharp-pdf-to-docx)
- [حفظ PDF كـ DOCX بلغة C#](#csharp-pdf-to-docx)
- [توليد DOCX من PDF بلغة C#](#csharp-pdf-to-docx)
- [إنشاء DOCX من PDF بلغة C#](#csharp-pdf-to-docx)
- [محول PDF إلى DOCX بلغة C#](#csharp-pdf-to-docx)
