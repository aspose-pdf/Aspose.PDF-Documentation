---
title: Добавление, Удаление и Получение Аннотаций - Фасады
type: docs
weight: 10
url: /ru/cpp/add-delete-and-get-annotation-facades/
---

## <ins>**Добавление аннотации в существующий PDF файл с использованием PdfContentEditor**
**PdfContentEditor** позволяет добавлять различные типы аннотаций в существующий PDF файл. Вы можете использовать соответствующий метод класса **PdfContentEditor**, чтобы добавить определенный тип аннотации в существующий PDF документ. Например, в следующих фрагментах кода мы использовали методы **CreateText(...)** и **CreateFreeText(...)**, чтобы добавить комментарии и аннотации свободного текста соответственно в существующий PDF. Вам нужно выполнить следующие шаги, чтобы добавить аннотации с использованием класса **PdfContentEditor**:

- Создайте объект Facades::PdfContentEditor.
- Используйте метод **BindPdf(...)** для загрузки существующего PDF.
- Вызовите соответствующий метод для создания аннотации, например, **CreateText(...), CreateFreeText(...), и т.д.**
- Сохраните PDF документ, используя метод **Save(...)**.
### **Добавление комментариев в существующий PDF документ**

Следующий фрагмент кода показывает, как добавить комментарий в существующий PDF файл.
```

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto editor = MakeObject<Facades::PdfContentEditor>();
editor->BindPdf(L"..\\Data\\Annotations\\input.pdf");

editor->CreateText(System::Drawing::Rectangle(400, 700, 100, 100), L"Title", L"Welcome to Aspose", true, L"Comment", 1);	
editor->Save(L"..\\Data\\Annotations\\input_out.pdf");
```
## <ins>**Удалить все аннотации из существующего PDF**
Aspose.PDF для C++ также предоставляет класс **PdfAnnotationEditor**, который позволяет удалять все аннотации из PDF-документа. Чтобы удалить все аннотации из существующего PDF, вам нужно создать объект класса **PdfAnnotationEditor** и открыть существующий документ. После этого вы можете использовать метод **DeleteAnnotations(...)** класса PdfAnnotationEditor, чтобы удалить аннотации. Следующий фрагмент кода показывает, как использовать PdfAnnotationEditor для этой цели:



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
## <ins>**Удалить все аннотации по указанному типу**
Вы можете использовать класс **PdfAnnotationEditor**, чтобы удалить все аннотации определенного типа из существующего PDF-файла. Для этого вам нужно создать объект **PdfAnnotationEditor** и связать входной PDF-файл, используя метод **BindPdf**. После этого вызовите метод **DeleteAnnotations** с строковым параметром, чтобы удалить все аннотации из файла; строковый параметр представляет тип аннотации, который нужно удалить. Наконец, используйте метод **Save**, чтобы сохранить обновленный PDF-файл. Следующий фрагмент кода показывает, как удалить все аннотации по заданному типу аннотации.

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
## <ins>**Обновление/Изменение аннотаций в существующем PDF-файле**
Для того чтобы обновить или изменить аннотацию в PDF-документе, вы можете использовать метод **ModifyAnnotations(...)** класса **PdfAnnotationEditor**, который принимает объект Annotation вместе с начальным и конечным индексом аннотаций. Следующий фрагмент кода демонстрирует использование метода **ModifyAnnotations(...)**:

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
```## <ins>**Импорт аннотаций из XFDF в PDF файл**
Метод **ImportAnnotationFromXfdf** класса **PdfAnnotationEditor** позволяет импортировать аннотации в PDF файл. Для того чтобы импортировать аннотации, необходимо создать объект **PdfAnnotationEditor** и связать PDF файл с помощью метода **BindPdf**. После этого нужно создать перечисление типов аннотаций, которые вы хотите импортировать в PDF файл. Затем вы можете использовать метод **ImportAnnotationFromXfdf** для импорта аннотаций. И, наконец, сохранить обновленный PDF файл с помощью метода **Save** объекта **PdfAnnotationEditor**. Следующий фрагмент кода показывает, как импортировать аннотации из XFDF файла.

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
## **Экспорт аннотаций из PDF файла в XFDF**
Метод **ExportAnnotationXfdf** позволяет экспортировать аннотации из PDF файла. Чтобы экспортировать аннотации, вам нужно создать объект **PdfAnnotationEditor** и привязать PDF-файл, используя метод **BindPdf**. После этого вам нужно создать перечисление типов аннотаций, которые вы хотите экспортировать из PDF-файла. Затем вы можете использовать метод **ExportAnnotationXfdf** для импорта аннотаций. И наконец, сохраните обновленный PDF-файл, используя метод **Save** объекта **PdfAnnotationEditor**. Следующий фрагмент кода показывает, как экспортировать аннотации в файл XFDF.

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
## <ins>**Извлечение аннотаций из существующего PDF-файла**
Метод **ExtractAnnotations** позволяет извлечь аннотации из PDF-файла. Чтобы извлечь аннотации, необходимо создать объект **PdfAnnotationEditor** и связать PDF файл с помощью метода **BindPdf**. После этого нужно создать перечисление типов аннотаций, которые вы хотите извлечь из PDF файлов. Затем вы можете использовать метод **Extract** **Annotations** для извлечения аннотаций в ArrayPtr. После этого вы можете перебрать этот список и получить отдельные аннотации. И, наконец, сохранить обновленный PDF файл с помощью метода **Save** объекта **PdfAnnotationEditor**. Следующий фрагмент кода показывает, как извлечь аннотации из PDF файлов.