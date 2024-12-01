---
title: Basics of Aspose.PDF DOM API
linktitle: Basics of DOM API
type: docs
weight: 110
url: /python-java/basics-of-dom-api/
description: Aspose.PDF for Java also uses the idea of DOM to represent the structure of a PDF document in terms of objects. Here you can read the description of this structure.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction to the DOM API

Document Object Model (DOM) is a form of representation of structured documents as an object-oriented model. DOM is the official World Wide Web Consortium (W3C) standard for representing structured document s in a platform and language-neutral manner.

In simple words, DOM is a tree of objects that represent the structure of some document. Aspose.PDF for Java also uses the idea of DOM to represent the structure of a PDF document in terms of objects. However, the aspects of the DOM (such as its Elements) are manipulated within the syntax of the programming language in use. The public interface of a DOM is specified in its application programming interface (API).

### Introduction to PDF Document 

Portable Document Format (PDF) is an open standard for document exchange. A PDF document is a combination of text and binary data. If you open it in a text editor, you will see the raw objects that define the structure and contents of the document.

The logical structure of a PDF file is hierarchical and determines the sequence by which a viewing application draws the document's pages and their contents. A PDF is composed of four components: objects, file structure, document structure and content streams.

### PDF Document Structure

As the structure of a PDF file is hierarchical, Aspose.PDF for Java also accesses the elements in the same way. The following hierarchy shows you how the PDF document is logically structured and how Aspose.PDF for Java DOM API constructs it.

![PDF Document Structure](/java/images/structure.png)

### Accessing PDF Document Elements

The Document object is at the root level of the object model. The Aspose.PDF for Java DOM API allows you to create a Document object and then access all other objects in the hierarchy. You can either access any of the collections like Pages or individual element like Page etc. The DOM API provides single entry and exit points to manipulate the PDF document as shown below:

- Open PDF document
- Access PDF document structure in DOM style
- Update data in the PDF document
- Validate PDF document
- Export PDF document into different formats
- Finally, save the updated PDF document

## How to Use New Aspose.PDF for Java API

This topic will explain the new Aspose.PDF for Java API and guide you to get started quickly and easily. Please note that the details regarding the use of the particular features are not the part of this article.

The Aspose.PDF for Java is composed of two parts:

- Aspose.PDF for Java DOM API
- Aspose.PDF.Facades

You'll find the details of each of these areas below.

### Aspose.PDF for Java DOM API

The new Aspose.PDF for Java DOM API corresponds to the PDF document structure, which helps you to work with the PDF documents not only at the file and document level, but also at the object level. We have provided more flexibility to the developers to access all of the elements and objects of the PDF document. Using the Aspose.PDF DOM API's classes, you can gain programmatic access to document elements and formatting. This new DOM API is comprised of various namespaces as given below:

### com.aspose.pdf

This namespace provides the Document class which allows you to open and save a PDF document. The License class is also a part of this namespace. It also provides classes related to PDF pages, attachments, and bookmarks like com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, and com.aspose.pdf.OutlineCollection etc.

#### com.aspose.pdf.text

This namespace provides classes which help you work with the text and its various aspects, for example com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment and com.aspose.pdf.TextSegmentCollection etc.

#### com.aspose.pdf.TextOptions

This namespace provides classes that allow you to set different options for searching, editing or replacing text, for example com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions,  and com.aspose.pdf.TextSearchOptions.

#### com.aspose.pdf.PdfAction

This namespace contains classes that help you work with the interactive features of the PDF document, for example working with the document and other actions. This namespace contains classes like com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction and com.aspose.pdf.GoToURIAction etc.

#### com.aspose.pdf.Annotation

Annotations are a part of a PDF document's interactive features. We have dedicated a namespace for annotations. This namespace contains classes that help you work with the annotations, for example, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation and com.aspose.pdf.LinkAnnotation etc.

#### com.aspose.pdf.Form

This namespace contains classes that help you work with PDF forms and form fields, for example com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField and com.aspose.pdf.OptionCollection etc.

#### com.aspose.pdf.devices

We can perform various operations on the PDF documents such as converting PDF document to various image formats. However, such operations do not belong to the Document object and we cannot extend the Document class for such operations. That's why we have introduced the concept of the Device in the new DOM API.

##### com.aspose.pdf.facades

Previous to Aspose.PDF for Java t.o.o, you needed Aspose.PDF.Kit for Java to manipulate existing PDF files. To execute old Aspose.PDF.Kit code, can use com.aspose.pdf.facades namespace.
