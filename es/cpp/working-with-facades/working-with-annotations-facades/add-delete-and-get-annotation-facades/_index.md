---
title: Añadir, Eliminar y Obtener Anotación - Fachadas
type: docs
weight: 10
url: /es/cpp/add-delete-and-get-annotation-facades/
---

## <ins>**Añadir Anotación en un archivo PDF existente usando PdfContentEditor**
**PdfContentEditor** te permite añadir diferentes tipos de anotaciones en un archivo PDF existente. Puedes usar el método respectivo de la clase **PdfContentEditor** para añadir un tipo particular de anotación en un documento PDF existente. Por ejemplo, en los siguientes fragmentos de código, hemos utilizado los métodos **CreateText(...)** y **CreateFreeText(...)**, para añadir comentarios y anotaciones de texto libre en el PDF existente respectivamente. Necesitas seguir los siguientes pasos, para añadir anotaciones usando la clase **PdfContentEditor**:

- Crea un objeto de Facades::PdfContentEditor.
- Usa el método **BindPdf(...)** para cargar un PDF existente.
- Llama al método respectivo para crear anotaciones. e.g **CreateText(...),CreateFreeText(...), etc.**
- Guarda el documento PDF usando el método **Save(...)**.
### **Añadir Comentarios a un Documento PDF Existente**

El siguiente fragmento de código te muestra cómo añadir un comentario en un archivo PDF existente.
```

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto editor = MakeObject<Facades::PdfContentEditor>();
editor->BindPdf(L"..\\Data\\Annotations\\input.pdf");

editor->CreateText(System::Drawing::Rectangle(400, 700, 100, 100), L"Title", L"Welcome to Aspose", true, L"Comment", 1);	
editor->Save(L"..\\Data\\Annotations\\input_out.pdf");
```
## <ins>**Eliminar todas las anotaciones de un PDF existente**
Aspose.PDF para C++ también ha proporcionado la clase **PdfAnnotationEditor**, que te permite eliminar todas las anotaciones de un documento PDF. Para eliminar todas las anotaciones del PDF existente, necesitas crear un objeto de la clase **PdfAnnotationEditor** y abrir el documento existente. Después de eso, puedes usar el método **DeleteAnnotations(...)** de la clase PdfAnnotationEditor para eliminar las anotaciones. El siguiente fragmento de código muestra el uso de PdfAnnotationEditor para cumplir con el propósito:



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
## <ins>**Eliminar todas las anotaciones por tipo especificado**
Puedes usar la clase **PdfAnnotationEditor** para eliminar todas las anotaciones, por un tipo de anotación especificado, del archivo PDF existente. Para hacer eso, necesitas crear un objeto **PdfAnnotationEditor** y vincular el archivo PDF de entrada usando el método **BindPdf**. Después de eso, llama al método **DeleteAnnotations**, con el parámetro de cadena, para eliminar todas las anotaciones del archivo; el parámetro de cadena representa el tipo de anotación que se va a eliminar. Finalmente, usa el método **Save** para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo eliminar todas las anotaciones por tipo de anotación especificado.

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
## <ins>**Actualizar/Modificar Anotaciones en un Archivo PDF Existente**
Para actualizar modificar una anotación en un documento PDF, puedes usar el método **ModifyAnnotations(...)** de la clase **PdfAnnotationEditor** que toma un objeto Annotation junto con el índice de inicio y fin de las anotaciones. El siguiente fragmento de código demostrará el uso del método **ModifyAnnotations(...)**:

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
```## <ins>**Importar Anotaciones desde XFDF en un Archivo PDF**
El método **ImportAnnotationFromXfdf** de la clase **PdfAnnotationEditor**, te permite importar anotaciones a un archivo PDF. Para importar anotaciones, necesitas crear un objeto **PdfAnnotationEditor** y vincular el archivo PDF usando el método **BindPdf**. Después de eso, necesitas crear una enumeración de los tipos de anotaciones que deseas importar al archivo PDF. Luego puedes usar el método **ImportAnnotationFromXfdf** para importar las anotaciones. Y finalmente, guarda el archivo PDF actualizado usando el método **Save** del objeto **PdfAnnotationEditor**. El siguiente fragmento de código te muestra cómo importar anotaciones desde el archivo XFDF.

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
## **Exportar Anotaciones desde un Archivo PDF a XFDF**
El método **ExportAnnotationXfdf** te permite exportar anotaciones desde un archivo PDF. Para exportar anotaciones, necesitas crear un objeto **PdfAnnotationEditor** y vincular el archivo PDF usando el método **BindPdf**. Después de eso, necesitas crear una enumeración de tipos de anotaciones que deseas exportar del archivo PDF. Luego puedes usar el método **ExportAnnotationXfdf** para importar las anotaciones. Y finalmente, guarda el archivo PDF actualizado usando el método **Save** del objeto **PdfAnnotationEditor**. El siguiente fragmento de código te muestra cómo exportar anotaciones al archivo XFDF.

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
## <ins>**Extraer Anotaciones de un Archivo PDF Existente**
El método **ExtractAnnotations** te permite extraer anotaciones de un archivo PDF. In order to extract annotations, you need to create a **PdfAnnotationEditor** object and bind PDF file using the **BindPdf** method. After that, you need to create an enumeration of annotation types that you want to extract from PDF files. You can then use the **Extract** **Annotations** method to extract the annotations to an ArrayPtr. After that, you can loop through this list and get individual annotations. And finally, save the updated PDF file using the **Save** method of the **PdfAnnotationEditor** object. The following code snippet shows you how to extract annotations from PDF files.

Para extraer anotaciones, necesitas crear un objeto **PdfAnnotationEditor** y vincular el archivo PDF utilizando el método **BindPdf**. Después de eso, necesitas crear una enumeración de los tipos de anotaciones que deseas extraer de los archivos PDF. Luego puedes usar el método **Extract** **Annotations** para extraer las anotaciones a un ArrayPtr. Después de eso, puedes recorrer esta lista y obtener anotaciones individuales. Y finalmente, guarda el archivo PDF actualizado utilizando el método **Save** del objeto **PdfAnnotationEditor**. El siguiente fragmento de código te muestra cómo extraer anotaciones de archivos PDF.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load Document where you want to import document
editor->BindPdf(L"..\\Data\\Annotations\\ExtractAnnotations.pdf");
System::ArrayPtr<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType> annotTypes = System::MakeArray<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType>({ Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Text, Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Highlight }); 
// Extract Annotations
System::SharedPtr<System::Collections::Generic::IList<System::SharedPtr<Aspose::Pdf::InteractiveFeatures::Annotations::Annotation>>> annotList = editor->ExtractAnnotations(1, 2, annotTypes);
```