---
title: Annotations des médias en PDF
linktitle: Annotations des médias
type: docs
weight: 40
url: /java/media-annotations/
description: Apprenez à utiliser les API de son, d'écran, de médias riches et d'annotation PDF 3D en Java, avec des conseils étape par étape pour les flux de travail multimédia courants.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Workflows d'annotation PDF liés aux médias en Java.
Abstract: Cette page explique les flux de travail d'annotation multimédia courants dans Aspose.PDF pour Java, y compris les scénarios de son, d'écran, multimédia enrichi, 3D, de suppression et d'inspection. Le référentiel actuel n'inclut pas de classe d'exemple de média `workingwithannotations` dédiée. Cet article documente donc directement les modèles d'API Java avec des conseils étape par étape.
---
Les annotations multimédias dans PDF couvrent généralement le contenu multimédia intégré ou lié, tel que les clips audio, les zones de lecture d'écran, les conteneurs Rich Media et les modèles 3D.


## 
Ajouter une annotation Rich Media



Utilisez cet exemple lorsqu'une page PDF doit héberger du contenu vidéo intégré avec un lecteur, une image d'affiche et un habillage personnalisés.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez une [RichMediaAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/), configurez les ressources du lecteur, l'affiche et le flux de contenu.
1. Ajoutez l'annotation à la page et enregistrez le document de sortie.


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
Supprimer les annotations Rich Media



Cet exemple supprime les annotations Rich Media existantes d'une page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Collectez les annotations de type [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia`.
1. Supprimez les annotations collectées et enregistrez le document mis à jour.


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
Obtenez des annotations multimédia



Utilisez cet exemple pour inspecter les annotations d’écran, de son et de médias enrichis déjà présentes sur la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Définissez l'ensemble des types d'annotations multimédia que vous souhaitez détecter.
1. Parcourez les annotations de page et imprimez le type et le rectangle pour chaque correspondance.


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
Ajouter une annotation 3D



Cet exemple ajoute une vue de modèle 3D interactive avec des perspectives et des options de rendu prédéfinies.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Chargez le modèle dans [PDF3DContent] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) et configurez un [PDF3DArtwork] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/).
1. Créez la [PDF3DAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/), ajoutez-la à une page et enregistrez le document.


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
Ajouter une annotation d'écran



Utilisez cet exemple lorsqu'une page doit référencer un fichier multimédia via une région de lecture d'écran.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez une [ScreenAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/) pour le fichier multimédia et le rectangle cible.
1. Ajoutez l'annotation à la page et enregistrez le document.


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
Ajouter une annotation sonore



Cet exemple place une annotation sonore sur la page et l'associe à un fichier WAV.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [SoundAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) pour le fichier audio cible et configurez ses métadonnées.
1. Ajoutez l'annotation à la page et enregistrez le document de sortie.


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
Sujets d'annotations associés


- 
[Annotations interactives] (/pdf/java/interactive-annotations/)

- 
[Annotations de balisage] (/pdf/java/markup-annotations/)

- 
[Annotations de sécurité] (/pdf/java/security-annotations/)
- [Annotations de forme] (/pdf/java/shape-annotations/)

- 
[Annotations de texte] (/pdf/java/text-based-annotations/)

- 
[Annotations en filigrane] (/pdf/java/watermark-annotations/)

- 
[Importer et exporter des annotations] (/pdf/java/import-export-annotations/)
