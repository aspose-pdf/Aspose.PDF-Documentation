---
title: HTML-форматирование
linktitle: HTML-форматирование
type: docs
weight: 20
url: /ru/reportingservices/html-formatting/
description: Включите форматирование HTML в PDF‑отчетах, используя Aspose.PDF for Reporting Services. Добавляйте стили и структуру с лёгкостью.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Иногда вы можете захотеть экспортировать текст в текстовых полях с форматированием. К сожалению, Reporting Services не поддерживает это. Однако вы всё равно можете реализовать это с помощью Aspose.PDF for Reporting Services. Просто включите специальный режим, в котором весь текст в текстовых полях рассматривается как HTML, и добавьте необходимые HTML‑теги для форматирования текста в выходном документе. Например, чтобы иметь обычный, жирный и курсивный текст в одном текстовом поле, введите следующее значение текстового поля:

Некоторая часть этого текста ```<b>bold</b>``` и другой текст ```<i>italic</i>```.

При экспорте текст будет выглядеть так, как будто часть этого текста **bold**, а другая часть *italic*.

Обратите внимание, что у этого подхода есть некоторые ограничения

{{% /alert %}}

{{% alert color="primary" %}}

- Форматирование не отображается во время разработки (в Report Builder, веб‑портале Reporting Services и т.д.). Вместо этого вы увидите HTML‑текст в виде обычного текста с тегами.
- Расширение рендеринга Aspose.PDF for Reporting Services распознаёт и правильно форматирует HTML‑код в текстовых полях. Стандартный PDF‑рендерер Reporting Services экспортирует эту разметку как обычный текст.

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

 
В настоящее время Aspose.Pdf for Reporting Services поддерживает подмножество всех HTML‑тегов. Вы можете найти более подробную информацию в Aspose.PDF. [Документация](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}

