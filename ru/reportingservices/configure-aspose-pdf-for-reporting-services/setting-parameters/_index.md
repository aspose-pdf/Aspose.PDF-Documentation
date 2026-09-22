---
title: Настройка параметров
linktitle: Настройка параметров
type: docs
weight: 10
url: /ru/reportingservices/setting-parameters/
description: Узнайте, как задавать параметры рендеринга PDF в Aspose.PDF for Reporting Services. Добейтесь точного контроля над выводом.
lastmod: "2021-06-05"
---
{{% alert color="primary" %}}

Вы можете указать определённые параметры конфигурации, которые влияют на то, как Aspose.PDF for Reporting Services генерирует документы. В этом разделе описывается этот процесс.

{{% /alert %}}

Чтобы настроить Aspose.Pdf for Reporting Services, необходимо отредактировать файл `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. Это XML‑файл, а конфигурация рендерера находится внутри элемента `<Extension>`, соответствующего рендереру Aspose.PDF.

## Пример

```xml
<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>
```

{{% alert color="primary" %}}

Если вы хотите задать параметры для конкретного файла отчёта, а не для всех отчётов на сервере, вы можете добавить параметр отчёта для конкретного отчёта в Report Builder, выполнив следующие шаги (например, мы добавим параметр **'IsLandscape'**, показанный ранее):

1. Откройте отчёт в Report Designer, щёлкните правой кнопкой мыши папку **'Parameters'** в панели **'Report Data'** и выберите **'Add Parameter…'** (или, альтернативно, раскройте список **'New'** и выберите **'Parameter…'**).

![Настройка параметров. Шаг 1](setting-parameters_1.png)

2. В диалоговом окне **'Report Parameter Properties'** создайте параметр с именем **'IsLandscape'**, укажите тип данных **Boolean** и добавьте значение **True** на вкладке **'Default Values'**.

![Настройка параметров. Шаг 2](setting-parameters_2.png)

{{% /alert %}}


