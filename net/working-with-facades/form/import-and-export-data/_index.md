---
title: Import and Export Data
type: docs
weight: 70
url: /net/import-and-export-data/
description: This section explains how to import and Export Data with Aspose.PDF Facades using Form Class.
lastmod: "2024-06-05"
draft: false
---

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class allows you to import data from an XML file to the PDF file using [ImportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.form/importxml/methods/1) method. In order to import data from XML, you need to create an object of [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class and then call the [ImportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxml/index) method using the FileStream object. Finally, you can save the PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) method of the [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class.The following code snippet shows you how to import data from XML file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ImportDataFromXML-ImportDataFromXML.cs" >}}

## Export Data to XML from a PDF File

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class allows you to export data to an XML file from the PDF file using [ExportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxml) method. In order to export data to XML, you need to create an object of [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class and then call the [ExportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxml) method using the FileStream object. Finally, you can close FileStream object and dispose Form object. The following code snippet shows you how to export data to XML file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ExportDataToXML-ExportDataToXML.cs" >}}

## Import Data from FDF into a PDF File

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class allows you to import data from an FDF file to the PDF file using [ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importfdf) method. In order to import data from FDF, you need to create an object of [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class and then call the [ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importfdf) method method using the FileStream object. Finally, you can save the PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) method of the [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class.The following code snippet shows you how to import data from FDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ImportDataFromPdf-ImportDataFromPdf.cs" >}}

## Export Data to FDF from a PDF File

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class allows you to export data to an FDF file from the PDF file using [ExportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportfdf) method. In order to export data to FDF, you need to create an object of [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class and then call the [ExportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportfdf) method using the FileStream object. Finally, you can save the PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) method of the [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class. The following code snippet shows you how to export data to FDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ExportDataToPdf-ExportDataToPdf.cs" >}}

## Import Data from XFDF into a PDF File

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class allows you to import data from an XFDF file to the PDF file using [ImportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxfdf) method. In order to import data from XFDF, you need to create an object of [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class and then call the [ImportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxfdf) method using the FileStream object. Finally, you can save the PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) method of the [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class. The following code snippet shows you how to import data from XFDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ImportDataFromXFDF-ImportDataFromXFDF.cs" >}}
 
## Export Data to XFDF from a PDF File

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class allows you to export data to an XFDF file from the PDF file using [ExportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxfdf) method. In order to export data to XFDF, you need to create an object of [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class and then call the [ExportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxfdf) method using the FileStream object. Finally, you can save the PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) method of the [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) class. The following code snippet shows you how to export data to XFDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ExportDataToXFDF-ExportDataToXFDF.cs" >}}

## Export values from fields to the JSON file

Aspose.Pdf.Facades provides an alternative API for working with form fields. This snippet demonstrates how to export and import field values using this API.

```cs
using (Form form = new Form())
{
    // Open Document
    form.BindPdf(dataDir + "Sample-Form-01.pdf");

    // Create XFDF file.
    using (FileStream jsonStream = new FileStream("Sample-Form-01.json", FileMode.Create))
    {
        // Export data
        form.ExportJson(jsonStream);
    }
}
```

## Import values to fields from the JSON file

This code snippet demonstrates how to import values into form fields of a PDF document from a JSON file using the Aspose.Pdf.Facades API. The FileStream is used to handle the JSON file.

```cs
using (Form form = new Form())
{
    // Open Document
    form.BindPdf("Sample-Form-01.pdf");

    // Create XFDF file.
    using (FileStream jsonStream = new FileStream("Sample-Form-01.json", FileMode.Open))
    {
        // Export data
        form.ImportJson(jsonStream);
    }
}
```
