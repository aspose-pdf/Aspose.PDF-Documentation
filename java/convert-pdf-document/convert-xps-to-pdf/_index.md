## Convert XPS to PDF 

{{% alert color="primary" %}} 

XPS, XML Paper Specification, is a Microsoft file format used to integrate document creation and viewing into Windows. With Aspose.PDF for Java, it is possible to convert XPS files to PDF, the portable file format from Adobe.

The file format is basically a zipped XML file, primarily used for distribution and storage. It's very difficult to edit and mostly implemented by Microsoft.

{{% /alert %}} 

To convert an XPS file to PDF using [Aspose.PDF for Java](https://products.aspose.com/pdf/java), use [XpsLoadOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/XpsLoadOptions) class. This is used to initialize a [LoadOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/LoadOptions) object. Later, this object is passed as an argument during the [Document](https://apireference.aspose.com/java/pdf/com.aspose.pdf/document) object initialization and helps the PDF rendering engine to determine the source document's input format.

In both XP and Windows 7, you should find an XPS Printer pre-installed if you look in the Control Panel and then **Printers**. To create XPS files you can use that printer for the output device. In Windows 7, you should be able to just double-click the file to open it in an XPS viewer. You may also download [XPS viewer](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer) from Microsoft's website.

The following code snippet shows the process of converting the XPS file into PDF format.
```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-Java
// Instantiate LoadOption object using XPS load option
LoadOptions options = new XpsLoadOptions();
// Create document object
Document document = new Document("printoutput.xps", options);
// Save the resultant PDF document
document.save("resultant.pdf");
```

