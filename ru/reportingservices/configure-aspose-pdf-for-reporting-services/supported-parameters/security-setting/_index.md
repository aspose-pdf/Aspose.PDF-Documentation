---
title: Security Setting
type: docs
weight: 30
url: ru/reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Безопасность всегда была самой важной проблемой в каждой области, будь то защита сети или PDF-документа. Документы делают безопасными по многим возможным причинам: автор документа может захотеть сохранить его содержание в безопасности и не хочет позволять другим изменять его и т.д.

Aspose.Pdf for Reporting Services уделяет большое внимание таким аспектам безопасности, предоставляя разработчикам функции, которые могут быть полезны для защиты их PDF-документов. Поэтому он содержит ряд параметров, которые позволяют разработчикам применять различные меры безопасности к PDF-документам.

Одной из этих мер является защита PDF-документа паролем во время шифрования. You can also restrict or allow contents modification, copying the content, document printing or allow/disable form filling. These features are at this time not supported by the default SQL Reporting Services PDF Exporter but you can implement these features using Aspose.Pdf for Reporting Services. Just add corresponding security parameters to a report or a report server configuration file, and you will be able to create secure PDF documents with limited privileges.

Currently, Aspose.Pdf for Reporting Services renderer supports following security attributes:

{{% /alert %}}

{{% alert color="primary" %}}

**Parameter Name**: User Password  
**Date Type**: String  
**Values supported**: Any plain text

**Parameter Name**: Master Password  
**Date Type**: String  
**Values supported**: Any plain text 

**Parameter Name**: IsCopyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Parameter Name**: IsPrintingAllowed  
**Date Type**: Boolean  

**Values supported**: True, False (default)  
**Имя параметра**: IsContentsModifyingAllowed  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (по умолчанию)  

**Имя параметра**: IsFormFillingAllowed  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (по умолчанию)  

**Пример**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}