---
title: Debug Information
type: docs
weight: 90
url: /reportingservices/debug-information/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Невозможно избежать проблем с отображением или результатом отображения. По некоторым причинам, таким как секретность или конфиденциальность, мы не можем получить источник данных, используемый в отчете пользователя, поэтому не можем воспроизвести ошибку в отчете. Чтобы сделать общение между клиентами и разработчиками проще и более гладким, мы добавили этот параметр. Если вы сталкиваетесь с проблемами при отображении вашего отчета с помощью Aspose.PDF для Reporting Services, пожалуйста, установите этот параметр отчета, затем вы получите отображенный документ в формате XML. После этого, пожалуйста, разместите файл XML для нас на форуме продукта.

{{% /alert %}}

{{% alert color="primary" %}}
**Parameter Name**: SavingXmlFormat  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Example**
{{< highlight csharp >}}

<Render>
...

<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">

<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```