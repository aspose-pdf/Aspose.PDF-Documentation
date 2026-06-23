---
title: Настройка параметров
linktitle: Настройка параметров
type: docs
weight: 10
url: /ru/reportingservices/setting-parameters/
description: Узнайте, как задать параметры для рендеринга PDF в Aspose.PDF for Reporting Services. Добейтесь точного контроля над выводом.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Вы можете указать определённые конфигурационные параметры, которые влияют на то, как Aspose.Pdf for Reporting Services генерирует документы. Этот раздел описывает этот процесс.

{{% /alert %}}

Чтобы настроить Aspose.Pdf for Reporting Services, вам нужно отредактировать файл C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config. Это XML‑файл, и конфигурация рендерера находится внутри ```<Extension>``` элемент, соответствующий рендереру Aspose.PDF.

**Пример**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% alert color="primary" %}}

Если вы хотите задать параметры для конкретного файла отчёта, а не для всех отчётов на сервере, вы можете добавить параметр отчёта для конкретного отчёта в Report Builder, следуя следующим шагам (например, мы добавим параметр ‘IsLandscape’, показанный ранее):

1. Откройте отчёт в Report Designer, щёлкните правой кнопкой мыши папку ‘Parameters’ в панели ‘Report Data’ и выберите ‘Add Parameter…’ (или, альтернативно, раскройте список ‘New’ и выберите ‘Parameter…’).
 
![todo:image_alt_text](setting-parameters_1.png)

1. В диалоговом окне ‘Report Parameter Properties’ создайте параметр с именем ‘IsLandscape’, типом данных Boolean, и добавьте значение True во вкладке ‘Default Values’.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}

