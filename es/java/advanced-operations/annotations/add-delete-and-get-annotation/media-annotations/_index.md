---
title: Anotaciones multimedia en PDF
linktitle: Anotaciones multimedia
type: docs
weight: 40
url: /es/java/media-annotations/
description: Aprenda cómo trabajar con APIs de anotación de sonido, pantalla, medios enriquecidos y PDF 3D en Java, con una guía paso a paso para flujos de trabajo multimedia comunes.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Flujos de trabajo de anotación de PDF relacionados con medios en Java.
Abstract: Esta página explica flujos de trabajo comunes de anotaciones multimedia en Aspose.PDF for Java, incluyendo sonido, pantalla, medios enriquecidos, 3D, eliminación y escenarios de inspección. El repositorio actual no incluye una clase de ejemplo multimedia dedicada `workingwithannotations`, por lo que este artículo documenta los patrones de la API de Java directamente con una guía paso a paso.
---
Las anotaciones de medios en PDF normalmente cubren contenido multimedia incrustado o vinculado, como clips de sonido, regiones de reproducción en pantalla, contenedores de medios enriquecidos y modelos 3D.

## Agregar una anotación de medios enriquecidos

Utilice este ejemplo cuando una página PDF deba alojar contenido de video incrustado con un reproductor personalizado, una imagen de póster y una piel.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Anotación RichMedia](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/), configure los activos del reproductor, el póster y la secuencia de contenido.
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

## Eliminar anotaciones de medios enriquecidos

Este ejemplo elimina las anotaciones de medios enriquecidos existentes de una página.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopilar anotaciones de tipo [TipoDeAnotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia`.
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

## Obtener anotaciones multimedia

Utilice este ejemplo para inspeccionar las anotaciones de pantalla, sonido y medios enriquecidos que ya están presentes en la página.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Define el conjunto de tipos de anotaciones multimedia que deseas detectar.
1. Iterar a través de las anotaciones de la página e imprimir el tipo y el rectángulo de cada coincidencia.

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

## Agregar una anotación 3D

Este ejemplo agrega una vista de modelo 3D interactiva con perspectivas predefinidas y opciones de renderizado.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cargar el modelo en [PDF3DContenido](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) y configure un [PDF3DArtwork](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/).
1. Crear el [PDF3DAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/), añádelo a una página, y guarda el documento.

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

## Agregar una anotación de pantalla

Utilice este ejemplo cuando una página deba hacer referencia a un archivo multimedia a través de una región de reproducción en pantalla.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Anotación de pantalla](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/) para el archivo multimedia y el rectángulo de destino.
1. Agrega la anotación a la página y guarda el documento.

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

## Agregar una anotación de sonido

Este ejemplo coloca una anotación de sonido en la página y la asocia con un archivo WAV.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [Anotación de sonido](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) para el archivo de audio de destino y configure sus metadatos.
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

## Temas relacionados de anotación

- [Anotaciones Interactivas](/pdf/es/java/interactive-annotations/)
- [Anotaciones de marcado](/pdf/es/java/markup-annotations/)
- [Anotaciones de seguridad](/pdf/es/java/security-annotations/)
- [Anotaciones de forma](/pdf/es/java/shape-annotations/)
- [Anotaciones de texto](/pdf/es/java/text-based-annotations/)
- [Anotaciones de marca de agua](/pdf/es/java/watermark-annotations/)
- [Importar y exportar anotaciones](/pdf/es/java/import-export-annotations/)
