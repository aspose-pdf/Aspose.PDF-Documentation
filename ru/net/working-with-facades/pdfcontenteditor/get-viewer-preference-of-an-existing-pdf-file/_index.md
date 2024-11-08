---
title: Получить предпочтения просмотра PDF файла
type: docs
weight: 70
url: /ru/net/get-viewer-preference-of-an-existing-pdf-file/
description: Этот раздел показывает, как получить предпочтения просмотра существующего PDF файла, используя класс PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Получить предпочтения просмотра существующего PDF файла

Класс [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) представляет собой режимы отображения PDF файлов; например, размещение окна документа в центре экрана, скрытие строки меню приложения просмотра и так далее.

Для того чтобы прочитать настройки, мы используем класс [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference). Этот метод возвращает переменную, в которой сохранены все настройки.

```csharp
      public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Изменить предпочтения просмотра
            var preferences = editor.GetViewerPreference();
            if ((preferences & ViewerPreference.CenterWindow) != 0)
                Console.WriteLine("CenterWindow");
            if ((preferences & ViewerPreference.HideMenubar) != 0)
                Console.WriteLine("Menu bar hided");
            if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
                Console.WriteLine("Page Mode Full Screen");
        }
```
```