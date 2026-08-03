---
title: Размер страницы
linktitle: Размер страницы
type: docs
weight: 60
url: /reportingservices/pagesize/
description: Настройте размеры страниц для отчетов в формате PDF в Aspose.PDF for Reporting Services в соответствии с конкретными требованиями к документу.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Конструктор отчетов служб Reporting Services не поддерживает распространенные размеры страниц, такие как A4, B5, Letter и т. д. С помощью Aspose.PDF for Reporting Services вы можете получить его, как показано в следующем примере.

{{% /alert %}}

```text
Parameter Name: PageSize  
Date Type: String  
Values supported: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  
```

## Пример

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>
```
