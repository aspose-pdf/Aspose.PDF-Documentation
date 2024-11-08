---
title: Настройка SharePoint на сервере Reporting Services
type: docs
weight: 30
url: /ru/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Теперь нам нужно выполнить аналогичные шаги, которые мы делали для SharePoint WFE. Первое, что нужно сделать, это пройти установку предварительных требований, и как только это будет завершено, запустить установку SharePoint.

{{% /alert %}}

Для установки я выбираю Server Farm и полную установку, чтобы соответствовать моей SharePoint Box, так как я не хочу устанавливать SharePoint как автономный.

## Конфигурация SharePoint

{{% alert color="primary" %}}

**В мастере конфигурации SharePoint мы хотим подключиться к существующей ферме.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Изображение1:- Мастер конфигурации SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Затем мы укажем на базу данных SharePoint_Config, которую использует наша ферма. 
Если вы не знаете, где это находится, вы можете узнать через Центральное администрирование через Настройки системы -> Управление серверами в этой ферме.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Изображение2:- Укажите настройки конфигурации базы данных**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Изображение3:- Мастер конфигурации SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Как только мастер завершит работу, это все, что нам нужно сделать на сервере отчетов на данный момент. Вернувшись к URL ReportServer, мы увидим другую ошибку, но это потому, что мы не настроили его через Централизованное администрирование.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Изображение4:- Ошибка сервера отчетов**
{{% /alert %}}
```