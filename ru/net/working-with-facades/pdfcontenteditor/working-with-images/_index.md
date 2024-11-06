---
title: Работа с изображениями с использованием PdfContentEditor
type: docs
weight: 50
url: ru/net/working-with-images-in-pdf
description: Этот раздел объясняет, как добавлять и удалять изображения с помощью Aspose.PDF Facades, используя класс PdfContentEditor.
lastmod: "2021-06-24"
---

## Удаление изображений с конкретной страницы PDF (Facades)

Чтобы удалить изображения с определенной страницы, вам нужно вызвать метод [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) с параметрами pageNumber и index. Параметр index представляет собой массив целых чисел – индексы изображений, которые нужно удалить. Прежде всего, вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и затем вызвать метод [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1). После этого вы можете сохранить обновленный PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Следующий кодовый фрагмент показывает, как удалить изображения с определенной страницы PDF.

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## Удаление всех изображений из PDF файла (Facades)

Все изображения могут быть удалены из PDF файла с использованием метода [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Вызовите метод [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) – перегрузку без параметров – чтобы удалить все изображения, а затем сохраните обновленный PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Следующий пример кода показывает, как удалить все изображения из PDF файла.

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## Замена изображения в PDF файле (Facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) позволяет заменить изображение в PDF файле, для этого вызовите метод [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) и сохраните результат.

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```