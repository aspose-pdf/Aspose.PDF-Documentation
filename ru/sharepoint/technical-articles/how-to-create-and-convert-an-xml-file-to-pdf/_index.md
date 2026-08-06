---
title: Как создать и преобразовать XML-файл в PDF
linktitle: Как создать и преобразовать XML-файл в PDF
type: docs
weight: 30
url: /ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint API способен создавать и преобразовывать XML-файлы в формат PDF.
---

{{% alert color="primary" %}}

Aspose.PDF для SharePoint создан на основе нашего отмеченного наградами компонента Aspose.PDF для .NET. Aspose.PDF для .NET предоставляет замечательные возможности: от создания PDF-документов с нуля до манипулирования существующими PDF-файлами. Среди этих функций преобразование XML в PDF является одной из замечательных функций, поддерживаемых этим продуктом. Поэтому мы считаем, что Aspose.PDF for SharePoint также сможет конвертировать XML-файлы в формат PDF.

{{% /alert %}}

## Создание XML-файла и его преобразование в PDF

{{% alert color="primary" %}}

Эта статья шаг за шагом проведет вас через процесс создания XML-файла и его преобразования в PDF:

1. [Create an XML file](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Создать шаблон PDF](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Загрузить шаблон XML](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Укажите путь к исходному пути](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Укажите свойства файла](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Экспортировать файл в PDF](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Сохраните PDF-файл](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document)

### Шаг 1. Создайте XML-файл

Сначала создайте XML-файл на основе объектной модели документа Aspose.PDF для .NET.

Согласно Aspose.PDF для .NET DOM, документ PDF содержит коллекцию объектов Раздела, а Раздел содержит один или несколько элементов Параграфа. Текст представляет собой объект уровня абзаца и может содержать один или несколько сегментов. Ниже пример текстовой строки добавляется к объекту «Сегмент» и добавляется к объекту «Текст». Наконец, элемент Text добавляется в коллекцию абзацев объекта Раздел.

```xml

<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hello World</Segment>

    </Text>

   </Section>

  </Pdf>

```

### Шаг 2. Создайте шаблон PDF

Прежде чем продолжить, убедитесь, что сервер SharePoint Foundation 2010 правильно установлен и настроен в системе, где будет выполняться преобразование.

1. Войдите на сайт SharePoint.
1. Выберите **Действие на сайте** и **Все элементы**.
1. Выберите опцию **Создать** и выберите **Шаблон PDF** из списка.
1. Введите имя шаблона.
1. Нажмите **Создать**.

![Create PDF Template](how-to-create-and-convert-an-xml-file-to-pdf_1.png)

### Шаг 3. Загрузите XML-шаблон

После создания шаблона загрузите [файл XML](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)

1. На странице шаблона PDF выберите **Добавить новый элемент**.

![Load XML Template](how-to-create-and-convert-an-xml-file-to-pdf_2.png)

### Шаг 4. Укажите путь к исходному файлу

В диалоге загрузки документа:

1. Нажмите **Обзор** и найдите XML-файл в вашей системе. Вы можете установить флажок, чтобы перезаписать существующий файл.
1. Нажмите кнопку **ОК**.

![Specify Source File Path](how-to-create-and-convert-an-xml-file-to-pdf_3.png)

### Шаг 5. Укажите свойства файла

Когда файл загрузится, добавьте информацию в обязательные поля (отмечены красной звездочкой: *).

В этом примере был добавлен образец описания и заполнены следующие поля:

1. Краткое описание документа.
1. Введите **AllListTypes** в поле **Назначенные типы списков**.
1. Выберите **Список** в меню **Тип**.
   Убедитесь, что статус остается **Активный**.
1. Нажмите **Сохранить**, чтобы сохранить свойства.

![Specify File Properties](how-to-create-and-convert-an-xml-file-to-pdf_4.png)

### Шаг 6: Экспорт в PDF

Когда XML-файл добавлен в шаблон PDF:
Или:

1. Щелкните правой кнопкой мыши файл test.xml.
1. В меню выберите **Экспорт в PDF**.

Или:

1. Выберите **Инструменты Aspose** в списке **Инструменты библиотеки**.
1. Нажмите **Экспорт**.

![Export to PDF](how-to-create-and-convert-an-xml-file-to-pdf_5.png)

### Шаг 7. Сохраните PDF-документ

1. В диалоговом окне «Экспорт в PDF» выберите **Хранилище шаблонов** (место хранения исходного файла).
1. Выберите файл для экспорта в меню **Имя шаблона**.
1. Нажмите **Экспорт в PDF**, чтобы сохранить окончательный PDF-документ.

![Save PDF Document](how-to-create-and-convert-an-xml-file-to-pdf_6.png)

## Откройте PDF-файл

PDF-документ сохранен и его можно открыть. На изображении ниже обратите внимание на фразу «Hello World», которая была в теге сегмента в XML. Также обратите внимание, что PDF Producer — это Aspose.PDF для SharePoint.

![Open the PDF](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}

