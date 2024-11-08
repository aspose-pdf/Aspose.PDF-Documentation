---
title: Извлечение данных из AcroForm
linktitle: Извлечение данных из AcroForm
type: docs
weight: 50
url: /ru/cpp/extract-data-from-acroform/
description: Aspose.PDF позволяет легко извлекать данные полей формы из PDF-файлов. Узнайте, как извлечь данные из AcroForms и сохранить их в формате XML или FDF.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение полей формы из PDF документа

Aspose.PDF для C++ позволяет не только создавать поля формы и заполнять их, но и легко извлекать данные полей формы или информацию о полях формы из PDF-файлов.

В примере кода ниже мы демонстрируем, как перебрать каждую страницу в PDF, чтобы извлечь информацию обо всех AcroForms в PDF, а также значения полей формы. Этот пример кода предполагает, что вы не знаете названия полей формы заранее.

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("StudentInfoFormElectronic.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Получить значения из всех полей
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "Имя поля :" << formField->get_PartialName() << std::endl;
        std::cout << "Значение : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Извлечение данных в XML из PDF-файла

Класс [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) позволяет экспортировать данные в XML-файл из PDF-файла, используя метод ExportXml. Чтобы экспортировать данные в XML, необходимо создать объект класса Form, а затем вызвать метод ExportXml, используя объект FileStream. Далее следует закрыть объект FileStream и освободить объект Form.

Следующий фрагмент кода показывает, как экспортировать данные в XML-файл.

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // Экспорт данных
    form->ExportXml(fdfOutputStream);

    // Закрытие потока файла
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Экспорт данных в FDF из PDF файла

Класс [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) позволяет экспортировать данные в FDF файл из PDF файла с помощью метода ExportFdf. Для того чтобы экспортировать данные в FDF, необходимо создать объект класса Form и затем вызвать метод ExportFdf, используя объект FileStream. После этого вы можете сохранить PDF файл, используя метод Save класса Form.

Следующий фрагмент кода показывает, как экспортировать данные в FDF файл.

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Экспорт данных
    form->ExportFdf(fdfOutputStream);

    // Закрыть поток файла
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Экспорт данных в XFDF из PDF файла

Aspose PDF для C++ с классом [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) позволяет экспортировать данные в файл XFDF из PDF файла, используя метод ExportXfdf. Чтобы экспортировать данные в XFDF, необходимо создать объект класса Form и затем вызвать метод ExportXfdf, используя объект FileStream.

В конце вы можете сохранить PDF файл, используя метод Save класса Form.

Следующий фрагмент кода показывает, как экспортировать данные в файл XFDF.

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Экспорт данных
    form->ExportXfdf(fdfOutputStream);

    // Закрыть поток файла
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```