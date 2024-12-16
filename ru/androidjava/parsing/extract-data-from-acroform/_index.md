---
title:  Извлечение данных из AcroForm
linktitle:  Извлечение данных из AcroForm
type: docs
weight: 50
url: /ru/androidjava/extract-data-from-acroform/
description: AcroForms существуют во многих PDF-документах. Эта статья нацелена на то, чтобы помочь вам понять, как извлечь данные из AcroForms с помощью Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение полей формы из PDF-документа

Aspose.PDF для Android через Java не только позволяет создавать и заполнять поля формы, но и облегчает извлечение данных полей формы или информации о полях формы из PDF-файлов.

Предположим, что мы не знаем названия полей формы заранее. Тогда мы должны перебрать каждую страницу в PDF, чтобы извлечь информацию обо всех AcroForms в PDF, а также значения полей формы. Для доступа к форме нам нужно использовать метод [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
 public void extractFormFields () {
        // Открыть документ
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Получить значения из всех полей
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Имя поля: ");
            sb.append(formField.getPartialName());
            sb.append(" Значение: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```


Если вы знаете название полей формы, из которых хотите извлечь значения, вы можете использовать индексатор в коллекции Documents.Form для быстрого извлечения этих данных.

## Извлечение значения поля формы по заголовку

Свойство Value поля формы позволяет получить значение конкретного поля. Чтобы получить значение, получите поле формы из [коллекции полей формы](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Этот пример выбирает [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) и извлекает его значение с помощью метода [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java

    public void extractFormDataByName () {
        // Открыть документ
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Фамилия: " + textBoxField1.getValue());

    }
```


## Извлечение данных в XML из PDF файла

Класс Form позволяет экспортировать данные в XML файл из PDF файла, используя метод ExportXml. Для того чтобы экспортировать данные в XML, вам нужно создать объект класса Form и затем вызвать метод ExportXml, используя объект FileStream. В конце, вы можете закрыть объект FileStream и освободить объект Form. Следующий фрагмент кода показывает, как экспортировать данные в XML файл.

```java
public void extractFormFieldsToXML () {
        // Открыть документ
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // Создать xml файл.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Экспортировать данные
            form.exportXml(xmlOutputStream);

            // Закрыть поток файла
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Закрыть документ
        form.dispose();
    }
```


## Экспорт данных в FDF из PDF файла

Чтобы экспортировать данные форм PDF в файл XFDF, мы можем использовать метод [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) в классе [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Обратите внимание, что это класс из `com.aspose.pdf.facades`. Несмотря на схожее название, этот класс имеет немного другое назначение.

Для того чтобы экспортировать данные в FDF, вам нужно создать объект класса `Form`, а затем вызвать метод `exportXfdf`, используя объект `OutputStream`. Следующий фрагмент кода показывает, как экспортировать данные в файл XFDF.

```java
public void extractFormExportFDF () {
        // Открыть документ
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Экспортировать данные
            form.exportFdf(fdfOutputStream);

            // Закрыть поток файла
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Экспорт данных в XFDF из PDF файла

Чтобы экспортировать данные форм PDF в файл XFDF, мы можем использовать метод [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) в классе [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Для того чтобы экспортировать данные в XFDF, необходимо создать объект класса `Form`, а затем вызвать метод `exportXfdf`, используя объект `OutputStream`. 
Следующий фрагмент кода показывает, как экспортировать данные в файл XFDF.

```java
    public void extractFormExportXFDF () {
        // Открыть документ
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Экспорт данных
            form.exportXfdf(fdfOutputStream);

            // Закрыть поток файла
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```