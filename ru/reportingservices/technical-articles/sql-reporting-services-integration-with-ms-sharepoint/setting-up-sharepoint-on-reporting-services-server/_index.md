---
title: Настройка SharePoint на сервере служб отчетов
linktitle: Настройка SharePoint на сервере служб отчетов
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Теперь нам нужно выполнить те же действия, что и для SharePoint WFE. Прежде всего необходимо выполнить установку Prerequisites и, как только это будет сделано, запустить установку SharePoint.

{{% /alert %}}

Для установки я выбираю ферму серверов и полную установку, соответствующую моему блоку SharePoint, поскольку мне не нужна отдельная установка SharePoint.

## Конфигурация SharePoint

{{% alert color="primary" %}}

**В мастере настройки SharePoint мы хотим подключиться к существующей ферме.**

![SharePoint Configuration Wizard](setting-up-sharepoint-on-reporting-services-server_1.png)

**Изображение1: — Мастер настройки SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Затем мы укажем его на базу данных SharePoint_Config, которую использует наша ферма. Если вы не знаете, где это находится, вы можете узнать это в Центре администрирования через Настройки системы -> Серверы диспетчера в этой ферме.**

![SharePoint Configuration Database](setting-up-sharepoint-on-reporting-services-server_2.png)

**Изображение2: – укажите параметры конфигурации базы данных**

![SharePoint Configuration Wizard](setting-up-sharepoint-on-reporting-services-server_3.png)

**Изображение3: — Мастер настройки SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**После завершения работы мастера это все, что нам нужно сделать в окне сервера отчетов. Возвращаясь к URL-адресу ReportServer, мы увидим еще одну ошибку, но это потому, что мы не настроили ее через Центральный администратор.**

![SharePoint Configuration Error](setting-up-sharepoint-on-reporting-services-server_4.png)

**Изображение4: – Ошибка сервера отчетов**
{{% /alert %}}
