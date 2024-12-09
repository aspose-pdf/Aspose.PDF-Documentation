---
title: Visual Studio Export GridView To PDF Control
type: docs
weight: 10
url: /net/visual-studio-export-gridview-to-pdf-control/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Visual Studio Export GridView To PDF Control",
    "alternativeHeadline": "Effortless PDF Export from ASP.NET GridViews",
    "abstract": "The Visual Studio Export GridView To PDF Control empowers ASP.NET developers to effortlessly convert GridView content into PDF documents. With customizable export options, including the ability to adjust button text and export orientation, users can create formatted offline copies for easy sharing and printing, enhancing workflow efficiency in .NET applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1801",
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
    "url": "/net/visual-studio-export-gridview-to-pdf-control/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/visual-studio-export-gridview-to-pdf-control/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Introduction

Export GridView To Pdf Control is an ASP.NET server control which allows exporting contents of GridView into Pdf document using [Aspose.PDF](https://products.aspose.com/pdf/net/). It adds **Export to Pdf** button on top of the GridView control. Clicking the button dynamically exports the content of the GridView control to a Pdf document and then automatically downloads the exported file to the disk location selected by the user in just couple of seconds.

### Module Features

This initial version of the control provides the following features:

- Get an offline copy of your favorite online GridView content for editing, sharing and printing in very popular Pdf document.
- Inherited from default ASP.NET GridView control and hence have all its features and properties.
- Works with all .NET versions starting from .NET 2.0.
- Ability to customize/localize Export button text.
- Option to Export in Landscape mode in case GridView content is wider and does not fit in default Portrait mode.
- Apply look and feel of your own theme on Export button using css.
- Option to add custom heading on top of the exported document.
- Option to save each exported document on server at configurable disk path.
- Option to export current page or all pages when paging is enabled.

## System Requirements and Supported Platforms

### System Requirements

Export GridView To Pdf Control for Visual Studio can be used on any system that have IIS and .NET framework 2.0 or greater installed.

### Supported Platforms

Export GridView To Pdf Control for Visual Studio is supported of all version of ASP.NET running on .NET framework 2.0 or greater. You can use any of the following Visual Studio versions to use this control in your ASP.NET applications

- Visual Studio 2005.
- Visual Studio 2008.
- Visual Studio 2010.
- Visual Studio 2012.
- Visual Studio 2013.

## Downloading

You can download Export GridView To Pdf Control from one of the following locations

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/releases/tag/AsposeExportGridViewToPdfControl_1.0).

## Installing

It is very simple and easy to install Export GridView To Pdf Control, please follow these simple steps

### **For Visual Studio 2010, 2012 and 2013**

1. Extract the downloaded zip file i.e. Aspose.PDF.GridViewExport_1.0.zip.
1. Double click the VSIX file Aspose.PDF.GridViewExport.vsix.
1. A dialog will appear showing you the available and supported Visual Studio versions installed on your machine.
1. Select the ones you want to add the Export GridView To Pdf Control to.
1. Click Install.

You will get a success dialog once the installation is completed.

**Note:** Please make sure to restart Visual Studio for the changes to take effect.

### **For Visual Studio 2005, 2008 and Express editions**

Please follow these steps to integrate Export GridView To Pdf Control in Visual studio for easy drag and drop just like other ASP.NET controls

1. Extract the downloaded zip file i.e. Aspose.PDF.GridViewExport.NET2.0_1.0.zip.
1. Make sure to run Visual Studio as Administrator.

On the Tools menu, click Choose Toolbox Items.

1. Click Browse.
   The Open dialog box appears.
1. Browse to the extracted folder and select Aspose.PDF.GridViewExport.dll.
1. Click OK.

When you open an aspx or ascx control in the left side Toolbox you will see ExportGridViewToPdf under General Tab

![todo:image_alt_text](visual-studio-export-gridview-to-pdf-control_2.png)

## Using

Once installed, it is very easy to start using this control in your ASP.NET applications

|**For .NET framework 4.0 and above**|**For .NET framework 2.0 and above**|** |
| :- | :- | :- |
|For applications running in .NET framework 4.0 and above in Visual Studio 2010 and above, you should see **ExportGridViewToPdf** control in **Aspose** Tab in Toolbar as shown below. You can simply drag drop this control onto your ASP.NET page, control or master page just like any other .NET control and get started.|In order you use this control in applications running in .NET 2.0 in any visual studio version make sure that you have added ExportGridViewToPdf to your toolbox as per instructions on [4.2.1 Downloading and Installing]() under heading **For Visual Studio 2005, 2008 and Express editions** <br>You should see **ExportGridViewToPdf** control in **General** Tab in Toolbar as shown below. You can simply drag drop this control onto your ASP.NET page, control or master page just like any other .NET control and get started.| |

### Manually adding ExportGridViewToPdf control

If you have any issues using the above methods which uses Visual Studio Toolbox, you can manually add this control to your ASP.NET application running on any .NET framework greater than 2.0

1. If you are using Visual Studio make sure to Run it as Administrator.
1. Add reference to **Aspose.PDF.GridViewExport.dll** available in extracted download package in your ASP.NET project or web application. Make sure your web application/Visual Studio have full access to this folder otherwise you might get Access is denied exception.
1. Add this line to the top of the page, control or MasterPage.

```csharp
 <%@ Register assembly="Aspose.PDF.GridViewExport" namespace="Aspose.PDF.GridViewExport" tagprefix="aspose" %>
```

1. Add the following to a place on your ASP.NET page, control or masterpage where you want the control to be added

```csharp
 <aspose:ExportGridViewToPdf ID="ExportGridViewToPdf1" runat="server"></aspose:ExportGridViewToPdf>
```

### FAQs

Common questions and issues you might face while using this Control

<div class="schema-faq-code" itemscope="" itemtype="https://schema.org/FAQPage">
    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">1. I cannot see ExportGridViewToPdf control in Toolbox</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <p><strong>Visual Studio 2010 and higher</strong></p>
<ol><li>Make sure that you have installed this control using VSIX extension file found in downloaded package. To verify go to Tools -&gt; Extension and Updates. Unders Installed you should see 'Aspose Export Export GridView To Pdf Control'. If don't see it please try re-installing it</li>
<li>Make sure your web application is running in .NET framework 4.0 or higher, for lower versions of .NET framework please check the above alternate method.
Older Versions of Visual Studio</li>
<li>Make sure that you have manually added this control to your Toolbox as per above instructions.</li></ol>
          </div>
        </div>
    </div>

    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">2. I am getting 'Access is denied' error when running the application</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <ol>
               <li>If you are experiencing this problem on production then make sure that you copy both Aspose.PDF.dll and Aspose.PDF.GridViewExport.dll to your bin folder.</li>
               <li>If you are using Visual Studio make sure to run it as Administrator even if you are already logged-in as administrator.</li>
               </ol>
            </div>
        </div>
    </div>
</div>

### **Aspose .NET Export GridView To Pdf Control Properties**

The following properties are exposed to configure and use cool features provided by this control

|**Property Name**|**Type**|**Example/Possible values**|**Description**|
| :- | :- | :- | :- |
|ExportButtonText|string|Export to Pdf|You can use this property to override existing default text.|
|ExportButtonCssClass|string|btn btn-primary|Css Class that is applied to the outer div of the export button. To apply css on button you can use .yourClass input.|
|ExportInLandscape|bool|true or false|If true it changes the orientation of the output document to landscape. Default is Portrait.|
| | | | |
|ExportFileHeading|string|GridView Export Example Report|You can use html tags to add style to your heading.|
|ExportOutputPathOnServer|string|c:/temp|Local output Disk path on server where a copy of the export is automatically saved. Application must have write access to this path.|
|ExportDataSource|object|allRowsDataTable|Sets the object from which this data-bind control retrieves its list of data items. The object must have all the data that need to be exported. This property is used in addition to normal DataSource property and is useful when custom paging is enabled and current page only fetches rows to be displayed on screen.|
|LicenseFilePath|string| |Local path on server to the license file. For example c:/inetpub/Aspose.PDF.lic.|

An example of Export GridView to Pdf control with all properties used is shown below

```csharp
<aspose:ExportGridViewToPdf Width="800px" ID="ExportGridViewToPdf1" ExportButtonText="Export to Pdf"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExportOutputFormat="Doc"
    ExportInLandscape="true" ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h4>Example Report</h4>"
    OnPageIndexChanging="ExportGridViewToPdf1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\\inetpub\\Aspose.PDF.lic"
    runat="server" CellPadding="4" ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToPdf>
```

## Video Demo

Please check [the video](https://www.youtube.com/watch?v=WNJ7T8u4JlM) below to see the module in action.

### Support

From the very first days of Aspose, we knew that just giving our customers good products would not be enough. We also needed to deliver good service. We are developers ourselves and understand how frustrating it is when a technical issue or a quirk in the software stops you from doing what you need to do. We're here to solve problems, not create them.

This is why we offer free support. Anyone who uses our product, whether they have bought them or are using an evaluation, deserves our full attention and respect.

You can log any issues or suggestions related to this Pdf using any of the following platforms

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/issues).

### Extend and Contribute

Aspose .NET Export GridView To Pdf for Visual Studio is open source and its source code is available on the major social coding websites listed below. Developers are encouraged to download the source code and extend the functionality as per their own requirements.

#### Source Code

You can get the latest source code from one of the following locations

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.PDF.GridViewExport).

#### How to configure the source code

You need to have the following installed in order to open and extend the source code

- Visual Studio 2010.

Please follow these simple steps to get started

1. Download/Clone the source code.
1. Open Visual Studio 2010 and Choose `File > Open Project`.
1. Browse to the latest source code that you have downloaded and open **Aspose.PDF.GridViewExport.sln**.

#### Source code overview

There are three projects in the solution

- Aspose.PDF.GridViewExport - Contains VSIX package and Server Pdf for .NET 4.0.
- Aspose.PDF.GridViewExport_DotNet_2.0 - Extended GridView Pdf for .NET 2.0.
- Aspose.PDF.GridViewExport.Website - Web project for testing the Word Exportable GridView Pdf.
