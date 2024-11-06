---
title: Извлечение текста с надстрочными и подстрочными знаками из PDF
linktitle: Извлечение надстрочных и подстрочных знаков
type: docs
weight: 30
url: ru/net/extract-superscripts-subscripts-from-pdf/
description: Эта статья описывает различные способы извлечения текста с надстрочными и подстрочными знаками из PDF с использованием Aspose.PDF в C#.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста с надстрочными и подстрочными знаками

Извлечение текста из документа PDF является обычным делом. Однако такой текст, когда его извлекают, может не отображать содержащиеся в нем **надстрочные и подстрочные знаки**, которые типичны для технических документов и статей. Подстрочный или надстрочный знак - это символ, число или буква, размещенные ниже или выше обычной строки текста. Обычно они меньше остального текста.

**Подстрочные и надстрочные знаки** чаще всего используются в формулах, математических выражениях и спецификациях химических соединений.
**Подстрочные и надстрочные символы** чаще всего используются в формулах, математических выражениях и спецификациях химических соединений.
В одном из последних релизов библиотека **Aspose.PDF для .NET** получила поддержку извлечения текста с надстрочными и подстрочными символами из PDF.

Используйте класс **TextFragmentAbsorber** и вы уже можете делать что угодно с найденным текстом, то есть, вы можете просто использовать весь текст. Попробуйте следующий фрагмент кода:

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

Или используйте **TextFragments** отдельно и выполняйте с ними различные манипуляции, например, сортировку по координатам или по размеру.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).
Следующий код также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```
