---
title: PDF Multimedia Annotation 
linktitle: Multimedia Annotation
type: docs
weight: 40
url: /ar/java/multimedia-annotation/
description: يسمح لك Aspose.PDF for Java بإضافة وتعليم وحذف التعليقات التوضيحية متعددة الوسائط من مستند PDF الخاص بك.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

التعليقات التوضيحية في مستند PDF موجودة في مجموعة التعليقات التوضيحية لكائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page). تحتوي هذه المجموعة على جميع التعليقات التوضيحية لتلك الصفحة الفردية فقط: كل صفحة لها مجموعة التعليقات التوضيحية الخاصة بها. لإضافة تعليق توضيحي إلى صفحة معينة، قم بإضافته إلى مجموعة التعليقات التوضيحية لتلك الصفحة باستخدام طريقة Add.

استخدم فئة [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/ScreenAnnotation) في مساحة الأسماء Aspose.PDF.InteractiveFeatures.Annotations لتضمين ملفات SWF كتعليقات توضيحية في مستند PDF بدلاً من ذلك.
 شاشة التعليق توضح منطقة من الصفحة يمكن تشغيل مقاطع الوسائط عليها.

عندما تحتاج إلى إضافة رابط فيديو خارجي في مستند PDF، يمكنك استخدام [MovieAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/MovieAnnotation).
يحتوي التعليق الخاص بالفيلم على رسومات متحركة وصوت ليتم عرضها على شاشة الكمبيوتر ومن خلال مكبرات الصوت.

يجب أن يكون [Sound Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation) مماثلاً لتعليق نصي باستثناء أنه بدلاً من ملاحظة نصية، يحتوي على صوت مسجل من ميكروفون الكمبيوتر أو مستورد من ملف. عند تفعيل التعليق، يجب تشغيل الصوت. يجب أن يتصرف التعليق مثل تعليق نصي في معظم النواحي، مع رمز مختلف (افتراضيًا، مكبر صوت) للإشارة إلى أنه يمثل صوتًا.

ومع ذلك، عندما يكون هناك حاجة لتضمين وسائط داخل مستند PDF، تحتاج إلى استخدام [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/RichMediaAnnotation).
الطرق/الخصائص التالية لفئة RichMediaAnnotation يمكن استخدامها.

- Stream CustomPlayer { set; }: يسمح بتعيين المشغل المستخدم لتشغيل الفيديو.
- string CustomFlashVariables { set; }: يسمح بتعيين المتغيرات التي يتم تمريرها إلى تطبيق الفلاش. هذه السلسلة هي مجموعة من أزواج "key=value" والتي يتم فصلها بـ '&'.
- void AddCustomData(strig name, Stream data): إضافة بيانات إضافية للمشغل. على سبيل المثال source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: الحدث الذي ينشط المشغل؛ القيم الممكنة هي Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): تعيين بيانات الفيديو/الصوت التي سيتم تشغيلها
- void Update(): إنشاء بنية بيانات للتعليق التوضيحي. يجب استدعاء هذه الطريقة كآخر خطوة
- void SetPoster(Stream): تعيين ملصق الفيديو أي الصورة المعروضة عندما لا يكون المشغل نشطاً

## إضافة تعليق توضيحي للشاشة

يوضح مقطع الشيفرة التالي كيفية إضافة تعليق توضيحي للشاشة إلى ملف PDF:

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import com.aspose.pdf.*;

public class ExampleMultimediaAnnotation {

    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddScreenAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "input.swf";
        // إنشاء تعليق توضيحي للشاشة
        ScreenAnnotation screenAnnotation = new ScreenAnnotation(page, new Rectangle(170, 190, 470, 380), mediaFile);
        page.getAnnotations().add(screenAnnotation);

        document.save(_dataDir + "sample_swf.pdf");
    }
}
```


## إضافة تعليق صوتي

يظهر مقتطف الشيفرة التالي كيفية إضافة تعليق صوتي إلى ملف PDF:

```java
          public static void AddSoundAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "file_example_WAV_1MG.wav";

        // إنشاء تعليق صوتي
        SoundAnnotation soundAnnotation = new SoundAnnotation(page, new Rectangle(20, 700, 60, 740), mediaFile);
        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("عرض توضيحي للتعليق الصوتي");
        soundAnnotation.setPopup(new PopupAnnotation(document));

        page.getAnnotations().add(soundAnnotation);

        document.save(_dataDir + "sample_wav.pdf");
    }
```

## إضافة تعليق وسائط غنية

يظهر مقتطف الشيفرة التالي كيفية إضافة تعليق وسائط غنية إلى ملف PDF:

```java
     public static void AddRichMediaAnnotation() throws FileNotFoundException {
        Document doc = new Document();
        var pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        Page page = doc.getPages().add();

        // إعطاء اسم لبيانات الفيديو. سيتم تضمين هذه البيانات في المستند بهذا الاسم
        // والإشارة إليها من متغيرات الفلاش بهذا الاسم.
        // يجب ألا يحتوي videoName على مسار الملف؛ هو "مفتاح" للوصول
        // إلى البيانات داخل مستند PDF

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";

        // نستخدم أيضًا جلد لمشغل الفيديو
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation rma = new RichMediaAnnotation(page, new Rectangle(100, 500, 300, 600));

        // هنا ينبغي تحديد البث الذي يحتوي على كود مشغل الفيديو
        rma.setCustomPlayer(new FileInputStream(pathToAdobeApp + "Players" + "Videoplayer.swf"));

        // تكوين سطر متغيرات الفلاش للمشغل. يرجى ملاحظة أن المشغلات المختلفة
        // قد يكون لديها تنسيق مختلف لسطر متغيرات الفلاش.
        // راجع الوثائق لمشغلك.
        rma.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        // إضافة كود الجلد.
        rma.addCustomData(skinName, new FileInputStream(pathToAdobeApp + "SkinOverAllNoFullNoCaption.swf"));
        // تعيين الملصق للفيديو
        rma.setPoster(new FileInputStream(_dataDir + posterName));

        // تعيين محتوى الفيديو
        rma.setContent(videoName, new FileInputStream(_dataDir + videoName));

        // تعيين نوع المحتوى (فيديو)
        rma.setType(RichMediaAnnotation.ContentType.Video);

        // تنشيط المشغل بالنقر
        rma.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);

        // تحديث بيانات التعليق. يجب استدعاء هذه الطريقة بعد جميع
        // التعيينات/الإعداد. تقوم هذه الطريقة بتهيئة بنية بيانات التعليق
        // وتضمين البيانات المطلوبة.
        rma.update();

        // إضافة التعليق على الصفحة.
        page.getAnnotations().add(rma);

        doc.save(_dataDir + "RichMediaAnnotation.pdf");
    }
```


## الحصول على MultimediaAnnotation

يرجى محاولة استخدام مقطع الشيفرة التالي للحصول على MultimediaAnnotation من مستند PDF.

```java
public static void GetMultimediaAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();

        for (Annotation ma : mediaAnnotations) {
            System.out.println(ma.getAnnotationType() + " " + ma.getRect());
        }
    }
```

## حذف MultimediaAnnotation

يوضح مقطع الشيفرة التالي كيفية حذف MultimediaAnnotation من ملف PDF.

```java
    public static void DeletePolyAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();
        for (Annotation ma : mediaAnnotations) {
            page.getAnnotations().delete(ma);
        }
        document.save(_dataDir + "RichMediaAnnotation_del.pdf");
    }
```


## إضافة تعليقات توضيحية للعنصر

تستخدم النماذج التفاعلية [التعليقات التوضيحية للعنصر](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/WidgetAnnotation) لتمثيل مظهر الحقول وإدارة تفاعلات المستخدم.
نستخدم هذه العناصر النموذجية التي تُضاف إلى ملف PDF لتسهيل إدخال المعلومات أو إرسالها أو تنفيذ بعض التفاعلات الأخرى للمستخدم.

التعليقات التوضيحية للعنصر هي تمثيل رسومي لحقل نموذج على صفحات محددة، لذلك لا يمكننا إنشاؤها مباشرة كتوضيح.

كل تعليق توضيحي للعنصر سيكون له رسوميات مناسبة (مظهر) حسب نوعه. بعد الإنشاء، يمكن تغيير بعض الجوانب البصرية مثل نمط الحدود ولون الخلفية.
يمكن تغيير خصائص أخرى مثل لون النص والخط من خلال الحقل، بمجرد إرفاقه بواحد.

في بعض الحالات، قد ترغب في ظهور الحقل في أكثر من صفحة واحدة، مكررًا نفس القيمة.
 في هذه الحالة، قد تحتوي الحقول التي تحتوي عادةً على أداة واحدة فقط على عدة أدوات مرفقة: يحتوي TextField وListBox وComboBox وCheckBox عادةً على واحدة بالضبط، بينما يحتوي RadioGroup على عدة أدوات، واحدة لكل زر راديو. قد يستخدم شخص يملأ النموذج أيًا من هذه الأدوات لتحديث قيمة الحقل، وينعكس هذا في جميع الأدوات الأخرى أيضًا.

يمثل كل حقل نموذج لكل مكان في الوثيقة توضيح أداة واحدة. تتم إضافة البيانات الخاصة بالموقع لتوضيح الأداة إلى الصفحة المحددة. يحتوي كل حقل نموذج على عدة تنويعات. يمكن أن يكون الزر زر راديو، أو مربع اختيار، أو زر دفع. يمكن أن تكون أداة الاختيار عبارة عن صندوق قائمة أو صندوق تركيبة.

في هذا المثال، سنتعلم كيفية إضافة أزرار الدفع للتنقل في الوثيقة.

## إضافة زر إلى الوثيقة

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWidgetAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddButton()
    {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(72, 748, 164, 768);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("طباعة الوثيقة الحالية");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setNormalCaption("طباعة الوثيقة");

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);

        printButton.setBorder(border);
        printButton.getCharacteristics().setBorder(Color.fromArgb(255, 0, 0, 255));
        printButton.getCharacteristics().setBackground(Color.fromArgb(255, 0, 191, 255));
        document.getForm().add(printButton);

        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

هذا الزر لديه إطار وتم تعيين خلفية له. أيضًا قمنا بتعيين اسم للزر (Name)، تلميح (AlternateName)، تسمية (NormalCaption)، ولون نص التسمية (Color).

## استخدام إجراءات التنقل في المستند

يوجد مثال أكثر تعقيدًا لاستخدام تعليقات الودجيت - التنقل في المستند في مستند PDF. قد يكون هذا ضروريًا لتحضير عرض تقديمي لمستند PDF.

يظهر هذا المثال كيفية إنشاء 4 أزرار:

```java
public static void AddDocumentNavigationActions() {
// تحميل ملف PDF
Document document = new Document(_dataDir + "JSON Fundamenals.pdf");

ButtonField[] buttons = new ButtonField[4];
String[] alternateNames = { "الذهاب إلى الصفحة الأولى", "الذهاب إلى الصفحة السابقة", "الذهاب إلى الصفحة التالية", "الذهاب إلى الصفحة الأخيرة" };
String[] normalCaptions = { "الأولى", "السابق", "التالي", "الأخيرة" };
int[] actions = { PredefinedAction.FirstPage, PredefinedAction.PrevPage, PredefinedAction.NextPage,
PredefinedAction.LastPage };
Color clrBorder = Color.fromArgb(255, 0, 255, 0);
Color clrBackGround = Color.fromArgb(255, 0, 96, 70);

for (int i = 0; i < 4; i++) {
buttons[i] = new ButtonField(document, new Rectangle(32 + i * 80, 28, 104 + i * 80, 68));
buttons[i].setAlternateName(alternateNames[i]);
buttons[i].setColor(Color.getWhite());
buttons[i].setNormalCaption(normalCaptions[i]);
buttons[i].setOnActivated(new NamedAction(actions[i]));
Border border = new Border(buttons[i]);
border.setStyle(BorderStyle.Solid);
border.setWidth(2);
buttons[i].setBorder(border);
buttons[i].getCharacteristics().setBorder(clrBorder);
buttons[i].getCharacteristics().setBackground(clrBackGround);
}

for (int pageIndex = 1; pageIndex <= 1; pageIndex++)
for (int i = 0; i < 4; i++)
document.getForm().add(buttons[i], "btn" + pageIndex + "_" + (i + 1), pageIndex);

document.getForm().get("btn1_1").setReadOnly(true);
document.getForm().get("btn1_2").setReadOnly(true);

document.getForm().get("btn" + document.getPages().size() + "_3").setReadOnly(true);
document.getForm().get("btn" + document.getPages().size() + "_4").setReadOnly(true);
document.save(_dataDir + "sample_widgetannot_2.pdf");
}
```


## كيفية حذف تعليق الودجت

يحتوي Aspose.PDF for Java على قواعد لإزالة التعليقات التوضيحية من ملفك:

```java
public static void DeleteWidgetAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // تصفية التعليقات باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(new ButtonField(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> buttonFields = annotationSelector.getSelected();

        // حذف التعليقات
        for (Annotation wa : buttonFields) {
            page.getAnnotations().delete(wa);
        }
        document.save(_dataDir + "sample_widgetannot_del.pdf");
    }
```

في مستندات PDF، يمكنك عرض وإدارة المحتوى ثلاثي الأبعاد عالي الجودة الذي تم إنشاؤه باستخدام برامج CAD ثلاثية الأبعاد أو برامج النمذجة ثلاثية الأبعاد والمدمجة في مستند PDF.
 يمكن تدوير العناصر ثلاثية الأبعاد في جميع الاتجاهات كما لو كنت تمسكها بيديك.

لماذا تحتاج إلى عرض ثلاثي الأبعاد للصور على الإطلاق؟

على مدى السنوات القليلة الماضية، حققت التكنولوجيا تقدمًا كبيرًا في جميع المجالات بفضل الطباعة ثلاثية الأبعاد. يمكن تطبيق تقنيات الطباعة ثلاثية الأبعاد لتعليم المهارات التكنولوجية في البناء، والهندسة الميكانيكية، والتصميم كأداة رئيسية. هذه التقنيات بفضل ظهور أجهزة الطباعة الشخصية يمكن أن تساهم في إدخال أشكال جديدة من تنظيم العملية التعليمية، وزيادة الدافعية، وتشكيل الكفاءات اللازمة للخريجين والمعلمين.

المهمة الرئيسية للنمذجة ثلاثية الأبعاد هي فكرة كائن مستقبلي أو كائن لأنه، من أجل إصدار كائن، تحتاج إلى فهم ميزات تصميمه بكل التفاصيل للتجديد المتتالي في التصميم الصناعي أو الهندسة المعمارية.

## إضافة التعليق التوضيحي ثلاثي الأبعاد

يتم إضافة التعليق التوضيحي ثلاثي الأبعاد باستخدام نموذج تم إنشاؤه بتنسيق U3D مع Aspose.PDF for Java
1. إنشاء [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) جديد
1. تحميل بيانات النموذج ثلاثي الأبعاد المطلوب (في حالتنا "Ring.u3d") لإنشاء [محتوى PDF3D](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PDF3DContent)
1. إنشاء كائن [3dArtWork](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DArtwork) وربطه بالمستند و3DContent
1. ضبط كائن pdf3dArtWork:

    - مخطط الإضاءة ثلاثية الأبعاد - (سوف نقوم بتعيين `CAD` في المثال)
    - وضع العرض ثلاثي الأبعاد - (سوف نقوم بتعيين `Solid` في المثال)
    - ملء `ViewArray`، إنشاء على الأقل [3D View](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DView) واحد وإضافته إلى المصفوفة.

1. تعيين 3 معايير أساسية في التعليق التوضيحي:
    - `صفحة` التي سيتم وضع التعليق التوضيحي عليها،
    - `المستطيل`، الذي سيكون التعليق التوضيحي داخله،
    - وكائن `3dArtWork`.
1. لتحسين عرض الكائن ثلاثي الأبعاد، تعيين إطار الحدود
1. تعيين العرض الافتراضي (على سبيل المثال - TOP)

1. أضف بعض المعلمات الإضافية: الاسم، معاينة الملصق إلخ.
1. أضف التعليق التوضيحي إلى [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)
1. احفظ النتيجة

## مثال

يرجى التحقق من مقطع الكود التالي لإضافة تعليق توضيحي ثلاثي الأبعاد.

```java
    public class Example3DAnnotation
    {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";
    public static void Add3dAnnotation()
    {
    // تحميل ملف PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
    pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
    pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.getPages().add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
    pdf3dAnnotation.setDefaultViewIndex(1);
    pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
    pdf3dAnnotation.setName("Ring.u3d");
    //تعيين صورة المعاينة إذا لزم الأمر
    //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
    document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

    document.save(_dataDir+"sample_3d.pdf");
    }
}
```


This code example showed us such a model:

![عرض توضيحي للتعليق التوضيحي ثلاثي الأبعاد](3d_demo.png)