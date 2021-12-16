---
title:  Extract data from AcroForm 
linktitle:  Extract data from AcroForm
type: docs
weight: 50
url: /cpp/extract-data-from-acroform/
description: Aspose.PDF makes it easy to extract form field data from PDF files. Learn how to extract data from AcroForms and save it into XML, or FDF format.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract form fields from PDF document

Aspose.PDF for C++ allows you to not only create form fields and fill in form fields but also makes it easy to extract form field data or form field information from PDF files.

In the code example below, we demonstrate how to iterate over each page in PDF to extract information about all AcroForms in PDF as well as form field values. This code example assumes that you do not know the names of the form fields in advance.

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("StudentInfoFormElectronic.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Get values from all fields
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "Field Name :" << formField->get_PartialName() << std::endl;
        std::cout << "Value : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extract Data to XML from a PDF File

[Form](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) class allows you to export data to an XML file from the PDF file using ExportXml method. In order to export data to XML, you need to create an object of Form class and then call the ExportXml method using the FileStream object. Next you should close FileStream object and dispose Form object.

The following code snippet shows you how to export data to XML file.

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // Export data
    form->ExportXml(fdfOutputStream);

    // Close file stream
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Export Data to FDF from a PDF File

[Form](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) class allows you to export data to an FDF file from the PDF file using ExportFdf method. In order to export data to FDF, you need to create an object of Form class and then call the ExportFdf method using the FileStream object. After you may save the PDF file using Save method of the Form class.

The following code snippet shows you how to export data to FDF file.

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Export data
    form->ExportFdf(fdfOutputStream);

    // Close file stream
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Export Data to XFDF from a PDF File

Aspose PDF for C++ with [Form](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) class allows you to export data to an XFDF file from the PDF file using ExportXfdf method. In order to export data to XFDF, you need to create an object of Form class and then call the ExportXfdf method using the FileStream object.

In the end, you may save the PDF file using the Save method of the Form class.

The following code snippet shows you how to export data to XFDF file.

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Export data
    form->ExportXfdf(fdfOutputStream);

    // Close file stream
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```
