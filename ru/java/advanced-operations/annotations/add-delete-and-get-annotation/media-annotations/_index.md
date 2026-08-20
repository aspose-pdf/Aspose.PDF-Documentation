---
title: Медийные аннотации в PDF
linktitle: Медийные аннотации
type: docs
weight: 40
url: /ru/java/media-annotations/
description: Узнайте, как работать со звуком, экраном, rich media и 3D PDF annotation APIs в Java, получая пошаговое руководство для типичных мультимедийных рабочих процессов.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Рабочие процессы аннотации PDF, связанные с мультимедиа, в Java.
Abstract: Эта страница объясняет общие рабочие процессы аннотаций мультимедиа в Aspose.PDF for Java, включая звук, экран, rich media, 3D, сценарии удаления и проверки. Текущий репозиторий не содержит отдельного класса примера медиа `workingwithannotations`, поэтому эта статья документирует шаблоны Java API напрямую с пошаговым руководством.
---
Медиа-аннотации в PDF обычно охватывают встроенный или связанный мультимедийный контент, такой как звуковые клипы, области воспроизведения экрана, контейнеры rich media и 3D‑модели.

## Добавьте мультимедийную аннотацию

Используйте этот пример, когда страница PDF должна содержать встроенное видео с пользовательским плеером, изображением постера и скином.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/), настройте активы плеера, постер и поток контента.
1. Добавьте аннотацию на страницу и сохраните результирующий документ.

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

## Удалите аннотации rich media

Этот пример удаляет существующие аннотации rich media со страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Собрать аннотации типа [Тип аннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia`.
1. Удалите собранные аннотации и сохраните обновлённый документ.

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

## Получите мультимедийные аннотации

Используйте этот пример, чтобы просмотреть аннотации экрана, звука и мультимедиа, уже присутствующие на странице.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Определите набор типов мультимедийных аннотаций, которые вы хотите обнаружить.
1. Пройдите по аннотациям страницы и выведите тип и прямоугольник для каждого совпадения.

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

## Добавьте 3D‑аннотацию

В этом примере добавляется интерактивный просмотр 3D‑модели с предустановленными перспективами и параметрами рендеринга.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Загрузите модель в [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) и настроить [PDF3DArtwork](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/).
1. Создайте [PDF3DAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/), добавьте его на страницу, и сохраните документ.

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

## Добавьте аннотацию экрана

Используйте этот пример, когда страница должна ссылаться на медиофайл через регион воспроизведения на экране.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [Экранная аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/) для медиафайла и целевого прямоугольника.
1. Добавьте аннотацию на страницу и сохраните документ.

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

## Добавьте звуковую аннотацию

В этом примере звуковая аннотация размещается на странице и ассоциируется с файлом WAV.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [Звуковая аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) для целевого аудиофайла и настройте его метаданные.
1. Добавьте аннотацию на страницу и сохраните результирующий документ.

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

## Связанные темы аннотаций

- [Интерактивные аннотации](/pdf/ru/java/interactive-annotations/)
- [Разметка аннотаций](/pdf/ru/java/markup-annotations/)
- [Аннотации безопасности](/pdf/ru/java/security-annotations/)
- [Фигурные аннотации](/pdf/ru/java/shape-annotations/)
- [Текстовые аннотации](/pdf/ru/java/text-based-annotations/)
- [Аннотации водяного знака](/pdf/ru/java/watermark-annotations/)
- [Импорт и экспорт аннотаций](/pdf/ru/java/import-export-annotations/)


