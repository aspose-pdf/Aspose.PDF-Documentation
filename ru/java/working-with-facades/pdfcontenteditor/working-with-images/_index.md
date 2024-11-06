---
title: Работа с изображениями
type: docs
weight: 30
url: ru/java/working-with-image/
description: Этот раздел объясняет, как заменить изображение с помощью Aspose.PDF Facades - набора инструментов для популярных операций с PDF.
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Удаление изображений с определенной страницы PDF (Facades)

Класс [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) позволяет заменить изображение в существующем PDF-файле.
 [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) метод помогает вам достичь этой цели. Вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) и привязать входной PDF файл с помощью метода bindPdf. После этого вам нужно вызвать метод [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) с тремя параметрами: номер страницы, индекс заменяемого изображения и путь к изображению, которым нужно заменить.

Следующий фрагмент кода показывает, как заменить изображение в существующем PDF файле.

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## Удаление всех изображений из PDF файла (Facades)

Все изображения могут быть удалены из PDF файла с использованием метода [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) класса [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). Вызовите метод [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) – перегрузку без параметров – чтобы удалить все изображения, а затем сохраните обновленный PDF файл, используя метод Save.

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## Замена изображений в PDF файле (Facades)

Вы можете заменить изображения в PDF файле, используя метод [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) класса [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
   public static void ReplaceImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        // Заменить изображение
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```