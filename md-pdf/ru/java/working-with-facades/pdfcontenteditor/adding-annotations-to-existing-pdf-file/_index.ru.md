---
title: Добавление аннотаций в существующий PDF файл
type: docs
weight: 80
url: /java/adding-annotations-to-existing-pdf-file/
description: Этот раздел объясняет, как добавить аннотации в существующий PDF файл с помощью Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавление аннотации свободного текста в существующий PDF файл (facades)

Аннотация свободного текста отображает текст непосредственно на странице. [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) позволяет добавлять аннотации различных типов в существующий PDF файл. Вы можете использовать соответствующий метод для добавления определенной аннотации. Например, в следующем фрагменте кода мы использовали метод [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) для добавления аннотации типа FreeText.

Любой тип аннотаций может быть добавлен в PDF файл таким же образом.
 В первую очередь, вам нужно создать объект типа [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) и привязать входной PDF-файл с помощью метода bindPdf. Во-вторых, вы должны создать объект Rectangle, чтобы указать область аннотации. После этого вы можете вызвать метод [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-), чтобы добавить аннотацию FreeText, указав номер страницы, на которой расположена аннотация, а затем использовать метод save, чтобы сохранить обновленный PDF-файл.

Следующий фрагмент кода показывает, как добавить аннотацию свободного текста в PDF-файл.

```java
  public static void AddFreeTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createFreeText(rect, "Free Text Demo", 1); // последний параметр - это номер страницы
        editor.save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
    }
```

## Добавление текстовой аннотации в существующий PDF файл (фасады)

В этом примере вам также необходимо создать объект типа [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) и связать входной PDF файл, используя метод [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-). Во-вторых, вам нужно создать объект Rectangle, чтобы указать область аннотации. После этого вы можете вызвать метод [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) для добавления аннотации FreeText, создания заголовка ваших аннотаций и номера страницы, на которой расположена аннотация.

```java
 public static void AddTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
        editor.save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
    }
```


## Добавление аннотации линии в существующий PDF файл (фасады)

Мы также указываем Прямоугольник, координаты начала и конца линии, номер страницы, толщину, стиль и цвет рамки аннотации, тип штриха линии, тип начала и конца линии.

```java

    public static void AddLineAnnotation()
    {
        var document = new Document(_dataDir + "Appartments.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        // Создание аннотации линии
        editor.createLine(
            new java.awt.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 1,
            java.awt.Color.RED,
            "dash",
            new int[] { 1, 0, 3 },
            new String[] { "Open", "Open" });
        editor.save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
    }
```