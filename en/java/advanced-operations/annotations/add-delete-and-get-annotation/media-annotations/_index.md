---
title: Media Annotations in PDF
linktitle: Media Annotations
type: docs
weight: 40
url: /java/media-annotations/
description: Learn how to work with sound, screen, rich media, and 3D PDF annotation APIs in Java, with step-by-step guidance for common multimedia workflows.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Media-related PDF annotation workflows in Java.
Abstract: This page explains common media annotation workflows in Aspose.PDF for Java, including sound, screen, rich media, 3D, deletion, and inspection scenarios. The current repository does not include a dedicated `workingwithannotations` media example class, so this article documents the Java API patterns directly with step-by-step guidance.
---
Media annotations in PDF typically cover embedded or linked multimedia content such as sound clips, screen playback regions, rich media containers, and 3D models.

## Add rich media annotations

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Define the video, poster, skin, and player resource paths that will be attached to the annotation.
1. Create a [RichMediaAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/richmediaannotation/) with the destination page and annotation [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rectangle/).
1. Attach the player SWF, flash variables, custom skin data, poster image, and video content streams.
1. Configure the [RichMediaAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/richmediaannotation/) type and activation event, then call `update()`.
1. Add the annotation to the target page.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Delete rich media annotations

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Read or iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) items on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Iterate through the page annotation collection and collect items whose [AnnotationType](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotationtype/) is `RichMedia`.
1. Delete each collected [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) from the page.
1. Save the cleaned output [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Get multimedia annotations

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Read or iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) items on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Define the [AnnotationType](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotationtype/) values you want to treat as multimedia, such as screen, sound, and rich media.
1. Iterate through the first page annotation collection.
1. Print the annotation type and [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rectangle/) for each item that matches the selected multimedia types.

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

## Add 3D annotations

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Wrap the content in [PDF3DArtwork](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdf3dartwork/) by using [PDF3DContent](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdf3dcontent/) and configure the lighting scheme and render mode.
1. Create [Matrix3D](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/matrix3d/) view matrices for the predefined camera orientations you want to expose.
1. Add those named [PDF3DView](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdf3dview/) items to the 3D artwork view array.
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/), create a [PDF3DAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdf3dannotation/), and configure its border, default view, flags, and display name.
1. Add the annotation to the target page.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Add screen annotations

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Create the required [ScreenAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/screenannotation/) with the target [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rectangle/) and media file path.
1. Add the annotation to the target page.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Add sound annotations

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Resolve the WAV file path relative to the input file location.
1. Create a [SoundAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/soundannotation/) with the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/), [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rectangle/), and media file path.
1. Create the [PopupAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/popupannotation/) and associate it with the parent annotation.
1. Set the annotation color, title, subject, and popup note.
1. Add the annotation to the target page.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Related annotation topics

- [Interactive Annotations](/pdf/java/interactive-annotations/)
- [Markup Annotations](/pdf/java/markup-annotations/)
- [Security Annotations](/pdf/java/security-annotations/)
- [Shape Annotations](/pdf/java/shape-annotations/)
- [Text Annotations](/pdf/java/text-based-annotations/)
- [Watermark Annotations](/pdf/java/watermark-annotations/)
- [Import and Export Annotations](/pdf/java/import-export-annotations/)
