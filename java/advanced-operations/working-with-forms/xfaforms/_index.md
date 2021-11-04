---
title: Working with XFA Forms in PDF using Aspose.PDF for Java
linktitle: XFA Forms
type: docs
weight: 20
url: /java/xfa-forms/
description: With Aspose.PDF for Java you may create a form from scratch, fill the form field in a PDF document, extract data from the form, add or remove fields in the existing form.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA stands for XML Forms Architecture. It’s a set of proprietary XML specifications built originally for use with web forms in 1999, and has since become available for PDF.


{{% alert color="primary" %}}

Dynamic forms are based on an XML specification known as XFA, the “XML Forms Architecture”. It can also convert dynamic XFA form to standard Acroform. The information about the form (as far as PDF is concerned) is very vague – it specifies that fields exist, with properties, and JavaScript events, but does not specify any rendering. The objects of XFA form are drawn at the time loading the document.

{{% /alert %}}

## Fill XFA fields

The following code snippet shows you how to fill fields in XFA form.

```java
public class ExamplesXFA {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillXFA() {
	
        // Load XFA form
        Document document = new Document(_dataDir + "FillXFAFields.pdf");
    
        // Get names of XFA form fields
        String[] names = document.getForm().getXFA().getFieldNames();
    
        // Set field values        
        document.getForm().getXFA().set_Item(names[0],"Field 0");
        document.getForm().getXFA().set_Item(names[1],"Field 1");
    
        // Save the updated document
        document.save(_dataDir + "Filled_XFA_out.pdf");
    }
```

## Convert XFA-to-Acroform

{{% alert color="primary" %}}

Try online
You can check the quality of Aspose.PDF conversion and view the results online at this link: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Dynamic forms are based on an XML specification known as XFA, the “XML Forms Architecture”. The information about the form (as far as a PDF is concerned) is very vague – it specifies that fields exist, with properties, and JavaScript events, but does not specify any rendering.

Currently, PDF supports two different methods for integrating data and PDF forms:

- AcroForms (also known as Acrobat forms), introduced and included in the PDF 1.2 format specification.
- Adobe XML Forms Architecture (XFA) forms, introduced in the PDF 1.5 format specification as an optional feature (The XFA specification is not included in the PDF specification, it is only referenced.)

We cannot extract or manipulate pages of XFA Forms, because the form content is generated at runtime (during XFA form viewing) within the application trying to display or render the XFA form. Aspose.PDF has a feature that allows developers to convert XFA forms to standard AcroForms.

```java
 void ConvertXFAtoAcroForms() {
      
        // Load XFA form
        Document document = new Document(_dataDir + "DynamicXFAToAcroForm.pdf");
    
        // Set the form fields type as standard AcroForm
        document.getForm().setType(com.aspose.pdf.FormType.Standard);
    
        // Save the resultant PDF
        document.save(_dataDir + "Standard_AcroForm_out.pdf");
    }
```

## Get XFA field properties

To access field properties, first use Document.Form.XFA.Teamplate to access the field template. The following code snippet shows the steps of getting X and Y coordinates of XFA a form field.

```java
 void GetXFAProprties() {

        // Load XFA form
        Document document = new Document(_dataDir +"GetXFAProperties.pdf");
            
        String[] names = document.getForm().getXFA().getFieldNames();
    
        // Set field values
        document.getForm().getXFA().set_Item(names[0],"Field 0");
        document.getForm().getXFA().set_Item(names[1],"Field 1");
    
        // Get field position          
        System.out.println(document.getForm().getXFA().getFieldTemplate(names[0]).getAttributes().get_Item("x").get_Value());
    
        // Get field position
        System.out.println(document.getForm().getXFA().getFieldTemplate(names[0]).getAttributes().get_Item("y").get_Value());
    }
```
