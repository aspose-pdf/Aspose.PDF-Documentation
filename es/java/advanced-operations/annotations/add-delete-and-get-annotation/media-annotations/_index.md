---
title: Anotaciones multimedia en PDF
linktitle: Anotaciones multimedia
type: docs
weight: 40
url: /java/media-annotations/
description: Aprenda a trabajar con API de sonido, pantalla, medios enriquecidos y anotaciones de PDF 3D en Java, con orientación paso a paso para flujos de trabajo multimedia comunes.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Flujos de trabajo de anotaciones de PDF relacionados con medios en Java.
Abstract: Esta página explica los flujos de trabajo de anotación de medios comunes en Aspose.PDF para Java, incluidos escenarios de sonido, pantalla, medios enriquecidos, 3D, eliminación e inspección. El repositorio actual no incluye una clase de ejemplo de medios `workingwithannotations` dedicada, por lo que este artículo documenta los patrones de la API de Java directamente con una guía paso a paso.
---
Las anotaciones multimedia en PDF suelen cubrir contenido multimedia incrustado o vinculado, como clips de sonido, regiones de reproducción de pantalla, contenedores multimedia enriquecidos y modelos 3D.


## 
Agregar una anotación multimedia enriquecida



Utilice este ejemplo cuando una página PDF deba albergar contenido de vídeo incrustado con un reproductor, una imagen de póster y un diseño personalizados.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue una página.

1. 
Cree una [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/), configure los recursos del reproductor, el póster y el flujo de contenido.
1. Agregue la anotación a la página y guarde el documento de salida.


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

## 
Eliminar anotaciones multimedia enriquecidas



Este ejemplo elimina las anotaciones multimedia enriquecidas existentes de una página.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Recopile anotaciones de tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia`.
1. Elimine las anotaciones recopiladas y guarde el documento actualizado.


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

## 
Obtener anotaciones multimedia



Utilice este ejemplo para inspeccionar anotaciones de pantalla, sonido y medios enriquecidos que ya están presentes en la página.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Defina el conjunto de tipos de anotaciones multimedia que desea detectar.
1. Repita las anotaciones de la página e imprima el tipo y el rectángulo para cada coincidencia.


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

## 
Agregar una anotación 3D



Este ejemplo agrega una vista de modelo 3D interactiva con perspectivas predefinidas y opciones de renderizado.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cargue el modelo en [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) y configure una [PDF3DArtwork](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/).
1. Cree la [Anotación PDF3DA](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/), agréguela a una página y guarde el documento.


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

## 
Agregar una anotación en pantalla



Utilice este ejemplo cuando una página deba hacer referencia a un archivo multimedia a través de una región de reproducción de pantalla.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue una página.

1. 
Cree una [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/) para el archivo multimedia y el rectángulo de destino.
1. Agregue la anotación a la página y guarde el documento.


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

## 
Agregar una anotación de sonido



Este ejemplo coloca una anotación de sonido en la página y la asocia con un archivo WAV.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree una [SoundAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) para el archivo de audio de destino y configure sus metadatos.
1. Agregue la anotación a la página y guarde el documento de salida.


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

## 
Temas de anotaciones relacionados


- 
[Anotaciones interactivas](/pdf/java/interactive-annotations/)

- 
[Anotaciones de marcado](/pdf/java/markup-annotations/)

- 
[Anotaciones de seguridad](/pdf/java/security-annotations/)
- [Anotaciones de forma](/pdf/java/shape-annotations/)

- 
[Anotaciones de texto](/pdf/java/text-based-annotations/)

- 
[Anotaciones de marca de agua](/pdf/java/watermark-annotations/)

- 
[Importar y exportar anotaciones](/pdf/java/import-export-annotations/)
