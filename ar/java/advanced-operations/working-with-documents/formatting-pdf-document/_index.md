---
title: تنسيق مستند PDF 
linktitle: تنسيق مستند PDF
type: docs
weight: 20
url: ar/java/formatting-pdf-document/
description: تنسيق مستند PDF باستخدام Aspose.PDF لـ Java. استخدم المقتطف التالي من الكود لحل مهامك.
lastmod: "2021-06-05"
---

## الحصول على خصائص نافذة المستند وعرض الصفحات

هذا الموضوع يساعدك على فهم كيفية الحصول على خصائص نافذة المستند، تطبيق العارض، وكيفية عرض الصفحات.

لتعيين هذه الخصائص المختلفة، افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). يمكنك الآن الحصول على طرق [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مثل

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – تمركز نافذة المستند على الشاشة. الافتراضي: خطأ.
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – ترتيب القراءة.
 هذا يحدد كيفية ترتيب الصفحات عند عرضها جنبًا إلى جنب. الافتراضي: من اليسار إلى اليمين.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – عرض عنوان المستند في شريط عنوان نافذة المستند. الافتراضي: false (يتم عرض العنوان).
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – إخفاء أو عرض شريط القوائم في نافذة المستند. الافتراضي: false (يتم عرض شريط القوائم).
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – إخفاء أو عرض شريط الأدوات في نافذة المستند. الافتراضي: false (يتم عرض شريط الأدوات).
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – إخفاء أو عرض عناصر نافذة المستند مثل أشرطة التمرير. الافتراضي: false (يتم عرض عناصر واجهة المستخدم).

- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – كيفية عرض المستند عندما لا يتم عرضه في وضع الصفحة الكاملة.- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – تخطيط الصفحة.
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – كيفية عرض المستند عند فتحه لأول مرة. الخيارات هي عرض الصور المصغرة، ملء الشاشة، عرض لوحة المرفقات.

يوضح لك مقطع الشيفرة التالي كيفية الحصول على الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // افتح المستند
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // الحصول على خصائص المستند المختلفة
    // موضع نافذة المستند - الافتراضي: false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // ترتيب القراءة السائد؛ تحديد موضع الصفحة
    // عند العرض جنبًا إلى جنب - الافتراضي: L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // ما إذا كان شريط العنوان في النافذة يجب أن يعرض عنوان المستند.
    // إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // ما إذا كان يجب تغيير حجم نافذة المستند لتلائم حجم
    // الصفحة المعروضة أولاً - الافتراضي: false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // ما إذا كان يجب إخفاء شريط القوائم في تطبيق العارض - الافتراضي: false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // ما إذا كان يجب إخفاء شريط الأدوات في تطبيق العارض - الافتراضي: false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
    // وترك محتويات الصفحة فقط معروضة - الافتراضي: false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // وضع الصفحة في المستند. كيفية عرض المستند عند الخروج
    // من وضع ملء الشاشة.
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // تخطيط الصفحة أي صفحة واحدة، عمود واحد
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // كيفية عرض المستند عند فتحه.
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```

## ضبط نافذة المستند وخصائص عرض الصفحة

يشرح هذا الموضوع كيفية ضبط خصائص نافذة المستند، وتطبيق العارض، وعرض الصفحة.

لضبط هذه الخصائص المختلفة:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. قم بضبط خصائص كائن المستند.
3. احفظ ملف PDF المحدث باستخدام طريقة Save.

الخصائص المتاحة هي:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

يظهر لك مقتطف الشيفرة التالي كيفية تعيين الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // فتح المستند
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    
    // تعيين خصائص مختلفة للمستند
    // تحديد موضع نافذة المستند - الافتراضي: false
    pdfDocument.setCenterWindow(true);
    
    // اتجاه القراءة السائد؛ تحديد موضع الصفحة
    // عند العرض جنبًا إلى جنب - الافتراضي: L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);
    
    // تحديد ما إذا كان شريط عنوان النافذة يجب أن يعرض عنوان المستند
    // إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
    pdfDocument.setDisplayDocTitle(true);
    
    // تحديد ما إذا كان يجب تغيير حجم نافذة المستند لتناسب حجم
    // الصفحة الأولى المعروضة - الافتراضي: false
    pdfDocument.setFitWindow(true);
    
    // تحديد ما إذا كان يجب إخفاء شريط القوائم في تطبيق العارض - الافتراضي:
    // false
    pdfDocument.setHideMenubar(true);
    
    // تحديد ما إذا كان يجب إخفاء شريط الأدوات في تطبيق العارض - الافتراضي:
    // false
    pdfDocument.setHideToolBar(true);
    
    // تحديد ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
    // وعرض محتويات الصفحة فقط - الافتراضي: false
    pdfDocument.setHideWindowUI(true);
    
    // وضع صفحة المستند. تحديد كيفية عرض المستند عند الخروج
    // من وضع ملء الشاشة.
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);
    
    // تحديد تخطيط الصفحة أي صفحة واحدة، عمود واحد
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);
    
    // تحديد كيفية عرض المستند عند فتحه
    // أي عرض الصور المصغرة، ملء الشاشة، عرض لوحة المرفقات
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);
    
    // حفظ ملف PDF المحدث
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```

## تضمين الخطوط في ملف PDF موجود

يدعم قارئو PDF [مجموعة من 14 خطًا](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) بحيث يمكن عرض المستندات بنفس الطريقة بغض النظر عن النظام الأساسي الذي يتم عرض المستند عليه. عندما يحتوي ملف PDF على خط خارج الخطوط الأساسية، قم بتضمين الخط لتجنب استبدال الخط.

يدعم Aspose.PDF for Java تضمين الخطوط في مستندات PDF الموجودة. يمكنك تضمين خط كامل أو جزء منه. لتضمين الخط:

1. افتح ملف PDF موجود باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. استخدم فئة [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) لتضمين الخط.
   1. تقوم طريقة setEmbedded(true) بتضمين الخط الكامل.
   1. تقوم طريقة pageFont.isSubset(true) بتضمين جزء من الخط.

يقوم جزء من الخط بتضمين الأحرف المستخدمة فقط ويكون مفيدًا حيث يتم استخدام الخطوط لجمل قصيرة أو شعارات، على سبيل المثال حيث يتم استخدام خط الشركة لشعار ولكن ليس لنص الجسم.
 استخدام مجموعة فرعية يقلل من حجم ملف PDF الناتج.

ومع ذلك، إذا تم استخدام خط مخصص لنص الجسم، قم بتضمينه بالكامل.

يوضح مقطع الشيفرة التالي كيفية تضمين خط في ملف PDF.
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // فتح المستند
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // تكرار عبر جميع الصفحات
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // التحقق مما إذا كان الخط مضمن بالفعل
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // التحقق من كائنات النموذج
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // التحقق مما إذا كان الخط مضمن
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // حفظ ملف PDF المحدث
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## تضمين الخطوط أثناء إنشاء ملف PDF

إذا كنت بحاجة إلى استخدام أي خط آخر غير الخطوط الأساسية الأربعة عشر المدعومة من قبل Adobe Reader، فيجب تضمين وصف الخط أثناء إنشاء ملف PDF. إذا لم تكن معلومات الخط مضمنة، فسيأخذها Adobe Reader من نظام التشغيل إذا كان مثبتًا على النظام، أو سيقوم ببناء خط بديل وفقًا لوصف الخط في الـ PDF. يرجى ملاحظة أن الخط المضمن يجب أن يكون مثبتًا على الجهاز المضيف، أي في حالة الكود التالي، الخط 'Univers Condensed' مثبت على النظام.

نستخدم خاصية setEmbedded من فئة [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) لتضمين معلومات الخط في ملف PDF. تعيين قيمة هذه الخاصية إلى 'true' سيتضمن ملف الخط بالكامل في الـ PDF، مع العلم أن هذا سيزيد من حجم ملف الـ PDF. فيما يلي مقتطف الكود الذي يمكن استخدامه لتضمين معلومات الخط في الـ PDF.

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // إنشاء كائن PDF باستدعاء منشئه الفارغ
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // إنشاء قسم في كائن الـ PDF
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" هذا نص تجريبي يستخدم خط مخصص.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // حفظ ملف PDF المحدث
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## تعيين اسم الخط الافتراضي عند حفظ PDF

عندما يحتوي مستند PDF على خطوط غير متوفرة في المستند نفسه وعلى الجهاز، يقوم API باستبدال هذه الخطوط بالخط الافتراضي. عندما يكون الخط متوفرًا (مثبتًا على الجهاز أو مدمجًا في المستند)، يجب أن يحتوي ملف PDF الناتج على نفس الخط (لا يجب استبداله بالخط الافتراضي). يجب أن تحتوي قيمة الخط الافتراضي على اسم الخط (وليس مسار ملفات الخط). لقد قمنا بتنفيذ ميزة لتعيين اسم الخط الافتراضي عند حفظ المستند كملف PDF. يمكن استخدام المقتطف البرمجي التالي لتعيين الخط الافتراضي:

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // تحميل مستند PDF موجود
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // تهيئة خيارات الحفظ لصيغة PDF
    PdfSaveOptions ops = new PdfSaveOptions();

    // تعيين اسم الخط الافتراضي
    ops.setDefaultFontName(newName);

    // حفظ ملف PDF
    document.save(_dataDir + "output_out.pdf", ops);
  }
```


## الحصول على جميع الخطوط من مستند PDF

في حال كنت ترغب في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام طريقة **Document.getFontUtilities().getAllFonts()** المقدمة في فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). يرجى الاطلاع على مقتطف الشيفرة التالي للحصول على جميع الخطوط من مستند PDF موجود:

```java
public static void GetAllFontsFromPDFDocument() {

    // تحميل مستند PDF موجود
    Document document = new Document(_dataDir + "sample.pdf");

    // الحصول على جميع الخطوط من المستند
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```

## الحصول على وتعيين عامل التكبير لملف PDF

أحيانًا، ترغب في تعيين أو الحصول على عامل التكبير لمستند PDF. يمكنك تحقيق هذا المتطلب بسهولة باستخدام Aspose.PDF.

كائن [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) يسمح لك بالحصول على قيمة التكبير المرتبطة بملف PDF.
 Similarly, it can be used to set a file's Zoom factor.

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // تحميل مستند PDF موجود
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // تحديد عامل التكبير للمستند
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // تحديد الإجراء ليتناسب مع عرض الصفحة
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // تحديد الإجراء ليتناسب مع ارتفاع الصفحة
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

The following code snippet shows how to get the Zoom factor of a PDF file.

```java
    // إنشاء كائن Document جديد
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // إنشاء كائن GoToAction
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // الحصول على نسبة التكبير لملف PDF
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // حفظ ملف PDF المحدث
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```