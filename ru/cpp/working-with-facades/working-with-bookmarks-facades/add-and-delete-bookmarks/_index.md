```
---
title: Добавление и Удаление Закладок
type: docs
weight: 10
url: ru/cpp/add-and-delete-bookmarks/
---

## <ins>**Добавить Закладку**
Класс PdfBookmarkEditor позволяет добавлять закладки в PDF документ. Метод CreateBookmarkOfPage, предлагаемый этим классом, позволяет создать закладку, которая будет указывать на заданный номер страницы. Следующий фрагмент кода демонстрирует эту возможность Aspose.PDF для C++ API:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateBookmark-1.cpp" >}}
## <ins>**Добавить Дочернюю Закладку в существующий документ**
Вы можете добавить дочерние закладки в существующий PDF файл, используя **PdfBookmarkEditor** класс.
``` Для того чтобы добавить дочерние закладки, вам нужно создать объекты **Bookmarks** и *Bookmark*. Вы можете добавить отдельные объекты **Bookmark** в объект **Bookmarks**. Также необходимо создать объект **Bookmark** и установить его свойство **ChildItem** в объект **Bookmarks**. Затем вам нужно передать этот объект **Bookmark** с **ChildItem** в метод **CreateBookmarks**. Наконец, вам нужно сохранить обновленный PDF, используя метод **Save** класса **PdfBookmarkEditor**. Следующий фрагмент кода показывает, как добавить дочерние закладки в существующий PDF файл.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateChildBookmark-1.cpp" >}}

## <ins>**Удалить все закладки из PDF файла**

Вы можете удалить все закладки из PDF файла, используя метод **DeleteBookmarks** без каких-либо параметров. First of all, you need to create an object of **PdfBookmarkEditor** class and bind the input PDF file using **BindPdf** method. After that, you need to call the **DeleteBookmarks** method and then save the updated PDF file using **Save** method. The following code snippet shows you how to delete all the bookmarks from the PDF file.

Сначала вам нужно создать объект класса **PdfBookmarkEditor** и привязать входной PDF-файл с помощью метода **BindPdf**. После этого вам нужно вызвать метод **DeleteBookmarks**, а затем сохранить обновленный PDF-файл с помощью метода **Save**. В следующем примере кода показано, как удалить все закладки из PDF-файла.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteAllBookmarks-1.cpp" >}}
## <ins>**Delete a Particular Bookmark from a PDF File**

## <ins>**Удаление определенной закладки из PDF-файла**

In order to delete a particular bookmark, you need to call **DeleteBookmarks** method with string (title) parameter. The **title** here represents the bookmark to be deleted from the PDF. Create an object of **PdfBookmarkEditor** class and bind input PDF file using **BindPdf** method. After that, call **DeleteBookmarks** method and then save the updated PDF file using **Save** method. The following code snippet shows you how to delete a particular bookmark from a PDF file.

Чтобы удалить определенную закладку, вам нужно вызвать метод **DeleteBookmarks** с параметром типа строка (название). Здесь **title** представляет закладку, которую нужно удалить из PDF. Создайте объект класса **PdfBookmarkEditor** и привяжите входной PDF-файл с помощью метода **BindPdf**. После этого вызовите метод **DeleteBookmarks**, а затем сохраните обновленный PDF-файл с помощью метода **Save**. В следующем примере кода показано, как удалить определенную закладку из PDF-файла.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteBookmark-1.cpp" >}}