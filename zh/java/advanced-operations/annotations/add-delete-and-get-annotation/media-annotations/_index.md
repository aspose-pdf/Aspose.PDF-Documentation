---
title: PDF 中的媒体注释
linktitle: 媒体注释
type: docs
weight: 40
url: /java/media-annotations/
description: 了解如何在 Java 中使用声音、屏幕、富媒体和 3D PDF 注释 API，并提供常见多媒体工作流程的分步指导。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java 中与媒体相关的 PDF 注释工作流程。
Abstract: 本页介绍了 Aspose.PDF for Java 中的常见媒体注释工作流程，包括声音、屏幕、富媒体、3D、删除和检查场景。当前存储库不包含专用的 `workingwithannotations` 媒体示例类，因此本文通过分步指导直接记录 Java API 模式。
---
PDF 中的媒体注释通常涵盖嵌入或链接的多媒体内容，例如声音剪辑、屏幕播放区域、富媒体容器和 3D 模型。

## 添加富媒体注释

当 PDF 页面应托管带有自定义播放器、海报图像和皮肤的嵌入式视频内容时，请使用此示例。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 创建 [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/)，配置播放器资源、海报和内容流。
1. 将注释添加到页面并保存输出文档。

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

## 删除富媒体注释

此示例从页面中删除现有的富媒体注释。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 收集 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia` 类型的注释。
1. 删除收集的注释并保存更新的文档。

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

## 获取多媒体注释

使用此示例检查页面上已有的屏幕、声音和富媒体注释。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 定义您要检测的多媒体注释类型集。
1. 迭代页面注释并打印每个匹配的类型和矩形。

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

## 添加 3D 注释

This example adds an interactive 3D model view with predefined perspectives and rendering options.

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将模型加载到 [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) 中并配置 [PDF3DArtwork](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/)。
1. 创建 [PDF3DAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/)，将其添加到页面，然后保存文档。

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

## 添加屏幕注释

当页面应通过屏幕播放区域引用媒体文件时，请使用此示例。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 为媒体文件和目标矩形创建一个 [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/)。
1. 将注释添加到页面并保存文档。

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

## 添加声音注释

此示例在页面上放置声音注释并将其与 WAV 文件关联。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 为目标音频文件创建一个 [SoundAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) 并配置其元数据。
1. 将注释添加到页面并保存输出文档。

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

## 相关注释主题

- [交互式注释](/pdf/java/interactive-annotations/)
- [标记注释](/pdf/java/markup-annotations/)
- [安全注释](/pdf/java/security-annotations/)
- [形状注释](/pdf/java/shape-annotations/)
- [文字注释](/pdf/java/text-based-annotations/)
- [水印注释](/pdf/java/watermark-annotations/)
- [导入和导出注释](/pdf/java/import-export-annotations/)
