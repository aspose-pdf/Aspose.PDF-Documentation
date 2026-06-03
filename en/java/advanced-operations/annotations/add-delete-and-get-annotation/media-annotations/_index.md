---
title: Media Annotations in PDF
linktitle: Media Annotations
type: docs
weight: 40
url: /java/media-annotations/
description: Learn how to work with sound, screen, rich media, and 3D PDF annotation APIs in Java, with step-by-step guidance for common multimedia workflows.
lastmod: "2026-06-03"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Media-related PDF annotation workflows in Java.
Abstract: This page explains common media annotation workflows in Aspose.PDF for Java, including sound, screen, rich media, 3D, deletion, and inspection scenarios. The current repository does not include a dedicated `workingwithannotations` media example class, so this article documents the Java API patterns directly with step-by-step guidance.
---
Media annotations in PDF typically cover embedded or linked multimedia content such as sound clips, screen playback regions, rich media containers, and 3D models.

## Add rich media annotations

1. Create a new `Document` and add a target page for the rich media annotation.
2. Define the video, poster, skin, and player resource paths that will be attached to the annotation.
3. Create a `RichMediaAnnotation` with the destination page and annotation rectangle.
4. Attach the player SWF, flash variables, custom skin data, poster image, and video content streams.
5. Configure the annotation type and activation event, then call `update()`.
6. Add the annotation to the page and save the output PDF.

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

1. Open the input PDF and get the first page that contains the media annotations.
2. Iterate through the page annotation collection and collect items whose `AnnotationType` is `RichMedia`.
3. Delete each collected annotation from the page.
4. Save the cleaned output document.

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

1. Open the PDF document that should be inspected.
2. Define the annotation types you want to treat as multimedia, such as screen, sound, and rich media.
3. Iterate through the first page annotation collection.
4. Print the annotation type and rectangle for each item that matches the selected multimedia types.

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

1. Create a new PDF document and initialize `PDF3DContent` from the input model file.
2. Wrap the content in `PDF3DArtwork` and configure the lighting scheme and render mode.
3. Create view matrices for the predefined camera orientations you want to expose.
4. Add those named views to the 3D artwork view array.
5. Add a page, create a `PDF3DAnnotation`, and configure its border, default view, flags, and display name.
6. Add the annotation to the page and save the document.

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

1. Create a new PDF document and add a page where the media player region should appear.
2. Create a `ScreenAnnotation` with the target rectangle and the media file path.
3. Add the annotation to the page.
4. Save the output PDF.

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

1. Open the input PDF and get the first page where the sound annotation should be placed.
2. Resolve the WAV file path relative to the input file location.
3. Create a `SoundAnnotation` with the page, rectangle, and media file path.
4. Set the annotation color, title, subject, and popup note.
5. Add the annotation to the page and save the updated document.

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
