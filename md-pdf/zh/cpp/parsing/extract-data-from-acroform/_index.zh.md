---
title: 从AcroForm中提取数据 
linktitle: 从AcroForm中提取数据
type: docs
weight: 50
url: /cpp/extract-data-from-acroform/
description: Aspose.PDF使从PDF文件中提取表单字段数据变得容易。了解如何从AcroForms中提取数据并将其保存为XML或FDF格式。
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF文档中提取表单字段

Aspose.PDF for C++不仅允许您创建表单字段并填写表单字段，还使从PDF文件中提取表单字段数据或表单字段信息变得容易。

在下面的代码示例中，我们演示了如何遍历PDF中的每个页面以提取有关PDF中所有AcroForms的信息以及表单字段值。此代码示例假设您事先不知道表单字段的名称。

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // 用于路径名的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 用于文件名的字符串
    String infilename("StudentInfoFormElectronic.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 从所有字段获取值
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "Field Name :" << formField->get_PartialName() << std::endl;
        std::cout << "Value : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 从 PDF 文件提取数据到 XML

[Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) 类允许您使用 ExportXml 方法将数据从 PDF 文件导出到 XML 文件。为了将数据导出到 XML，您需要创建 Form 类的对象，然后使用 FileStream 对象调用 ExportXml 方法。接下来您应该关闭 FileStream 对象并释放 Form 对象。

以下代码片段向您展示了如何将数据导出到 XML 文件。

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名称的字符串
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // 导出数据
    form->ExportXml(fdfOutputStream);

    // 关闭文件流
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 从 PDF 文件导出数据到 FDF

[表单](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) 类允许您使用 ExportFdf 方法将数据从 PDF 文件导出到 FDF 文件。为了将数据导出到 FDF，您需要创建 Form 类的对象，然后使用 FileStream 对象调用 ExportFdf 方法。之后，您可以使用 Form 类的 Save 方法保存 PDF 文件。

下面的代码片段展示了如何将数据导出到 FDF 文件。

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名称的字符串
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // 导出数据
    form->ExportFdf(fdfOutputStream);

    // 关闭文件流
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 将数据从 PDF 文件导出到 XFDF

Aspose PDF for C++ 与 [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) 类允许您使用 ExportXfdf 方法将数据从 PDF 文件导出到 XFDF 文件。为了将数据导出到 XFDF，您需要创建一个 Form 类的对象，然后使用 FileStream 对象调用 ExportXfdf 方法。

最后，您可以使用 Form 类的 Save 方法保存 PDF 文件。

以下代码片段向您展示如何将数据导出到 XFDF 文件。

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名字符串
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // 导出数据
    form->ExportXfdf(fdfOutputStream);

    // 关闭文件流
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```