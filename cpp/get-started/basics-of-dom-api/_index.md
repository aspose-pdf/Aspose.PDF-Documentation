---
title: Basics of Aspose.PDF DOM API
linktitle: Basics of DOM API
type: docs
weight: 10
url: /cpp/basics-of-dom-api/
<<<<<<< HEAD
description: Aspose.PDF for C++ also uses the idea of DOM to represent the structure of a PDF document in terms of objects. Here you can read the description of this structure.
=======
description: Aspose.PDF for .NET also uses the idea of DOM to represent the structure of a PDF document in terms of objects. Here you can read the description of this structure.
>>>>>>> e2f23d8cd5f13b118d905b6d68f9147c569924c0
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction to the DOM API

Document Object Model (DOM) is a form of representation of structured documents as an object-oriented model. DOM is the official World Wide Web Consortium (W3C) standard for representing structured document s in a platform and language-neutral manner.

In simple words, DOM is a tree of objects that represent the structure of some document. Aspose.PDF for C++ also uses the idea of DOM to represent the structure of a PDF document in terms of objects. However, the aspects of the DOM (such as its Elements) are manipulated within the syntax of the programming language in use. The public interface of a DOM is specified in its application programming interface (API).

### Introduction to PDF Document

Portable Document Format (PDF) is an open standard for document exchange. A PDF document is a combination of text and binary data. If you open it in a text editor, you will see the raw objects that define the structure and contents of the document.

The logical structure of a PDF file is hierarchical and determines the sequence by which a viewing application draws the document’s pages and their contents. A PDF is composed of four components: objects, file structure, document structure and content streams.

### PDF Document Structure

As the structure of a PDF file is hierarchical, Aspose.PDF for C++ also accesses the elements in the same way. The following hierarchy shows you how the PDF document is logically structured and how Aspose.PDF for C++ DOM API constructs it.

![PDF Document Structure](../images/structure.png)

### Accessing PDF Document Elements

The Document object is at the root level of the object model. The Aspose.PDF for C++ DOM API allows you to create a Document object and then access all other objects in the hierarchy. You can either access any of the collections like Pages or individual element like Page etc. The DOM API provides single entry and exit points to manipulate the PDF document as shown below:

- Open PDF document
- Access PDF document structure in DOM style
- Update data in the PDF document
- Validate PDF document
- Export PDF document into different formats
- Finally, save the updated PDF document

## How to Use New Aspose.PDF for C++ API

This topic will explain the new Aspose.PDF for C++ API and guide you to get started quickly and easily. Please note that the details regarding the use of the particular features are not the part of this article.

The Aspose.PDF for C++ is composed of two parts:

- Aspose.PDF for C++ DOM API
- Aspose.PDF.Facades

You'll find the details of each of these areas below.

### Aspose.PDF for C++ DOM API

The Aspose.PDF for C++ DOM API corresponds to the PDF document structure, which helps you to work with the PDF documents not only at the file and document level, but also at the object level. We have provided more flexibility to the developers to access all of the elements and objects of the PDF document. Using the Aspose.PDF DOM API's classes, you can gain programmatic access to document elements and formatting. This new DOM API is comprised of various namespaces as given below:

### Aspose::Pdf Namespace Reference

This namespace provides the Document class which allows you to open and save a PDF document.

#### Aspose::Pdf::Text Namespace Reference

This namespace provides classes which help you work with the text and its various aspects, for example Font, FontCollection, FontRepository, FontSource, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment and TextSegmentCollection etc.

#### Aspose::Pdf::Collections Namespace Reference

This namespace provides class AsposeHashDictionary.

#### Aspose::Pdf::CommonData Namespace Reference

#### Aspose::Pdf::Diagnostics Namespace Reference

#### Aspose::Pdf::Drawing Namespace Reference

This namespace provides classes: Curve, Circle, Arc, Rectangle, Graph and etc, to add graphic elements to your PDF file.

#### Aspose::Pdf::Engine Namespace Reference

This namespace provides the Addressing, Interactive, Security, CommonData, 	IO, Presentation classes.

#### Aspose::Pdf::GroupProcessor Namespace Reference

This namespace provides classes: ExtractorFactory - represents factory for creating IPdfTypeExtractor objects, IDocumentPageTextExtractor, IDocumentTextExtractor, IPdfTypeExtractor classes- represents interface to interacting with extractor. 

#### Aspose::Pdf::Interchange Namespace Reference

#### Aspose::Pdf::LogicalStructure Namespace Reference

This namespace provides classes: AnnotationElement, AttributeOwnerStandard, CaptionElement, DocumentElement, FormElement, GroupingElement, ILSTextElement, PrivateElement, WarichuWTElement, and etc.

#### Aspose::Pdf::Operators Namespace Reference

This namespace provides classes of next operators: BasicSetColorAndPatternOperator, BlockTextOperator, SetCharWidthBoundingBox, SetColorStroke, SetHorizontalTextScaling, SetTextRenderingMode, TextShowOperator, and etc.

#### Aspose::Pdf::Optimization Namespace Reference

This namespace provides two classes - ImageCompressionOptions and OptimizationOptions.  

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

This namespace provides two classes: FontEmbeddingOptions - PDF/A standard requires, that all fonts must be embedded into document. This class includes flags for cases when it's not possible to embed some font cause this font is absent on destination PC. ToUnicodeProcessingRules - This class describes rules which can be used to solve Adobe Preflight error "Text cannot be mapped to Unicode".

#### Aspose::Pdf::Sanitization Namespace Reference

This namespace provides two classes: Details_SanitizationException and IRecovery. 

#### Aspose::Pdf::Tagged Namespace Reference

This namespace provides classes Details_TaggedException - Represents exception for TaggedPDF content of document. ITaggedContent - Represents interface for work with TaggedPdf content of document? and TaggedPdfExceptionCode.

#### Aspose::Pdf::Validation Namespace Reference

#### Aspose::Pdf::XfaConverter Namespace Reference

This namespace provides class XfaParserOptions - class to handle related data incapsulation.

#### Aspose::Pdf::Annotations Namespace Reference

Annotations are a part of a PDF document's interactive features. We have dedicated a namespace for annotations. This namespace contains classes that help you work with the annotations, for example, Annotation, AnnotationCollection, CircleAnnotation and LinkAnnotation etc.

#### Aspose::Pdf::Forms Namespace Reference

This namespace contains classes that help you work with PDF forms and form fields, for example Form, Field, TextBoxField and OptionCollection etc.

#### Aspose::Pdf::Devices Namespace Reference

We can perform various operations on the PDF documents such as converting PDF document to various image formats. However, such operations do not belong to the Document object and we cannot extend the Document class for such operations. That's why we have introduced the concept of the Device in the new DOM API.

##### Aspose::Pdf::Facades Namespace Reference

You can use Aspose.PDF.Facades namespace. This Namespace provides classes AutoFiller - represents a class to receive data from database or other datasource. Bookmark, Form, Stamp, PdfConverter anr more classes.
