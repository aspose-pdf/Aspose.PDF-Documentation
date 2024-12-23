---
title: Работа с AcroForms в PDF 
linktitle: AcroForms
type: docs
weight: 10
url: /ru/java/acroforms/
description: С помощью Aspose.PDF for Java вы можете создать форму с нуля, заполнить поле формы в PDF-документе, извлечь данные из формы, добавить или удалить поля в существующей форме.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Основы AcroForms

**AcroForms** — это оригинальная технология форм PDF. AcroForms — это ориентированная на страницы форма. Они были впервые представлены в 1998 году. Они принимают ввод в формате данных форм или FDF и формате данных XML форм или xFDF. Сторонние поставщики поддерживают AcroForms. Когда Adobe представила AcroForms, они называли их «PDF-формой, созданной с помощью Adobe Acrobat Pro/Standard и не являющейся специальным типом статической или динамической формы XFA. AcroForms являются портативными и работают на всех платформах.

Вы можете использовать AcroForms для добавления дополнительных страниц в документ формы PDF.
 Благодаря концепции Шаблонов, вы можете использовать AcroForms для заполнения формы несколькими записями из базы данных.

PDF 1.7 поддерживает два различных метода интеграции данных и PDF-форм.

*AcroForms (также известные как формы Acrobat)*, представленные и включенные в спецификацию формата PDF 1.2.

*Adobe XML Forms Architecture (XFA) формы*, представленные в спецификации формата PDF 1.5 в качестве дополнительной функции (спецификация XFA не включена в спецификацию PDF, она только упоминается).

Чтобы понять **Acroforms** и формы **XFA**, нам нужно сначала понять основы. Для начала, обе являются PDF-формами, которые вы можете использовать. Acroforms является более старой, созданной еще в 1998 году, и до сих пор считается классической PDF-формой. Формы XFA — это веб-страницы, которые вы можете сохранить в формате PDF, и они появились в 2003 году. Потребовалось некоторое время, прежде чем PDF начал принимать формы XFA.

AcroForms обладают возможностями, отсутствующими в XFA, и наоборот, XFA имеет возможности, отсутствующие в AcroForms. Например:

- AcroForms поддерживают концепцию "Шаблонов", позволяя добавлять дополнительные страницы в документ PDF-формы для поддержки заполнения формы несколькими записями из базы данных.- XFA поддерживает концепцию перелива документа, позволяя полю изменять размер, если это необходимо для размещения данных.

Таким образом, PDF — лучший формат файлов для форм, так как они могут распространяться в электронном виде, заполняться внутри документа и отправляться обратно отправителю без необходимости печати или отправки по традиционной почте.

Для более детального изучения возможностей работы с формами изучите следующие статьи в разделе:

-[Create AcroForm](/pdf/ru/java/create-form/) - создание формы с нуля, добавление RadioButtonField, TextBoxField, Caption Field с использованием Java.

-[Fill AcroForm](/pdf/ru/java/fill-form/) - чтобы заполнить поле формы, получите поле из коллекции Form объекта Document.

-[Extract Data AcroForm](/pdf/ru/java/extract-form/) - получение значений из всех и отдельных полей и т.д.

-[Modifing AcroForm](/pdf/ru/java/modifing-form/) - установка/получение FieldLimit, удаление полей в существующей форме, установка шрифта поля формы, отличного от 14 основных шрифтов PDF с помощью Java.