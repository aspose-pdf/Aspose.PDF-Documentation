---
title: How to Create and Convert an XML File to PDF
type: docs
weight: 30
url: /ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint API is capable of creating and converting XML files into PDF format.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint основан на нашем отмеченном наградами компоненте Aspose.PDF for .NET. Aspose.PDF for .NET предоставляет замечательные функции от создания PDF-документа с нуля до манипуляции существующими PDF-файлами. Среди этих функций, конвертация XML в PDF является одной из замечательных функций, поддерживаемых этим продуктом. Поэтому мы считаем, что Aspose.PDF for SharePoint также будет способен конвертировать XML-файлы в формат PDF.

{{% /alert %}}

## **Создание XML-файла и его конвертация в PDF**

{{% alert color="primary" %}}

Шаг за шагом, эта статья проведет вас через процесс создания XML-файла и его конвертации в PDF:


1. [Создайте XML файл](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Создайте PDF шаблон](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Загрузите XML шаблон](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Укажите путь к исходному файлу](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Укажите свойства файла](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Экспортируйте файл в PDF](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Сохраните PDF файл](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).

#### **Шаг 1: Создайте XML файл**
Сначала создайте XML файл на основе объектной модели документа Aspose.PDF для .NET.

Согласно DOM Aspose.PDF для .NET, PDF документ содержит коллекцию объектов Section, а Section содержит один или несколько элементов Paragraph.
 Текст является объектом уровня абзаца и может содержать один или несколько сегментов. Ниже приведен пример текстовой строки, добавленной в объект Segment и добавленной в объект Text. Наконец, элемент Text добавляется в коллекцию абзацев объекта Section.

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
#### **Шаг 2: Создание шаблона PDF**
Перед продолжением убедитесь, что сервер SharePoint Foundation 2010 правильно установлен и настроен на системе, где будет происходить преобразование.

1. Войдите на сайт SharePoint.
1. Выберите **Действие сайта** и **Все элементы**.
1. Выберите опцию **Создать** и выберите **PDF Template** из списка.
1. Введите имя шаблона.
1. Нажмите **Создать**.

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **Шаг 3: Загрузка XML-шаблона**

После создания шаблона загрузите [XML файл](/pdf/ru/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):
1. На странице шаблона PDF выберите **Добавить новый элемент**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **Шаг 4: Укажите путь к исходному файлу**
В диалоговом окне загрузки документа:

1. Нажмите **Обзор** и найдите XML-файл на вашей системе. Вы можете установить флажок, чтобы перезаписать существующий файл.
1. Нажмите кнопку **ОК**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **Шаг 5: Укажите свойства файла**
Когда файл загружен, добавьте информацию в обязательные поля (отмеченные красной звездочкой: *).

Для этого примера было добавлено примерное описание, и следующие поля заполнены:

1. Краткое описание документа.
1. Введите **AllListTypes** для поля **Назначенные типы списков**.
1. Выберите **Список** из меню **Тип**.
   Убедитесь, что статус остается **Активный**.
1. Нажмите **Сохранить**, чтобы сохранить свойства.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **Шаг 6: Экспорт в PDF**

Когда XML-файл добавлен в шаблон PDF:
 Либо:

1. Щелкните правой кнопкой мыши файл test.xml.
1. Выберите **Экспорт в PDF** в меню.

Или:

1. Выберите **Aspose Tools** из **Библиотечные инструменты**.
1. Нажмите **Экспорт**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **Шаг 7: Сохранение документа PDF**
1. В диалоге Экспорт в PDF выберите **Хранилище шаблонов** (место, где хранится исходный файл).
1. Выберите файл для экспорта из меню **Имя шаблона**.
1. Нажмите **Экспорт в PDF**, чтобы сохранить итоговый PDF-документ.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **Открыть PDF**
Документ PDF сохранен и может быть открыт. На изображении ниже обратите внимание на фразу "Hello World", которая была в теге {segment] в XML. Также обратите внимание, что производитель PDF — Aspose.PDF для SharePoint.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}