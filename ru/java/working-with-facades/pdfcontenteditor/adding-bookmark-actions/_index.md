---
title: Добавление действий закладки в существующий PDF файл
type: docs
weight: 20
url: /ru/java/adding-bookmark-actions/
description: В этом разделе объясняется, как добавить действия закладки в существующий PDF файл с помощью Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Класс [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), находящийся в пакете com.aspose.pdf.facades, предоставляет гибкость для добавления действий закладки в PDF файл. Вы можете создать ссылку с последовательными действиями, соответствующими выполнению элемента меню в средстве просмотра PDF. Этот класс также предоставляет возможность создания дополнительных действий для событий документа.

Следующий пример кода демонстрирует, как добавить действие закладки в документ PDF.
 Если вы нажмете на эту вкладку, будет выполнено желаемое действие. С помощью Закладки, нажимая на нее, мы выполняем желаемое действие. Затем создайте [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-), установите параметры текста, цвета, укажите имя закладки, а также номер страницы. Последнее действие выполняется с помощью "GoTo", оно позволяет перейти откуда угодно на нужную нам страницу.

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Закладка 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // Сохраняет результат в файл PDF
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```