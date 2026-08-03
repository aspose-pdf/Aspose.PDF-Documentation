---
title: HTML-форматирование
linktitle: HTML-форматирование
type: docs
weight: 20
url: /reportingservices/html-formatting/
description: Включите форматирование HTML в отчетах PDF с помощью Aspose.PDF для служб Reporting Services. Легко добавляйте стили и структуру.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Иногда вам может потребоваться экспортировать текст в текстовые поля с форматированием. К сожалению, службы Reporting Services не поддерживают это. Однако вы все равно можете реализовать его с помощью Aspose.PDF для служб Reporting Services. Просто включите специальный режим, в котором весь текст в текстовых полях обрабатывается как HTML, и поместите необходимые HTML-теги для форматирования текста в выходном документе. Например, чтобы в одном текстовом поле был обычный, жирный и курсивный текст, введите следующее значение текстового поля:

Часть этого текста — `<b>bold</b>`, а другая — `<i>italic</i>`.

При экспорте текст будет выглядеть так: часть этого текста выделена **жирным**, а другая часть — *курсивом*.

Обратите внимание, что этот подход имеет некоторые ограничения.

{{% /alert %}}

{{% alert color="primary" %}}

- Форматирование не отображается во время разработки (в построителе отчетов, веб-портале служб Reporting Services и т. д.). Вместо этого вы увидите HTML-текст в виде обычного текста с тегами.
- Расширение рендеринга Aspose.PDF для служб Reporting Services распознает и правильно форматирует HTML-код в текстовых полях. Средство обработки PDF-файлов по умолчанию служб Reporting Services экспортирует эту разметку как обычный текст.

```text
Parameter Name: IsHtmlTagSupported  
Date Type: Boolean  
Values supported: True, False (default)   
```

## Пример

```xml
<Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>
```

Если вы хотите добавить этот параметр в Дизайнер отчетов, используйте тип данных `Boolean`.

В настоящее время Aspose.Pdf для служб Reporting Services поддерживает подмножество всех тегов HTML. Дополнительную информацию можно найти в Aspose.PDF [Документация](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}
