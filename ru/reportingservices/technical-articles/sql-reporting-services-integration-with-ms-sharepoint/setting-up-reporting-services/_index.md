---
title: Настройка Reporting Services
linktitle: Настройка Reporting Services
type: docs
weight: 20
url: /ru/reportingservices/setting-up-reporting-services/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Нашей первой остановкой на сервере Reporting Services является Reporting Services Configuration Manager.

{{% /alert %}}

## Служебная учетная запись:

**Убедитесь, что вы понимаете, какую служебную учетную запись используете для Reporting Services. Если возникнут проблемы, они могут быть связаны с используемой служебной учетной записью. По умолчанию используется Network Service. При развертывании новых сборок мы всегда используем доменные учетные записи, поскольку именно в этом случае мы, скорее всего, столкнёмся с проблемами. Для данного экземпляра сервера мы использовали доменную учетную запись под названием RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- Настройка служебной учетной записи**

## URL веб‑сервиса:

{{% alert color="primary" %}}

**Нам нужно будет настроить URL веб‑сервиса. Это виртуальный каталог (vdir) ReportServer, в котором размещаются веб‑сервисы, используемые Reporting Services, и с которым будет взаимодействовать SharePoint. Если вы не хотите настраивать свойства vdir (т. е. SSL, порты, заголовки хоста и т. д.), вы просто можете нажать «Применить» здесь, и всё будет готово.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Настройка URL веб‑сервиса После настройки URL веб‑сервиса вы должны увидеть следующие результаты**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Успешная настройка URL веб‑сервиса**
{{% /alert %}}

## База данных:

**Нам необходимо создать базу данных каталога Reporting Services. Она может быть размещена на любом SQL 2008 или SQL 2008 R2 Database Engine. SQL11 также подойдет, но всё ещё находится в BETA. Это действие создаст по умолчанию две базы данных, ReportServer и ReportServerTempDB.**

{{% alert color="primary" %}}
**Другой важный шаг — убедиться, что вы выбираете тип базы данных SharePoint Integrated. После того как этот выбор сделан, его нельзя изменить.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- Создание базы данных сервера отчетов**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- Настройка сервера баз данных и типа аутентификации**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- Настройка имени базы данных и режима**
{{% /alert %}}

**Для учетных данных это то, как Report Server будет взаимодействовать с SQL Server. Любая выбранная вами учетная запись получит определенные права в базе данных Catalog, а также в нескольких системных базах данных через роль RSExecRole. MSDB — одна из этих баз данных для использования подписок, поскольку мы используем SQL Agent.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- Настройка учетных данных базы данных Report Server**

{{% alert color="primary" %}}

**Как только учетные данные базы данных указаны, мы должны получить результаты, как указано ниже.**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- Прогресс создания базы данных Report Server**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Сводка завершения базы данных Report Server**
{{% /alert %}}

## URL-адрес Report Manager:

**Мы можем пропустить URL Report Manager, поскольку он не используется в режиме интеграции с SharePoint. SharePoint — наш фронтенд. Report Manager не работает.**

## Ключи шифрования:

{{% alert color="primary" %}}
**Сделайте резервную копию ваших ключей шифрования и убедитесь, что знаете, где их храните. Если возникнет ситуация, когда вам понадобится мигрировать базу данных или восстановить её, эти ключи понадобятся.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Резервное копирование ключа шифрования сервера отчетов**
{{% /alert %}}

{{% alert color="primary" %}}
**Поздравляем! Мы успешно настроили Reporting Services с помощью Configuration Manager. Если перейти по URL на вкладке Web Service URL, должно отображаться что-то похожее на следующее.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Доступ к Report Server после установки**

**Причина ошибки: SharePoint установлен на нашем WFE, и мы завершили настройку Reporting Services. В этом примере Reporting Services и SharePoint находятся на разных машинах. Если бы они были на одной машине, вы бы не увидели эту ошибку. Технически нам нужно установить SharePoint на RS Box. Это означает, что IIS также будет включён.**
{{% /alert %}}

