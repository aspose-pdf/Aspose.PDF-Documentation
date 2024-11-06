---
title: Установка предпочтений просмотра существующего PDF файла
type: docs
weight: 60
url: ru/java/set-viewer-preference-of-an-existing-pdf-file/
description: Этот раздел показывает, как работать с Aspose.PDF Facades, используя класс PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Установка предпочтений просмотра существующего PDF файла

Класс [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) представляет режимы отображения PDF файлов; например, позиционирование окна документа в центре экрана, скрытие строки меню приложения для просмотра и т.д.

Метод [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) в классе [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) позволяет изменить предпочтения просмотра.
 Чтобы сделать это, вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) и связать входной PDF файл, используя метод [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-).

После этого вы можете вызвать метод [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-), чтобы установить любое предпочтение. Наконец, вам нужно сохранить обновленный PDF файл, используя метод Save. Следующий фрагмент кода показывает, как изменить предпочтение просмотра в существующем PDF файле.

Например, мы указываем параметр [CENTER WINDOW](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW), с помощью которого мы центрируем окно, затем убираем верхнюю панель инструментов с помощью [HIDE MENUBAR](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR) и с [PAGE MODE USE NONE](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE) открываем полноэкранный режим.
```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Изменить настройки просмотра
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```