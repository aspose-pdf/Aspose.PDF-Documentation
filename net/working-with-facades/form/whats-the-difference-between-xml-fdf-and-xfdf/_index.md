---
title: What's is the difference between FDF, XML, and XFDF formats
type: docs
weight: 30
url: /net/whats-the-difference-between-xml-fdf-and-xfdf/
description: This section difference between XML, FDF and XFDF forms with Aspose.PDF Facades using Form Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "Discover the differences between FDF, XML, and XFDF formats in PDF form data manipulation through Aspose.PDF for .NET. This feature enables developers to seamlessly export interactive form field values in various formats each with its own syntax while enhancing understanding and usage of these essential file types in PDF processing. Optimize your PDF form handling with detailed insights on how to represent form fields across different data formats",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

We mixed many different terms like FDF, XML and XFDF. All these terms are related to each other somehow. This article explores these concepts and their relationship to each other.

{{% /alert %}}

## Unraveling Forms

Aspose.PDF for .NET is used to manipulate PDF documents standardized by Adobe. And PDF documents contain interactive forms called AcroForms. These interactive forms have a number of form fields, like combo, text box, and radio button. Adobe's interactive forms, and form fields, work in the same way as an HTML form and its form fields.

It is possible to store the values of form fields in a separate file: an FDF (Forms Data Format) file. This contains the values of the form fields in key/pair fashion. FDF files are still used for this purpose. But Adobe also provides an XML encoded type of FDF called XFDF. An XFDF file stores the values of the form fields in a hierarchical manner using XML tags.

With Aspose.PDF developers can not only export the values of PDF form fields to an FDF or XFDF file but also to an XML file. All these files use different syntax to save PDF form field values. The example below explains the differences.

Let's assume that there are some PDF form fields whose values need to be presented in FDF, XML and XFDF forms. These assumed form fields with their field names and values are shown below:

|**Field Name**|**Field Value**|
| :- | :- |
|Company|Aspose.com|
|Address.1|Sydney, Australia|
|Address.2|Additional Address Line|
Let's see how to represent these values in FDF, XML and XFDF formats.

### What is FDF format?

As we know that FDF file store data in Key/Pair fashion where /T represents a Key, /V represents the Value and data in parenthesis () represents the content of either a Key or a Value. For example, /T(Company) means Company is the field key and /V(Aspose.com) is meant for a field value.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)

### What is XML format? 

Developers can represent each PDF form field in the form of a field tag, `<field>`. Each field tag has an attribute, name showing the field name and a sub tag, `<value>` represeting the field value as shown below:

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### What is XFDF format?  

The representation of above data in XFDF form is similar to XML form except with few differences. In XFDF files, we add their XML Namespace, which is <http://ns.adpbe.com/xfdf/> and their is an additional tag, `<f>` that is used to point towards the PDF document containing these PDF form fields. Like XML, XFDF also contains fields in the form of field tags, `<field>` as shown below:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### Identifying form fields names

Aspose.PDF for .NET provides the capability to create, edit and fill already created PDF forms. It contains [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) class, which has the function named [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) , and it takes two parameters i.e. Field name that needs to be filled, and the field value. So in-order to fill the form fields, you must be aware of the exact form field name.
We often come across the scenario in which we need to fill the form which is created in some tool i.e. Adobe Designer, and we are not sure about the form fields names. To accomplish our requirement, we need to read the names of all the PDF form fields. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) class provides the property named [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) which returns all the fields’ names and returns null if PDF have no field. But this property will return all the PDF form field's names and we won’t be sure, which name corresponds to which field over the form.

As a solution to this problem, we would require the appearance attributes of each field. [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) class has a function named GetFieldFacade which returns attributes, including location, color, border style, font, list item and so on. To save these values we will be using [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) class, which is used to record visual attributes of the fields. Once we have these attributes we can add a text field beneath every field which would be displaying the field name. Here a question arises how we would determine the location where to add the text field? Solution to this problem is Box property in [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) class, which holds the field's location. We would save these values to an array of rectangle type and use these values to identify the position where to add the new text fields.
In Aspose.Pdf.Facades namespace, we have a class named [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) which provides the capability to manipulate PDF form. Open a PDF form add a text field beneath every existing form field and save the PDF form with new name.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}
