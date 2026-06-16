---

title: Add, Delete and Get Annotation - Facades

linktitle: Add, Delete and Get Annotation - Facades

type: docs

weight: 10

url: /cpp/add-delete-and-get-annotation-facades/

description: Discover how to add, delete, and retrieve annotations in PDF documents using C++ and Aspose.PDF for advanced document markup.

---



## <ins>**Add Annotation in an existing PDF file using PdfContentEditor**

**PdfContentEditor** allows you to add different types of annotations in an existing PDF file. You can use the respective method of **PdfContentEditor** class to add a particular type of annotation in an existing PDF document. For example, in the following code snippets, we have used **CreateText(...)** and **CreateFreeText(...)** methods, to add comments and free text annotation in the existing PDF respectively. You need to do the following steps, in order to add annotations using **PdfContentEditor** class:



- Create an object of Facades::PdfContentEditor.

- Use **BindPdf(...)** method to load an existing PDF.

- Call respective method to create annotation. e.g **CreateText(...),CreateFreeText(...), etc.**

- Save the PDF document by using the **Save(...)** method.

### **Add Comments to Existing PDF Document**

The following code snippet shows you how to add a comment in an existing PDF file.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto editor = MakeObject<Facades::PdfContentEditor>();
editor->BindPdf(L"..\\Data\\Annotations\\input.pdf");

editor->CreateText(System::Drawing::Rectangle(400, 700, 100, 100), L"Title", L"Welcome to Aspose", true, L"Comment", 1);	
editor->Save(L"..\\Data\\Annotations\\input_out.pdf");
```

## <ins>**Delete All Annotations from an existing PDF**

Aspose.PDF for C++ has also provided the **PdfAnnotationEditor** class, which enables you to delete all annotations from a PDF document. In order to delete all annotations from the existing PDF, you need to create an object of the **PdfAnnotationEditor** class and open the existing document. After that, you can use the **DeleteAnnotations(...)** method of the PdfAnnotationEditor class to delete the annotations. Following code snippet shows you the usage of PdfAnnotationEditor to serve the purpose:

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Annotations\\DeleteAllAnnotations.pdf");
// Delete All Annotations
editor->DeleteAnnotations();
// Save the document
editor->Save(L"..\\Data\\Annotations\\DeleteAllAnnotations_out.pdf");
```

## <ins>**Delete All Annotations by Specified Type**

You can use **PdfAnnotationEditor** class to delete all the annotations, by a specified annotation type, from the existing PDF file. In order to do that you need to create a **PdfAnnotationEditor** object and bind input PDF file using the **BindPdf** method. After that, call **DeleteAnnotations** method, with the string parameter, to delete all the annotations from the file; the string parameter represents the annotation type to be deleted. Finally, use the **Save** method to save the updated PDF file. The following code snippet shows you how to delete all annotations by specified annotation type.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Annotations\\DeleteAllAnnotations.pdf");
// Delete All Text Annotations
editor->DeleteAnnotations(L"Text");
// Save the document
editor->Save(L"..\\Data\\Annotations\\DeleteAllAnnotations_out.pdf");
```

## <ins>**Update/Modify Annotations in an Existing PDF File**

In order to update modify an annotation in a PDF document, you can use the **ModifyAnnotations(...)** method of the **PdfAnnotationEditor** class which takes an Annotation object along with the start and end index of annotations. The following code snippet will demonstrate the usage of **ModifyAnnotations(...)** method:

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto doc = MakeObject <Aspose::Pdf::Document>(L"..\\Data\\Annotations\\input.pdf");
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor =  System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load an existing PDF document
editor->BindPdf(doc);
// Create an annotation object
System::SharedPtr<Aspose::Pdf::InteractiveFeatures::Annotations::TextAnnotation> annot = System::MakeObject<Aspose::Pdf::InteractiveFeatures::Annotations::TextAnnotation>(doc->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(200, 400, 400, 600));
// Set modified date
annot->set_Modified(System::DateTime::get_Now());
// Set Title
annot->set_Title(L"NEW AUTHOR");
// Set Content
annot->set_Contents(L"NEW CONTENTS");
// Set Color
annot->set_Color(Color::get_Red());
// Set Object
annot->set_Subject(L"NEW SUBJECT");
// Set open flag
annot->set_Open(true);
// Modify Annotation
editor->ModifyAnnotations(1, 1, annot);
// Save the document
editor->Save(L"..\\Data\\Annotations\\output_out.pdf");
```

## <ins>**Import Annotations from XFDF into PDF File**

**ImportAnnotationFromXfdf** method of **PdfAnnotationEditor** class, allows you to import annotations to a PDF file. In order to import annotations, you need to create a **PdfAnnotationEditor** object and bind PDF file using the **BindPdf** method. After that, you need to create an enumeration of annotation types that you want to import to PDF file. You can then use the **ImportAnnotationFromXfdf** method to import the annotations. And finally, save the updated PDF file using the **Save** method of the **PdfAnnotationEditor** object. The following code snippet shows you how to import annotations from the XFDF file.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load Document where you want to import document
editor->BindPdf(L"..\\Data\\Annotations\\ImportAnnotations.pdf");
// Import annotations from XFDF file
editor->ImportAnnotationFromXfdf(L"..\\Data\\Annotations\\annotations.xfdf");
// Save the document
editor->Save(L"..\\Data\\Annotations\\ImportAnnotations_out.pdf");
```

## **Export Annotations from PDF File to XFDF**

The **ExportAnnotationXfdf** method allows you to export annotations from a PDF file. In order to export annotations, you need to create a **PdfAnnotationEditor** object and bind PDF file using the **BindPdf** method. After that, you need to create an enumeration of annotation types that you want to export from PDF file. You can then use the **ExportAnnotationXfdf** method to import the annotations. And finally, save the updated PDF file using the **Save** method of the **PdfAnnotationEditor** object. The following code snippet shows you how to export annotations to the XFDF file.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load Document where you want to import document
editor->BindPdf(L"..\\Data\\Annotations\\ExportAnnotations.pdf");
System::ArrayPtr<System::String> annotTypes = System::MakeArray<System::String>({ L"Text", L"Highlight" });
{
	System::SharedPtr<System::IO::Stream> stream = System::IO::File::Create(L"..\\Data\\Annotations\\Exported_out.xfdf");
	editor->ExportAnnotationsXfdf(stream, 1, 2, annotTypes);
}
```

## <ins>**Extract Annotations from an Existing PDF File**

**ExtractAnnotations** method allows you to extract annotations from a PDF file. In order to extract annotations, you need to create a **PdfAnnotationEditor** object and bind PDF file using the **BindPdf** method. After that, you need to create an enumeration of annotation types that you want to extract from PDF files. You can then use the **Extract** **Annotations** method to extract the annotations to an ArrayPtr. After that, you can loop through this list and get individual annotations. And finally, save the updated PDF file using the **Save** method of the **PdfAnnotationEditor** object. The following code snippet shows you how to extract annotations from PDF files.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load Document where you want to import document
editor->BindPdf(L"..\\Data\\Annotations\\ExtractAnnotations.pdf");
System::ArrayPtr<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType> annotTypes = System::MakeArray<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType>({ Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Text, Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Highlight }); 
// Extract Annotations
System::SharedPtr<System::Collections::Generic::IList<System::SharedPtr<Aspose::Pdf::InteractiveFeatures::Annotations::Annotation>>> annotList = editor->ExtractAnnotations(1, 2, annotTypes);
```

