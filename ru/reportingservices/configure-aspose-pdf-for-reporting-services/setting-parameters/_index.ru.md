---
title: Установка Параметров
type: docs
weight: 10
url: /reportingservices/setting-parameters/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Вы можете указать определенные параметры конфигурации, которые влияют на то, как Aspose.Pdf для Reporting Services генерирует документы. Этот раздел описывает этот процесс.

{{% /alert %}}

Чтобы настроить Aspose.Pdf для Reporting Services, вам нужно отредактировать файл C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config. Это XML-файл, и конфигурация рендерера находится внутри элемента ```<Extension>```, соответствующего рендереру Aspose.PDF.

**Пример**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Вставьте элементы конфигурации для экспорта в PDF здесь. Следующий пример
Для PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% alert color="primary" %}}

Если вы хотите установить параметры для конкретного файла отчета, но не для каждого отчета на сервере, вы можете добавить параметр отчета для конкретного отчета в Конструкторе отчетов, выполнив следующие шаги (например, мы добавим параметр 'IsLandscape', показанный ранее):

1. Откройте отчет в Дизайнере отчетов, щелкните правой кнопкой мыши на папке 'Parameters' в области 'Report Data' и выберите 'Add Parameter…' (или, альтернативно, раскройте список 'New' и выберите 'Parameter…').
 
![todo:image_alt_text](setting-parameters_1.png)

1. В диалоговом окне 'Report Parameter Properties' создайте параметр с именем 'IsLandscape', с типом данных Boolean и добавьте значение True на вкладке 'Default Values'.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}