---
title: Añadir y Eliminar Marcadores
type: docs
weight: 10
url: /es/cpp/add-and-delete-bookmarks/
---

## <ins>**Añadir Marcador**
La clase PdfBookmarkEditor te permite añadir marcadores dentro del documento PDF. El método CreateBookmarkOfPage ofrecido por esta clase, te permite crear un marcador, que apuntará al número de página especificado. El siguiente fragmento de código demuestra esta característica de la API Aspose.PDF para C++:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateBookmark-1.cpp" >}}
## <ins>**Añadir Marcador Hijo en documento existente**
Puedes añadir marcadores hijos en un archivo PDF existente utilizando la clase **PdfBookmarkEditor**. Para agregar marcadores secundarios, necesitas crear objetos **Bookmarks** y *Bookmark*. Puedes agregar objetos **Bookmark** individuales dentro del objeto **Bookmarks**. También necesitas crear un objeto **Bookmark** y establecer su propiedad **ChildItem** al objeto **Bookmarks**. Luego, debes pasar este objeto **Bookmark** con **ChildItem** al método **CreateBookmarks**. Finalmente, necesitas guardar el PDF actualizado usando el método **Save** de la clase **PdfBookmarkEditor**. El siguiente fragmento de código te muestra cómo agregar marcadores secundarios en un archivo PDF existente.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateChildBookmark-1.cpp" >}}
## <ins>**Eliminar todos los marcadores del archivo PDF**
Puedes eliminar todos los marcadores del archivo PDF usando el método **DeleteBookmarks** sin ningún parámetro. Primero, necesitas crear un objeto de la clase **PdfBookmarkEditor** y vincular el archivo PDF de entrada usando el método **BindPdf**. Después de eso, necesitas llamar al método **DeleteBookmarks** y luego guardar el archivo PDF actualizado usando el método **Save**. El siguiente fragmento de código te muestra cómo eliminar todos los marcadores del archivo PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteAllBookmarks-1.cpp" >}}
## <ins>**Eliminar un Marcador Particular de un Archivo PDF**
Para eliminar un marcador particular, necesitas llamar al método **DeleteBookmarks** con un parámetro de cadena (título). El **título** aquí representa el marcador que se va a eliminar del PDF. Crea un objeto de la clase **PdfBookmarkEditor** y vincula el archivo PDF de entrada usando el método **BindPdf**. Después de eso, llama al método **DeleteBookmarks** y luego guarda el archivo PDF actualizado usando el método **Save**. El siguiente fragmento de código te muestra cómo eliminar un marcador particular de un archivo PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteBookmark-1.cpp" >}}