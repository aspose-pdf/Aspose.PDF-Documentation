---
title: Applying a License
type: docs
weight: 30
url: /jasperreports/applying-a-license/
---

To apply a license:

1. Save the license file to a folder on your disk. For example C:\Lic\Aspose.BarCode.JasperReport.lic.
1. Call the License.setLicense(filename) method and pass the file name as an argument.
   When this statement is called, the licensed is set and the **Aspose.Demo** label no longer appears on top of the barcode image.

The following code snippet sets the license for Aspose.BarCode for JasperReports. 

**Java**

{{< highlight csharp >}}

 // Set license

License lic = new License();

lic.setLicense("C:\\ Lic\\Aspose.BarCode.JasperReports.lic");



{{< /highlight >}}

{{% alert color="primary" %}} 

You need to call the setLicense() method only once per process or application.

{{% /alert %}}
