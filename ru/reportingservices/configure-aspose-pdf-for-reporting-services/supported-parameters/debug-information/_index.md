---
title: Информация об отладке
linktitle: Информация об отладке
type: docs
weight: 90
url: /reportingservices/debug-information/
description: Доступ и анализ отладочной информации для рендеринга PDF в Aspose.PDF для служб Reporting Services для эффективного устранения неполадок.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Неизбежно, что с рендерингом или с полученным результатом что-то не так. По некоторым причинам, таким как секретность или конфиденциальность, нам не удалось получить источник данных, используемый в отчете пользователя, поэтому мы не смогли воспроизвести ошибку в отчете. Чтобы сделать общение между клиентами и разработчиками проще и удобнее, мы добавляем этот параметр. Если у вас возникли проблемы при визуализации отчета с помощью Aspose.PDF для служб Reporting Services, установите этот параметр отчета, и вы получите подготовленный документ в формате XML. После этого опубликуйте XML-файл для нас на форуме продукта.

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
