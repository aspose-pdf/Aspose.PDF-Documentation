---
title: احصل على خصائص الصفحة واضبطها
type: docs
weight: 30
url: /java/get-and-set-page-properties/
description: يشرح هذا الموضوع كيفية الحصول على الأرقام في ملف PDF، والحصول على خصائص الصفحة وتحديد لون الصفحة باستخدام Aspose.PDF لـ Java.
lastmod: "2021-06-05"
---

يتيح لك Aspose.PDF لـ Java قراءة وضبط خصائص الصفحات في ملف PDF في تطبيقات Java الخاصة بك. يوضح هذا القسم كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وضبط خصائص الصفحة.

## الحصول على عدد الصفحات في ملف PDF

عند العمل مع المستندات، غالبًا ما ترغب في معرفة عدد الصفحات التي تحتويها. مع Aspose.PDF، يستغرق هذا الأمر أكثر من سطرين من التعليمات البرمجية.

للحصول على عدد الصفحات في ملف PDF:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. ثم استخدم خاصية Count من مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) (من كائن المستند) للحصول على العدد الإجمالي للصفحات في المستند.

يوضح مقتطف الشيفرة التالي كيفية الحصول على عدد صفحات ملف PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // الحصول على عدد الصفحات
        System.out.println("عدد الصفحات : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### الحصول على عدد الصفحات دون حفظ المستند

ما لم يتم حفظ ملف PDF ووضع جميع العناصر فعليًا داخل ملف PDF، لا يمكننا الحصول على عدد الصفحات لمستند معين (لأننا لا يمكن أن نكون متأكدين من عدد الصفحات التي سيتم استيعاب جميع العناصر فيها).
 ومع ذلك، بدءًا من إصدار Aspose.PDF لـ Java 10.1.0، قمنا بإدخال طريقة تسمى [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) والتي توفر ميزة الحصول على عدد صفحات مستند PDF، دون حفظ الملف. لذلك يمكننا الحصول على معلومات عدد الصفحات فورًا. يرجى محاولة استخدام مقتطف الكود التالي لتحقيق هذا المتطلب.

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // إنشاء مثيل Document
        Document doc = new Document();
        // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
        Page page = doc.getPages().add();
        // إنشاء حلقة لإضافة 300 مثيل من TextFragment
        for (int i = 0; i < 300; i++)
            // إضافة TextFragment إلى مجموعة الفقرات في الصفحة الأولى من PDF
            page.getParagraphs().add(new TextFragment("اختبار عدد الصفحات"));
        // معالجة الفقرات للحصول على معلومات عدد الصفحات
        doc.processParagraphs();
        System.out.println("عدد الصفحات في PDF = " + doc.getPages().size());
    }
```

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF تحتوي على عدد من الخصائص، مثل العرض، الارتفاع، مساحات النزيف، القص والتشذيب. تتيح لك Aspose.PDF الوصول إلى هذه الخصائص.

### **فهم خصائص الصفحة: الفرق بين Artbox وBleedBox وCropBox وMediaBox وTrimBox وRect property**

- **Media box**: صندوق الوسائط هو أكبر صندوق صفحة. يتوافق مع حجم الصفحة (على سبيل المثال A4، A5، الرسالة الأمريكية، إلخ) التي تم اختيارها عندما تم طباعة المستند إلى PostScript أو PDF. بمعنى آخر، يحدد صندوق الوسائط الحجم الفعلي للوسائط التي يتم عرض أو طباعة مستند PDF عليها.
- **Bleed box**: إذا كان المستند يحتوي على نزيف، فإن ملف PDF سيحتوي أيضًا على صندوق نزيف.
 Bleed هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما بعد حافة الصفحة. يُستخدم لضمان أنه عند طباعة المستند وقصه إلى الحجم المطلوب ("التقليم")، سيصل الحبر إلى حافة الصفحة. حتى إذا تم قص الصفحة بشكل خاطئ - أي قصها قليلاً خارج علامات القص - فلن تظهر حواف بيضاء على الصفحة.
- **صندوق القص**: يشير صندوق القص إلى الحجم النهائي للمستند بعد الطباعة والتقليم.
- **صندوق الفن**: صندوق الفن هو الصندوق المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يُستخدم هذا الصندوق عند استيراد مستندات PDF في تطبيقات أخرى.
- **صندوق القصاصات**: هو حجم "الصفحة" الذي يُعرض عنده مستند PDF الخاص بك في Adobe Acrobat. في العرض العادي، تُعرض فقط محتويات صندوق القصاصات في Adobe Acrobat.
  للحصول على أوصاف مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وخاصة 10.10.1 حدود الصفحة.
- **Page.Rect**: التقاطع (المستطيل المرئي عادةً) بين MediaBox وDropBox. الصورة أدناه توضح هذه الخصائص.

لمزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### الوصول إلى خصائص الصفحة

توفر فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) جميع الخصائص المتعلقة بصفحة PDF معينة. جميع صفحات ملفات PDF موجودة في مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

من هناك، من الممكن الوصول إلى كائنات الصفحة الفردية باستخدام فهرسها، أو التجول عبر المجموعة باستخدام حلقة foreach للحصول على جميع الصفحات. بمجرد الوصول إلى صفحة معينة، يمكننا الحصول على خصائصها. يظهر مقتطف الشيفرة التالي كيفية الحصول على خصائص الصفحة.

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // احصل على مجموعة الصفحات
        PageCollection pageCollection = pdfDocument.getPages();

        // احصل على صفحة معينة
        Page pdfPage = pageCollection.get_Item(1);

        // احصل على خصائص الصفحة
        System.out.printf("\n ArtBox : Height = " + pdfPage.getArtBox().getHeight() + ", Width = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Height = " + pdfPage.getBleedBox().getHeight() + ", Width = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Height = " + pdfPage.getCropBox().getHeight() + ", Width = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Height = " + pdfPage.getMediaBox().getHeight() + ", Width = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Height = " + pdfPage.getTrimBox().getHeight() + ", Width = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Height = " + pdfPage.getRect().getHeight() + ", Width = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Page Number :- " + pdfPage.getNumber());
        System.out.printf("\n Rotate :-" + pdfPage.getRotate());
    }
```

## تحديد لون الصفحة

توفر فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) الخصائص المتعلقة بصفحة معينة في مستند PDF، بما في ذلك نوع اللون المستخدم في الصفحة - RGB، أبيض وأسود، تدرج رمادي أو غير محدد.

تحتوي مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) على جميع صفحات ملفات PDF. تحدد خاصية [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) لون العناصر في الصفحة. للحصول على أو تحديد معلومات اللون لصفحة PDF معينة، استخدم خاصية [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) لكائن فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

يظهر مقتطف الشيفرة التالي كيفية التكرار عبر كل صفحة فردية من ملف PDF للحصول على معلومات اللون.

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // تكرار جميع صفحات ملف PDF
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // احصل على معلومات نوع اللون لصفحة PDF معينة
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("الصفحة # -" + pageCount + " بالأبيض والأسود..");
                break;
            case 1:
                System.out.println("الصفحة # -" + pageCount + " تدرج الرمادي...");
                break;
            case 0:
                System.out.println("الصفحة # -" + pageCount + " RGB..");
                break;
            case 3:
                System.out.println("لون الصفحة # -" + pageCount + " غير محدد..");
                break;
            }
        }
    }
}
```