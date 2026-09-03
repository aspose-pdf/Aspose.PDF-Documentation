---
title: Настройка параметров
linktitle: Настройка параметров
type: docs
weight: 10
url: /ru/reportingservices/setting-parameters/
description: Узнайте, как задать параметры для рендеринга PDF в Aspose.PDF for Reporting Services и добиться точного контроля над выводом.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Вы можете указать определенные параметры конфигурации, которые влияют на то, как Aspose.PDF for Reporting Services создает документы. В этом разделе описан данный процесс.

{{% /alert %}}

Чтобы настроить Aspose.PDF for Reporting Services, нужно отредактировать файл `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. Это XML-файл, а конфигурация рендерера находится внутри элемента ```<Extension>```, соответствующего рендереру Aspose.PDF.

**Пример**

{{< highlight csharp >}}

<Render>
...
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

Если вы хотите задать параметры только для конкретного файла отчета, а не для всех отчетов на сервере, вы можете добавить параметр отчета для этого отчета в Report Builder, выполнив следующие действия. В качестве примера ниже добавляется параметр `IsLandscape`, показанный ранее.

1. Откройте отчет в Report Designer, щелкните правой кнопкой мыши папку `Parameters` на панели `Report Data` и выберите `Add Parameter...`. Также можно открыть список `New` и выбрать `Parameter...`.
 
![todo:image_alt_text](setting-parameters_1.png)

1. В диалоговом окне `Report Parameter Properties` создайте параметр с именем `IsLandscape`, задайте тип данных Boolean и добавьте значение True на вкладке `Default Values`.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}

