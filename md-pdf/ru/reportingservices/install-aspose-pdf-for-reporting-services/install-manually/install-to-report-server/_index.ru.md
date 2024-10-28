---
title: Установка на сервер отчетов
type: docs
weight: 10
url: /reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Вам нужно выполнить эти шаги только в том случае, если вы устанавливаете Aspose.PDF для Reporting Services вручную, а не с помощью MSI установщика. MSI установщик выполняет все необходимые действия по установке и регистрации автоматически.

{{% /alert %}}

В следующих шагах вам потребуется копировать и изменять файлы в каталоге, где установлены службы отчетов Microsoft SQL Server. Сборка SSRS 2016 находится в каталоге \Bin\SSRS2016 zip-пакета; сборка SSRS 2017 находится в каталоге \Bin\SSRS2017; сборка SSRS 2019 находится в каталоге \Bin\SSRS2019; сборка SSRS 2022 находится в каталоге \Bin\SSRS2022; сборка Power BI Report Server находится в каталоге \Bin\PowerBI.

{{% alert color="primary" %}}

**Шаг 1.** Найдите каталог установки сервера отчетов. The root directory for Microsoft SQL Server is usually C:\Program Files\Microsoft SQL Server. Further process is slightly different for Reporting Services 2016, Reporting Services 2017 and later, and Power BI Report Server:

- Report Server 2016 по умолчанию устанавливается в каталог C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Если вы используете настраиваемые именованные экземпляры вместо стандартного, то путь по умолчанию будет C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- Report Server 2017 и позже по умолчанию устанавливается в каталог C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Power BI Report Server по умолчанию устанавливается в каталог C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

В следующем тексте каталог установки Reporting Services (один из вышеупомянутых путей) будет обозначаться как ```<Instance>```.
{{% /alert %}}


{{% alert color="primary" %}}**Шаг 2.** Скопируйте Aspose.Pdf.ReportingServices.dll для соответствующей версии SSRS в папку ```<Instance>```\bin.
{{% /alert %}}

{{% alert color="primary" %}}
**Шаг 3.** Зарегистрируйте Aspose.Pdf для Reporting Services как расширение рендеринга. Откройте файл ```<Instance>```\rsreportserver.config и добавьте следующие строки в элемент ```<Render>```:
{{% /alert %}}

**Пример**

{{< highlight csharp >}}

<Render>
...
<!--Начните здесь.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**Шаг 4.** Предоставьте Aspose.Pdf для Reporting Services разрешения на выполнение. Откройте файл ```<Instance>```\rssrvpolicy.config и добавьте следующий текст в качестве последнего элемента во второй до внешней элемент ```<CodeGroup>``` (который должен быть ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```

{{% /alert %}}

**Example**

{{< highlight csharp >}}

<CodeGroup>
...

<CodeGroup>
...

<!--Начните здесь.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="Эта группа кода предоставляет полный доступ к сборке AP4SSRS.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--Закончите здесь.-->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

{{% alert color="primary" %}}
**Шаг 5.** Убедитесь, что Aspose.Pdf for Reporting Services был успешно установлен. Откройте веб-портал Reporting Services и проверьте список доступных форматов экспорта для отчета. Вы можете запустить веб-портал, открыв веб-браузер и введя URL веб-портала Reporting Services в адресной строке (по умолчанию это http://```<Reporting_Services_server_name>```/reports/). Выберите один из доступных отчетов на вашем веб-портале и откройте выпадающий список Экспорт. Вы должны увидеть список форматов экспорта, включая те, которые предоставлены расширением Aspose.Pdf for Reporting Services. Выберите пункт PDF через Aspose.PDF.

![todo:image_alt_text](install-to-report-server_1.png)

Нажмите на выбранный пункт. Это сгенерирует отчет в выбранном формате, отправит его клиенту и, в зависимости от настроек вашего веб-браузера, либо покажет вам диалоговое окно Сохранить файл, чтобы выбрать, куда сохранить экспортированный отчет, либо автоматически загрузит файл в вашу папку Загрузки.

{{% alert color="primary" %}}

Поздравляем, вы успешно установили Aspose.Pdf for Reporting Services и экспортировали отчет в формате PDF!Извините, но не предоставлен текст для перевода. Пожалуйста, предоставьте текст документа, который вы хотите перевести на русский язык.