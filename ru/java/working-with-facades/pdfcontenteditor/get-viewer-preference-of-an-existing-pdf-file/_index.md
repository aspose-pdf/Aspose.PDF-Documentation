---
title: Получение предпочтений просмотра существующего PDF файла
type: docs
weight: 70
url: /ru/java/get-viewer-preference-of-an-existing-pdf-file/
description: Этот раздел показывает, как работать с Aspose.PDF Facades, используя класс PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Получение предпочтений просмотра существующего PDF файла

Класс [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) представляет режимы отображения PDF файлов, например, позиционирование окна документа в центре экрана, скрытие меню приложения для просмотра и т.д.

Для того чтобы прочитать настройки, мы используем 'getViewerPreference'. Этот метод возвращает переменную, в которой сохранены все настройки.

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Изменение предпочтений просмотра
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("CenterWindow");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("Меню скрыто");
        }
```