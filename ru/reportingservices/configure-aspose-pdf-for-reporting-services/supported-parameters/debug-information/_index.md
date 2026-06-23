---
title: Отладочная информация
linktitle: Отладочная информация
type: docs
weight: 90
url: /ru/reportingservices/debug-information/
description: Получайте доступ к отладочной информации и анализируйте её при рендеринге PDF в Aspose.PDF for Reporting Services для эффективного устранения проблем.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Нельзя избежать того, что при рендеринге или в результате рендеринга может возникнуть ошибка. По некоторым причинам, таким как секретность или конфиденциальность, мы не можем получить источник данных, использованный в отчете пользователя, поэтому не можем воспроизвести ошибку в отчете. Чтобы упростить и облегчить общение между клиентами и разработчиками, мы добавляем этот параметр. Если вы сталкиваетесь с проблемами при рендеринге вашего отчета с помощью Aspose.PDF for Reporting Services, пожалуйста, установите этот параметр отчета, после чего вы получите отрендеренный документ в формате XML. Затем, пожалуйста, разместите XML‑файл для нас на форуме продукта.

{{% /alert %}}

{{% alert color="primary" %}}
**Имя параметра**: SavingXmlFormat  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (по умолчанию)  

**Пример**
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

