---
title: Конфигурация Reporting Services и SharePoint
linktitle: Конфигурация Reporting Services и SharePoint
type: docs
weight: 40
url: /ru/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Теперь, когда SharePoint установлен и сконфигурирован на сервере RS, а RS настроен через Reporting Services Configuration Manager, мы можем перейти к настройке в Central Admin. RS 2008 R2 действительно упростил этот процесс. Раньше был трехшаговый процесс, который нужно было выполнить, чтобы всё работало. Теперь у нас только один шаг.

{{% /alert %}}

{{% alert color="primary" %}}

Мы хотим перейти на веб‑сайт Central Administrator, а затем в раздел General Application Settings. Прокручивая вниз, мы увидим Reporting Services.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- диалог конфигурации SharePoint

Выберите ссылку "Reporting Services Integration". Будет отображён следующий экран.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Укажите учетные данные интеграции Reporting Services

{{% /alert %}}

## URL веб‑сервиса:

**Мы предоставим URL для сервера отчетов, который мы нашли в Reporting Services Configuration Manager.**

## Режим аутентификации:

**Мы также выберем режим аутентификации. Следующая ссылка MSDN подробно описывает, что это такое.
Обзор безопасности для Reporting Services в режиме интеграции с SharePoint**

{{% alert color="primary" %}}

**Короче говоря, если ваш сайт использует Claims Authentication, вы всегда будете использовать Trusted Authentication независимо от того, что вы выберете здесь. Если вы хотите передать учётные данные Windows, вам следует выбрать Windows Authentication. Для Trusted Authentication мы будем передавать токен SPUser и не полагаться на учётные данные Windows. Вы также захотите использовать Trusted Authentication, если вы настроили свои сайты в Classic Mode для NTLM и RS настроен на NTLM. Для использования Windows Authentication и передачи её через ваш источник данных понадобится Kerberos.**

{{% /alert %}}

## Activate feature:

{{% alert color="primary" %}}

**Это дает вам возможность активировать Reporting Services во всех коллекциях сайтов, или вы можете выбрать, в каких именно вы хотите её активировать. По сути это означает, какие сайты смогут использовать Reporting Services. Когда это будет сделано, вы должны увидеть следующие результаты**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3:**- Успешная интеграция Reporting Services со средой SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Вернувшись к URL ReportServer, мы должны увидеть нечто похожее на следующее

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4:**- Reporting Services успешно подключён к среде SharePoint

**NOTE:** ***Если ваш сайт SharePoint настроен на SSL, он не будет отображаться в этом списке. Это известная проблема и не означает, что есть проблема. Ваши отчёты всё равно должны работать.***
{{% /alert %}}

{{% alert color="primary" %}}

Now that we have successfully integrated both products, we are ready to use Reporting Services in SharePoint 2010. As the previous version we have a feature (activated when we configure Reporting Services Integration) in the “Site Collection Feature”. Also the installation added 3 content types to add to our site. In Image 7 we can see 2 of them content types added in a document library to create a custom report us ing the, as we can see in Image5 below.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- Report Builder

The “Reporter Builder” is an ActiveX control so we need to download it over the server, as we can see in Image 6 below.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- Загрузите и установите Report Builder
{{% /alert %}}

{{% alert color="primary" %}}

После завершения процесса загрузки загрузите элемент управления «Report Builder». Теперь мы готовы разработать наш первый отчёт, как показано ниже на Image7.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – Мастер создания нового отчёта
{{% /alert %}}

{{% alert color="primary" %}}

После создания нашего отчёта мы можем сохранить его в библиотеке документов, созданной для размещения отчётов в нашем SharePoint 2010. Другой тип содержимого должен быть использован для создания общих соединений в качестве источника данных и их сохранения в библиотеке документов в SharePoint. Мы можем создать библиотеку документов, добавить этот тип содержимого, и затем наши соединения будут доступны для изменения источника данных отчётов.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Успешная интеграция Aspose.PDF for Reporting Services с MS SharePoint
{{% /alert %}}


