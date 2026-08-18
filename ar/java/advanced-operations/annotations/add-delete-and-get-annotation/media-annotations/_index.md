---
title: التعليقات التوضيحية للوسائط في PDF
linktitle: التعليقات التوضيحية للوسائط
type: docs
weight: 40
url: /java/media-annotations/
description: تعرف على كيفية العمل مع الصوت والشاشة والوسائط الغنية وواجهات برمجة تطبيقات التعليقات التوضيحية ثلاثية الأبعاد بتنسيق PDF في Java، مع إرشادات خطوة بخطوة لعمليات سير عمل الوسائط المتعددة الشائعة.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: سير عمل التعليقات التوضيحية لملفات PDF المتعلقة بالوسائط في Java.
Abstract: تشرح هذه الصفحة سير عمل التعليقات التوضيحية الشائعة للوسائط في Aspose.PDF لـ Java، بما في ذلك سيناريوهات الصوت والشاشة والوسائط الغنية والأبعاد الثلاثية والحذف والفحص. لا يشتمل المستودع الحالي على فئة أمثلة وسائط `workingwithannotations` مخصصة، لذا توثق هذه المقالة أنماط Java API مباشرة مع إرشادات خطوة بخطوة.
---
عادةً ما تغطي التعليقات التوضيحية للوسائط في PDF محتوى الوسائط المتعددة المضمن أو المرتبط مثل مقاطع الصوت ومناطق تشغيل الشاشة وحاويات الوسائط الغنية والنماذج ثلاثية الأبعاد.

## أضف تعليقًا توضيحيًا للوسائط الغنية

استخدم هذا المثال عندما يجب أن تستضيف صفحة PDF محتوى فيديو مضمنًا مع مشغل مخصص وصورة الملصق والسطح.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. أنشئ [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/)، وقم بتكوين أصول المشغل، والملصق، وبث المحتوى.
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

## حذف التعليقات التوضيحية للوسائط الغنية

يقوم هذا المثال بإزالة التعليقات التوضيحية الموجودة بالوسائط المتعددة التفاعلية من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات التوضيحية من النوع [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia`.
1. احذف التعليقات التوضيحية المجمعة واحفظ المستند المحدث.

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

## احصل على شروح الوسائط المتعددة

استخدم هذا المثال لفحص التعليقات التوضيحية على الشاشة والصوت والوسائط الغنية الموجودة بالفعل على الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حدد مجموعة أنواع التعليقات التوضيحية للوسائط المتعددة التي تريد اكتشافها.
1. كرر من خلال التعليقات التوضيحية للصفحة واطبع النوع والمستطيل لكل تطابق.

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

## أضف تعليقًا توضيحيًا ثلاثي الأبعاد

يضيف هذا المثال عرضًا تفاعليًا لنموذج ثلاثي الأبعاد بمنظورات وخيارات عرض محددة مسبقًا.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتحميل النموذج في [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) وقم بتكوين [PDF3DArtwork](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/).
1. أنشئ [PDF3DAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/)، وأضفه إلى الصفحة، واحفظ المستند.

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

## إضافة تعليق توضيحي على الشاشة

استخدم هذا المثال عندما يجب أن تشير الصفحة إلى ملف وسائط من خلال منطقة تشغيل الشاشة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/) لملف الوسائط والمستطيل المستهدف.
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

يضع هذا المثال تعليقًا توضيحيًا صوتيًا على الصفحة ويربطه بملف WAV.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [SoundAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) للملف الصوتي المستهدف وقم بتكوين بيانات التعريف الخاصة به.
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

## مواضيع ذات صلة بالتعليقات

- [التعليقات التوضيحية التفاعلية](/pdf/java/interactive-annotations/)
- [التعليقات التوضيحية الترميزية](/pdf/java/markup-annotations/)
- [التعليقات التوضيحية الأمنية](/pdf/java/security-annotations/)
- [التعليقات التوضيحية للشكل](/pdf/java/shape-annotations/)
- [التعليقات التوضيحية النصية](/pdf/java/text-based-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/pdf/java/watermark-annotations/)
- [استيراد وتصدير التعليقات التوضيحية](/pdf/java/import-export-annotations/)
