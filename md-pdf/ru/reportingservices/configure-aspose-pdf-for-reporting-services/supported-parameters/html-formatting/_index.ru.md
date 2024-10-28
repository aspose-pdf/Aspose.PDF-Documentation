---
title: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Иногда вы можете захотеть экспортировать текст в текстовых полях с форматированием. К сожалению, Reporting Services не поддерживает это. Однако, вы все еще можете реализовать это с помощью Aspose.PDF для Reporting Services. Просто включите специальный режим, в котором весь текст в текстовых полях рассматривается как HTML и добавьте необходимые HTML-теги для форматирования текста в выходном документе. Например, чтобы иметь обычный, жирный и курсивный текст в одном текстовом поле, введите следующее значение текстового поля:

Часть этого текста ```<b>жирная</b>``` и другой текст ```<i>курсивный</i>```.

При экспорте текст будет выглядеть так: часть этого текста **жирная** и другой текст *курсивный*.

Пожалуйста, обратите внимание, что у этого подхода есть некоторые ограничения

{{% /alert %}}

{{% alert color="primary" %}}

- Форматирование не видно на этапе разработки (в Report Builder, веб-портале Reporting Services и т.д.).  Вместо этого вы увидите HTML-текст в виде обычного текста с тегами.
- Расширение рендеринга Aspose.PDF для Reporting Services распознает и правильно форматирует HTML-код в текстовых полях. Стандартный PDF-рендерер Reporting Services экспортирует эту разметку как обычный текст.

**Имя параметра**: IsHtmlTagSupported  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (по умолчанию)   

**Пример**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

Если вы хотите добавить этот параметр в Report Designer, используйте тип данных 'Boolean'.

В настоящее время Aspose.Pdf для Reporting Services поддерживает подмножество всех HTML-тегов. Более подробную информацию вы можете найти в [документации](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom) Aspose.PDF.

{{% /alert %}}