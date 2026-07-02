---
title:  Извлечь данные из AcroForm
linktitle:  Извлечь данные из AcroForm
type: docs
weight: 50
url: /ru/androidjava/extract-data-from-acroform/
description: AcroForms существует во многих PDF‑документах. Эта статья направлена на то, чтобы помочь вам понять, как извлекать данные из AcroForms с помощью Aspose.PDF.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечь поля формы из PDF‑документа

Aspose.PDF for Android via Java не только позволяет создавать и заполнять поля формы, но и облегчает извлечение данных полей формы или информации о полях формы из PDF‑файлов.

Предположим, что мы заранее не знаем названий полей формы. Тогда нам следует пройтись по каждой странице PDF, чтобы извлечь информацию обо всех AcroForms в PDF, а также значения полей формы. Чтобы получить доступ к форме, нам нужно использовать [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) метод.

```java
 public void extractFormFields () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get values from all fields
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```

Если вы знаете имя полей формы, из которых хотите извлечь значения, то можете воспользоваться индексатором в коллекции Documents.Form для быстрой выборки этих данных.

## Получить значение поля формы по названию

Свойство Value поля формы позволяет получить значение конкретного поля. Чтобы получить значение, получите поле формы из [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) объекта [коллекция полей формы](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). Этот пример выбирает a [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) и получает его значение с помощью [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) метод.

```java

    public void extractFormDataByName () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```

## Извлечь данные в XML из PDF-файла

Класс Form позволяет экспортировать данные в XML‑файл из PDF‑файла с помощью метода ExportXml. Чтобы экспортировать данные в XML, необходимо создать объект класса Form и затем вызвать метод ExportXml, используя объект FileStream. В конце можно закрыть объект FileStream и освободить объект Form. Ниже приведён фрагмент кода, показывающий, как экспортировать данные в XML‑файл.

```java
public void extractFormFieldsToXML () {
        // Open document
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
            // Create xml file.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Export data
            form.exportXml(xmlOutputStream);

            // Close file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Close the document
        form.dispose();
    }
```

## Экспорт данных в FDF из PDF-файла

Для экспорта данных форм PDF в файл XFDF мы можем использовать [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) метод в [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) класс.

Обратите внимание, что это класс из `com.aspose.pdf.facades`. Несмотря на похожее название, у этого класса немного другая цель.

Чтобы экспортировать данные в FDF, вам нужно создать объект `Form` класс, а затем вызвать `exportXfdf` метод, использующий `OutputStream` объект. Следующий фрагмент кода показывает, как экспортировать данные в файл XFDF.

```java
public void extractFormExportFDF () {
        // Open document
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

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Экспорт данных в XFDF из PDF‑файла

Для экспорта данных форм PDF в файл XFDF мы можем использовать [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) метод в [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) класс.

Чтобы экспортировать данные в XFDF, вам нужно создать объект `Form` класс, а затем вызвать `exportXfdf` метод, использующий `OutputStream` объект. 
Следующий фрагмент кода показывает, как экспортировать данные в файл XFDF.

```java
    public void extractFormExportXFDF () {
        // Open document
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

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

