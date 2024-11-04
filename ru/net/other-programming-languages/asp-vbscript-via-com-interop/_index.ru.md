---
title: ASP - VBScript через COM Interop
type: docs
weight: 30
url: /net/asp-vbscript-via-com-interop/
---

## Предварительные требования

{{% alert color="primary" %}}

    Пожалуйста, ознакомьтесь со статьей под названием Использование Aspose.pdf для .NET через COM Interop.

{{% /alert %}}

## Пример "Hello World!" на VB Script

{{% alert color="primary" %}}

Это простое приложение ASP, которое показывает, как создать PDF-файл с образцом текста с использованием [Aspose.PDF для .NET](/pdf/net/) и VBScript через COM Interop.

{{% /alert %}}

```vb

<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title> использование Aspose.PDF для .NET в классическом примере ASP</title>
    </head>
<body>

<h3>создание образца PDF-документа при использовании Aspose.PDF для .NET с классическим ASP и VBScript</h3>

<%

'установка лицензии
Dim lic
Set lic = CreateObject("Aspose.PDF.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'Создание экземпляра Pdf, вызвав его пустой конструктор
Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

'Создание нового раздела в объекте Pdf
Dim pdfsection
Set pdfsection = CreateObject("Aspose.PDF.Generator.Section")

'Добавление раздела в объект Pdf
pdf.Sections.Add(pdfsection)

' Создание объекта текста
Dim SampleText
Set SampleText = CreateObject("Aspose.PDF.Generator.Text")

'Добавление текстового сегмента к текстовому объекту
Dim seg1
Set seg1 = CreateObject("Aspose.PDF.Generator.Segment")

'Присвоение содержимого сегменту
seg1.Content = "HelloWorld используя ASP и VBScript"

'Добавление сегмента (с красным цветом текста) в абзац
SampleText.Segments.Add(seg1)

' Добавление текстового абзаца в коллекцию абзацев раздела
pdfsection.Paragraphs.Add(SampleText)

' Сохранение документа PDF
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")

%>

    </body>
</html>
```
## Извлечение текста с использованием VBScript

{{% alert color="primary" %}}
    Этот образец VBScript извлекает текст из существующего PDF-документа через COM Interop.
    Ошибка при рендеринге макроса 'code' : Указано неверное значение для параметра lang
{{% /alert %}}
