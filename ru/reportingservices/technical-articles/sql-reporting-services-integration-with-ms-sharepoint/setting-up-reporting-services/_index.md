---
title: Настройка Reporting Services
linktitle: Настройка Reporting Services
type: docs
weight: 20
url: /ru/reportingservices/setting-up-reporting-services/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Наша первая остановка на сервере Reporting Services — Reporting Services Configuration Manager.

{{% /alert %}}

## Учётная запись службы:

**Убедитесь, что вы понимаете, какую учётную запись службы вы используете для Reporting Services. Если возникнут проблемы, они могут быть связаны с используемой вами учётной записью службы. По умолчанию используется Network Service. При развертывании новых сборок мы всегда используем доменные учётные записи, потому что именно там, скорее всего, возникнут проблемы. Для этого экземпляра сервера мы использовали доменную учётную запись под названием RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- Настройка учётной записи службы**

## URL веб‑сервиса:

{{% alert color="primary" %}}

**Нам понадобится настроить URL веб‑сервиса. Это виртуальная директория ReportServer (vdir), в которой размещаются веб‑службы, используемые Reporting Services, и с которой будет взаимодействовать SharePoint. Если только вы не хотите настроить свойства vdir (например, SSL, порты, заголовки хоста и т.д.), вы просто можете нажать Apply здесь, и всё будет готово.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Настройка URL веб‑сервиса После того как URL веб‑сервиса будет настроен, вы должны увидеть следующие результаты**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Успешная настройка URL веб‑сервиса**
{{% /alert %}}

## База данных:

**Нужно создать базу данных каталога Reporting Services. Ее можно разместить на любом движке Database Engine SQL 2008 или SQL 2008 R2. SQL11 тоже подойдет, но он все еще в BETA. Это действие по умолчанию создаст две базы данных: ReportServer и ReportServerTempDB.**

{{% alert color="primary" %}}
**Другой важный шаг — убедиться, что вы выбираете тип базы данных SharePoint Integrated. После выбора изменить его невозможно.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- Создание базы данных сервера отчетов**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- Настройка сервера базы данных и типа аутентификации**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- Настройка имени базы данных и режима**
{{% /alert %}}

**Для учетных данных именно так Report Server будет взаимодействовать с SQL Server. Любой выбранный вами аккаунт получит определённые права в базе данных Catalog, а также в нескольких системных базах данных через роль RSExecRole. MSDB — одна из этих баз данных, используемая для подписок, так как мы используем SQL Agent.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- Настройка учетных данных базы данных Report Server**

{{% alert color="primary" %}}

**Как только указаны учетные данные базы данных, мы должны получить результаты, как указано ниже.**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- Прогресс создания базы данных Report Server**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Сводка завершения базы данных Report Server**
{{% /alert %}}

## URL‑адрес Report Manager:

**Мы можем пропустить URL Report Manager, так как он не используется в режиме интеграции с SharePoint. SharePoint — наш фронтенд. Report Manager не работает.**

## Ключи шифрования:

{{% alert color="primary" %}}
**Создайте резервную копию ваших ключей шифрования и убедитесь, что знаете, где они хранятся. Если возникнет ситуация, когда вам понадобится переместить базу данных или восстановить её, эти ключи вам понадобятся.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Резервное копирование ключа шифрования сервера отчетов**
{{% /alert %}}

{{% alert color="primary" %}}
**Поздравляем! Мы успешно сконфигурировали Reporting Services с помощью Configuration Manager. Если открыть URL на вкладке Web Service URL, должно отобразиться что-то похожее на следующее.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Доступ к Report Server после установки**

**Причина ошибки: SharePoint установлен на нашем WFE, и мы завершили настройку Reporting Services. В этом примере Reporting Services и SharePoint находятся на разных машинах. Если бы они были на одной машине, вы бы не увидели эту ошибку. Технически нам нужно установить SharePoint на коробку RS. Это значит, что IIS также будет включен.**
{{% /alert %}}


