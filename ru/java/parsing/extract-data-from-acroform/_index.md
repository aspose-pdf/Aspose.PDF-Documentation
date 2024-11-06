---
title: Извлечение данных из AcroForm
linktitle: Извлечение данных из AcroForm
type: docs
weight: 50
url: ru/java/extract-data-from-acroform/
description: AcroForms существуют во многих PDF-документах. Эта статья поможет вам понять, как извлекать данные из AcroForms с помощью Java и Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение полей формы из PDF-документа

Aspose.PDF для Java не только позволяет создавать и заполнять поля формы, но и упрощает извлечение данных полей формы или информации о полях формы из файлов PDF.

Предположим, мы не знаем названия полей формы заранее. Тогда нам следует проходить по каждой странице в PDF, чтобы извлечь информацию обо всех AcroForms в PDF, а также значения полей формы. Для доступа к форме нам нужно использовать метод [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // Получить значения из всех полей
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("Имя поля :" + formField.getPartialName());
        System.out.println("Значение : " + formField.getValue());
    }
}
```


Если вы знаете названия полей формы, из которых хотите извлечь значения, вы можете использовать индексатор в коллекции Documents.Form, чтобы быстро получить эти данные.

## Извлечение значения поля формы по заголовку

Свойство Value поля формы позволяет получить значение конкретного поля. Чтобы получить значение, получите поле формы из [объекта Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [коллекции полей формы](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). В этом примере выбирается [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) и извлекается его значение с использованием метода [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Фамилия :" + textBoxField1.getValue());
}
```


## Извлечение полей формы из PDF документа в JSON

Для экспорта данных формы в JSON, мы рекомендуем использовать стороннюю библиотеку, такую как [Gson](https://github.com/google/gson).
Следующие фрагменты показывают, как экспортировать `Name` и `Value` в JSON:

```java
public static void ExtractFormFieldsToJson() {
    String path = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);

    java.util.List<FormElement> formData = new java.util.ArrayList<FormElement>();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        formData.add(new FormElement(formField.getPartialName(), formField.getValue()));
    }

    Gson gson = new Gson();
    String jsonString = gson.toJson(formData);
    System.out.println(jsonString);
}
```

В этом примере мы использовали дополнительный класс

```java
public class FormElement {
    public FormElement(String partialName, String Value) {
        this.Name = partialName;
        this.Value = Value;
    }
    public String Name;
    public String Value;
}
```


## Извлечение данных в XML из PDF файла

Класс Form позволяет экспортировать данные в файл XML из PDF файла, используя метод ExportXml. Чтобы экспортировать данные в XML, вам нужно создать объект класса Form, а затем вызвать метод ExportXml, используя объект FileStream. Наконец, вы можете закрыть объект FileStream и освободить объект Form. Следующий фрагмент кода показывает, как экспортировать данные в файл XML.

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // Открыть документ
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // Создать XML файл.
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // Экспорт данных
        form.exportXml(xmlOutputStream);

        // Закрыть поток файла
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // Закрыть документ
    form.dispose();
    ;
}
```


## Экспорт данных в FDF из PDF файла

Чтобы экспортировать данные форм PDF в XFDF файл, мы можем использовать метод [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) в классе [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Обратите внимание, что это класс из `com.aspose.pdf.facades`. Несмотря на схожее название, этот класс имеет несколько иное назначение.

Для того чтобы экспортировать данные в FDF, вам нужно создать объект класса `Form` и затем вызвать метод `exportXfdf`, используя объект `OutputStream`. Следующий фрагмент кода показывает, как экспортировать данные в XFDF файл.

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Экспорт данных
            form.exportFdf(fdfOutputStream);

            // Закрыть поток файла
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: обработать исключение
            e.printStackTrace();
        }

    }
```


## Экспорт данных в XFDF из PDF файла

Чтобы экспортировать данные форм PDF в файл XFDF, мы можем использовать метод [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) в классе [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Для экспорта данных в XFDF, вам нужно создать объект класса `Form`, а затем вызвать метод `exportXfdf`, используя объект `OutputStream`. В следующем кодовом фрагменте показано, как экспортировать данные в файл XFDF.

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Экспорт данных
            form.exportXfdf(fdfOutputStream);

            // Закрыть поток файла
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: обработать исключение
            e.printStackTrace();
        }
    }
```