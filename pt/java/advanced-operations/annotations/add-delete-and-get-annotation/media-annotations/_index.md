---
title: Anotações de mídia em PDF
linktitle: Anotações de mídia
type: docs
weight: 40
url: /java/media-annotations/
description: Aprenda como trabalhar com APIs de som, tela, rich media e anotação de PDF 3D em Java, com orientação passo a passo para fluxos de trabalho multimídia comuns.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Fluxos de trabalho de anotação de PDF relacionados à mídia em Java.
Abstract: Esta página explica fluxos de trabalho comuns de anotação de mídia em Aspose.PDF para Java, incluindo cenários de som, tela, rich media, 3D, exclusão e inspeção. O repositório atual não inclui uma classe de exemplo de mídia `workingwithannotations` dedicada, portanto, este artigo documenta os padrões da API Java diretamente com orientação passo a passo.
---
As anotações de mídia em PDF normalmente abrangem conteúdo multimídia incorporado ou vinculado, como clipes de som, regiões de reprodução de tela, contêineres de rich media e modelos 3D.

## Adicionar uma anotação rich media

Use este exemplo quando uma página PDF precisar hospedar conteúdo de vídeo incorporado com um player, imagem de pôster e skin personalizados.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie uma [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/), configure os ativos do player, o pôster e o fluxo de conteúdo.
1. Adicione a anotação à página e salve o documento de saída.

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

## Excluir anotações de rich media

Este exemplo remove anotações rich media existentes de uma página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações do tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia`.
1. Exclua as anotações coletadas e salve o documento atualizado.

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

## Obtenha anotações multimídia

Use este exemplo para inspecionar anotações de tela, som e rich media já presentes na página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Defina o conjunto de tipos de anotações multimídia que você deseja detectar.
1. Itere pelas anotações da página e imprima o tipo e o retângulo de cada correspondência.

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

## Adicione uma anotação 3D

Este exemplo adiciona uma visualização interativa do modelo 3D com perspectivas e opções de renderização predefinidas.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Carregue o modelo em [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) e configure um [PDF3DArtwork](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/).
1. Crie a [PDF3DAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/), adicione-a a uma página e salve o documento.

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

## Adicione uma anotação na tela

Use este exemplo quando uma página fizer referência a um arquivo de mídia por meio de uma região de reprodução da tela.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie uma [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/) para o arquivo de mídia e o retângulo de destino.
1. Adicione a anotação à página e salve o documento.

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

## Adicione uma anotação sonora

Este exemplo coloca uma anotação sonora na página e a associa a um arquivo WAV.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [SoundAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) para o arquivo de áudio de destino e configure seus metadados.
1. Adicione a anotação à página e salve o documento de saída.

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

## Tópicos de anotação relacionados

- [Anotações interativas](/pdf/java/interactive-annotations/)
- [Anotações de marcação](/pdf/java/markup-annotations/)
- [Anotações de segurança](/pdf/java/security-annotations/)
- [Anotações de forma](/pdf/java/shape-annotations/)
- [Anotações de texto](/pdf/java/text-based-annotations/)
- [Anotações de marca d'água](/pdf/java/watermark-annotations/)
- [Importar e exportar anotações](/pdf/java/import-export-annotations/)
