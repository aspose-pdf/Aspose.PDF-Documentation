---
title: Aspose.PDF for C++ 23.8 Release Notes
type: docs
weight: 120
url: /cpp/aspose-pdf-for-cpp-23-8-release-notes/
description: This article decsribes changes and updates in version 23.8 of Aspose.PDF for C++ library
lastmod: "2023-08-17"
---
{{% alert color="primary" %}}

This page contains release notes information for Aspose.PDF for C++ 23.8.

{{% /alert %}}

## Changes and Improvements

The new version of Aspose.PDF for C++ has a codebase of Aspose.PDF for .Net 23.8.

Fixed TiffDevice for saving PDF document into multipage tiff file.

## Public API and Backward Incompatible Changes

### Added API

* class Aspose::Pdf::Plugins::PdfGeneratorTableBuilder 
* class Aspose::Pdf::Plugins::PdfGeneratorTableCellBuilder 
* class Aspose::Pdf::Plugins::PdfGeneratorTableRowBuidler 
* class Aspose::Pdf::Vector::XFormPlacement 
* class Aspose::Pdf::Vector::GraphicElement 
* class Aspose::Pdf::Vector::GraphicElementCollection 
* bool Aspose::Pdf::Text::TextFragmentState::IsFitRectangle(System::String, Aspose::Pdf::Rectangle)
* void Aspose::Pdf::Forms::CheckboxField::AddOption(System::String)
* void Aspose::Pdf::Forms::CheckboxField::AddOption(System::String, Aspose::Pdf::Rectangle)
* void Aspose::Pdf::Forms::Field::CopyToWidgetArray(Aspose::Pdf::Annotations::WidgetAnnotation[], int)
* bool Aspose::Pdf::Forms::RadioButtonField::get_NoToggleToOff()
* System::String Aspose::Pdf::Annotations::WidgetAnnotation::GetCheckedStateName()
* Aspose::Pdf::Rectangle Aspose::Pdf::Vector::SubPath::get_Rectangle()

* bool Aspose::Pdf::Document::HasIncrementalUpdate()
* bool Method:Aspose::Pdf::Operator::ValueEquals(Aspose::Pdf::Operator)
* void Aspose::Pdf::Page::AddGraphics(Aspose::Pdf::Vector::GraphicElementCollection,Aspose::Pdf::Rectangle)
* void Aspose::Pdf::Page::DeleteGraphics(Aspose::Pdf::Vector::GraphicElementCollection)
* System::String Aspose::Pdf::Point::ToString()
* Aspose::Pdf::Rectangle Aspose::Pdf::Rectangle::FromRect(System::Drawing::RectangleF) 

Removed:

### Removed APIs

* class Aspose::Pdf::Plugins::Generator::PdfGeneratorTableBuilder 
* class Aspose::Pdf::Plugins::Generator::PdfGeneratorTableCellBuilder 
* class Aspose::Pdf::Plugins::Generator::PdfGeneratorTableRowBuidler 

Complete details of API can be referenced from [Aspose.PDF for C++ API Reference Guide](https://reference.aspose.com/pdf/cpp).
