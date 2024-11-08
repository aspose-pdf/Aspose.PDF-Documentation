---
title: ASP - JScript через COM Interop
type: docs
weight: 40
url: /ru/net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

Это простое приложение ASP, которое показывает, как добавить простую текстовую строку в файл PDF с использованием [Aspose.PDF для .NET](/pdf/ru/net/) и JScript через COM Interop.

{{% /alert %}}

Пример:

{{% alert color="primary" %}}

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title>Использование Aspose.PDF для .NET в классическом примере ASP</title>
    </head>
    <body>
        <h3>Создание образца PDF-документа с использованием Aspose.PDF для .NET в классическом ASP и JScript</h3>
<%
// установка лицензии
var lic = Server.CreateObject("Aspose.PDF.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// Создание экземпляра Pdf, вызвав его пустой конструктор
var pdf = Server.CreateObject("Aspose.PDF.Document");

// Создание новой страницы в объекте PDF
var pdfpage = pdf.Pages.Add();

// Создание объекта текстового фрагмента
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// Назначение содержимого фрагменту
sampleText.Text = "HelloWorld с использованием ASP и JScript";

// Добавление текстового параграфа в коллекцию параграфов раздела
pdfpage.Paragraphs.Add(sampleText);

// Сохранение документа PDF
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```

{{% /alert %}}

