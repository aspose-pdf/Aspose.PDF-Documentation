---
title:  Извлечение данных из AcroForm
linktitle:  Извлечение данных из AcroForm
type: docs
weight: 50
url: /ru/php-java/extract-data-from-acroform/
description: AcroForms существуют во многих PDF-документах. Эта статья поможет вам понять, как извлечь данные из AcroForms с использованием PHP и Aspose.PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение полей формы из PDF-документа

Aspose.PDF для PHP не только позволяет создавать и заполнять поля формы, но также облегчает извлечение данных полей формы или информации о полях формы из файлов PDF.

Предположим, что мы не знаем названия полей формы заранее. Тогда мы должны пройти по каждой странице в PDF, чтобы извлечь информацию обо всех AcroForms в PDF, а также значения полей формы. Чтобы получить доступ к форме, нам нужно использовать метод [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```php

    // Создайте новый экземпляр класса License и установите файл лицензии
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Установите путь к каталогу, содержащему PDF-документ
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // Установите путь к входному PDF-файлу
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // Установите заголовок ответа, чтобы указать, что ответ будет в формате JSON
    header('Content-Type: application/json; charset=utf-8');

    // Инициализируйте переменную данных ответа
    $responseData = "";

    try {
        // Создайте новый экземпляр класса Document и загрузите входной PDF-файл
        $document = new Document($inputFile);

        // Получите поля формы из документа и преобразуйте их в значения PHP
        $fields = java_values($document->getForm()->getFields());

        // Пройдите через каждое поле формы и извлеките имя поля и значение
        foreach ($fields as $formField) {
            // Конкатенируйте имя поля и значение к данным ответа
            $responseData = $responseData . "(Имя поля: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " Значение: " . $formField->getValue() . "),";
        }

        // Закройте документ
        $document->close();
    }
```


Если вы знаете названия полей формы, из которых хотите извлечь значения, вы можете использовать индексатор в коллекции Documents.Form для быстрого извлечения этих данных.

## Извлечение данных в XML из PDF файла

Класс Form позволяет экспортировать данные в XML файл из PDF файла с помощью метода ExportXml. Для того чтобы экспортировать данные в XML, вам нужно создать объект класса Form, а затем вызвать метод ExportXml, используя объект FileStream. Наконец, вы можете закрыть объект FileStream и освободить объект Form. Следующий фрагмент кода показывает, как экспортировать данные в XML файл.

```php

    // Открыть документ
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Создать объект FileOutputStream для записи файла шрифта.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // Экспорт данных
    $form->exportXml($xmlOutputStream);

    // Закрыть поток файла
    $xmlOutputStream->close();

    // Закрыть документ
    $form->close();
```

## Экспорт данных в FDF из PDF файла

Для экспорта данных форм PDF в файл XFDF мы можем использовать метод [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) в классе [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Обратите внимание, что это класс из `com.aspose.pdf.facades`. Несмотря на схожее название, этот класс имеет немного другую цель.

Чтобы экспортировать данные в FDF, вам нужно создать объект класса `Form`, а затем вызвать метод `exportXfdf`, используя объект `OutputStream`. Следующий фрагмент кода показывает, как экспортировать данные в файл XFDF.

```php

    // Открыть документ
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Создать объект FileOutputStream для записи файла шрифта.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // Экспорт данных
    $form->exportFdf($xmlOutputStream);

    // Закрыть поток файла
    $xmlOutputStream->close();

    // Закрыть документ
    $form->close();
```

## Экспорт данных в XFDF из PDF файла

Чтобы экспортировать данные форм PDF в файл XFDF, мы можем использовать метод [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) в классе [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Для экспорта данных в XFDF необходимо создать объект класса `Form`, а затем вызвать метод `exportXfdf` с использованием объекта `OutputStream`. Следующий фрагмент кода показывает, как экспортировать данные в файл XFDF.

```php

    // Открыть документ
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Создать объект FileOutputStream для записи файла шрифта.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // Экспорт данных
    $form->exportXfdf($xmlOutputStream);

    // Закрыть поток файла
    $xmlOutputStream->close();

    // Закрыть документ
    $form->close();
```