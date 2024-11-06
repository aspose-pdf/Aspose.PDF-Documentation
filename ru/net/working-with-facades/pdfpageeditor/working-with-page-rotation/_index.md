---
title: Работа с Поворотом Страницы
type: docs
weight: 10
url: ru/net/working-with-page-rotation/
description: Этот раздел объясняет, как работать с поворотом страниц, используя класс PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

Класс [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) предоставляет возможность поворота страницы.

{{% /alert %}}

## Поворот страницы с использованием PageRotations

Для поворота страниц в документе мы можем использовать [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` содержит номер страницы и угол поворота, ключ представляет номер страницы, значение ключа представляет поворот в градусах.

```csharp
public static void RotatePages1()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.PageRotations = new System.Collections.Generic.Dictionary<int, int> { { 1, 90 }, { 2, 180 }, { 3,270 } };

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```

## Поворот страницы с использованием Rotation

Мы также можем использовать свойство [Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation). Угол поворота должен быть 0, 90, 180 или 270

```csharp
public static void RotatePages2()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.ProcessPages = new int[] { 1, 3 };
    editor.Rotation = 90;

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```