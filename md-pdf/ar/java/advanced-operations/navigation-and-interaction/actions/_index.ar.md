---
title: العمل مع الإجراءات
linktitle: الإجراءات
type: docs
weight: 20
url: /java/actions/
description: يشرح هذا القسم كيفية إضافة الإجراءات إلى المستند وحقول النموذج برمجيًا باستخدام Java. تعلم كيفية إضافة، إنشاء، والحصول على الارتباط التشعبي في ملف PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكن أن يحتوي ملف PDF على مرفقات ملفات مدمجة وغالبًا ما يكون من الضروري إنشاء ارتباط تشعبي لهذه المستندات. يمكنك توجيه القراء من مستند PDF الرئيسي إلى مرفق PDF عن طريق إنشاء رابط في المستند الرئيسي يشير إلى المرفق.

## إضافة ارتباط تشعبي في ملف PDF

من الممكن إضافة روابط تشعبية إلى ملفات PDF، إما للسماح للقراء بالتنقل إلى جزء آخر من ملف PDF، أو إلى محتوى خارجي.

لإضافة روابط تشعبية إلى مستندات PDF:

1. قم بإنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. احصل على فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) التي تريد إضافة الرابط إليها.
1. قم بإنشاء كائن [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) باستخدام كائنات Page و[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle). يتم استخدام كائن المستطيل لتحديد الموقع على الصفحة حيث يجب إضافة الرابط.
1. اضبط طريقة getAction على كائن [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction) الذي يحدد موقع URI البعيد.
1. لعرض نص الارتباط التشعبي، أضف سلسلة نصية على موقع مشابه للمكان الذي يوجد به كائن [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation).
1. لإضافة نص حر:

- قم بإنشاء كائن [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation).
 It أيضًا يقبل كائنات Page و Rectangle كمعامل، لذلك من الممكن توفير نفس القيم كما هو محدد في منشئ LinkAnnotation.
- باستخدام خاصية Contents لكائن [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation)، حدد السلسلة التي يجب عرضها في ملف PDF الناتج.
- اختياريًا، قم بتعيين عرض الحدود لكل من كائنات [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) و FreeTextAnnotation إلى 0 حتى لا تظهر في وثيقة PDF.
- بمجرد تحديد كائنات [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) و [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation)، أضف هذه الروابط إلى مجموعة التعليقات التوضيحية لكائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

- أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة Save لكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
The following code snippet shows you how to add a hyperlink to a PDF file.

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // فتح المستند
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // إنشاء رابط
        Page page = document.getPages().get_Item(1);
        // إنشاء كائن تعليقات توضيحية للرابط
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // إنشاء كائن الحدود لتعليقات التوضيح للرابط
        Border border = new Border(link);
        // ضبط قيمة عرض الحدود على 0
        border.setWidth(0);
        // ضبط الحدود لتعليقات التوضيح للرابط
        link.setBorder(border);
        // تحديد نوع الرابط كـ URI بعيد
        link.setAction(new GoToURIAction("www.aspose.com"));
        // إضافة تعليق توضيحي للرابط إلى مجموعة التعليقات التوضيحية للصفحة الأولى من ملف PDF
        page.getAnnotations().add(link);

        // إنشاء تعليق توضيحي للنص الحر
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // سلسلة لإضافتها كنص حر
        textAnnotation.setContents("رابط إلى موقع Aspose");
        // ضبط الحدود لتعليقات التوضيح للنص الحر
        textAnnotation.setBorder(border);
        // إضافة تعليق توضيحي للنص الحر إلى مجموعة التعليقات التوضيحية للصفحة الأولى من المستند
        page.getAnnotations().add(textAnnotation);

        // حفظ المستند المحدث
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```


## إنشاء رابط للصفحات في نفس ملف PDF

يوفر Aspose.PDF for Java ميزة رائعة لإنشاء ملفات PDF وكذلك التلاعب بها. كما يقدم ميزة إضافة روابط لصفحات PDF ويمكن أن يوجه الرابط إما إلى صفحات في ملف PDF آخر، أو إلى عنوان URL على الويب، أو رابط لبدء تطبيق أو حتى رابط لصفحات في نفس ملف PDF.

لإضافة الارتباط المحلي، نحتاج إلى إنشاء TextFragment بحيث يمكن ربط الرابط بـ TextFragment. تحتوي فئة [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) على دالة تسمى [getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--) والتي تُستخدم لربط مثيل LocalHyperlink. يوضح المقتطف البرمجي التالي الخطوات اللازمة لتحقيق هذا المتطلب.

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // إنشاء مثيل للمستند
        Document document = new Document();

        // إضافة صفحة إلى مجموعة صفحات ملف PDF
        Page page = document.getPages().add();

        // إنشاء مثيل لجزء النص
        TextFragment text = new TextFragment("رابط اختبار رقم الصفحة إلى الصفحة 2");

        // إنشاء مثيل للارتباط المحلي
        LocalHyperlink link = new LocalHyperlink();

        // تعيين الصفحة المستهدفة لمثيل الرابط
        link.setTargetPageNumber(2);

        // ضبط الارتباط لجسم TextFragment
        text.setHyperlink(link);

        // إضافة النص إلى مجموعة الفقرات في الصفحة
        page.getParagraphs().add(text);

        // إنشاء مثيل جديد لجزء النص
        text = new TextFragment("رابط اختبار رقم الصفحة إلى الصفحة 1");

        // يجب إضافة TextFragment على صفحة جديدة
        text.setInNewPage(true);

        // إنشاء مثيل آخر للارتباط المحلي
        link = new LocalHyperlink();

        // تعيين الصفحة المستهدفة للارتباط الثاني
        link.setTargetPageNumber(1);

        // تعيين الرابط لجزء النص الثاني
        text.setHyperlink(link);

        // إضافة النص إلى مجموعة الفقرات في كائن الصفحة
        page.getParagraphs().add(text);

        // حفظ المستند المحدث
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```


## الحصول على وجهة رابط PDF (URL)

يتم تمثيل الروابط كتعليقات توضيحية في ملف PDF ويمكن إضافتها أو تحديثها أو حذفها. كما يدعم Aspose.PDF for Java الحصول على وجهة (URL) الرابط في ملف PDF.

للحصول على URL للرابط:

1. أنشئ كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. احصل على [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) الذي تريد استخراج الروابط منه.
1. استخدم فئة [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) لاستخراج جميع كائنات [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) من الصفحة المحددة.
1. مرر كائن [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) إلى طريقة Accept لكائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

1. احصل على جميع التعليقات التوضيحية للروابط المحددة في كائن IList باستخدام خاصية Selected لكائن [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector).
1. أخيرًا، استخرج عمل LinkAnnotation كـ GoToURIAction.

يظهر مقتطف الكود التالي كيفية الحصول على وجهات الارتباط التشعبي (URL) من ملف PDF.

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // استخراج الإجراءات
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // التكرار عبر العناصر الفردية داخل القائمة
        if (list.size() == 0)
            System.out.println("No Hyperlinks found..");
        else {
            // التكرار عبر جميع العلامات المرجعية
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // طباعة عنوان URL الوجهة
                    System.out.println("Destination: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // نهاية else
    }
```


## الحصول على نص الرابط التشعبي

يتكون الرابط التشعبي من جزئين: النص الذي يظهر في المستند، وعنوان URL الوجهة. في بعض الحالات، يكون النص هو الذي نحتاجه بدلاً من عنوان URL.

يتم تمثيل النص والتعليقات التوضيحية/الإجراءات في ملف PDF بواسطة كيانات مختلفة. النص في الصفحة هو مجرد مجموعة من الكلمات والحروف، بينما تجلب التعليقات التوضيحية بعض التفاعلية مثل تلك الموجودة في الرابط التشعبي.

للعثور على محتوى عنوان URL، تحتاج إلى العمل مع كل من التعليق التوضيحي والنص. كائن [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) لا يحتوي على النص بنفسه ولكنه يقع تحت النص في الصفحة. لذا للحصول على النص، يعطي التعليق التوضيحي حدود عنوان URL، بينما يعطي كائن النص محتويات عنوان URL. يرجى الاطلاع على مقتطف الشيفرة التالي.

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // استخراج الإجراءات
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // طباعة عنوان URL لكل تعليق توضيحي للرابط
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // طباعة النص المرتبط بالرابط التشعبي
                System.out.println(extractedText);
            }
        }
    }
```


## إزالة إجراء فتح المستند من ملف PDF

[كيفية تحديد صفحة PDF عند عرض المستند](#how-to-specify-pdf-page-when-viewing-document) أوضحت كيفية إخبار المستند بفتحه على صفحة مختلفة عن الأولى. عند دمج عدة مستندات، وإذا كان أحدها أو أكثر يحتوي على إجراء GoTo مضبوط، فمن المحتمل أنك تريد إزالتها. على سبيل المثال، إذا تم دمج مستندين وكان المستند الثاني يحتوي على إجراء GoTo يأخذك إلى الصفحة الثانية، فسيتم فتح المستند الناتج على الصفحة الثانية من المستند الثاني بدلاً من الصفحة الأولى من المستند المدمج. لتجنب هذا السلوك، قم بإزالة أمر فتح الإجراء.

لإزالة إجراء الفتح:

1. قم بتعيين طريقة [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) إلى null.
2. احفظ ملف PDF المحدث باستخدام طريقة Save الخاصة بكائن Document.

يظهر مقطع الشيفرة التالي كيفية إزالة إجراء فتح المستند من ملف PDF.

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // افتح المستند
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // إزالة إجراء فتح المستند
        document.setOpenAction(null);
        
        // احفظ المستند المحدث
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```


## كيفية تحديد صفحة PDF عند عرض المستند {#how-to-specify-pdf-page-when-viewing-document}

عند عرض ملفات PDF في عارض PDF مثل Adobe Reader، تفتح الملفات عادةً على الصفحة الأولى. ومع ذلك، من الممكن ضبط الملف ليفتح على صفحة مختلفة.

تسمح لك فئة [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) بتحديد صفحة في ملف PDF تريد فتحها. عند تمرير قيمة كائن GoToAction إلى طريقة getOpenAction لفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)، يفتح المستند في الصفحة المحددة ضد كائن XYZExplicitDestination. يوضح مقتطف الشفرة التالي كيفية تحديد صفحة كإجراء فتح المستند.

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // تحميل ملف PDF
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // الحصول على مثيل الصفحة الثانية من المستند
        Page page2 = document.getPages().get_Item(2);
        // إنشاء متغير لتعيين عامل التكبير للصفحة المستهدفة
        double zoom = 1;
        // إنشاء مثيل GoToAction
        GoToAction action = new GoToAction(page2);
        // الانتقال إلى الصفحة الثانية
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // تعيين إجراء فتح المستند
        document.setOpenAction (action);
        // حفظ المستند المحدث
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```