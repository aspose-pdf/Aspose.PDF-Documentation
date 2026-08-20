---
title: Установить на сервер отчетов
linktitle: Установить на сервер отчетов
type: docs
weight: 10
url: /ru/reportingservices/install-to-report-server/
description: Узнайте, как установить Aspose.PDF for Reporting Services на сервер отчетов.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Вам необходимо выполнить эти шаги только в том случае, если вы устанавливаете Aspose.PDF для служб Reporting Services вручную, не используя установщик MSI. Установщик MSI автоматически выполняет все необходимые действия по установке и регистрации.

{{% /alert %}}

На следующих шагах вам потребуется скопировать и изменить файлы в каталоге, в котором установлены службы отчетов Microsoft SQL Server. Сборка SSRS 2016 расположена в каталоге \Bin\SSRS2016 zip-пакета; сборка SSRS 2017 находится в каталоге \Bin\SSRS2017; сборка SSRS 2019 находится в каталоге \Bin\SSRS2019; сборка SSRS 2022 находится в каталоге \Bin\SSRS2022; сборка Сервера отчетов Power BI находится в каталоге \Bin\PowerBI.

**Шаг 1.** Найдите каталог установки сервера отчетов. Корневым каталогом Microsoft SQL Server обычно является C:\Program Files\Microsoft SQL Server. Дальнейший процесс немного отличается для служб Reporting Services 2016, Reporting Services 2017 и более поздних версий, а также сервера отчетов Power BI:

- Сервер отчетов 2016 по умолчанию устанавливается в каталог C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Если вы используете экземпляры с собственным именем вместо экземпляра по умолчанию, путь по умолчанию будет C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer.
- Сервер отчетов 2017 и более поздних версий по умолчанию устанавливается в каталог C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Сервер отчетов Power BI по умолчанию устанавливается в каталог C:\Program Files\Microsoft Сервер отчетов Power BI\PBIRS\ReportServer.

В следующем тексте каталог установки служб Reporting Services (один из вышеупомянутых путей) будет называться `<Instance>`.

**Шаг 2.** Скопируйте Aspose.Pdf.ReportingServices.dll для соответствующей версии SSRS в папку `<Instance>\bin`.

**Шаг 3.** Зарегистрируйте Aspose.PDF для служб Reporting Services в качестве расширения рендеринга. Откройте файл `<Instance>\rsreportserver.config` и добавьте в элемент `<Render>` следующие строки:

## Пример

```xml
<Render>
...
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>
</Render>
```

**Шаг 4.** Предоставьте Aspose.PDF для служб Reporting Services разрешения на выполнение. Откройте файл `<Instance>\rssrvpolicy.config` и добавьте следующий текст в качестве последнего элемента во втором после внешнего элементе `<CodeGroup>`, который должен иметь вид `<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):`.

## Пример

```xml

 <CodeGroup>
...

<CodeGroup>
...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="This code group grants full trust to the AP4SSRS assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--End here. -->

</CodeGroup>

</CodeGroup>
```

**Шаг 5.** Убедитесь, что Aspose.PDF for Reporting Services успешно установлен. Откройте веб-портал служб Reporting Services и проверьте список доступных форматов экспорта отчета. Вы можете запустить веб-портал, запустив веб-браузер и введя URL-адрес веб-портала служб Reporting Services в адресной строке (по умолчанию это http://@@KEEP_0@@/reports/).). Выберите один из отчетов, доступных на вашем веб-портале, и откройте раскрывающийся список «Экспорт». Вы должны увидеть список форматов экспорта, включая те, которые предоставляются расширением Aspose.PDF для служб Reporting Services. Выберите PDF через элемент Aspose.PDF.

![Install to report server](install-to-report-server_1.png)

Нажмите выбранный элемент. Он сгенерирует отчет в выбранном формате, отправит его клиенту и, в зависимости от настроек вашего веб-браузера, либо покажет вам диалоговое окно «Сохранить файл», чтобы выбрать, где сохранить экспортированный отчет, либо автоматически загрузит файл в папку «Загрузки».

Поздравляем, вы успешно установили Aspose.PDF для Reporting Services и экспортировали отчет в PDF-документ!




