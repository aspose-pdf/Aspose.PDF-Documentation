---
title: Работа с JavaScript
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /ru/net/working-with-javascript/
description: Узнайте, как добавлять, изменять и выполнять JavaScript в PDF-документах с помощью Aspose.PDF for .NET. Улучшите интерактивность и автоматизацию.
lastmod: "2025-02-07"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with JavaScript",
    "alternativeHeadline": "Enhance PDF with Custom JavaScript Actions",
    "abstract": "Откройте для себя расширенные возможности интеграции JavaScript в PDF-документы с помощью Aspose.PDF for .NET. Эта новая функция позволяет разработчикам добавлять и управлять действиями JavaScript как на уровне документа, так и на уровне страницы, обеспечивая интерактивный и динамичный опыт работы с PDF, направленный на улучшение вовлеченности пользователей и функциональности. Откройте потенциал JavaScript для создания сложных PDF-форм, которые имитируют поведение веб-приложений, улучшая ваши рабочие процессы генерации документов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "JavaScript, Acrobat JavaScript, PDF document generation, JavaScript collection, document level JavaScript, JavaScript Action, interactive PDF forms, manipulate PDF files, HTML JavaScript, Aspose.PDF for .NET",
    "wordcount": "423",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Добавление JavaScript (DOM)

### Что такое Acrobat JavaScript?

Acrobat JavaScript — это язык, основанный на ядре JavaScript версии 1.5 ISO-16262, ранее известный как ECMAScript, объектно-ориентированный язык сценариев, разработанный компанией Netscape Communications. JavaScript был создан для разгрузки обработки веб-страниц с сервера на клиент в веб-приложениях. Acrobat JavaScript реализует расширения в виде новых объектов и их сопутствующих методов и свойств для языка JavaScript. Эти специфические для Acrobat объекты позволяют разработчику управлять безопасностью документа, взаимодействовать с базой данных, обрабатывать вложения файлов, манипулировать PDF-файлом так, чтобы он вел себя как интерактивная форма, поддерживающая веб, и так далее. Поскольку специфические для Acrobat объекты добавляются поверх основного JavaScript, у вас по-прежнему есть доступ к его стандартным классам, включая Math, String, Date, Array и RegExp.

### Acrobat JavaScript против HTML (Web) JavaScript

PDF-документы обладают большой универсальностью, так как их можно отображать как в программном обеспечении Acrobat, так и в веб-браузере. Поэтому важно быть в курсе различий между Acrobat JavaScript и JavaScript, используемым в веб-браузере, также известным как HTML JavaScript:

- Acrobat JavaScript не имеет доступа к объектам внутри HTML-страницы. Аналогично, HTML JavaScript не может получить доступ к объектам внутри PDF-файла.
- HTML JavaScript может манипулировать такими объектами, как Window. Acrobat JavaScript не может получить доступ к этому конкретному объекту, но может манипулировать специфическими для PDF объектами.

Вы можете добавлять JavaScript как на уровне документа, так и на уровне страницы, используя [Aspose.PDF for .NET](/pdf/ru/net/). Чтобы добавить JavaScript:

### Добавление JavaScript к действию документа или страницы

1. Объявите и создайте объект JavascriptAction с желаемым оператором JavaScript в качестве аргумента конструктора.
1. Назначьте объект JavascriptAction желаемому действию PDF-документа или страницы.

Пример ниже применяет OpenAction к конкретному документу.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Adding JavaScript at Document Level
        // Instantiate JavascriptAction with desired JavaScript statement
        var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

        // Assign JavascriptAction object to desired action of Document
        document.OpenAction = javaScript;

        // Adding JavaScript at Page Level
        document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
        document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

        // Save PDF Document
        document.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Adding JavaScript at Document Level
    // Instantiate JavascriptAction with desired JavaScript statement
    var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    // Assign JavascriptAction object to desired action of Document
    document.OpenAction = javaScript;

    // Adding JavaScript at Page Level
    document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
    document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

    // Save PDF Document
    document.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Добавление/удаление JavaScript на уровне документа

В классе Document добавлено новое свойство с именем JavaScript, которое имеет тип коллекции JavaScript и предоставляет доступ к сценариям JavaScript по его ключу. Это свойство используется для добавления JavaScript на уровне документа. Коллекция JavaScript имеет следующие свойства и методы:

- string this(string key)– Получает или устанавливает JavaScript по его имени.
- IList Keys – предоставляет список существующих ключей в коллекции JavaScript.
- bool Remove(string key) – удаляет JavaScript по его ключу.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        document.JavaScript["func1"] = "function func1() { hello(); }";
        document.JavaScript["func2"] = "function func2() { hello(); }";
        document.Save(dataDir + "AddJavascript.pdf");
    }

    // Remove Document level JavaScript
    using (var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf"))
    {
        var keys = (IList)document1.JavaScript.Keys;

        Console.WriteLine("=============================== ");

        foreach (string key in keys)
        {
            Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
        }

        document1.JavaScript.Remove("func1");

        Console.WriteLine("Key 'func1' removed ");
        Console.WriteLine("=============================== ");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();
    document.JavaScript["func1"] = "function func1() { hello(); }";
    document.JavaScript["func2"] = "function func2() { hello(); }";
    document.Save(dataDir + "AddJavascript.pdf");

    // Remove Document level JavaScript
    using var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf");
    IList keys = (IList)document1.JavaScript.Keys;

    Console.WriteLine("=============================== ");

    foreach (string key in keys)
    {
        Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
    }

    document1.JavaScript.Remove("func1");

    Console.WriteLine("Key 'func1' removed ");
    Console.WriteLine("=============================== ");
}
```
{{< /tab >}}
{{< /tabs >}}

### Установка даты истечения срока действия PDF-документа с помощью действий JavaScript

Aspose.PDF позволяет устанавливать дату истечения срока действия для PDF-документа, встраивая действия JavaScript. Эта функциональность обеспечивает недоступность PDF после указанной даты и времени, повышая безопасность и контроль документа. Используя действия JavaScript, вы можете определить точные условия истечения вплоть до секунды, обеспечивая строгую регуляцию доступности документа.

**Вы можете достичь этого, следуя этим шагам**

1. **Инициализация документа:** Создайте новый PDF-документ и добавьте пустую страницу или откройте существующий PDF-документ.
2. **Определите дату и время истечения:** Установите дату и время, после которых документ истечет.
3. **Подготовьте код JavaScript:** 
    - Получите текущую дату и время.
    - Определите точную дату и время истечения, учитывая, что месяцы в JavaScript начинаются с нуля.
    - Сравните текущую дату и время с датой и временем истечения.
    - Если текущая дата и время превышают дату и время истечения, отобразите предупреждение и закройте документ.
4. **Установите действие открытия:** Свяжите действие JavaScript с действием открытия документа.
5. **Сохраните документ:** Сохраните PDF с встроенным JavaScript, который обеспечивает условие истечения.

Ниже приведены фрагменты кода, демонстрирующие эту функциональность как на C# (.NET), так и на Java.

Следующий фрагмент кода на C# демонстрирует, как установить дату и время истечения для PDF-документа с помощью действий JavaScript с Aspose.PDF:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();

        // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
        DateTime expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

        // Create JavaScript code to enforce the expiry date and time
        string jsCode =
            // Get the current date and time
            "var rightNow = new Date();\n" +
            // Set the expiry date and time
            "var endDate = new Date(" +
            $"{expiryDateTime.Year}," +
            $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
            $"{expiryDateTime.Day}," +
            $"{expiryDateTime.Hour}," +
            $"{expiryDateTime.Minute}," +
            $"{expiryDateTime.Second}" +
            ");\n" +
            "if(rightNow > endDate)\n" +
            "{\n" +
            "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
            "    this.closeDoc();\n" +
            "}";

        // Create a JavascriptAction with the defined JavaScript code
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

        // Set the JavaScript action to execute when the document is opened
        document.OpenAction = javaScript;

        // Save PDF document
        document.Save(dataDir + "PDFExpiry_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();

    // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
    var expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

    // Create JavaScript code to enforce the expiry date and time
    string jsCode =
        // Get the current date and time
        "var rightNow = new Date();\n" +
        // Set the expiry date and time
        "var endDate = new Date(" +
        $"{expiryDateTime.Year}," +
        $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
        $"{expiryDateTime.Day}," +
        $"{expiryDateTime.Hour}," +
        $"{expiryDateTime.Minute}," +
        $"{expiryDateTime.Second}" +
        ");\n" +
        "if(rightNow > endDate)\n" +
        "{\n" +
        "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
        "    this.closeDoc();\n" +
        "}";

    // Create a JavascriptAction with the defined JavaScript code
    var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

    // Set the JavaScript action to execute when the document is opened
    document.OpenAction = javaScript;

    // Save PDF document
    document.Save(dataDir + "PDFExpiry_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

- **Объект даты JavaScript:** В JavaScript индекс месяца начинается с `0` для января и заканчивается на `11` для декабря. Убедитесь, что значение месяца скорректировано соответствующим образом при установке даты и времени истечения.
  
- **Соображения безопасности:** Хотя действия JavaScript могут контролировать поведение PDF-документа, они зависят от поддержки JavaScript со стороны просмотрщика PDF. Не все просмотрщики PDF могут учитывать эти скрипты, и пользователи могут отключить выполнение JavaScript по соображениям безопасности.

- **Настройка:** Измените код JavaScript, чтобы выполнять дополнительные действия по истечении, такие как отключение определенных функций, перенаправление на конкретную страницу или ведение журнала события. Кроме того, при необходимости вы можете проверять только дату истечения без указания времени.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>