---
title: التعليقات التوضيحية للوسائط في PDF
linktitle: التعليقات التوضيحية للوسائط
type: docs
weight: 40
url: /ar/java/media-annotations/
description: تعلم كيفية العمل مع واجهات برمجة تطبيقات التعليقات الصوتية، الشاشة، الوسائط المتعددة، وتعليقات PDF ثلاثية الأبعاد في Java، مع إرشادات خطوة بخطوة لتدفقات العمل الشائعة للوسائط المتعددة.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: تدفقات عمل تعليقات PDF المتعلقة بالوسائط في Java.
Abstract: توضح هذه الصفحة سير عمل تعليقات الوسائط الشائعة في Aspose.PDF for Java، بما في ذلك الصوت، الشاشة، الوسائط الغنية، ثلاثي الأبعاد، الحذف، وسيناريوهات الفحص. المستودع الحالي لا يتضمن فئة مثال وسائط مخصصة تسمى `workingwithannotations`، لذا توثق هذه المقالة أنماط API الخاصة بجافا مباشرةً مع إرشادات خطوة بخطوة.
---
عادةً ما تغطي التعليقات التوضيحية للوسائط في PDF المحتوى المتعدد الوسائط المدمج أو المرتبط مثل مقاطع الصوت، ومناطق تشغيل الشاشة، وحاويات الوسائط الغنية، والنماذج ثلاثية الأبعاد.

## أضف تعليقا بوسائط غنية

استخدم هذا المثال عندما يجب أن تستضيف صفحة PDF محتوى فيديو مدمج مع مشغل مخصص، صورة ملصق، ومظهر.

1. إنشاء ملف PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. إنشاء [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/), قم بتكوين أصول المشغل، الملصق، وتدفق المحتوى.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ مستند الإخراج.

```java
public static void richMediaAnnotationsAdd(Path mediaDir, Path outputFile) throws Exception {
    String pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";

    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation richMediaAnnotation = new RichMediaAnnotation(
                page,
                new Rectangle(100, 500, 300, 600, true));

        String playerPath = pathToAdobeApp + "\\Players\\Videoplayer.swf";
        richMediaAnnotation.setCustomPlayer(new FileInputStream(playerPath));
        richMediaAnnotation.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        String skinPath = pathToAdobeApp + "\\" + skinName;
        richMediaAnnotation.addCustomData(skinName, new FileInputStream(skinPath));

        Path posterPath = mediaDir.resolve(posterName);
        richMediaAnnotation.setPoster(new FileInputStream(posterPath.toString()));

        Path videoPath = mediaDir.resolve(videoName);
        try (FileInputStream videoStream = new FileInputStream(videoPath.toString())) {
            richMediaAnnotation.setContent(videoName, videoStream);
        }

        richMediaAnnotation.setType(RichMediaAnnotation.ContentType.Video);
        richMediaAnnotation.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);
        richMediaAnnotation.update();

        page.getAnnotations().add(richMediaAnnotation);
        document.save(outputFile.toString());
    }
}
```

## حذف تعليقات الوسائط الغنية

يقوم هذا المثال بإزالة التعليقات التوضيحية للوسائط المتعددة الغنية الموجودة من صفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات التوضيحية من النوع [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia`.
1. احذف التعليقات التوضيحية المجمعة واحفظ المستند المحدَّث.

```java
public static void richMediaAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.RichMedia) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            page.getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## احصل على التعليقات المتعددة الوسائط

استخدم هذا المثال لتفقد التعليقات التوضيحية للصور المتحركة والصوت والوسائط الغنية الموجودة بالفعل على الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حدد مجموعة أنواع التعليقات التوضيحية المتعددة الوسائط التي تريد اكتشافها.
1. التنقل عبر ملاحظات الصفحة وطباعة النوع والمستطيل لكل مطابقة.

```java
public static void multimediaAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Set<AnnotationType> targetTypes = Set.of(
                AnnotationType.Screen,
                AnnotationType.Sound,
                AnnotationType.RichMedia);

        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (targetTypes.contains(annotation.getAnnotationType())) {
                System.out.println(annotation.getAnnotationType() + " [" + annotation.getRect() + "]");
            }
        }
    }
}
```

## إضافة تعليق ثلاثي الأبعاد

يضيف هذا المثال عرضًا تفاعليًا للنموذج ثلاثي الأبعاد مع وجهات نظر محددة مسبقًا وخيارات التصيير.

1. إنشاء ملف PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حمّل النموذج إلى [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) وتكوين [PDF3DArtwork](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/).
1. إنشاء [PDF3DAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/), أضفه إلى صفحة، واحفظ المستند.

```java
public static void annotation3dAdd(Path modelFile, Path outputFile) {
    try (Document document = new Document()) {
        PDF3DContent pdf3dContent = new PDF3DContent(modelFile.toString());
        PDF3DArtwork pdf3dArtwork = new PDF3DArtwork(document, pdf3dContent);
        pdf3dArtwork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtwork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        Matrix3D topMatrix = new Matrix3D(
                1, 0, 0,
                0, -1, 0,
                0, 0, -1,
                0.10271, 0.08184, 0.273836);

        Matrix3D frontMatrix = new Matrix3D(
                0, -1, 0,
                0, 0, 1,
                -1, 0, 0,
                0.332652, 0.08184, 0.085273);

        pdf3dArtwork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top"));
        pdf3dArtwork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left"));

        Page page = document.getPages().add();

        PDF3DAnnotation pdf3dAnnotation = new PDF3DAnnotation(
                page,
                new Rectangle(100, 500, 300, 700, true),
                pdf3dArtwork);

        pdf3dAnnotation.setBorder(new com.aspose.pdf.Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName(modelFile.getFileName().toString());

        page.getAnnotations().add(pdf3dAnnotation);
        document.save(outputFile.toString());
    }
}
```

## إضافة تعليق على الشاشة

استخدم هذا المثال عندما يجب على الصفحة الإشارة إلى ملف وسائط عبر منطقة تشغيل الشاشة.

1. إنشاء ملف PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. إنشاء [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/) لملف الوسائط والمستطيل الهدف.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند.

```java
public static void screenAnnotationWithMediaAdd(Path mediaFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ScreenAnnotation screenAnnotation = new ScreenAnnotation(
                page,
                new Rectangle(170, 190, 470, 380, true),
                mediaFile.toString());

        page.getAnnotations().add(screenAnnotation);
        document.save(outputFile.toString());
    }
}
```

## إضافة تعليق صوتي

يوضح هذا المثال وضع ملاحظة صوتية على الصفحة وربطها بملف WAV.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [SoundAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) لملف الصوت الهدف وتكوين البيانات الوصفية الخاصة به.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ مستند الإخراج.

```java
public static void soundAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Path mediaFile = inputFile.getParent().resolve("file_example_WAV_1MG.wav");

        SoundAnnotation soundAnnotation = new SoundAnnotation(
                page,
                new Rectangle(20, 700, 60, 740, true),
                mediaFile.toString());

        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Sound Annotation demo");

        soundAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(20, 700, 60, 740, true)));

        page.getAnnotations().add(soundAnnotation);
        document.save(outputFile.toString());
    }
}
```

## المواضيع المتعلقة بالتعليقات التوضيحية

- [التعليقات التفاعلية](/pdf/ar/java/interactive-annotations/)
- [تعليقات توضيحية للعلامات](/pdf/ar/java/markup-annotations/)
- [تعليقات الأمان](/pdf/ar/java/security-annotations/)
- [ملاحظات الشكل](/pdf/ar/java/shape-annotations/)
- [ملاحظات نصية](/pdf/ar/java/text-based-annotations/)
- [ملاحظات العلامة المائية](/pdf/ar/java/watermark-annotations/)
- [استيراد وتصدير التعليقات التوضيحية](/pdf/ar/java/import-export-annotations/)
