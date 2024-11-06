---
title: ASP.NET без использования Visual Studio
type: docs
weight: 60
url: ru/net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF для .NET](/pdf/net/) может использоваться для разработки страниц или приложений ASP.NET без использования Visual Studio. В этом примере мы напишем HTML и код на C# или VB.NET в одном файле .aspx; это обычно называется Instant ASP.NET.

{{% /alert %}}

## Детали реализации

{{% alert color="primary" %}}

Создайте образец веб-приложения и скопируйте Aspose.PDF.dll в каталог под названием "Bin" в директории вашего сайта ( *если папка bin не существует, создайте её* ). Затем создайте вашу .aspx страницу и скопируйте следующий код в неё.
Этот пример показывает, как использовать [Aspose.PDF для .NET](/pdf/net/) с встроенным кодом на странице ASP.NET для создания простого PDF-документа с некоторым образцом текста внутри.
{{% /alert %}}

```cs

<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> используя Aspose.PDF для .NET с Inline ASP.NET</title>
    </head>
    <body>
        <h3>создание простого PDF-документа при использовании Aspose.PDF для .NET с Inline ASP.NET</h3>
<%
    // установка лицензии
    Aspose.PDF.License lic = new Aspose.PDF.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // Инициализация объекта документа
    Document document = new Document();
    // Добавление страницы
    Page page = document.Pages.Add();
    // Добавление текста на новую страницу
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Привет, мир!"));
    // Сохранение обновленного PDF
    var outputFileName = Path.Combine(_dataDir, "HelloWorld_out.pdf");
    document.Save( outputFileName );
%>

    </body>
</html>
```

