---
title: Разрыв страницы в существующем PDF
type: docs
weight: 30
url: /ru/net/page-break-in-existing-pdf/
description: В этом разделе объясняется, как разорвать страницы в существующем PDF с использованием класса PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

По умолчанию содержимое внутри PDF файлов добавляется в макете сверху-слева вниз-вправо. Когда содержимое превышает нижнее поле страницы, происходит разрыв страницы. Однако, вы можете столкнуться с требованием вставить разрыв страницы в зависимости от нужд. Метод под названием AddPageBreak(...) добавлен в класс [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor), чтобы выполнить это требование.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1) ```csharp
[public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/addpagebreak)

- src — исходный документ/путь к документу/поток с исходным документом
- dest — целевой документ/путь, куда будет сохранен документ/поток, где будет сохранен документ
- PageBreak — массив объектов разрыва страницы. Он имеет два свойства: индекс страницы, где должен быть размещен разрыв страницы, и вертикальная позиция разрыва страницы на странице.

## Пример 1 (Добавление разрыва страницы)

```csharp
public static void PageBrakeExample01()
{
    // Создать экземпляр класса Document
    Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
    // Создать пустой экземпляр класса Document
    Document dest = new Document();
    // Создать объект PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[]
    {
        new PdfFileEditor.PageBreak(1, 450)
    });
    // Сохранить полученный файл
    dest.Save(_dataDir + "PageBreak_out.pdf");
}
```
## Пример 2

```csharp
public static void PageBrakeExample02()
{
    // Создать объект PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();

    fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf",
        _dataDir + "PageBreakWithDestPath_out.pdf",
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
}
```

## Пример 3

```csharp
public static void PageBrakeExample03()
{
    Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
    Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(src, dest,
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
    dest.Close();
    src.Close();
}
```