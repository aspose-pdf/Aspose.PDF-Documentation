---
title: Лицензия Aspose PDF
linktitle: Лицензирование и ограничения
type: docs
weight: 90
url: ru/net/licensing/
description: Aspose. PDF для .NET приглашает своих клиентов получить Классическую лицензию и Лицензию на измерение. Также использовать ограниченную лицензию для лучшего изучения продукта.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ограничение версии для оценки

Мы хотим, чтобы наши клиенты тщательно тестировали наши компоненты перед покупкой, поэтому версия для оценки позволяет вам использовать её, как обычно.

- **PDF создан с водяным знаком оценочной версии.** Оценочная версия Aspose.PDF для .NET обеспечивает полную функциональность продукта, но все страницы в созданных PDF документах помечены водяным знаком "Только для оценки. Создано с Aspose.PDF. Авторское право 2002-2020 Aspose Pty Ltd" в верхней части.

- **Лимит количества элементов коллекции, которые можно обработать.**
В оценочной версии из любой коллекции вы можете обработать только четыре элемента (например, только 4 страницы, 4 поля формы и т.д.).
В версии для оценки из любой коллекции можно обработать только четыре элемента (например, только 4 страницы, 4 поля формы и т. д.).

> Если вы хотите протестировать Aspose.HTML для .NET без ограничений версии для оценки, вы также можете запросить временную лицензию на 30 дней. Пожалуйста, обратитесь к [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)

## Классическая лицензия

Лицензию можно загрузить из файла или объекта потока. Самый простой способ установить лицензию - поместить файл лицензии в ту же папку, что и файл Aspose.PDF.dll, и указать имя файла без пути, как показано в примере ниже.

Если вы используете любой другой компонент Aspose для .NET вместе с Aspose.PDF для .NET, пожалуйста, укажите пространство имен для License, как [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### Загрузка лицензии из файла

Самый простой способ применить лицензию - поместить файл лицензии в ту же папку, что и файл Aspose.PDF.dll, и указать только имя файла без пути.

Когда вы вызываете метод [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), имя лицензии, которое вы передаете, должно соответствовать имени вашего файла лицензии.
Когда вы вызываете метод [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), имя лицензии, которое вы передаете, должно соответствовать имени вашего лицензионного файла.

```csharp
public static void SetLicenseExample()
{
    // Инициализация объекта лицензии
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    try
    {
        // Установка лицензии
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // что-то пошло не так
        throw;
    }
    Console.WriteLine("Лицензия успешно установлена.");
}
```
### Загрузка лицензии из объекта потока

Следующий пример показывает, как загрузить лицензию из потока.

```csharp
public static void SetLicenseFromStream()
{
    // Инициализация объекта лицензии
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    // Загрузка лицензии из потока файла
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // Установка лицензии
    license.SetLicense(myStream);
    Console.WriteLine("Лицензия успешно установлена.");
}
```
## Метрическая Лицензия

Aspose.PDF позволяет разработчикам применять метрический ключ. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться вместе с существующим методом лицензирования. Те клиенты, которые хотят получать счета в зависимости от использования функций API, могут использовать метрическое лицензирование. Для получения дополнительной информации, пожалуйста, обратитесь к разделу Часто задаваемые вопросы о метрическом лицензировании.

Был введен новый класс Metered для применения метрического ключа. Ниже приведен пример кода, демонстрирующий, как установить метрические публичные и приватные ключи.

Для получения дополнительной информации, пожалуйста, обратитесь к разделу [Часто задаваемые вопросы о метрическом лицензировании](https://purchase.aspose.com/faqs/licensing/metered).

```csharp
public static void SetMeteredLicense()
{
    // установка метрических публичного и приватного ключей
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // Доступ к свойству setMeteredKey и передача публичного и приватного ключей в качестве параметров
    metered.SetMeteredKey(
        "<введите публичный ключ здесь>",
        "<введите приватный ключ здесь>");

    // Загрузка документа с диска.
    Document doc = new Document("input.pdf");
    // Получение количества страниц документа
    Console.WriteLine(doc.Pages.Count);
}
```
Обратите внимание, что COM-приложения, работающие с **Aspose.PDF для .NET**, также должны использовать класс License.

Один момент, который требует внимания:
Обратите внимание, что встроенные ресурсы включены в сборку так, как они были добавлены, т.е. если вы добавляете текстовый файл в качестве встроенного ресурса в приложение и открываете полученный EXE-файл в блокноте, вы увидите точное содержимое текстового файла. Поэтому, когда используете файл лицензии в качестве встроенного ресурса, любой может открыть exe-файл в простом текстовом редакторе и увидеть/извлечь содержимое лицензии.

Следовательно, чтобы добавить дополнительный уровень безопасности при встраивании лицензии в приложение, вы можете сжать/зашифровать лицензию, а затем встроить её в сборку. Предположим, у нас есть файл лицензии Aspose.PDF.lic, давайте создадим Aspose.PDF.zip с паролем test и встроим этот zip-файл в решение. Следующий фрагмент кода можно использовать для инициализации лицензии:

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            //Получаем количество страниц документа
            Console.WriteLine(doc.Pages.Count);
        }

        private static Stream GetSecureLicenseFromStream()
        {
            var assembly = Assembly.GetExecutingAssembly();
            var memoryStream = new MemoryStream();
            using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
            {
                using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
                {
                    var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
                    unpackedLicense?.Open().CopyTo(memoryStream);
                }
            }

            memoryStream.Position = 0;
            return memoryStream;
        }
    }
}
```
### Применение лицензии, купленной до 22.01.2005

Aspose.PDF для .NET больше не поддерживает лицензии старого образца. Если у вас есть лицензия, купленная до 22 января 2005 года, и вы обновились до более новой версии Aspose.PDF, пожалуйста, свяжитесь с нашей командой продаж, чтобы получить новый файл лицензии.
