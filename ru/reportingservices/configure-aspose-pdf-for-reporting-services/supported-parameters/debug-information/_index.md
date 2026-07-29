---
title: Отладочная информация
linktitle: Отладочная информация
type: docs
weight: 90
url: /ru/reportingservices/debug-information/
description: Получайте доступ к отладочной информации и анализируйте её для рендеринга PDF в Aspose.PDF for Reporting Services, чтобы эффективно устранять проблемы.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Невозможно полностью исключить наличие ошибок в процессе рендеринга или в полученном результате. По определённым причинам, таким как секретность или конфиденциальность, мы не можем получить источник данных, использованный в отчёте пользователя, поэтому не способны воспроизвести ошибку в отчёте. Чтобы облегчить и упростить взаимодействие между клиентами и разработчиками, мы добавляем этот параметр. Если вы сталкиваетесь с проблемами при рендеринге вашего отчёта с помощью Aspose.PDF for Reporting Services, пожалуйста, установите этот параметр отчёта, после чего вы получите отрендеренный документ в формате XML. Затем, пожалуйста, разместите XML‑файл для нас на форуме продукта.

{{% /alert %}}

{{% alert color="primary" %}}
**Имя параметра**: SavingXmlFormat  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (default)  

**Пример**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > Истина </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
