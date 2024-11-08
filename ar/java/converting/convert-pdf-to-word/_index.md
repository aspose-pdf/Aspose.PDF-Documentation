---
title: تحويل PDF إلى مستندات Microsoft Word في Java
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /ar/java/convert-pdf-to-word/
lastmod: "2021-11-19"
description: تحويل ملف PDF إلى صيغة DOC و DOCX بسهولة وتحكم كامل باستخدام Aspose.PDF لـ Java. تعلم المزيد حول كيفية تحسين تحويل PDF إلى مستندات Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## نظرة عامة

تشرح هذه المقالة كيفية تحويل PDF إلى Word باستخدام Java. الكود بسيط جداً، فقط قم بتحميل PDF إلى فئة Document واحفظه كصيغة إخراج Microsoft Word DOC أو DOCX. يغطي المواضيع التالية

- [تحويل PDF إلى Word في Java](#convert-pdf-to-doc)
- [تحويل PDF إلى DOC في Java](#convert-pdf-to-doc)
- [تحويل PDF إلى DOCX في Java](#convert-pdf-to-docx)
- [تحويل PDF إلى Word في Java](#convert-pdf-to-docx)
- [تحويل PDF إلى DOC في Java](#convert-pdf-to-doc)
- [تحويل PDF إلى DOCX في Java](#convert-pdf-to-docx)
- [كيفية تحويل ملف PDF إلى Word DOC في Java](#convert-pdf-to-doc) أو [Word DOCX](#convert-pdf-to-docx)

- [مكتبة PDF إلى Word في Java، API أو كود لحفظ، إنشاء أو توليد مستندات Word برمجياً من PDF](#convert-pdf-to-docx)

## تحويل PDF إلى DOC

أحد أكثر الميزات شهرة هو تحويل PDF إلى مستند Microsoft Word DOC، مما يجعل المحتوى سهل التعديل. يسمح Aspose.PDF for Java لك بتحويل ملفات PDF إلى DOC.

**Aspose.PDF for Java** يمكنه إنشاء مستندات PDF من الصفر وهو مجموعة أدوات رائعة لتحديث وتحرير وتعديل مستندات PDF الموجودة. ميزة مهمة هي القدرة على تحويل الصفحات والمستندات الكاملة إلى صور. ميزة أخرى شهيرة هي تحويل PDF إلى مستند Microsoft Word DOC، مما يجعل المحتوى سهل التعديل. (معظم المستخدمين لا يمكنهم تحرير مستندات PDF ولكن يمكنهم بسهولة العمل مع الجداول والنصوص والصور في Microsoft Word.)

لتبسيط الأمور وجعلها مفهومة، يوفر Aspose.PDF for Java شفرة برمجية مكونة من سطرين لتحويل ملف PDF المصدر إلى ملف DOC.

يوضح مقطع الشفرة البرمجية التالي بلغة Java عملية تحويل ملف PDF إلى تنسيق DOC.

```java
// Load PDF document
Document pdfDocument = new Document("input.pdf");

// Save the file into DOC format
pdfDocument.save("output.doc", SaveFormat.Doc);

1. إنشاء مثيل لكائن [Document](https://reference.aspose.com/page/java/com.aspose.page/document) مع وثيقة PDF المصدر.
2. حفظه بصيغة **SaveFormat.Doc** عن طريق استدعاء طريقة **Document.save()**.

```java
public static void convertPDFtoWord() {
    // افتح وثيقة PDF المصدر
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // احفظ الملف في صيغة مستند MS
    document.save(DATA_DIR + "PDFToDOC_out.doc", SaveFormat.Doc);
    document.close();
}
```

## استخدام فئة DocSaveOptions

توفر [فئة DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) العديد من الخصائص التي تحسن عملية تحويل ملفات PDF إلى صيغة DOC. من بين هذه الخصائص، تتيح لك Mode تحديد وضع التعرف على محتوى PDF. يمكنك تحديد أي قيمة من تعداد RecognitionMode لهذه الخاصية. لكل من هذه القيم فوائد وحدود معينة:

- وضع [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) سريع وجيد للحفاظ على الشكل الأصلي لملف PDF، لكن قد تكون إمكانية تعديل المستند الناتج محدودة.
 كل كتلة نصية مجمعة بصريًا في ملف PDF الأصلي تُحوَّل إلى مربع نص في مستند الإخراج. هذا يحقق تشابهًا أقصى مع الأصل بحيث يبدو مستند الإخراج جيدًا، ولكنه يتكون بالكامل من مربعات نصية وقد يجعل التحرير في Microsoft Word صعبًا.

- التدفق هو وضع التعرف الكامل، حيث يقوم المحرك بتجميع وتحليل متعدد المستويات لاستعادة المستند الأصلي كما قصد المؤلف مع إنتاج مستند سهل التحرير. القيد هو أن مستند الإخراج قد يبدو مختلفًا عن الأصل.

- يمكن استخدام خاصية RelativeHorizontalProximity للتحكم في القرب النسبي بين العناصر النصية وتعني أن المسافة تُقاس بحجم الخط. قد تحتوي الخطوط الأكبر على مسافات أكبر بين المقاطع الصوتية ولا تزال تعتبر ككل واحد. يتم تحديده كنسبة مئوية من حجم الخط، على سبيل المثال، 1 = 100%. هذا يعني أن حرفين بحجم 12 نقطة يتم وضعهما على بعد 12 نقطة يعتبران قريبين.

- يتم استخدام RecognitionBullets لتفعيل التعرف على النقاط أثناء التحويل.
```java
public static void convertPDFtoWordDocAdvanced() {
    Path pdfFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.pdf");
    Path docFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.doc");
    Document document = new Document(pdfFile.toString());
    DocSaveOptions saveOptions = new DocSaveOptions();

    // تحديد تنسيق الإخراج كـ DOC
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    // تعيين وضع التعرف كـ Flow
    saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);

    // تعيين القرب الأفقي كـ 2.5
    saveOptions.setRelativeHorizontalProximity(2.5f);

    // تمكين القيمة للتعرف على النقاط أثناء عملية التحويل
    saveOptions.setRecognizeBullets(true);

    document.save(docFile.toString(), saveOptions);
    document.close();
}
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**


تقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![تحويل PDF إلى DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## تحويل PDF إلى DOCX

يوفر تعداد DocFormat أيضًا خيار اختيار DOCX كصيغة إخراج لمستندات Word. لاستخراج ملف PDF المصدر إلى صيغة DOCX، استخدم مقتطف الشيفرة المحدد أدناه.

## كيفية تحويل PDF إلى DOCX

يظهر مقتطف الشيفرة Java التالي عملية تحويل ملف PDF إلى صيغة DOCX.

1. إنشاء مثيل لكائن [Document](https://reference.aspose.com/page/java/com.aspose.page/document) باستخدام مستند PDF المصدر.
2. احفظه بصيغة **SaveFormat.DocX** عن طريق استدعاء طريقة **Document.save()**.

```java
public static void convertPDFtoWord_DOCX_Format() {
    // افتح مستند PDF المصدر
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // احفظ الملف DOC الناتج
    document.save(DATA_DIR + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    document.close();
}
```

تحتوي فئة [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) على خاصية اسمها Format توفر القدرة على تحديد صيغة المستند الناتج، وهي DOC أو DOCX.
 من أجل تحويل ملف PDF إلى تنسيق DOCX، يرجى تمرير القيمة Docx من تعداد DocSaveOptions.DocFormat.

يرجى إلقاء نظرة على الشيفرة البرمجية التالية التي توفر القدرة على تحويل ملف PDF إلى تنسيق DOCX باستخدام Java.

```java
public static void convertPDFtoWord_Advanced_DOCX_Format() {
    // افتح مستند PDF المصدر
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");

    // إنشاء كائن DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions();
    // حدد تنسيق الإخراج كـ DOCX
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    // تعيين معلمات DocSaveOptions الأخرى
    // ....

    // احفظ المستند بتنسيق docx
    document.save("ConvertToDOCX_out.docx", saveOptions);
    document.close();
}
```

{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.
[![Aspose.PDF تطبيق مجاني لتحويل PDF إلى DOCX](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}