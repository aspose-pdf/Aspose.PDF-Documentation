---
title: Работа с артефактами
linktitle: Работа с артефактами
type: docs
weight: 110
url: ru/java/artifacts/
description: Эта страница описывает, как работать с классом Artifact, используя Aspose.PDF для Java. Примеры кода показывают, как добавить фоновое изображение на страницы PDF и как получить каждый водяной знак на первой странице PDF-файла.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Артефакты, как правило, это графические объекты или другие отметки, которые не являются частью авторского контента. В вашем PDF примеры артефактов включают различную информацию, есть заголовок или нижний колонтитул страницы, линии или другие графики, разделяющие секции страницы, или декоративные изображения.

Класс [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) содержит:

- [Artifact.Type](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, где значения включают Background, Layout, Page, Pagination и Undefined).
- [Artifact.Subtype](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – получает подтип артефакта (поддерживает значения перечисления Artifact.ArtifactSubtype, где значения включают Background, Footer, Header, Undefined, Watermark).

Водяной знак, созданный с помощью Adobe Acrobat, называется артефактом (как описано в разделе 14.8.2.2 Real Content and Artifacts спецификации PDF). Для работы с артефактами Aspose.PDF имеет два класса: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) и [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection).

Чтобы получить все артефакты на определенной странице, класс [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) имеет свойство Artifacts. В этой теме объясняется, как работать с артефактами в PDF-файлах.

Следующий фрагмент кода показывает, как установить водяной знак на первой странице PDF-файла.

```java

 public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```


Фоновые изображения могут использоваться для добавления водяного знака или других тонких элементов дизайна в документы. В Aspose.PDF для Java каждый PDF-документ является коллекцией страниц, и каждая страница содержит коллекцию артефактов. Класс [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) может быть использован для добавления фонового изображения к объекту страницы.

Следующий фрагмент кода показывает, как добавить фоновое изображение к страницам PDF, используя объект BackgroundArtifact.

```java

    public static void SetBackground() throws FileNotFoundException {

        // Открыть документ
        Document pdfDocument = new Document();
                
        // Добавить новую страницу к объекту документа
        Page page = pdfDocument.getPages().add();

        // Создать объект Background Artifact
        BackgroundArtifact background = new BackgroundArtifact();

        // Указать изображение для объекта backgroundartifact
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // Добавить BackgroundArtifact в коллекцию артефактов страницы
        page.getArtifacts().add(background);

        // Сохранить измененный PDF
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```


## Примеры программирования: Получение водяного знака

Следующий фрагмент кода показывает, как получить каждый водяной знак на первой странице PDF файла.

```java
    public static void GettingWatermarks() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // Перебрать и получить подтип, текст и расположение артефакта
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## Примеры программирования: Подсчет артефактов определенного типа

Чтобы вычислить общее количество артефактов определенного типа (например, общее количество водяных знаков), используйте следующий код:

```java
    public static void CountingArtifacts() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // Если тип артефакта - водяной знак, увеличить счетчик
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("Страница содержит " + count + " водяных знаков");
    }
```