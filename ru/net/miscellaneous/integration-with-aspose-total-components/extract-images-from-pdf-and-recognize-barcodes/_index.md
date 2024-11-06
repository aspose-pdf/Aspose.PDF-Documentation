---
title: Извлечение изображений из PDF и распознавание штрих-кодов
type: docs
weight: 20
url: ru/net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Документы PDF обычно содержат текст, изображения, таблицы, вложения, графики, аннотации и другие связанные объекты. В некоторых случаях в файл PDF встраиваются штрих-коды, и у некоторых клиентов возникает потребность идентифицировать штрих-коды, присутствующие в файле PDF. Следующая статья объясняет шаги по извлечению изображений со страниц PDF и идентификации штрих-кодов внутри них.

{{% /alert %}}

Согласно модели объектов документа Aspose.PDF для .NET, файл PDF содержит одну или несколько страниц, каждая из которых содержит коллекцию изображений, форм и шрифтов в объекте ресурсов.
Согласно объектной модели документа Aspose.PDF для .NET, файл PDF содержит одну или несколько страниц, каждая из которых содержит коллекцию изображений, форм и шрифтов в объекте ресурсов.

**C#**

```csharp
// открыть документ
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// перебор отдельных страниц файла PDF
for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    // перебор каждого изображения, извлеченного со страниц PDF
    foreach (XImage xImage in pdfDocument.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            // сохранить выходное изображение
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
   
            // установить позицию потока в начало потока
            imageStream.Position = 0;
   
            // Создать объект BarCodeReader
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
   
            while (barcodeReader.Read())
            {
                // получить текст штрих-кода из изображения штрих-кода
                string code = barcodeReader.GetCodeText();
   
                // вывести текст штрих-кода в консоль
                Console.WriteLine("BARCODE : " + code);
            }
   
            // закрыть объект BarCodeReader для освобождения файла изображения
            barcodeReader.Close();
        }
    }
}
```

Для получения дополнительной информации по темам, рассмотренным в этой статье, пожалуйста, посетите следующие ссылки:

- [Извлечение изображений из PDF файла](/net/extract-images-from-the-pdf-file/)
- [Считывание штрихкодов](https://docs.aspose.com/barcode/net/read-barcodes/)
