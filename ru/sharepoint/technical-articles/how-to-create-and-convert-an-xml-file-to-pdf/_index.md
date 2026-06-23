---
title: Как создать и преобразовать XML‑файл в PDF
linktitle: Как создать и преобразовать XML‑файл в PDF
type: docs
weight: 30
url: /ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2026-06-18"
description: API PDF SharePoint способен создавать и конвертировать XML‑файлы в формат PDF.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint построен на основе нашего отмеченного наградами компонента Aspose.PDF for .NET. Aspose.PDF for .NET предоставляет замечательные возможности — от создания PDF‑документа с нуля до манипуляций с существующими PDF‑файлами. Среди этих возможностей конвертация XML в PDF является одной из отличных функций, поддерживаемых этим продуктом. Поэтому мы считаем, что Aspose.PDF for SharePoint также будет способен конвертировать XML‑файлы в формат PDF.

{{% /alert %}}

## **Создание XML‑файла и преобразование его в PDF**

{{% alert color="primary" %}}

Шаг за шагом эта статья проведёт вас через процесс создания XML‑файла и его преобразования в PDF:

1. [Создать XML‑файл](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Создать шаблон PDF](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Загрузить XML‑шаблон](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Указать путь к исходному пути](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Указать свойства файла](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Экспортировать файл в PDF](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Сохранить PDF‑файл](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).
#### **Шаг 1: Создать XML-файл**
Сначала создайте XML-файл на основе модели объектного документа Aspose.PDF for .NET.

Согласно DOM Aspose.PDF for .NET, PDF-документ содержит коллекцию объектов Section, а Section содержит один или несколько элементов Paragraph. Текст является объектом уровня Paragraph и может содержать один или несколько сегментов. Ниже пример строки текста добавляется в объект Segment и затем в объект Text. В конце элемент Text добавляется в коллекцию параграфов объекта Section.

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hello World</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **Шаг 2: Создать PDF‑шаблон**
Прежде чем продолжить, убедитесь, что сервер SharePoint Foundation 2010 правильно установлен и настроен на системе, где будет происходить преобразование.

1. Войдите в сайт SharePoint.
1. Выберите **Site Action** и **All Items**.
1. Выберите параметр **Create** и выберите **PDF Template** из списка.
1. Введите имя шаблона.
1. Нажмите **Create**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **Шаг 3: Загрузить XML шаблон**
После создания шаблона загрузите [XML файл](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):

1. На странице шаблона PDF выберите **Add new item**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **Шаг 4: Укажите путь к исходному файлу**
В диалоговом окне загрузки документа:

1. Нажмите **Browse** и найдите файл XML на своей системе. Вы можете включить флажок, позволяющий перезаписать существующий файл.
1. Нажмите кнопку **OK**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **Шаг 5: Укажите свойства файла**
Когда файл загружен, добавьте информацию в обязательные поля (отмеченные красной звездочкой: *).

Для этого примера было добавлено образцовое описание, и были заполнены следующие поля:

1. Краткое описание документа.
1. Введите **AllListTypes** для поля **Assigned List Types**.
1. Выберите **List** в меню **Type**.
   Убедитесь, что статус остаётся **Active**.
1. Нажмите **Save**, чтобы сохранить свойства.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **Шаг 6: Export to PDF**
Когда XML‑файл добавлен в шаблон PDF:
Либо:

1. Щелкните правой кнопкой мыши файл test.xml.
1. Выберите **Export to PDF** в меню.

Или:

1. Выберите **Aspose Tools** из **Library Tools**.
1. Нажмите **Export**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **Шаг 7: Сохранить PDF‑документ**
1. В диалоговом окне Export to PDF выберите **Template storage** (место, где хранится исходный файл).
1. Выберите файл для экспорта в меню **Template name**.
1. Нажмите **Export to PDF**, чтобы сохранить окончательный PDF документ.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **Откройте PDF**
PDF‑документ был сохранён и может быть открыт. На изображении ниже обратите внимание на фразу “Hello World”, которая была в теге {segment] в XML. Также обратите внимание, что производителем PDF является Aspose.PDF for SharePoint.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
