---
title:  Извлечение данных из AcroForm с использованием C#
linktitle:  Извлечение данных из AcroForm
type: docs
weight: 50
url: ru/net/extract-data-from-acroform/
description: Aspose.PDF облегчает извлечение данных из полей формы в PDF файлах. Узнайте, как извлечь данные из AcroForms и сохранить их в формате JSON, XML или FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение полей форм из PDF документа

Aspose.PDF для .NET не только позволяет создавать поля форм и заполнять их, но и облегчает извлечение данных из полей форм или информации о полях форм из PDF файлов.

В приведенном ниже примере кода мы демонстрируем, как перебирать каждую страницу в PDF для извлечения информации обо всех AcroForm в PDF, а также о значениях полей форм. Этот пример кода предполагает, что вы заранее не знаете названия полей форм.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // Получение значений из всех полей
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("Название поля : {0} ", formField.PartialName);
        Console.WriteLine("Значение : {0} ", formField.Value);
    }
}
```
Если вы знаете название полей формы, из которых хотите извлечь значения, то можете использовать индексатор в коллекции Documents.Form для быстрого получения этих данных. Смотрите в конце этой статьи пример кода, показывающий, как использовать эту функцию.

## Получение значения поля формы по названию

Свойство Value поля формы позволяет получить значение определенного поля. Чтобы получить значение, получите поле формы из коллекции Form объекта Document. В этом примере выбирается TextBoxField и извлекается его значение с использованием свойства Value.

## Извлечение полей формы из PDF-документа в JSON

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```
## Извлечение данных в XML из файла PDF

Класс Form позволяет вам экспортировать данные в XML-файл из PDF-файла с использованием метода ExportXml. Для экспорта данных в XML вам необходимо создать объект класса Form, а затем вызвать метод ExportXml с использованием объекта FileStream. В конце вы можете закрыть объект FileStream и утилизировать объект Form. Следующий фрагмент кода показывает, как экспортировать данные в XML-файл.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// Открыть документ
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// Создать XML файл.
System.IO.FileStream xmlOutputStream = new FileStream( dataDir + "input.xml", FileMode.Create);
// Экспортировать данные
form.ExportXml(xmlOutputStream);
// Закрыть поток файла
xmlOutputStream.Close();

// Закрыть документ
form.Dispose();
```
## Экспорт данных в FDF из файла PDF

Класс Form позволяет вам экспортировать данные в файл FDF из файла PDF с использованием метода ExportFdf. Для экспорта данных в FDF вам необходимо создать объект класса Form и затем вызвать метод ExportFdf с использованием объекта FileStream. Наконец, вы можете сохранить файл PDF с использованием метода Save класса Form. Следующий фрагмент кода показывает, как экспортировать данные в файл FDF.

Данный фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Открыть документ
form.BindPdf(dataDir + "input.pdf");

// Создать файл fdf.
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// Экспортировать данные
form.ExportFdf(fdfOutputStream);

// Закрыть поток файла
fdfOutputStream.Close();

// Сохранить обновленный документ
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```
## Экспорт данных в XFDF из PDF файла

Класс Form позволяет вам экспортировать данные в файл XFDF из PDF файла с использованием метода ExportXfdf. Для экспорта данных в XFDF вам необходимо создать объект класса Form, а затем вызвать метод ExportXfdf используя объект FileStream. В конце вы можете сохранить PDF файл с помощью метода Save класса Form. Следующий фрагмент кода показывает, как экспортировать данные в файл XFDF.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Открыть документ
form.BindPdf(dataDir + "input.pdf");

// Создать xfdf файл.
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// Экспортировать данные
form.ExportXfdf(xfdfOutputStream);

// Закрыть файловый поток
xfdfOutputStream.Close();

// Сохранить обновленный документ
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```

