---
title: Convert PDF to XML
type: docs
weight: 230
url: /net/convert-pdf-to-xml/
description: It is possible to convert PDF documents to XML with Aspose.PDF for .NET. Сheck the snippet code for this task.
---

{{% alert color="primary" %}} 

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-xml](https://products.aspose.app/pdf/conversion/pdf-to-xml)

{{% /alert %}}

With Aspose.PDF for .NET, it is possible to convert PDF documents to XML.

### Schema

The schema is extended with the ability to use external fonts. Furthermore, when converting PDF files to XML, images are represented as separate files in the same directory as the output XML is created. Fonts are represented as TrueType fonts and the corresponding files (filename_fontN.ttf) are created along with the output XML.

XML is formed in accordance with the DTD schema specified below:

XML
```csharp<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="pdf2xml">
    <xs:complexType>
      <xs:sequence>
        <xs:element type="xs:string" name="title"/>
        <xs:element name="page" maxOccurs="unbounded" minOccurs="0">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="font" maxOccurs="unbounded" minOccurs="0">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="text" maxOccurs="unbounded" minOccurs="0">
                      <xs:complexType>
                        <xs:simpleContent>
                          <xs:extension base="xs:string">
                            <xs:attribute type="xs:float" name="x" use="optional"/>
                            <xs:attribute type="xs:float" name="y" use="optional"/>
                            <xs:attribute type="xs:float" name="width" use="optional"/>
                            <xs:attribute type="xs:float" name="height" use="optional"/>
                          </xs:extension>
                        </xs:simpleContent>
                      </xs:complexType>
                    </xs:element>
                    <xs:element name="img" minOccurs="0">
                      <xs:complexType>
                        <xs:simpleContent>
                          <xs:extension base="xs:string">
                            <xs:attribute type="xs:float" name="x" use="optional"/>
                            <xs:attribute type="xs:float" name="y" use="optional"/>
                            <xs:attribute type="xs:float" name="width" use="optional"/>
                            <xs:attribute type="xs:float" name="height" use="optional"/>
                            <xs:attribute type="xs:string" name="src" use="optional"/>
                          </xs:extension>
                        </xs:simpleContent>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                  <xs:attribute type="xs:float" name="size" use="optional"/>
                  <xs:attribute type="xs:string" name="face" use="optional"/>
                  <xs:attribute type="xs:string" name="src" use="optional"/>
                  <xs:attribute type="xs:string" name="color" use="optional"/>
                  <xs:attribute type="xs:boolean" name="italic" use="optional"/>
                  <xs:attribute type="xs:boolean" name="bold" use="optional"/>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
            <xs:attribute type="xs:short" name="width" use="optional"/>
            <xs:attribute type="xs:short" name="height" use="optional"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
      <xs:attribute type="xs:byte" name="pages"/>
    </xs:complexType>
  </xs:element>
</xs:schema>
```
The following code snippet shows the process of converting a PDF file to XML (MobiXML) format.

```csharp// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();            
// Load source PDF file
Document doc = new Document(dataDir + "input.pdf");
// Save output in XML format
doc.Save(dataDir + "PDFToXML_out.xml", SaveFormat.MobiXml);
```
Once the PDF file is converted to XML format, we need to verify that either the conversion is correctly performed or not. In order to cater this requirement, we have created a utility to convert XML contents to XPS format. Please find attached the AsposeMobiXmlToXpsConverter.zip archive which contains AsposeMobiXmlToXpsConverter.exe utility to convert MobiXML file to XPS format. The resultant .xps file can be viewed with any XPS-viewer to ensure that MobiXML files generated with Aspose.PDF for .NET are correct. In attached .zip package, you can find a file *start.bat* which contains the path for AsposeMobiXmlToXpsConverter.exe utility and the path of input XML, which is provided as an argument to this utility.

In case the source PDF contains images, they are represented as separate files (filename_picN.jpg|png) in the directory where output xml is created. Also the fonts are represented as True Type fonts and corresponding files (filename_fontN.ttf) are created along the output XML. Where N is order number (1, 2, ...).
