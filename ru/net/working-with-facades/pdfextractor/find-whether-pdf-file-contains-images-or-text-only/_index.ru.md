---
title: Узнать, содержит ли PDF изображения или текст
linktitle: Проверка наличия текста и изображений
type: docs
weight: 40
url: /net/find-whether-pdf-file-contains-images-or-text-only/
description: Эта тема объясняет, как определить, содержит ли файл PDF только изображения или только текст с помощью класса PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

## Фон

PDF файл может содержать как текст, так и изображения. Иногда пользователю может потребоваться узнать, содержит ли файл PDF только текст или только изображения. Мы также можем определить, содержит ли он и то, и другое, или ни того, ни другого.

{{% alert color="primary" %}}

Следующий фрагмент кода показывает, как выполнить это требование.

{{% /alert %}}

```csharp
public static void CheckIfPdfContainsTextOrImages()
{
    // Создаем объект memoryStream для хранения извлеченного текста из документа
    MemoryStream ms = new MemoryStream();
    // Создаем объект PdfExtractor
    PdfExtractor extractor = new PdfExtractor();

    // Привязываем входной PDF документ к extractor
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // Извлекаем текст из входного PDF документа
    extractor.ExtractText();
    // Сохраняем извлеченный текст в текстовый файл
    extractor.GetText(ms);
    // Проверяем, если длина MemoryStream больше или равна 1

    bool containsText = ms.Length >= 1;

    // Извлекаем изображения из входного PDF документа
    extractor.ExtractImage();

    // Вызываем метод HasNextImage в цикле while. Когда изображения закончатся, цикл завершится
    bool containsImage = extractor.HasNextImage();

    // Теперь узнаем, является ли этот PDF только текстом или только изображением

    if (containsText && !containsImage)
        Console.WriteLine("PDF содержит только текст");
    else if (!containsText && containsImage)
        Console.WriteLine("PDF содержит только изображение");
    else if (containsText && containsImage)
        Console.WriteLine("PDF содержит как текст, так и изображение");
    else if (!containsText && !containsImage)
        Console.WriteLine("PDF не содержит ни текста, ни изображения");
}
```