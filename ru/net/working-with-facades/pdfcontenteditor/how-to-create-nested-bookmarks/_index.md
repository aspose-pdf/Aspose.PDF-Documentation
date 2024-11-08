---
title: Добавление закладок в PDF файл
type: docs
weight: 20
url: /ru/net/how-to-create-nested-bookmarks/
description: Этот раздел объясняет, как создать вложенные закладки с помощью класса PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

Закладки дают вам возможность отслеживать/связывать с определенной страницей внутри PDF-документа. Класс [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) в [пространстве имен Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) предоставляет функцию, которая позволяет создать собственную закладку сложным, но интуитивно понятным способом в существующем PDF-файле, на заданной странице или на всех страницах.

## Детали реализации

Помимо создания простых закладок, иногда у вас возникает необходимость создать закладку в виде глав, где вы вкладываете отдельные закладки внутри закладок главы, так что, когда вы нажмете на знак + для главы, вы увидите страницы внутри, когда закладки разворачиваются, как показано на рисунке ниже.
```csharp
   public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.CreateBookmarksAction("Закладка 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

            // Сохраняет результат в PDF файл
            editor.Save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```