---
title: Настройка параметров
linktitle: Настройка параметров
type: docs
weight: 10
url: /reportingservices/setting-parameters/
description: Узнайте, как установить параметры рендеринга PDF в Aspose.PDF для служб Reporting Services. Обеспечьте точный контроль над производительностью.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Вы можете указать определенные параметры конфигурации, которые влияют на то, как Aspose.PDF for Reporting Services генерирует документы. В этом разделе описан этот процесс.

{{% /alert %}}

Чтобы настроить Aspose.Pdf для служб Reporting Services, вам необходимо отредактировать файл `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. Это файл XML, и конфигурация средства визуализации находится внутри элемента `<Extension>`, соответствующего средству визуализации Aspose.PDF.

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

Если вы хотите установить параметры для конкретного файла отчета, а не для каждого отчета на сервере, вы можете добавить параметр отчета для конкретного отчета в построителе отчетов, выполнив следующие действия (например, мы добавим параметр «IsLandscape», показанный ранее):

1. Откройте отчет в Дизайнере отчетов, щелкните правой кнопкой мыши папку «Параметры» на панели «Данные отчета» и выберите «Добавить параметр…» (или, альтернативно, вытащите список «Новый» и выберите «Параметр…»).

![Parameters set up. Step 1](setting-parameters_1.png)

1. В диалоговом окне «Свойства параметра отчета» создайте параметр с именем «IsLandscape» с типом данных Boolean и добавьте значение True на вкладке «Значения по умолчанию».

![Parameters set up. Step 2](setting-parameters_2.png)

{{% /alert %}}
