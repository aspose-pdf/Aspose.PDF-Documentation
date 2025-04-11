---
title: Лицензия Aspose PDF
linktitle: Лицензирование и ограничения
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ru/net/licensing/
description: Aspose. PDF для .NET приглашает своих клиентов получить классическую лицензию и лицензии с учетом использования. А также использовать ограниченную лицензию для более глубокого изучения продукта.
lastmod: "2025-02-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose PDF for .NET License",
    "alternativeHeadline": "Licensing Options for Aspose.PDF for .NET Users",
    "abstract": "Aspose PDF для .NET представляет собой надежную лицензионную структуру, включающую как классические, так и лицензии с учетом использования, позволяя пользователям выбирать между фиксированными ценами и расчетами на основе использования. Классическую лицензию можно легко загрузить из файла или потока, в то время как инновационная лицензия с учетом использования предоставляет гибкое измерение на основе использования API, удовлетворяя разнообразные потребности пользователей. Эта стратегия двойного лицензирования улучшает доступность и масштабируемость PDF-решений для разработчиков.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "869",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/licensing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/licensing/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для опытных пользователей и разработчиков."
}
</script>

## Ограничение оценочной версии

Мы хотим, чтобы наши клиенты тщательно протестировали наши компоненты перед покупкой, поэтому оценочная версия позволяет вам использовать ее так, как вы обычно это делаете.

- **PDF, созданный с оценочным водяным знаком.** Оценочная версия Aspose.PDF for .NET предоставляет полную функциональность продукта, но все страницы в сгенерированных PDF-документах имеют водяной знак с текстом "Только для оценки. Создано с помощью Aspose.PDF. Авторские права 2002-2025 Aspose Pty Ltd." вверху.

- **Ограничение количества страниц, которые можно обработать.**
В оценочной версии вы можете обрабатывать только первые четыре страницы документа.

> Если вы хотите протестировать Aspose.PDF for .NET без ограничений оценочной версии, вы также можете запросить временную лицензию на 30 дней. Пожалуйста, обратитесь к [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)

## Классическая лицензия

Лицензия может быть загружена из файла или объекта потока. Самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.PDF.dll, и указать имя файла без пути, как показано в примере ниже.

Если вы используете любой другой компонент Aspose для .NET вместе с Aspose.PDF for .NET, пожалуйста, укажите пространство имен для лицензии, например [Aspose.Pdf.License](https://reference.aspose.com/pdf/ru/net/aspose.pdf/license).

### Загрузка лицензии из файла

Самый простой способ применить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.PDF.dll, и указать только имя файла без пути.

Когда вы вызываете метод [SetLicense](https://reference.aspose.com/pdf/ru/net/aspose.pdf/license/methods/setlicense/index), имя лицензии, которое вы передаете, должно соответствовать имени вашего файла лицензии. Например, если вы измените имя файла лицензии на "Aspose.PDF.lic.xml", передайте это имя файла в метод Pdf.SetLicense(…).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseExample()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // Something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### Загрузка лицензии из объекта потока

Следующий пример показывает, как загрузить лицензию из потока.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    // Load license from the file stream
    var myStream = new FileStream(
            "Aspose.Pdf.lic",
            FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## Лицензия с учетом использования

Aspose.PDF позволяет разработчикам применять лицензионный ключ с учетом использования. Механизм лицензирования с учетом использования будет использоваться вместе с существующим методом лицензирования. Те клиенты, которые хотят получать счета на основе использования функций API, могут использовать лицензирование с учетом использования. Для получения дополнительной информации, пожалуйста, обратитесь к разделу Часто задаваемые вопросы по лицензированию с учетом использования.
Этот гид предоставляет лучшие практики для плавной реализации и предотвращения сбоев из-за изменений статуса лицензии.

Класс "Metered" используется для применения лицензий с учетом использования. Следующий пример кода демонстрирует, как установить публичные и приватные ключи с учетом использования.

Для получения дополнительной информации, пожалуйста, обратитесь к разделу [Часто задаваемые вопросы по лицензированию с учетом использования](https://purchase.aspose.com/faqs/licensing/metered).

__Методы лицензирования с учетом использования__

Применяя лицензию с учетом использования, используйте метод `SetMeteredKey`, чтобы активировать лицензию с учетом использования, предоставив ваши публичные и приватные ключи. Это должно быть сделано один раз во время инициализации приложения, чтобы обеспечить правильное лицензирование.

Пример:

```csharp
 var metered = new Aspose.Pdf.Metered();
 metered.SetMeteredKey("your-public-key", "your-private-key");
 ```
Проверка статуса лицензии использует `IsMeteredLicensed()`, чтобы проверить, активна ли лицензия с учетом использования.

Пример:

```csharp
bool isLicensed = Aspose.Pdf.License.IsMeteredLicensed();
if (!isLicensed) 
{
    metered.SetMeteredKey("your-public-key", "your-private-key");
}
 ```
Метод `Metered.GetConsumptionCredit()` используется для получения информации о кредитах потребления.
Метод `Metered.GetConsumptionQuantity()` используется для получения информации о размере файла потребления.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMeteredLicense()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    // Set metered public and private keys
    var metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey("your public key", "your private key");
    // Get current Consumption Credit and Quantity
    var currentMonthCreditsSpent = Aspose.Pdf.Metered.GetConsumptionCredit();
    var currentMonthConsumedMegabytes = Aspose.Pdf.Metered.GetConsumptionQuantity();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Add five pages
        AddPages(document, 5);

        // Save the document
        document.Save(dataDir + "output.pdf");

        // Wait to be sure the transaction completed
        System.Threading.Thread.Sleep(10000);
        // Get current Consumption Credit and Quantity
        var nowCredit = Aspose.Pdf.Metered.GetConsumptionCredit();
        var nowQuantity = Aspose.Pdf.Metered.GetConsumptionQuantity();
        Console.WriteLine("Credit: was={0} now={1} difference={2}", currentMonthCreditsSpent, nowCredit, nowCredit - currentMonthCreditsSpent);
        Console.WriteLine("Quantity: was={0} now={1} difference={2}", currentMonthConsumedMegabytes, nowQuantity, nowQuantity - currentMonthConsumedMegabytes); 
    }
}

private static void AddPages(Document document, int n)
{
    for (int i = 0; i < n; i++)
    {
        document.Pages.Add();
    }
}
```

__Лучшие практики для лицензирования с учетом использования__

✅ Рекомендуемый подход: Паттерн Singleton
Чтобы обеспечить стабильную настройку лицензирования:

- Применяйте лицензию один раз при запуске приложения.
- Используйте паттерн Singleton (или аналогичный подход) для создания и повторного использования экземпляра лицензии с учетом использования.
- Периодически проверяйте статус лицензии с помощью `IsMeteredLicensed()`. Повторно применяйте лицензию только в случае ее недействительности.
- Если реализовано правильно, лицензия остается действительной в течение 24 часов, даже если сервер лицензий временно недоступен.

Пример: Реализация Singleton

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public class AsposeLicenseManager
{
    private static AsposeLicenseManager _instance;
    private static readonly object _lock = new object();
    private Aspose.Pdf.Metered _metered;

    private AsposeLicenseManager()
    {
        _metered = new Aspose.Pdf.Metered();
        _metered.SetMeteredKey("your-public-key", "your-private-key");
    }

    public static AsposeLicenseManager Instance
    {
        get
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new AsposeLicenseManager();
                }
                return _instance;
            }
        }
    }

    public void ValidateLicense()
    {
        if (!Aspose.Pdf.License.IsMeteredLicensed())
        {
        _metered.SetMeteredKey("your-public-key", "your-private-key");
        }
    }
}
```

❌ Общие ошибки, которых следует избегать:

- Частые применения лицензии
- Не создавайте новый экземпляр лицензии с учетом использования для каждой операции.
- Если сервер лицензий недоступен во время инициализации, лицензия может вернуться в режим оценки.
- Не применяйте лицензию повторно для каждой операции.
- Частые применения лицензии могут привести к возврату в режим пробной версии, если сервер лицензий временно недоступен.

__Резюме:__

✅ Установите лицензию с учетом использования один раз при запуске приложения.
✅ Используйте паттерн Singleton для управления единственным экземпляром.
✅ Периодически проверяйте и повторно применяйте лицензию при необходимости.
❌ Избегайте частых применений лицензии, чтобы предотвратить возврат в режим пробной версии.
Следуя этим лучшим практикам, вы обеспечите плавное и непрерывное использование Aspose.PDF с лицензированием с учетом использования.

Если лицензия была инициализирована, то пока этот объект "существует", даже если соединение с сервером лицензий потеряно по какой-либо причине, лицензия будет считаться активной еще в течение 7 дней. Если вы инициализируете лицензию каждый раз, когда вам нужно что-то сделать, и в момент инициализации нет соединения с сервером, лицензия перейдет в режим оценки.
Следует дополнительно подчеркнуть, что если пользователь инициализировал лицензию, то пока этот объект "существует", даже если соединение с сервером лицензий потеряно по какой-либо причине, лицензия будет считаться активной еще в течение 24 часов. Если вы инициализируете лицензию каждый раз, когда вам нужно что-то сделать, и в момент инициализации нет соединения с сервером, лицензия перейдет в режим оценки.

Пожалуйста, обратите внимание, что приложения COM, которые работают с **Aspose.PDF for .NET**, также должны использовать класс License.

Один момент, который требует внимания:
Пожалуйста, обратите внимание, что встроенные ресурсы включены в сборку так, как они добавлены, т.е. если вы добавите текстовый файл как встроенный ресурс в приложение и откроете полученный EXE в блокноте, вы увидите точное содержимое текстового файла. Поэтому, когда вы используете файл лицензии как встроенный ресурс, любой может открыть exe-файл в простом текстовом редакторе и увидеть/извлечь содержимое встроенной лицензии.

Поэтому, чтобы добавить дополнительный уровень безопасности при встраивании лицензии в приложение, вы можете сжать/зашифровать лицензию, а затем встроить ее в сборку. Предположим, у нас есть файл лицензии Aspose.PDF.lic, так что давайте создадим Aspose.PDF.zip с паролем test и встроим этот zip-файл в решение. Следующий фрагмент кода можно использовать для инициализации лицензии:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    var license = new Aspose.Pdf.License();
    license.SetLicense(GetSecureLicenseFromStream());
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the page count of document
        Console.WriteLine(document.Pages.Count);
    }
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
```