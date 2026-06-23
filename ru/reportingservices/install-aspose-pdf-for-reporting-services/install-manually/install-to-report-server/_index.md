---
title: Установить на сервер отчетов
linktitle: Установить на сервер отчетов
type: docs
weight: 10
url: /ru/reportingservices/install-to-report-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Вам нужно следовать этим шагам только в том случае, если вы устанавливаете Aspose.PDF for Reporting Services вручную, а не с помощью MSI‑установщика. MSI‑установщик выполняет все необходимые действия по установке и регистрации автоматически.

{{% /alert %}}

В последующих шагах вам потребуется копировать и изменять файлы в каталоге, где установлены Microsoft SQL Server Reporting Services. Сборка SSRS 2016 находится в каталоге \\Bin\\SSRS2016 zip‑пакета; сборка SSRS 2017 находится в каталоге \\Bin\\SSRS2017; сборка SSRS 2019 находится в каталоге \\Bin\\SSRS2019; сборка SSRS 2022 находится в каталоге \\Bin\\SSRS2022; сборка Power BI Report Server находится в каталоге \\Bin\\PowerBI. 

{{% alert color="primary" %}}

**Step 1.** Найдите каталог установки Report Server. Корневой каталог Microsoft SQL Server обычно находится по пути C:\Program Files\Microsoft SQL Server. Дальнейший процесс немного отличается для Reporting Services 2016, Reporting Services 2017 и более новых версий, а также Power BI Report Server:

- Report Server 2016 по умолчанию устанавливается в каталог C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Если вы используете пользовательские именованные экземпляры вместо стандартного, путь по умолчанию будет C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- Report Server 2017 и более новые версии по умолчанию устанавливаются в каталог C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Power BI Report Server по умолчанию устанавливается в каталог C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

В дальнейшем тексте каталог установки Reporting Services (один из вышеупомянутых путей) будет обозначен как ```<Instance>```.
{{% /alert %}}

{{% alert color="primary" %}}
**Шаг 2.** Скопируйте Aspose.Pdf.ReportingServices.dll для соответствующей версии SSRS в ```<Instance>```\bin папка.
{{% /alert %}}

{{% alert color="primary" %}}
**Шаг 3.** Зарегистрируйте Aspose.Pdf for Reporting Services как расширение рендеринга. Откройте ```<Instance>```файл \rsreportserver.config и добавить следующие строки в ```<Render>``` элемент:
{{% /alert %}}

**Пример**

{{< highlight csharp >}}

 <Render>
...
<!--Start here.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**Шаг 4.** Предоставьте Aspose.Pdf for Reporting Services с разрешениями на выполнение. Откройте ```<Instance>```\rssrvpolicy.config файл и добавить следующий текст в качестве последнего элемента во втором от внешнего ```<CodeGroup>``` элемент (который должен быть ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```
{{% /alert %}}

**Example**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% alert color="primary" %}}
**Шаг 5.** Убедитесь, что Aspose.Pdf for Reporting Services был успешно установлен. Откройте веб‑портал Reporting Services и проверьте список доступных форматов экспорта для отчёта. Вы можете запустить веб‑портал, запустив веб‑браузер и введя URL веб‑портала Reporting Services в адресную строку (по умолчанию это http://```<Reporting_Services_server_name>```/reports/). Выберите один из отчетов, доступных в вашем веб‑портале, и откройте выпадающий список Export. Вы должны увидеть список форматов экспорта, включая те, которые предоставляет расширение Aspose.PDF for Reporting Services. Выберите пункт PDF via Aspose.PDF.

 
{{% /alert %}}

![todo:image_alt_text](install-to-report-server_1.png)

Щелкните выбранный элемент. Он сгенерирует отчёт в выбранном формате, отправит его клиенту и, в зависимости от настроек вашего веб‑браузера, либо покажет диалоговое окно «Сохранить файл», чтобы выбрать место сохранения экспортированного отчёта, либо автоматически загрузит файл в вашу папку «Загрузки».

{{% alert color="primary" %}}
Поздравляем, вы успешно установили Aspose.Pdf for Reporting Services и экспортировали отчёт в виде PDF‑документа!
{{% /alert %}}






