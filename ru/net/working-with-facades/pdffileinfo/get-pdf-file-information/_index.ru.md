---
title: Получение информации о PDF файле
type: docs
weight: 50
url: /net/get-pdf-file-information/
description: Этот раздел объясняет, как получить информацию о PDF файле с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Для получения специфической информации о PDF файле, необходимо создать объект класса [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). После этого, вы можете получить значения отдельных свойств, таких как Тема, Название, Ключевые слова и Создатель и т.д.

Следующий фрагмент кода показывает, как получить информацию о PDF файле.

```csharp
 public static void GetPdfInfo()
        {
            // Открыть документ
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
            // Получить информацию о PDF
            Console.WriteLine("Тема: {0}", fileInfo.Subject);
            Console.WriteLine("Название: {0}", fileInfo.Title);
            Console.WriteLine("Ключевые слова: {0}", fileInfo.Keywords);
            Console.WriteLine("Создатель: {0}", fileInfo.Creator);
            Console.WriteLine("Дата создания: {0}", fileInfo.CreationDate);
            Console.WriteLine("Дата изменения: {0}", fileInfo.ModDate);
            // Определить, является ли это действительным PDF и зашифрован ли он
            Console.WriteLine("Действительный PDF: {0}", fileInfo.IsPdfFile);
            Console.WriteLine("Зашифрован: {0}", fileInfo.IsEncrypted);

            Console.WriteLine("Ширина страницы:{0}", fileInfo.GetPageWidth(1));
            Console.WriteLine("Высота страницы:{0}", fileInfo.GetPageHeight(1));
        }
```

## Получить Метаинформацию

Чтобы получить информацию, мы используем свойство [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header). С помощью 'Hashtable' мы получаем все возможные значения.

```csharp
public static void GetMetaInfo()
        {
            // Создаем экземпляр объекта PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");
            // Получаем все существующие пользовательские атрибуты
            Hashtable hTable = new Hashtable(fInfo.Header);

            IDictionaryEnumerator enumerator = hTable.GetEnumerator();
            while (enumerator.MoveNext())
            {
                string output = enumerator.Key.ToString() + " " + enumerator.Value;
                Console.WriteLine(output);
            }

            // Получаем один пользовательский атрибут
            Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
```