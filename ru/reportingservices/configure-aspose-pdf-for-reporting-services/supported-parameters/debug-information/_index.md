---
title: Отладочная информация
linktitle: Отладочная информация
type: docs
weight: 90
url: /ru/reportingservices/debug-information/
description: Получайте доступ к отладочной информации и анализируйте её для рендеринга PDF в Aspose.PDF for Reporting Services, чтобы эффективно устранять проблемы.
lastmod: "2026-08-20"
---

{{% alert color="primary" %}}

Неправильно отрендеренный документ или результат рендеринга неизбежно могут возникнуть. По некоторым причинам, таким как секретность или конфиденциальность, мы не можем получить источник данных, используемый в отчете пользователя, и поэтому не можем воспроизвести ошибку в отчете. Чтобы упростить и облегчить коммуникацию между клиентами и разработчиками, мы добавили этот параметр. Если у вас возникают проблемы при рендеринге отчёта с помощью Aspose.PDF for Reporting Services, пожалуйста, установите этот параметр отчёта, после чего вы получите отрендеренный документ в формате XML. Затем, пожалуйста, разместите XML‑файл у нас на форуме продукта.

{{% /alert %}}

{{% alert color="primary" %}}

```txt
Parameter Name: SavingXmlFormat
Date Type: Boolean  
Values supported**: True, False (default)
```

## Пример

```xml
<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>
```

{{% /alert %}}

