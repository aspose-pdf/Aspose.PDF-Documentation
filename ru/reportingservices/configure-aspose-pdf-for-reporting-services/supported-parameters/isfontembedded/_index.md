---
title: IsFontEmbedded
type: docs
weight: 50
url: /ru/reportingservices/isfontembedded/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Дизайнер RS не поддерживает встроенный шрифт для текста; с помощью Aspose.PDF для Reporting Services вы можете легко встроить информацию о шрифте в ваш PDF-документ.

{{% /alert %}}

{{% alert color="primary" %}}
**Имя параметра**: IsFontEmbedded  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (по умолчанию)  

**Пример**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsFontEmbedded>True</IsFontEmbedded>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}