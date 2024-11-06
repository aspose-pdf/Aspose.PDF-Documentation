---
title: Añadir, Eliminar y Obtener Anotación - Fachadas
type: docs
weight: 10
url: es/cpp/add-delete-and-get-annotation-facades/
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

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-AddAnnotation-AddAnnotation.cpp" >}}
## <ins>**Eliminar todas las anotaciones de un PDF existente**
Aspose.PDF para C++ también ha proporcionado la clase **PdfAnnotationEditor**, que te permite eliminar todas las anotaciones de un documento PDF. Para eliminar todas las anotaciones del PDF existente, necesitas crear un objeto de la clase **PdfAnnotationEditor** y abrir el documento existente. Después de eso, puedes usar el método **DeleteAnnotations(...)** de la clase PdfAnnotationEditor para eliminar las anotaciones. El siguiente fragmento de código muestra el uso de PdfAnnotationEditor para cumplir con el propósito:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteAllAnnotations-1.cpp" >}}
## <ins>**Eliminar todas las anotaciones por tipo especificado**
Puedes usar la clase **PdfAnnotationEditor** para eliminar todas las anotaciones, por un tipo de anotación especificado, del archivo PDF existente. Para hacer eso, necesitas crear un objeto **PdfAnnotationEditor** y vincular el archivo PDF de entrada usando el método **BindPdf**. Después de eso, llama al método **DeleteAnnotations**, con el parámetro de cadena, para eliminar todas las anotaciones del archivo; el parámetro de cadena representa el tipo de anotación que se va a eliminar. Finalmente, usa el método **Save** para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo eliminar todas las anotaciones por tipo de anotación especificado.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteParticularAnnotation-1.cpp" >}}
## <ins>**Actualizar/Modificar Anotaciones en un Archivo PDF Existente**
Para actualizar modificar una anotación en un documento PDF, puedes usar el método **ModifyAnnotations(...)** de la clase **PdfAnnotationEditor** que toma un objeto Annotation junto con el índice de inicio y fin de las anotaciones. El siguiente fragmento de código demostrará el uso del método **ModifyAnnotations(...)**:

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ModifyAnnotations-1.cpp" >}}## <ins>**Importar Anotaciones desde XFDF en un Archivo PDF**
El método **ImportAnnotationFromXfdf** de la clase **PdfAnnotationEditor**, te permite importar anotaciones a un archivo PDF. Para importar anotaciones, necesitas crear un objeto **PdfAnnotationEditor** y vincular el archivo PDF usando el método **BindPdf**. Después de eso, necesitas crear una enumeración de los tipos de anotaciones que deseas importar al archivo PDF. Luego puedes usar el método **ImportAnnotationFromXfdf** para importar las anotaciones. Y finalmente, guarda el archivo PDF actualizado usando el método **Save** del objeto **PdfAnnotationEditor**. El siguiente fragmento de código te muestra cómo importar anotaciones desde el archivo XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ImportAnnotations-1.cpp" >}}
## **Exportar Anotaciones desde un Archivo PDF a XFDF**
El método **ExportAnnotationXfdf** te permite exportar anotaciones desde un archivo PDF. Para exportar anotaciones, necesitas crear un objeto **PdfAnnotationEditor** y vincular el archivo PDF usando el método **BindPdf**. Después de eso, necesitas crear una enumeración de tipos de anotaciones que deseas exportar del archivo PDF. Luego puedes usar el método **ExportAnnotationXfdf** para importar las anotaciones. Y finalmente, guarda el archivo PDF actualizado usando el método **Save** del objeto **PdfAnnotationEditor**. El siguiente fragmento de código te muestra cómo exportar anotaciones al archivo XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExportAnnotations-1.cpp" >}}
## <ins>**Extraer Anotaciones de un Archivo PDF Existente**
El método **ExtractAnnotations** te permite extraer anotaciones de un archivo PDF. In order to extract annotations, you need to create a **PdfAnnotationEditor** object and bind PDF file using the **BindPdf** method. After that, you need to create an enumeration of annotation types that you want to extract from PDF files. You can then use the **Extract** **Annotations** method to extract the annotations to an ArrayPtr. After that, you can loop through this list and get individual annotations. And finally, save the updated PDF file using the **Save** method of the **PdfAnnotationEditor** object. The following code snippet shows you how to extract annotations from PDF files.

Para extraer anotaciones, necesitas crear un objeto **PdfAnnotationEditor** y vincular el archivo PDF utilizando el método **BindPdf**. Después de eso, necesitas crear una enumeración de los tipos de anotaciones que deseas extraer de los archivos PDF. Luego puedes usar el método **Extract** **Annotations** para extraer las anotaciones a un ArrayPtr. Después de eso, puedes recorrer esta lista y obtener anotaciones individuales. Y finalmente, guarda el archivo PDF actualizado utilizando el método **Save** del objeto **PdfAnnotationEditor**. El siguiente fragmento de código te muestra cómo extraer anotaciones de archivos PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExtractAnnotations-1.cpp" >}}