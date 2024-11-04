---
title: تحويل ملف PDF إلى صيغ أخرى 
linktitle: تحويل PDF إلى صيغ أخرى 
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لتحويل ملف PDF إلى صيغ ملفات أخرى.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF إلى EPUB

{{% alert color="success" %}}
**حاول تحويل PDF إلى EPUB عبر الإنترنت**

تقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى EPUB باستخدام التطبيق المجاني](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="النشر الإلكتروني">EPUB</abbr>** (اختصار للنشر الإلكتروني) هو معيار كتاب إلكتروني مجاني ومفتوح من المنتدى الدولي للنشر الرقمي (IDPF).
 ملفات لها الامتداد .epub. تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين. كما يدعم EPUB المحتوى ذو التخطيط الثابت. يُقصد من هذا التنسيق أن يكون صيغة واحدة يمكن للناشرين وبيوت التحويل استخدامها داخليًا، وكذلك للتوزيع والبيع. يحل محل معيار Open eBook.

يدعم Aspose.PDF for Java ميزة تحويل مستندات PDF إلى تنسيق EPUB. يحتوي Aspose.PDF for Java على فئة تسمى [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) والتي يمكن استخدامها كحجة ثانية لطريقة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..)، لتوليد ملف EPUB. يرجى محاولة استخدام مقطع الشيفرة التالي لتحقيق هذا المطلب.

```java
// تحميل مستند PDF
Document document = new Document(DATA_DIR + "PDFToEPUB.pdf");
// إنشاء خيارات حفظ Epub
EpubSaveOptions options = new EpubSaveOptions();
// تحديد التخطيط للمحتويات
options.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
// حفظ مستند ePUB
document.save(DATA_DIR + "PDFToEPUB_out.epub", options);
document.close();
```

## تحويل PDF إلى LaTeX/TeX

**Aspose.PDF for Java** تدعم تحويل PDF إلى LaTeX/TeX. 
تنسيق ملف LaTeX هو تنسيق ملف نصي مع تعليمات تنسيق خاصة ويستخدم في نظام إعداد المستندات المستند على TeX للطباعة عالية الجودة.

لتحويل ملفات PDF إلى TeX، يحتوي Aspose.PDF على الفئة [TeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions) التي توفر الطريقة `setOutDirectoryPath` لحفظ الصور المؤقتة أثناء عملية التحويل.

يُظهر المقتطف البرمجي التالي عملية تحويل ملفات PDF إلى تنسيق TEX باستخدام Java.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX.pdf").toString();
String texDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX_out.tex").toString();

// إنشاء كائن Document
Document document = new Document(documentFileName);

// إنشاء خيار حفظ LaTex
TeXSaveOptions saveOptions = new TeXSaveOptions();

// تحديد دليل الإخراج
String pathToOutputDirectory = DATA_DIR.toString();

// تعيين مسار دليل الإخراج لكائن خيار الحفظ
saveOptions.setOutDirectoryPath(pathToOutputDirectory);

// حفظ ملف PDF بتنسيق LaTex
document.save(texDocumentFileName, saveOptions);
document.close();
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى LaTeX/TeX مع تطبيق مجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## تحويل PDF إلى نص

يدعم **Aspose.PDF for Java** تحويل مستند PDF بالكامل وصفحة واحدة إلى ملف نصي.

### تحويل مستند PDF بالكامل إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام طريقة Visit من فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

يوضح مقتطف الشيفرة التالي كيفية استخراج النصوص من جميع الصفحات.

```java
// فتح المستند
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// تحميل مستند PDF
Document document = new Document(pdfFileName);
TextAbsorber ta = new TextAbsorber();
ta.visit(document);
// حفظ النص المستخرج في ملف نصي
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى نص عبر الإنترنت**

تقدم Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى نص"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك تجربة التحقيق في الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى نص باستخدام تطبيق مجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### تحويل صفحة PDF إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام Aspose.PDF for Java. يجب عليك استخدام طريقة Visit من فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) لحل هذه المهمة.

يشرح مقطع الشيفرة التالي كيفية استخراج النصوص من الصفحات المحددة.

```java
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// تحميل مستند PDF
Document document = new Document(pdfFileName);

TextAbsorber ta = new TextAbsorber();
int[] pages = new int[] { 1, 3, 4 };

for (int page : pages) {
    ta.visit(document.getPages().get_Item(page));
}

// احفظ النص المستخرج في ملف نصي
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
document.close();
```


## تحويل PDF إلى XPS

يعطي **Aspose.PDF for Java** إمكانية تحويل ملفات PDF إلى صيغة <abbr title="XML Paper Specification">XPS</abbr>. دعونا نحاول استخدام الشيفرة المقدمة لتحويل ملفات PDF إلى صيغة XPS باستخدام Java.

{{% alert color="success" %}}
**حاول تحويل PDF إلى XPS عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى XPS باستخدام التطبيق المجاني](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

نوع ملف XPS مرتبط بشكل رئيسي بمواصفات ورق XML من قبل شركة Microsoft Corporation. مواصفات ورق XML (XPS)، التي كانت تسمى سابقًا كودًا Metro وتحتوي على مفهوم التسويق Next Generation Print Path (NGPP)، هي مبادرة من Microsoft لدمج إنشاء المستندات وعرضها في نظام التشغيل Windows.

لتحويل ملفات PDF إلى XPS، يحتوي Aspose.PDF على فئة [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) التي تُستخدم كوسيطة ثانية لمنشئ Document.save(..) لتوليد ملف XPS.
 يُظهر مقطع الشيفرة التالي عملية تحويل ملفات PDF إلى تنسيق XPS.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(DATA_DIR.toString(), "sample-res-xps.xps").toString();

// إنشاء كائن المستند
Document document = new Document(documentFileName);

// إنشاء خيارات الحفظ بصيغة XPS
XpsSaveOptions saveOptions = new XpsSaveOptions();

// حفظ الناتج بتنسيق XML
document.save(xpsDocumentFileName, saveOptions);
document.close();
```