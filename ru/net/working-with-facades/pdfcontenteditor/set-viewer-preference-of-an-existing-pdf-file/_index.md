---
title: Установить предпочтения просмотра PDF
type: docs
weight: 60
url: ru/net/set-viewer-preference-of-an-existing-pdf-file/
description: Этот раздел показывает, как установить предпочтения просмотра существующего PDF файла с использованием класса PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Установить предпочтения просмотра существующего PDF файла

Класс [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) представляет режимы отображения PDF файлов, например, размещение окна документа в центре экрана, скрытие строки меню приложения просмотра и т. д.

Метод [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) в классе [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) позволяет изменить предпочтения просмотра. Для этого вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

После этого вы можете вызвать метод [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference), чтобы установить любые предпочтения. Наконец, вам нужно сохранить обновленный PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). Следующий фрагмент кода показывает, как изменить предпочтения просмотра в существующем PDF-файле.

Например, мы указываем параметр [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow), с помощью которого мы центрируем окно, затем удаляем верхнюю панель инструментов с [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) и с [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) открываем полноэкранный режим.
```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Изменение предпочтений просмотра
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // Сохранение результирующего PDF в файл
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```