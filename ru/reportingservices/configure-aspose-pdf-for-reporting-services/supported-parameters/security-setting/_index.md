---
title: Настройка безопасности
linktitle: Настройка безопасности
type: docs
weight: 30
url: /ru/reportingservices/security-setting/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Безопасность всегда была самой важной проблемой во всех областях, будь то защита сети или PDF‑документа. Документы защищают по многим возможным причинам: автор документа может захотеть сохранить его содержание в безопасности и не желать, чтобы другие могли изменить его и т.д.

Aspose.PDF for Reporting Services уделяет большое внимание таким вопросам безопасности, предоставляя разработчикам функции, которые могут быть полезны для защиты их PDF‑документов. Поэтому он содержит ряд параметров, позволяющих разработчикам применять различные меры безопасности к PDF‑документам.

Одной из таких мер является защита PDF‑документа паролем во время шифрования. Вы также можете ограничить или разрешить изменение содержания, копирование содержимого, печать документа или разрешить/запретить заполнение форм. В данный момент эти функции не поддерживаются экспортером PDF по умолчанию в SQL Reporting Services, но их можно реализовать с помощью Aspose.PDF for Reporting Services. Просто добавьте соответствующие параметры безопасности в отчёт или в файл конфигурации сервера отчетов, и вы сможете создавать защищённые PDF‑документы с ограниченными привилегиями.

В настоящее время рендерер Aspose.PDF for Reporting Services поддерживает следующие атрибуты безопасности:

{{% /alert %}}

{{% alert color="primary" %}}

**Имя параметра**: Пароль пользователя  
**Тип данных**: String  
**Поддерживаемые значения**: Any plain text

**Имя параметра**: Главный пароль  
**Тип данных**: String  
**Поддерживаемые значения**: Any plain text 

**Имя параметра**: IsCopyingAllowed  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (default)  

**Имя параметра**: IsPrintingAllowed  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (default)  

**Имя параметра**: IsContentsModifyingAllowed  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (default)  

**Имя параметра**: IsFormFillingAllowed  
**Тип данных**: Boolean  
**Поддерживаемые значения**: True, False (default)  

**Пример**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>Ложь</IsCopyingAllowed>
    <IsPrintingAllowed>Ложь</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
