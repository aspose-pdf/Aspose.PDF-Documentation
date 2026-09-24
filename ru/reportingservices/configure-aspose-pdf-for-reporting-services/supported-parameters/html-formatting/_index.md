---
title: HTML‑форматирование
linktitle: HTML‑форматирование
type: docs
weight: 20
url: /ru/reportingservices/html-formatting/
description: Включите HTML‑форматирование в PDF‑отчётах с помощью Aspose.PDF for Reporting Services. Добавляйте стили и структуру с лёгкостью.
lastmod: "2021-06-05"
---
{{% alert color="primary" %}}

Иногда вам может потребоваться экспортировать текст в текстовых полях с форматированием. К сожалению, Reporting Services этого не поддерживает. Тем не менее, вы всё равно можете реализовать это с помощью **Aspose.PDF for Reporting Services**. Просто включите специальный режим, в котором весь текст в текстовых полях рассматривается как HTML, и добавьте необходимые HTML‑теги для форматирования текста в выходном документе. Например, чтобы в одном текстовом поле было обычный, жирный и курсивный текст, введите следующее значение текстового поля:

Некоторая часть этого текста `<b>bold</b>`, а другой текст `<i>italic</i>`.

При экспорте текст будет выглядеть так: некоторая часть этого текста **жирный** и другой текст *курсивный*.

Обратите внимание, что у этого подхода есть некоторые ограничения

{{% /alert %}}

{{% alert color="primary" %}}

- Форматирование не видно в режиме дизайна (в Report Builder, веб‑портале Reporting Services и т.д.). Вместо этого вы увидите HTML‑текст в виде обычного текста с тегами.
- Расширение рендеринга **Aspose.PDF for Reporting Services** распознаёт и правильно форматирует HTML‑код в текстовых полях. Стандартный PDF‑рендерер Reporting Services экспортирует эту разметку как обычный текст.

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

Если вы хотите добавить этот параметр в Report Designer, используйте тип данных `Boolean`.

В настоящее время Aspose.Pdf for Reporting Services поддерживает подмножество всех HTML‑тегов. Более подробную информацию можно найти в [Документации](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom) Aspose.PDF.

{{% /alert %}}


