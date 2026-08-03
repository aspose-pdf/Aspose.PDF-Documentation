---
title: Настройка безопасности
linktitle: Настройка безопасности
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Безопасность всегда была самым важным вопросом в каждой области, будь то защита сети или PDF-документа. Документы защищены по многим возможным причинам: автор документа может захотеть сохранить содержимое документа в безопасности и не хочет, чтобы другие могли его изменить и т. д.

Aspose.PDF for Reporting Services уделил большое внимание таким аспектам безопасности, предоставив разработчикам эти функции, которые могут быть полезны для защиты их PDF-документов. Поэтому он содержит ряд параметров, которые позволяют разработчикам применять к PDF-документам различные меры безопасности.

Одной из таких мер является защита PDF-документа паролем во время шифрования. Вы также можете ограничить или разрешить изменение содержимого, копирование содержимого, печать документа или разрешить/запретить заполнение форм. Эти функции в настоящее время не поддерживаются стандартным PDF-экспортером SQL Reporting Services, но вы можете реализовать эти функции с помощью Aspose.PDF для Reporting Services. Просто добавьте соответствующие параметры безопасности в отчет или файл конфигурации сервера отчетов, и вы сможете создавать защищенные PDF-документы с ограниченными правами.

В настоящее время средство визуализации Aspose.PDF для служб Reporting Services поддерживает следующие атрибуты безопасности:

{{% /alert %}}

```text
Parameter Name: User Password  
Date Type: String  
Values supported: Any plain text
```

```text
Parameter Name: Master Password  
Date Type: String  
Values supported: Any plain text 
```

```text
Parameter Name: IsCopyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsPrintingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

```text
Parameter Name: IsContentsModifyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsFormFillingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

## Пример

```xml
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
```

