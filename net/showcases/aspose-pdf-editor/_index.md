---
title: Aspose.PDF Editor
type: docs
weight: 10
url: /net/aspose-pdf-editor/
description: Aspose.PDF for .NET demonstrate HTML5 PDF Editor is an open source web-based PDF editor.
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## What is Html5 PDF Editor by Aspose.PDF for .NET?

HTML5 PDF Editor by Aspose.PDF for .NET is an open source web based PDF editor that allows users to create, edit and convert PDF files online and users can easily embed the editor in their own web applications for viewing and editing PDF files. HTML5 PDF Editor is developed using HTML5, jQuery Ajax, ASP.NET, Bootstrap and backend is powered by Aspose.PDF for .NET. The UI of the editor is kept very simple for easy understanding and enhancement of the features as per user requirements.

![Image](../images/aspose-pdf-editor.png)

## Features

Currently, it supports the following features:

- Create new PDF files
- Loading and Viewing PDF files
- Loading PDF and Image files from Dropbox
- Exporting PDF file to different file formats
- Appending or Merging PDF files
- Inserting New Pages
- Deleting Pages
- Moving Pages in PDF file
- Inserting Text in PDF
- Highlight Text in PDF
- Rotate Inserted Text in PDF
- Searching Text in PDF
- Replace Text in PDF
- Inserting Images
- Resizing Signature and Images
- Dragging and Positioning inserted items
- Loading PDF files with form fields
- Fill Form fields using the Editor
- Save and Export PDF with form fields data
- Highlighting required form fields
- Add Attachments to PDF Files
- Load Attachments from input PDF file
- Download the Attachment files
- Remove the Attachment files
- Signing PDF using Free-Hand Drawing

## System Requirements

As HTML5 PDF Editor is .NET Web application which is developed using ASP.NET, C#, HTML5, jQuery, Javascript. You will need the following system environment to setup HTML5 PDF Editor at your end.

- Visual Studio 2010 (or above)
- .NET Framework 3.5 (or above)
- Aspose.PDF for .NET
- jQuery 2.0.3
- Bootstrap 3.2.0

You can use any of the following browsers to run the application at your end:

- Mozilla Firefox (recommended)
- Internet Explorer (version 9 or later)
- Google Chrome
- Apple Safari

## Support

We, at Aspose, make sure to provide best possible support to our customers / users for their queries of any nature i.e. technical or sales. Please use the below links for any license and sales related or technical query.

# PDF Editor Developer Guide

## Create New PDF Files

Besides editing existing PDF documents, Html5 PDF Editor also supports creating new PDF files from scratch which you can do by using Create New File option from the menu bar. Using this feature, you may create a blank PDF in editor, add some text/images to it and save it in any desired format. In our next section, we will discuss the technical details behind this feature.

### How it works?
**HTML - "Create New File" menu item is clicked on the page**

When you click "Create New File" menu item, onNewFileClicked method is called in Editor.js file.

**jQuery - Send Ajax request to server for CreateNewFile method.**

See Editor.js tab below for source code of onNewFileClicked method, it calls CreateNewFile method in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below with source code of CreateNewFile method. It clears any existing data regarding previously loaded file using ResetData method.

**New PDF file creation using Aspose.PDF for .NET**

After clearing the data using ResetData method, CreateNewFile method creates a new PDF file using Document class of Aspose.PDF for .NET.
As you can see in the below tab, the Document object is generating a file with one empty page. After the file is generated on the server, the file is converted to image using ImageConverter method to be loaded on canvas.

**Loading the resultant file to canvas.**

After file gets converted to image on server side, the control is returned back to onNewFileClicked method in Editor.js. onNewFileClicked method resets all the client side collections and load the generated image file to canvas using resetData method.

## Exporting PDF to Different File Formats

HTML5 PDF Editor supports exporting PDF file to different file formats which you can do by using Export File option from the menu bar. Using this feature, you can export the PDF file to your desired format. In our next section, we will discuss the technical details behind this feature.

### How it works?

**HTML - "Export File" menu item is clicked on the page.**

When you click "Export File" menu item, you can choose the export format from the list. After selecting the export format, "ExportFile" method is called in Editor.js file.

**jQuery - Send Ajax server request for method btnFileExport_Click method**

See Editor.js tab below for source code of "ExportFile" method. It send a request to server method btnFileExport_Click with file format parameter in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below. Based on the file format parameter passed to btnFileExport_Click, the PDF file is converted using Save method of Aspose.PDF Document object.

**Export file to Download on Client Browser**

After the file is generated on the server, the control is returned back to ExportFile method in Editor.js from where the file is sent to the browser for user to download using ExportToBrowser method.

## Appending or Merging PDF Files

Html5 PDF Editor supports appending or merging of PDF files which you can do by using Append File option from the menu bar. Using this feature, you can append the PDF file to your input file. In our next section, we will discuss the technical details behind this feature.

### How it works?

**HTML - "Append File" menu item is clicked on the page.**

When you click "Append File" menu item, you can upload the file using file upload dialog. After the file gets uploaded, "fileSelected" method is called in Editor.js file.

**jQuery - Send server request for ProcessRequest method**

See Editor.js tab below for source code of "fileSelected" method. File gets posted to the server and method "ProcessRequest" is called in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below. Based on the form parameter passed, the file to be appended is saved on the server and "AppendFile" method is called. AppendFile method, append the uploaded file using Aspose.PDF for .NET, convert the resultant file to image and return the control back to "fileSelected" method in Editor.js

**Update the canvas content after appending the file**

After the file is generated on the server, the control is returned back to "fileSeleceted" method in Editor.js which update the contents of the editor.

## Upload Local PDF File

HTML5 PDF Editor supports uploading PDF file from local machine using Open From Computer option from the menu bar. Using this feature, you can open an existing PDF file and perform editing on your PDF file. In our next section, we will discuss the technical details behind this feature. 

### How it works?

**HTML - "Open From Computer" menu item is clicked on the page.**

When you click "Open From Computer" menu item, you can upload the input file using file upload dialog. After the file gets uploaded, "fileSelected" method is called in Editor.js file.

**jQuery - Send server request for ProcessRequest method**

See Editor.js tab below for source code of "fileSelected" method. File gets posted to the server and method "ProcessRequest" is called in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below. Based on the form parameter passed, the file to be uploaded is saved on the server, resets the data using "ResetData" method and "ImageConverter" method is called. ImageConverter method, converts the uploaded file to images using Aspose.PDF for .NET and return the control back to "fileSelected" method in Editor.js

**Update the canvas content after uploading the file**

After the file is generated on the server, the control is returned back to "fileSeleceted" method in Editor.js which update the contents of the editor i.e. resets the canvas, load the newly uploaded file.

## Adding Page in PDF File

Using Html5 PDF Editor, you can add new pages in PDF files using Add Page option from the menu bar. Using this feature, you may add a blank page to your PDF file. In our next section, we will discuss the technical details behind this feature.

### How it works?

**HTML - "Add Page" menu item is clicked on the page**

When you click "Add Page" menu item, "AddPage" method is called in Editor.js file.

**jQuery - Send Ajax request to server for AddPage_Click method.**

See Editor.js tab below for source code of AddPage method, it calls AddPage_Click method in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below with source code of AddPage_Click method. It adds a new empty page in PDF file using Aspose.PDF.Document class. After adding the page to PDF file, it converts the page to image to be displayed in the editor.The control is then returned back to Editor.js file which updates the page numbering in AddPage method.

## Deleting Page from PDF File

Using Html5 PDF Editor, you can delete a page from PDF files using Delete Page option from the menu bar. In our next section, we will discuss the technical details behind this feature.

### How it works?

**HTML - "Delete Page" menu item is clicked on the page**

When you click "Delete Page" menu item, DeletePage method is called in Editor.js file.

**jQuery - Send Ajax request to server for DeletePage_Click method.**

See Editor.js tab below for source code of DeletePage method, it calls DeletePage_Click method in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below with source code of DeletePage_Click method. It deletes the selected page from PDF file using Delete method of Aspose.PDF.Document.Page collection.

**Updating editing content**

After deleting the page from PDF file, the control is then returned back to DeletePage method in Editor.js file which updates the page numbering, remove any collections associated with the deleted page using updateIndexesDelete method.

## Move Pages in PDF File

Using Html5 PDF Editor, you can move pages in PDF files using Move Page option from the menu bar. Once you press the Move Page menu item, you are presented with an input dialog to specify the selected page's new location. In our next section, we will discuss the technical details behind this feature.

### How it works?

**HTML - "Move Page" menu item is clicked on the page**

When you click "Move Page" menu item, input dialog is shown to get the new location of the selected page. After providing the page number and pressing "Move" button, "Move" method is called in Editor.js file.

**jQuery - Send Ajax request to server for MovePages method.**

See Editor.js tab below for source code of Move method, which calls MovePage method and it passes the details like move from, move to, pages list to MovePages method in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below with source code of MovePages method. It uses Aspose.PDF.Document.Pages collection to move the pages.

**Updating editing content**

After moving the page, the control is then returned back to MovePage method in Editor.js file which updates the page indexes and information related to different collections in the editor using MoveUpdate method.

## Inserting Text in PDF File

Using Html5 PDF Editor, you can insert text in PDF files using Text Mode option from the menu bar. Once you select the Text Mode menu item and click on any location on the editor where you want to add the text, you are presented with an input dialog to input and format your desired text as shown below:

In our next section, we will discuss the technical details behind this feature.

### How it works?

**HTML - "Text Mode" menu item is selected on the page**

When you select "Text Mode" menu item and click your desired location on the editor to insert text in PDF file, input dialog is shown to get the text you need to insert on the page. After providing the text and pressing "OK" button, "saveTextFromArea" method is called in Editor.js file.

**Javascript - Get the input text from input dialog and show on the editor.**

See Editor.js tab below for source code of saveTextFromArea method, which gets the text from the input dialog and show it on the editor. Also, it saves the data in shapes collection which is later used on server side to insert text in the PDF file. You can check the source code of saveFile method which is called when the file is saved.

**ASP.NET web method handles server requests**

As mentioned above, the text will actually get inserted into our source PDF file when we perform the save operation which uses GetTextStamp method to create the text stamp to insert in PDF file. See Canvas.aspx.cs tab below with source code of GetTextStamp method. It uses Aspose.PDF.TextStamp class to insert the text in the PDF file.

## Highlight Text in PDF File

Using Html5 PDF Editor, you can highlight text in PDF files using Highlight Mode option from the menu bar. Once you select the Highlight Mode menu item, you can highlight any text and area using the rectangular highlighting tool. In our next section, we will discuss the technical details behind this feature.

### How it works?

**HTML - "Highlight Mode" menu item is selected on the page**

When you select "Highlight Mode" menu item, you can draw a rectangular highlight around any text or item in your PDF file. The implementation of this process can be seen in "tools.rect" method in Editor.js file.

**Javascript - Draw highlighting rectangle on the editor.**

See Editor.js tab below for source code of tool.rect method, which allows the user to draw highlighting rectangle at any location on the editor. Also, it saves the data in shapes collection which is later used on server side to insert highlighting in source PDF file. You can check the source code of saveFile method which is called when the file is saved.

**ASP.NET web method handles server requests**

As mentioned above, the highlighting is actually inserted into our source PDF file when we perform the save operation which uses GetImageStamp method to insert the image stamp in source PDF file at the location specified on editor. See Canvas.aspx.cs tab below with source code of GetImageStamp method. It uses Aspose.PDF.ImageStamp class to insert the highlighting rectangle in the PDF file.

## Searching Text in PDF File

Using Html5 PDF Editor, you can search text in PDF files using Search Text option from the menu bar. Once you click the Search Text menu item, you will be presented with a dialog box to input the text to be searched as shown below:

On providing the text and pressing search, all the instances of the word searched will get highlighted as shown below:

### How it works?

**HTML - "Search Text" menu item is clicked on the page**

When you click "Search Text" menu item, you are presented with an input dialog to enter the text you want to search. After entering the text and pressing search button, "Move" method is called which checks whether the move page operation is performed or search operation is performed and then it calls performSearch method in Editor.js file.

**jQuery - Send Ajax server request for method SearchData method**

See Editor.js tab below for source code of performSearch method, which gets the input text and a request to server method SearchData in _CanvasSave.aspx.cs_ file.

**ASP.NET web method handles server requests**

See _Canvas.aspx.cs_ tab below. Using the input text passed from performSearch method, SearchData method uses Aspose.PDF.Text.TextFragmentAbsorber class to search for all the instances of the input text in our source PDF file and System.Drawing.Brush class to draw highlighting against the searched text. Once the data is searched, the resultant file is again converted to image and gets loaded in the editor.

## Replacing Text in PDF File

Using Html5 PDF Editor, you can replace the existing text in PDF files using Replace Text option from the menu bar. Once you click the Replace Text menu item, you will be presented with a dialog box to input the text to be searched and replaced with.

### How it works?

**HTML - "Replace Text" menu item is clicked on the page**

When you click "Replace Text" menu item, you are presented with an input dialog to enter the text to search and replace. After entering the text and pressing Replace button, "ReplaceText" method is called in Editor.js file.

**jQuery - Send Ajax server request for method ReplaceText method**

See Editor.js tab below for source code of ReplaceText method, which gets the input text from input text dialog and a request to server method ReplaceText in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below. ReplaceText method uses Aspose.PDF.Text.TextFragmentAbsorber class to search for all the instances of the text to be replaced in our source PDF file and replaces all the instances with the replaced text. Once the text is replaced, the resultant file is again converted to image and gets loaded in the editor.

## Loading PDF File with Form Fields

Using Html5 PDF Editor, you can load and work with a PDF file containing form fields. Once the file with form fields is loaded in the editor, all the form fields are loaded for editing. In our next section, we will discuss the technical details behind this feature.

### How it works?

**HTML - "Open From Computer" menu item is clicked on the page.**

When you click "Open From Computer" menu item, you can upload the input file containing the form fields using file upload dialog. After the file gets uploaded, "fileSelected" method is called in Editor.js file.

**jQuery - Send server request for ProcessRequest method**

File gets posted to the server and method "ProcessRequest" is called in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below. Based on the form parameter passed, the file to be uploaded is saved on the server, ImageConverter method, converts the uploaded file to images and "CheckFields" method is called which uses Aspose.PDF.InteractiveFeatures.Forms class to check for all the form fields and collect the information regarding the fields i.e. FieldType, Location etc. and return the field's collection back to ImageConverter method. ImageConverter method returns the control back to "fileSelected" method in Editor.js

**Loading form fields on canvas**

See Editor.js tab below, manageFields method in Editor.js is used to generate all the fields on the canvas based on the information sent back from the server side. It draws HTML field controls using the type and location information from the server side to the canvas.

## Highlighting Required Form Fields

Using Html5 PDF Editor, you can highlight the required form fields in the editor. Once the file with form fields is loaded in the editor, all the required form fields are highlighted for the users to assist in editing. In our next section, we will discuss the technical details behind this feature.

### How it works?

**HTML - "Open From Computer" menu item is clicked on the page.**

When you click "Open From Computer" menu item, you can upload the input file containing the form fields using file upload dialog. After the file gets uploaded, "fileSelected" method is called in Editor.js file.

**jQuery - Send server request for ProcessRequest method**

File gets posted to the server and method "ProcessRequest" is called in CanvasSave.aspx.cs file.

**ASP.NET web method handles server requests**

See Canvas.aspx.cs tab below. Based on the form parameter passed, the file to be uploaded is saved on the server, ImageConverter method, converts the uploaded file to images and "CheckFields" method is called which uses Aspose.PDF.InteractiveFeatures.Forms class to check for all the form fields and collect the information regarding the fields i.e. FieldType, Location etc.. After getting the details of all the form fields, we get the information whether a form field is required form fields using Aspose.PDF.Facades.IsRequiredField method and return the field's collection back to ImageConverter method. ImageConverter method returns the control back to "fileSelected" method in Editor.js

**Loading form fields on canvas**

See Editor.js tab below, manageFields method in Editor.js is used to generate all the fields on the canvas based on the information sent back from the server side. It draws HTML field controls using the type and location information from the server side to the canvas. If a certain field is required, it uses the div (named as wrapper) around the control and change the background color property of the div to show it as highlighted required field.

