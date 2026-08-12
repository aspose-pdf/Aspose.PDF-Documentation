---
title: Creating and Exporting Template
linktitle: Создание и экспорт шаблона
type: docs
weight: 10
url: /ru/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: Вы можете создавать и экспортировать шаблоны в PDF в SharePoint с помощью PDF SharePoint API.
---

{{% alert color="primary" %}}

В этой статье показано, как создавать и экспортировать шаблоны с помощью Aspose.PDF для SharePoint.

From Aspose.PDF for SharePoint 1.9.2, PDF template support also covers SharePoint subsites.

{{% /alert %}}

## Создание и экспорт шаблонов

{{% alert color="primary" %}}

To use the Aspose.PDF for SharePoint export feature, first create a list that uses “PDF Templates”.

Создание списка, использующего шаблоны PDF:

![Create PDF Template List](creating-and-exporting-template_1.png)

Создаются два шаблона документов: шаблоны форм задач и шаблоны списков задач:

![Document Templates](creating-and-exporting-template_2.png)

The template form lets you enter the following information:

- **Name**: the template's file name.
- **Название**: название шаблона. (По умолчанию совпадает с именем файла.)
- **Description**: a description of the template. A good description makes the template easier to use.
- **Назначенные типы списков**: идентификаторы списков, разделенные запятыми (относящиеся к шаблону). Это поле также может содержать значение
- **ВсеТипыСписков**. Это поле применимо только в том случае, если для поля **Тип** установлено значение **Список**).
- **Назначенные типы контента**: идентификаторы типов контента, разделенные запятыми, связанные с шаблоном. Это поле может содержать значение **AllListTypes**. Это поле применимо только в том случае, если в поле **Тип** установлено значение **Товар**.
- **Тип**: либо шаблон списка, либо шаблон элемента.
- **Status**: the options are active, inactive (invisible to all), and debugging (visible only to admins).

Форма «Шаблоны списка задач»:

![Task List Templates](creating-and-exporting-template_3.png)

The Task Form Templates form:

![Task Form Templates](creating-and-exporting-template_4.png)

После сохранения новые шаблоны появятся в списке шаблонов и будут готовы к использованию:

Два шаблона списка задач:*

![Task List Templates](creating-and-exporting-template_5.png)

A task forms template:

![Task Form Templates](creating-and-exporting-template_6.png)

### Разрабатывайте шаблоны

A template is an XML file based on Aspose XML PDF. To make a template for a list, place special markers related to the SharePoint target content type field's internal name into the XML PDF file.

### Маркеры

- **SPListItemsCount** – заменено количеством элементов списка.
- **SPListTitle** – заменяется заголовком списка.
- **SPTableIterator** — помещается в первую ячейку таблицы и помечает таблицу для полной итерации.
- **SPRowIterator** – placed to first table cell and mark table for row iteration.
- **SPField** – заменяется значением поля элемента.

Для справки загрузите [файлы шаблонов XML](attachments/8421394/8618082.zip).

### Экспорт в PDF

When a template is completely configured, you are ready to export lists or items to PDF files.

Exporting a list to PDF using a task list template:

![Export to PDF](creating-and-exporting-template_7.png)

{{% /alert %}}

