---
title: Создание и экспорт шаблона
linktitle: Создание и экспорт шаблона
type: docs
weight: 10
url: /ru/sharepoint/creating-and-exporting-template/
lastmod: "2026-06-18"
description: Вы можете создавать и экспортировать шаблоны в PDF в SharePoint, используя PDF SharePoint API.
---

{{% alert color="primary" %}}

В этой статье показано, как создавать и экспортировать шаблоны, используя Aspose.PDF for SharePoint.

Начиная с Aspose.PDF for SharePoint 1.9.2, поддержка PDF-шаблонов также охватывает подсайты SharePoint.

{{% /alert %}}

## **Создание и экспорт шаблонов**
{{% alert color="primary" %}}

Чтобы использовать функцию экспорта Aspose.PDF for SharePoint, сначала создайте список, использующий “PDF Templates”.

Создание списка, использующего шаблоны PDF:

![todo:image_alt_text](creating-and-exporting-template_1.png)

Созданы два шаблона документов, Task Form Templates и Task List Templates:

![todo:image_alt_text](creating-and-exporting-template_2.png)



Форма шаблона позволяет ввести следующую информацию:

- **Name**: имя файла шаблона.
- **Title**: заголовок шаблона. (По умолчанию тот же, что и имя файла.)
- **Description**: описание шаблона. Хорошее описание упрощает использование шаблона.
- **Assigned List Types**: список идентификаторов, разделённых запятыми (относятся к шаблону. Это поле может также содержать значение **AllListTypes**. Это поле применимо только когда поле **Type** установлено в **List**).
- **Assigned Content Types**: список идентификаторов типов контента, разделённых запятыми (относятся к шаблону. Это поле может быть установлено в **AllListTypes**. Это поле применимо только когда поле **Type** установлено в **Item**).
- **Type**: либо шаблон списка, либо шаблон элемента.
- **Status**: варианты — active, inactive (невидим для всех) и debugging (видим только администраторам).

**Форма шаблонов списка задач:**

![todo:image_alt_text](creating-and-exporting-template_3.png)




**Форма шаблонов формы задачи:**

![todo:image_alt_text](creating-and-exporting-template_4.png)




Когда они будут сохранены, новые шаблоны появятся в списке шаблонов, готовые к использованию:

**Два шаблона списка задач:**

![todo:image_alt_text](creating-and-exporting-template_5.png)



**Шаблон форм задач:**

![todo:image_alt_text](creating-and-exporting-template_6.png)



#### **Разработка шаблонов**
Шаблон — это XML‑файл, основанный на Aspose XML PDF. Чтобы создать шаблон для списка, поместите специальные маркеры, связанные с внутренним именем поля целевого типа контента SharePoint, в файл XML PDF.
##### **Маркеры**
- **SPListItemsCount** – заменяется количеством элементов списка.
- **SPListTitle** – заменяется заголовком списка.
- **SPTableIterator** – помещается в первую ячейку таблицы и отмечает таблицу для полной итерации.
- **SPRowIterator** – помещается в первую ячейку таблицы и отмечает таблицу для итерации по строкам.
- **SPField** – заменяется значением поля элемента.

Для справки, пожалуйста, скачайте [XML‑файлы шаблонов](attachments/8421394/8618082.zip).
#### **Экспорт в PDF**
Когда шаблон полностью настроен, вы готовы экспортировать списки или элементы в файлы PDF.

**Экспорт списка в PDF с использованием шаблона списка задач:**

![todo:image_alt_text](creating-and-exporting-template_7.png)

{{% /alert %}}
