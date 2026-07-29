---
title: IsFontEmbedded
linktitle: IsFontEmbedded
type: docs
weight: 50
url: /ru/reportingservices/isfontembedded/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

RS designer не поддерживает встроенный шрифт для текста; с помощью Aspose.PDF for Reporting Services вы легко сможете внедрить информацию о шрифте в ваш PDF‑документ.

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
    <IsFontEmbedded>Истина</IsFontEmbedded>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
