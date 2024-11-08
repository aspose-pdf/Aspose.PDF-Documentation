---
title: Разрыв страницы в существующем PDF
type: docs
weight: 30
url: /ru/java/page-break-in-existing-pdf/
description: Этот раздел объясняет, как вставить разрывы страниц в существующий PDF с использованием класса PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

По умолчанию содержимое внутри PDF файлов добавляется в макете сверху-слева вниз-вправо. Как только содержимое превышает нижний край страницы, происходит разрыв страницы. Однако, вы можете столкнуться с требованием вставить разрыв страницы в зависимости от необходимости. Метод с именем AddPageBreak(...) добавлен в класс [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor), чтобы выполнить это требование.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-com.aspose.pdf.IDocument-com.aspose.pdf.IDocument-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)

1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-java.lang.String-java.lang.String-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html?is-external=true)

- src — исходный документ/путь к документу/поток с исходным документом
- dest — целевой документ/путь, где документ будет сохранен/поток, где документ будет сохранен
- PageBreak — массив объектов разрыва страницы. Имеет два свойства: индекс страницы, где должен быть установлен разрыв страницы, и вертикальная позиция разрыва страницы на странице.

## Пример 1 (Добавить разрыв страницы)

```java
   public static void PageBrakeExample01() {
        // Создать экземпляр класса Document
        Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
        // Создать пустой экземпляр класса Document
        Document dest = new Document();
        // Создать объект PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        // Сохранить полученный файл
        dest.Save(_dataDir + "PageBreak_out.pdf");
    }
```


## Пример 2

```java
  public static void PageBrakeExample02() {
        // Создать объект PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();

        fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf", _dataDir + "PageBreakWithDestPath_out.pdf",
                new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
    }
```

## Пример 3

```java
 public static void PageBrakeExample03() {
        Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
        Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(src, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        dest.Close();
        src.Close();
    }
```