---
title: Конфигурация Reporting Services и SharePoint
linktitle: Конфигурация Reporting Services и SharePoint
type: docs
weight: 40
url: /ru/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Теперь, когда SharePoint установлен и настроен на сервере RS, а RS настроен через Reporting Services Configuration Manager, мы можем перейти к конфигурации в Central Admin. RS 2008 R2 действительно упростил этот процесс. Раньше был процесс из 3 шагов, которые нужно было выполнить, чтобы это работало. Сейчас нужен только один шаг.

{{% /alert %}}

{{% alert color="primary" %}}

Мы хотим перейти на веб‑сайт Central Administrator, а затем в General Application Settings. В нижней части мы увидим Reporting Services.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- диалог конфигурации SharePoint

Выберите ссылку "Reporting Services Integration". Появится следующий экран.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Укажите учетные данные интеграции Reporting Services

{{% /alert %}}

## URL веб‑сервиса:

**Мы предоставим URL сервера отчетов, который мы нашли в Reporting Services Configuration Manager.**

## Режим аутентификации:

**Мы также выберем режим аутентификации. Следующая ссылка MSDN подробно описывает, что это такое.
Обзор безопасности Reporting Services в интегрированном режиме SharePoint**

{{% alert color="primary" %}}

**Короче говоря, если ваш сайт использует аутентификацию Claims, вы всегда будете использовать Trusted Authentication, независимо от того, что выберете здесь. Если вы хотите передать учетные данные Windows, следует выбрать Windows Authentication. При Trusted Authentication мы передаем токен SPUser и не полагаемся на учетные данные Windows. Также следует использовать Trusted Authentication, если вы настроили сайты в Classic Mode для NTLM, а RS настроен на NTLM. Для использования Windows Authentication и передачи её через источник данных потребуется Kerberos.**

{{% /alert %}}

## Activate feature:

{{% alert color="primary" %}}

**Это дает вам возможность активировать Reporting Services во всех коллекциях сайтов, или вы можете выбрать, какие из них хотите активировать. Это по сути означает, какие сайты смогут использовать Reporting Services. Когда это будет сделано, вы должны увидеть следующие результаты**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3:**- Успешная интеграция Reporting Services с средой SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Возвращаясь к URL ReportServer, мы должны увидеть что-то похожее на следующее

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4:**- Reporting Services успешно подключен к среде SharePoint

**NOTE:** ***Если ваш сайт SharePoint настроен на SSL, он не будет отображаться в этом списке. Это известная проблема и не означает, что есть ошибка. Ваши отчеты всё равно должны работать.***
{{% /alert %}}

{{% alert color="primary" %}}

Теперь, когда мы успешно интегрировали оба продукта, мы готовы использовать Reporting Services в SharePoint 2010. Как и в предыдущей версии, у нас есть функция (активируется при настройке интеграции Reporting Services) в «Site Collection Feature». Также установка добавила 3 типа контента в наш сайт. На изображении 7 мы видим, что 2 из этих типов контента добавлены в библиотеку документов для создания пользовательского отчёта, как показано на изображении 5 ниже.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- Report Builder

“Reporter Builder” — это ActiveX‑контроль, поэтому его необходимо загрузить на сервер, как показано на изображении 6 ниже.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- Скачать и установить Report Builder
{{% /alert %}}

{{% alert color="primary" %}}

После завершения процесса загрузки загрузите элемент управления “Report Builder”. Теперь мы готовы разработать наш первый отчёт, как показано ниже на изображении Image7.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – Мастер создания нового отчёта
{{% /alert %}}

{{% alert color="primary" %}}

После создания нашего отчёта мы можем сохранить его в библиотеку документов, созданную для размещения отчётов в нашем SharePoint 2010. Для создания общего подключения в качестве источника данных необходимо использовать другой тип содержимого и сохранить его в библиотеку документов в SharePoint. Мы можем создать библиотеку документов, добавить в неё этот тип содержимого, и после этого наши подключения будут доступны для изменения источника данных отчётов.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Успешная интеграция Aspose.PDF for Reporting Services с MS SharePoint
{{% /alert %}}

