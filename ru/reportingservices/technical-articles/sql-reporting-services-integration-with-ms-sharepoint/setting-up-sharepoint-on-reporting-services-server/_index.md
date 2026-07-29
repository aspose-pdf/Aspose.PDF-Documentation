---
title: Настройка SharePoint на сервере Reporting Services
linktitle: Настройка SharePoint на сервере Reporting Services
type: docs
weight: 30
url: /ru/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Теперь нам нужно выполнить аналогичные шаги, как мы делали для SharePoint WFE. Первое — пройти установку Prereq uisites, и после её завершения запустить настройку SharePoint.

{{% /alert %}}

Для установки я выбираю Server Farm и полную установку, соответствующую моему SharePoint Box, так как я не хочу отдельную установку для SharePoint.

## Конфигурация SharePoint

{{% alert color="primary" %}}

**В мастере конфигурации SharePoint мы хотим подключиться к существующей ферме.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- Мастер настройки SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Затем мы укажем её на базу данных SharePoint_Config, которую использует наша ферма. Если вы не знаете, где она находится, вы можете узнать об этом через Централизованное администрирование в разделе Системные настройки -> Управление серверами в этой ферме.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- Укажите настройки конфигурации базы данных**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- Мастер настройки SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Как только мастер завершит работу, это всё, что нам сейчас нужно сделать на коробке Report Server. Возвращаясь к URL ReportServer, мы увидим другую ошибку, но это потому, что мы не настроили её через Central Administrator.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- Ошибка сервера отчётов**
{{% /alert %}}
