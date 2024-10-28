---
title: تحويل صيغ الملفات المختلفة إلى PDF
linktitle: تحويل صيغ الملفات الأخرى إلى PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيفية تحويل Aspose.PDF لصيغ الملفات الأخرى إلى مستند PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## تحويل EPUB إلى PDF

يتيح لك **Aspose.PDF for Java** ببساطة تحويل ملفات EPUB إلى صيغة PDF.

<abbr title="النشر الإلكتروني">EPUB</abbr> (اختصار للنشر الإلكتروني) هو معيار كتاب إلكتروني مجاني ومفتوح من المنتدى الدولي للنشر الرقمي (IDPF). الملفات تحمل الامتداد .epub. تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين.

من أجل تحويل ملفات EPUB إلى صيغة PDF، يحتوي Aspose.PDF for Java على فئة باسم [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) والتي تُستخدم لتحميل ملف EPUB المصدر.
 بعد ذلك، يتم تمرير الكائن كوسيطة لأداة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) لتهيئة الكائن، حيث يساعد محرك عرض PDF في تحديد تنسيق الإدخال للمستند المصدر.

يوضح مقتطف الشيفرة التالي عملية تحويل ملف EPUB إلى تنسيق PDF.

1. إنشاء كائن [`LoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions) لـ EPUB.
2. تهيئة كائن [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
3. حفظ مستند PDF الناتج.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // إنشاء كائن LoadOptions لـ EPUB
        EpubLoadOptions options = new EpubLoadOptions();

        // تهيئة كائن document
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // حفظ مستند PDF الناتج
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**حاول تحويل EPUB إلى PDF عبر الإنترنت**

تقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["EPUB إلى PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من EPUB إلى PDF باستخدام تطبيق مجاني](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## تحويل Markdown إلى PDF

**يتم دعم هذه الميزة بواسطة الإصدار 19.6 أو أكبر.**

{{% alert color="success" %}}
**حاول تحويل Markdown إلى PDF عبر الإنترنت**

تقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["Markdown إلى PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من Markdown إلى PDF باستخدام تطبيق مجاني](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown هو أداة لتحويل النص إلى HTML لمؤلفي الويب.
 Markdown يسمح لك بالكتابة بتنسيق نص عادي سهل القراءة والكتابة ثم تحويله إلى XHTML (أو HTML) صالح هيكليًا.

يظهر مقطع الشيفرة التالي كيفية استخدام هذه الوظيفة مع Aspose.PDF لـ Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // إنشاء كائن خيار تحميل Latex
        MdLoadOptions options = new MdLoadOptions();
        
        // إنشاء كائن المستند
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // حفظ مستند PDF الناتج
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}

```

## تحويل PCL إلى PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) هي لغة طابعة طورتها شركة Hewlett-Packard للوصول إلى ميزات الطابعة القياسية. مستويات PCL من 1 إلى 5e/5c هي لغات قائمة على الأوامر تستخدم تسلسلات التحكم التي تتم معالجتها وتفسيرها بالترتيب الذي يتم استلامها به. على مستوى المستهلك، يتم إنشاء تدفقات بيانات PCL بواسطة برنامج تشغيل الطابعة. يمكن أيضًا إنشاء مخرجات PCL بسهولة بواسطة التطبيقات المخصصة.

{{% alert color="success" %}}
**حاول تحويل PCL إلى PDF عبر الإنترنت**

تقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PCL إلى PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PCL إلى PDF بتطبيق مجاني](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**حاليًا، يتم دعم PCL5 والإصدارات الأقدم فقط.**

|**مجموعات الأوامر**|**الدعم**|**الاستثناءات**|**الوصف**|

| :- | :- | :- | :- |
|أوامر التحكم في الوظيفة|+|وضع الطباعة المزدوجة|التحكم في عملية الطباعة: عدد النسخ، صندوق الإخراج، الطباعة الفردية/المزدوجة، الإزاحات اليسرى والعلوية إلخ.|
|أوامر التحكم في الصفحة|+|أمر تخطي التثقيب|تحديد حجم الصفحة، الهوامش، اتجاه الصفحة، التباعد بين السطور، المسافات بين الحروف إلخ.|
|أوامر تحديد موضع المؤشر|+| |تحديد موضع المؤشر، وبالتالي، أصول النصوص، الصور النقطية أو المتجهة والتفاصيل.|

|أوامر اختيار الخطوط|+|<p>1. أمر بيانات الطباعة الشفافة.</p><p>2. الخطوط الناعمة المدمجة. في الإصدار الحالي بدلاً من إنشاء خط ناعم، تقوم مكتبتنا باختيار الخط المناسب من خطوط TrueType "الصلبة" الموجودة والمثبتة على الجهاز المستهدف. <br>   يتم تحديد الملاءمة بناءً على نسبة العرض/الارتفاع. <br>   هذه الميزة تعمل فقط للخطوط النقطية وخطوط TrueType ولا تضمن أن النص المطبوع بخط ناعم سيكون مطابقاً للنص في ملف المصدر. <br>   لأن رموز الحروف في الخط الناعم قد لا تتطابق مع الرموز الافتراضية.</p><p>3. مجموعات الرموز المعرفة من قبل المستخدم.</p>|السماح بتحميل الخطوط الناعمة (المضمنة) من ملف PCL وإدارتها في الذاكرة.|
|أوامر الرسومات النقطية|+|أبيض وأسود فقط|السماح بتحميل الصور النقطية من ملف PCL إلى الذاكرة، وتحديد معلمات النقطية <br>مثل العرض، الارتفاع، نوع الضغط، الدقة، إلخ.|
|أوامر الألوان|+| |السماح بالتلوين لجميع الكائنات القابلة للطباعة.|
|أوامر نموذج الطباعة|+| |السماح بملء النصوص، الصور النقطية والمناطق المستطيلة بأنماط نقطية محددة مسبقاً ومعرفة من قبل المستخدم، تحديد وضع الشفافية للأنماط والصورة النقطية المصدر.|
 <br>الأنماط المحددة مسبقًا هي التظليل، التهشير المتقاطع وتظليل الخطوط.|
|أوامر تعبئة منطقة المستطيل|+| |تسمح بإنشاء وتعبئة مناطق مستطيلة باستخدام الأنماط.|
|أوامر الرسومات الشعاعية HP-GL/2|+|أمر المتجهات المفروزة (SV)، أمر وضع الشفافية (TR)، أمر البيانات الشفافة (TD)، RO (نظام إحداثيات الدوران)، أمر الخطوط القابلة للتحجيم أو الخطوط النقطية (SB)، أمر انحراف الحرف (SL) والمساحة الإضافية (ES) غير منفذة و أوامر DV (تعريف مسار النص المتغير) محققة في النسخة التجريبية.|<p>- السماح بتحميل صور شعاعية HP-GL/2 من ملف PCL في الذاكرة. Vector image has an origin at the lower-left corner of the printable area, can be scaled, translated, rotated and clipped.</p><p>- يمكن أن تحتوي الصورة المتجهة على نص كعناوين وأشكال هندسية مثل المستطيل، الدائرة، القطع الناقص، الخط، القوس، المنحنى بيزييه والأشكال المعقدة المكونة من الأشكال البسيطة.</p><p>- يمكن ملء الأشكال المغلقة بما في ذلك حروف العناوين بملء صلب أو نمط متجه.</p><p>- يمكن أن يكون النمط تظليل، تظليل متقاطع، تظليل، نمط مستخدم محدد، تظليل PCL أو تظليل متقاطع وPCL مستخدم محدد. الأنماط PCL نقطية. يمكن تدوير العناوين بشكل فردي وتغيير حجمها وتوجيهها في أربعة اتجاهات: لأعلى ولأسفل ولليسار ولليمين. تتضمن الاتجاهات اليسرى واليمنى ترتيب الحروف واحدًا بعد الآخر. بينما تتضمن الاتجاهات العلوية والسفلية ترتيب الحروف واحدًا تحت الآخر.</p>|  
|Macross|―| |السماح بتحميل تسلسل من أوامر PCL في الذاكرة واستخدام هذا التسلسل عدة مرات، على سبيل المثال، لطباعة رأس الصفحة أو تعيين تنسيق واحد لمجموعة من الصفحات.|  
|Unicode text|―| |السماح بطباعة الأحرف غير الموجودة في ASCII.|   غير منفذ بسبب نقص ملفات العينة مع <br>نص Unicode|
|PCL6 (PCL-XL)| |تم تحقيقه فقط في الإصدار التجريبي بسبب نقص في ملفات الاختبار. الخطوط المدمجة غير مدعومة أيضًا. الامتداد JetReady غير مدعوم لأنه من المستحيل الحصول على مواصفات JetReady.|تنسيق ملف ثنائي.|

### تحويل ملف PCL إلى تنسيق PDF

للسماح بالتحويل من PCL إلى PDF، تحتوي [Aspose.PDF for Java](https://products.aspose.com/pdf/java) على الفئة [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) التي تُستخدم لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). يتم تمرير هذا الكائن كمعامل أثناء تهيئة كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) ويساعد محرك عرض PDF في تحديد تنسيق إدخال المستند المصدر.

يوضح مقطع الشيفرة التالي عملية تحويل ملف PCL إلى تنسيق PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPCLtoPDF {

    private ConvertPCLtoPDF() {
        
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {        
        ConvertPCLtoPDF_Simple();
        ConvertPCLtoPDF_Advanced();
    }

    public static void ConvertPCLtoPDF_Simple() {
        PclLoadOptions options = new PclLoadOptions();
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        pdfDocument.save(_dataDir + "epub_test.pdf");        
    }

    public static void ConvertPCLtoPDF_Advanced() {
        PclLoadOptions options = new PclLoadOptions();
        options.SupressErrors=true;
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        if (options.Exceptions!=null)
            for (Exception ex : options.Exceptions)
            {
                System.out.println(ex.getMessage());
            }
        pdfDocument.save(_dataDir + "pcl_test.pdf");        
    }
}
```

### المشاكل المعروفة

1. يمكن أن يختلف مصدر السلاسل النصية والصور قليلاً عن تلك الموجودة في ملف PCL المصدر إذا لم يكن اتجاه الطباعة 0 درجة. وينطبق الأمر نفسه على الصور المتجهة إذا كان نظام إحداثيات الرسم المتجه دوارًا (تم تقديم الأمر RO).
2. يمكن أن يختلف مصدر الملصقات في الصور المتجهة عن تلك الموجودة في ملف PCL المصدر إذا كانت الملصقات متأثرة بتسلسل الأوامر: مصدر الملصق (LO)، تحديد مسار النص المتغير (DV)، الاتجاه المطلق (DI) أو الاتجاه النسبي (DR).
3. يمكن أن يتم قراءة النص بشكل غير صحيح إذا كان يجب عرضه بخط Bitmap أو TrueType ناعم (مضمن)، لأن هذه الخطوط مدعومة حاليًا بشكل جزئي فقط (انظر الاستثناءات في "جدول الميزات المدعومة"). في هذه الحالة، يمكن قراءة النص بشكل صحيح فقط إذا كانت رموز الأحرف في الخط الناعم تتوافق مع الرموز الافتراضية. ويمكن أيضًا أن يختلف نمط النص المقروء عن الموجود في ملف PCL المصدر لأنه ليس من الضروري ضبط النمط في رأس الخط الناعم.

1. إذا كان ملف PCL المُحلل يحتوي على خطوط Intellifont أو خطوط ناعمة شاملة، فسيتم طرح استثناء، لأن خطوط Intellifont والخطوط الشاملة غير مدعومة على الإطلاق.
1. إذا كان ملف PCL المُحلل يحتوي على أوامر الماكرو، فإن نتيجة التحليل ستختلف بشكل كبير عن ملف المصدر، لأن أوامر الماكرو غير مدعومة.

## تحويل النص إلى PDF

يوفر **Aspose.PDF for Java** القدرة على تحويل ملفات النص إلى صيغة PDF. في هذه المقالة، نوضح كيف يمكننا بسهولة وكفاءة تحويل ملف نصي إلى PDF باستخدام Aspose.PDF.

عندما تحتاج إلى تحويل ملف نصي إلى PDF، قم بقراءة ملف النص المصدر في البداية باستخدام قارئ ما. لقد استخدمنا StringBuilder لقراءة محتويات ملف النص. قم بإنشاء كائن Document وأضف صفحة جديدة في مجموعة Pages. أنشئ كائنًا جديدًا من TextFragment ومرر كائن StringBuilder إلى منشئه. أضف فقرة جديدة في مجموعة Paragraphs باستخدام كائن TextFragment واحفظ ملف PDF الناتج باستخدام طريقة Save لفئة Document.
 **حاول تحويل النص إلى PDF عبر الإنترنت**

توفر لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["النص إلى PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF النص إلى PDF باستخدام التطبيق المجاني](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### تحويل ملف نصي عادي إلى PDF

```java
package com.aspose.pdf.examples;
/**
 * تحويل TXT إلى PDF
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // تهيئة كائن المستند

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // إنشاء كائن المستند عن طريق استدعاء منشئه الفارغ
        Document pdfDocument = new Document();

        // إضافة صفحة جديدة في مجموعة الصفحات للمستند
        Page page = pdfDocument.getPages().add();

        // إنشاء مثيل لـ TextFragment وتمرير النص من كائن القارئ إلى منشئه كمعامل
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // إضافة فقرة نص جديدة في مجموعة الفقرات وتمرير كائن TextFragment
        page.getParagraphs().add(text);

        // حفظ ملف PDF الناتج
        pdfDocument.save(pdfDocumentFileName);
    }
```


### تحويل ملف نصي مسبق التنسيق إلى PDF

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // قراءة الملف النصي كمصفوفة من السلاسل
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // إنشاء كائن Document باستدعاء منشئه الفارغ
        Document pdfDocument = new Document();

        // إضافة صفحة جديدة إلى مجموعة الصفحات في وثيقة
        Page page = pdfDocument.getPages().add();

        // ضبط الهوامش اليسرى واليمنى لتحسين العرض
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // التحقق مما إذا كانت السطر يحتوي على حرف "تغذية النموذج"
            // انظر https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // إنشاء مثيل من TextFragment و
                // تمرير السطر إلى
                // منشئه كوسيطة
                TextFragment text = new TextFragment(line);

                // إضافة فقرة نصية جديدة في مجموعة الفقرات وتمرير كائن TextFragment
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}
```


## تحويل XPS إلى PDF

**Aspose.PDF for Java** يدعم ميزة تحويل ملفات <abbr title="XML Paper Specification">XPS</abbr> إلى تنسيق PDF. تحقق من هذه المقالة لحل مهامك.

XPS، مواصفات ورق XML، هو تنسيق ملف من مايكروسوفت يُستخدم لدمج إنشاء المستندات وعرضها في ويندوز. مع Aspose.PDF for Java، من الممكن تحويل ملفات XPS إلى PDF، وهو تنسيق الملف المحمول من أدوبي.

تنسيق الملف هو في الأساس ملف XML مضغوط، يُستخدم أساسًا للتوزيع والتخزين. من الصعب جدًا تحريره ويتم تنفيذه بشكل رئيسي من قبل مايكروسوفت.

لتحويل ملف XPS إلى PDF باستخدام [Aspose.PDF for Java](https://products.aspose.com/pdf/java)، استخدم فئة [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 هذا يُستخدم لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). لاحقًا، يتم تمرير هذا الكائن كوسيطة خلال تهيئة كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) ويساعد محرك عرض PDF في تحديد تنسيق إدخال المستند المصدر.

في كل من XP وWindows 7، يجب أن تجد طابعة XPS مثبتة مسبقًا إذا نظرت في لوحة التحكم ثم الطابعات. لإنشاء ملفات XPS يمكنك استخدام تلك الطابعة كجهاز إخراج. في Windows 7، يجب أن تكون قادرًا على النقر المزدوج على الملف لفتحه في عارض XPS. يمكنك أيضًا تنزيل [عارض XPS](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer) من موقع Microsoft على الويب.

يوضح مقتطف الشيفرة التالي عملية تحويل ملف XPS إلى تنسيق PDF.

```java
public final class ConvertXPStoPDF {

    private ConvertXPStoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // تهيئة كائن المستند

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();

        // إنشاء كائن LoadOption باستخدام خيار تحميل XPS
        LoadOptions options = new XpsLoadOptions();

        // إنشاء كائن Document باستدعاء منشئه الفارغ
        Document pdfDocument = new Document(xpsDocumentFileName, options);

        // حفظ ملف PDF الناتج
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

{{% alert color="success" %}}
**حاول تحويل تنسيق XPS إلى PDF عبر الإنترنت**

Aspose.PDF لـ Java يقدم لك تطبيق مجاني عبر الإنترنت ["XPS إلى PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من XPS إلى PDF باستخدام تطبيق مجاني](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## تحويل PostScript إلى PDF

يدعم **Aspose.PDF لـ Java** ميزات تحويل ملفات PostScript إلى تنسيق PDF. واحدة من الميزات في Aspose.PDF هي أنه يمكنك تعيين مجموعة من مجلدات الخطوط لاستخدامها أثناء التحويل.

من أجل تحويل ملف PostScript إلى تنسيق PDF، يوفر Aspose.PDF لـ Java فئة [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) التي تُستخدم لتهيئة كائن LoadOptions. يمكن لاحقًا تمرير هذا الكائن كمعامل إلى مُنشئ كائن Document، مما سيساعد محرك عرض PDF في تحديد تنسيق المستند المصدر.


Following code snippet can be used to convert a PostScript file into PDF format:

```java
public static void ConvertPostScriptToPDF_Simple(){
        // تهيئة كائن المستند

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // إنشاء كائن المستند
        Document document = new Document(psDocumentFileName, options);

        // حفظ مستند PDF الناتج
        document.save(pdfDocumentFileName);
    }
```

Additionally, you can set a set of font folders that will be used during conversion:

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // إنشاء كائن المستند
        Document document = new Document(psDocumentFileName, options);

        // حفظ مستند PDF الناتج
        document.save(pdfDocumentFileName);
    }
```


## تحويل XML إلى PDF

يُستخدم تنسيق XML لتخزين البيانات المهيكلة. هناك عدة طرق لتحويل <abbr title="Extensible Markup Language">XML</abbr> إلى PDF في Aspose.PDF.

{{% alert color="success" %}}
**حاول تحويل XML إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)، حيث يمكنك تجربة التحقيق في الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل XML إلى PDF باستخدام التطبيق المجاني](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

النظر في الخيار باستخدام مستند XML بناءً على معيار XSL-FO.

### تحويل XSL-FO إلى PDF

يمكن تنفيذ تحويل ملفات XSL-FO إلى PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) مع [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```java
package com.aspose.pdf.examples;
/**
 * تحويل XML إلى PDF
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // تهيئة كائن المستند

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // إنشاء كائن Document من خلال استدعاء منشئه الفارغ
        Document pdfDocument = new Document(xmlDocumentFileName, options);

        // حفظ ملف PDF الناتج
        pdfDocument.save(pdfDocumentFileName);
    }
}
```


### تحويل XSL-FO إلى PDF مع تعيين استراتيجية معالجة الأخطاء

```java
// تهيئة كائن المستند

String documentFileName = Paths.get(DATA_DIR.toString(), "demo_txt.pdf").toString();
String xmlDocumentFileName = Paths.get(DATA_DIR.toString(), "demo.xml").toString();
String xsltDocumentFileName = Paths.get(DATA_DIR.toString(), "employees.xslt").toString();

XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

// تعيين استراتيجية معالجة الأخطاء
options.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);

// إنشاء كائن Document باستدعاء منشئه الفارغ
Document document = new Document(xmlDocumentFileName, options);

// حفظ ملف PDF الناتج
document.save(documentFileName);
document.close();
```

## تحويل LaTeX/TeX إلى PDF

تنسيق ملف LaTeX هو تنسيق ملف نصي يحتوي على ترميز في مشتق LaTeX لعائلة لغات TeX، وLaTeX هو تنسيق مشتق من نظام TeX.
 LaTeX (ˈleɪtɛk/ lay-tek or lah-tek) هو نظام إعداد مستندات ولغة ترميز مستندات. يُستخدم على نطاق واسع في التواصل ونشر المستندات العلمية في العديد من المجالات، بما في ذلك الرياضيات، الفيزياء، وعلوم الكمبيوتر. كما أن له دور بارز في إعداد ونشر الكتب والمقالات التي تحتوي على مواد متعددة اللغات ومعقدة، مثل السنسكريتية والعربية، بما في ذلك الطبعات النقدية. يستخدم LaTeX برنامج تنضيد TeX لتنسيق مخرجاته وهو مكتوب بنفسه بلغة الماكرو TeX.

**Aspose.PDF for Java** يدعم ميزة تحويل ملفات TeX إلى تنسيق PDF ولتحقيق هذا المتطلب، يحتوي حزمة com.aspose.pdf على فئة اسمها [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) والتي توفر إمكانيات تحميل ملفات LaTeX وعرض المخرجات بتنسيق PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). يعرض مقطع الشيفرة التالي عملية تحويل ملف LaTex إلى تنسيق PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // إنشاء كائن خيار تحميل Latex
        TeXLoadOptions options = new TeXLoadOptions();
        
        // إنشاء كائن المستند
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // حفظ مستند PDF الناتج
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**حاول تحويل LaTeX/TeX إلى PDF عبر الإنترنت**

تقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.
[![Aspose.PDF تحويل LaTeX/TeX إلى PDF مع تطبيق مجاني](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}