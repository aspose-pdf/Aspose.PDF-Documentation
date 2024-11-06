---
title: Извлечение текста из штампов с использованием C#
type: docs
weight: 60
url: ru/net/extract-text-from-stamps/
description: Узнайте, как использовать специальную функцию Aspose.PDF для .NET - извлечение текста из аннотаций штампов
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение текста из аннотаций штампов

Aspose.PDF для NET позволяет извлекать текст из аннотаций штампов. Для извлечения текста из аннотаций штампов в PDF можно использовать следующие шаги.

1. Создайте объект класса `Document`
1. Получите нужную `Annotation` из списка аннотаций страницы
1. Определите новый объект класса `TextAbsorber`
1. Используйте метод visit класса TextAbsorber, чтобы получить текст

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```

