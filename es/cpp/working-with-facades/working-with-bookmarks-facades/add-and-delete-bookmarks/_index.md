---
title: Añadir y Eliminar Marcadores
type: docs
weight: 10
url: /es/cpp/add-and-delete-bookmarks/
---

## <ins>**Añadir Marcador**
La clase PdfBookmarkEditor te permite añadir marcadores dentro del documento PDF. El método CreateBookmarkOfPage ofrecido por esta clase, te permite crear un marcador, que apuntará al número de página especificado. El siguiente fragmento de código demuestra esta característica de la API Aspose.PDF para C++:



```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfBookmarkEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Bookmarks\\AddBookmark.pdf");
// Create Bookmark
editor->CreateBookmarkOfPage(L"bookmark for page 1", 1);
// Save the document
editor->Save(L"..\\Data\\Bookmarks\\AddBookmark_out.pdf");
```
## <ins>**Añadir Marcador Hijo en documento existente**
Puedes añadir marcadores hijos en un archivo PDF existente utilizando la clase **PdfBookmarkEditor**. Para agregar marcadores secundarios, necesitas crear objetos **Bookmarks** y *Bookmark*. Puedes agregar objetos **Bookmark** individuales dentro del objeto **Bookmarks**. También necesitas crear un objeto **Bookmark** y establecer su propiedad **ChildItem** al objeto **Bookmarks**. Luego, debes pasar este objeto **Bookmark** con **ChildItem** al método **CreateBookmarks**. Finalmente, necesitas guardar el PDF actualizado usando el método **Save** de la clase **PdfBookmarkEditor**. El siguiente fragmento de código te muestra cómo agregar marcadores secundarios en un archivo PDF existente.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfBookmarkEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Bookmarks\\AddChildBookmark.pdf");
System::SharedPtr<Aspose::Pdf::Facades::Bookmark> bm1 = System::MakeObject<Aspose::Pdf::Facades::Bookmark>();
bm1->set_PageNumber(1);
bm1->set_Title(L"First child");
System::SharedPtr<Aspose::Pdf::Facades::Bookmark> bm2 = System::MakeObject<Aspose::Pdf::Facades::Bookmark>();
bm2->set_PageNumber(2);
bm2->set_Title(L"Second child");
System::SharedPtr<Aspose::Pdf::Facades::Bookmark> bm = System::MakeObject<Aspose::Pdf::Facades::Bookmark>();
bm->set_Action(L"GoTo");
bm->set_PageNumber(1);
bm->set_Title(L"Parent");
System::SharedPtr<Aspose::Pdf::Facades::Bookmarks> bms = System::MakeObject<Aspose::Pdf::Facades::Bookmarks>();
bms->Add(bm1);
bms->Add(bm2);
bm->set_ChildItem(bms);
editor->CreateBookmarks(bm);
// Save the document
editor->Save(L"..\\Data\\Bookmarks\\AddChildBookmark_out.pdf");
```
## <ins>**Eliminar todos los marcadores del archivo PDF**
Puedes eliminar todos los marcadores del archivo PDF usando el método **DeleteBookmarks** sin ningún parámetro. Primero, necesitas crear un objeto de la clase **PdfBookmarkEditor** y vincular el archivo PDF de entrada usando el método **BindPdf**. Después de eso, necesitas llamar al método **DeleteBookmarks** y luego guardar el archivo PDF actualizado usando el método **Save**. El siguiente fragmento de código te muestra cómo eliminar todos los marcadores del archivo PDF.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfBookmarkEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Bookmarks\\DeleteAllBookmarks.pdf");
// Delete All Bookmarks
editor->DeleteBookmarks();
// Save the document
editor->Save(L"..\\Data\\Bookmarks\\DeleteAllBookmarks_out.pdf");
```
## <ins>**Eliminar un Marcador Particular de un Archivo PDF**
Para eliminar un marcador particular, necesitas llamar al método **DeleteBookmarks** con un parámetro de cadena (título). El **título** aquí representa el marcador que se va a eliminar del PDF. Crea un objeto de la clase **PdfBookmarkEditor** y vincula el archivo PDF de entrada usando el método **BindPdf**. Después de eso, llama al método **DeleteBookmarks** y luego guarda el archivo PDF actualizado usando el método **Save**. El siguiente fragmento de código te muestra cómo eliminar un marcador particular de un archivo PDF.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfBookmarkEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Bookmarks\\DeleteParticularBookmark.pdf");
// Delete Particular Bookmarks
editor->DeleteBookmarks(L"Parent Outline");
// Save the document
editor->Save(L"..\\Data\\Bookmarks\\DeleteParticularBookmark_out.pdf");
```