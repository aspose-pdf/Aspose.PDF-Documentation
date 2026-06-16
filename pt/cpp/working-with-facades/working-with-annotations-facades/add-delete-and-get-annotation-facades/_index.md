---
title: Add, Delete and Get Annotation - Facades
type: docs
weight: 10
url: /pt/cpp/add-delete-and-get-annotation-facades/
---

## <ins>**Adicionar Anotação em um arquivo PDF existente usando PdfContentEditor**
**PdfContentEditor** permite que você adicione diferentes tipos de anotações em um arquivo PDF existente. Você pode usar o método correspondente da classe **PdfContentEditor** para adicionar um tipo particular de anotação em um documento PDF existente. Por exemplo, nos trechos de código a seguir, usamos os métodos **CreateText(...)** e **CreateFreeText(...)** para adicionar comentários e anotações de texto livre no PDF existente, respectivamente. Você precisa seguir as seguintes etapas, para adicionar anotações usando a classe **PdfContentEditor**:

- Crie um objeto de Facades::PdfContentEditor.
- Use o método **BindPdf(...)** para carregar um PDF existente.
- Chame o método correspondente para criar a anotação, por exemplo, **CreateText(...), CreateFreeText(...), etc.**
- Salve o documento PDF usando o método **Save(...)**.
### **Adicionar Comentários a um Documento PDF Existente**

O trecho de código a seguir mostra como adicionar um comentário em um arquivo PDF existente.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto editor = MakeObject<Facades::PdfContentEditor>();
editor->BindPdf(L"..\\Data\\Annotations\\input.pdf");

editor->CreateText(System::Drawing::Rectangle(400, 700, 100, 100), L"Title", L"Welcome to Aspose", true, L"Comment", 1);	
editor->Save(L"..\\Data\\Annotations\\input_out.pdf");
```
## <ins>**Excluir Todas as Anotações de um PDF existente**
Aspose.PDF para C++ também forneceu a classe **PdfAnnotationEditor**, que permite excluir todas as anotações de um documento PDF. Para excluir todas as anotações do PDF existente, você precisa criar um objeto da classe **PdfAnnotationEditor** e abrir o documento existente. Depois disso, você pode usar o método **DeleteAnnotations(...)** da classe PdfAnnotationEditor para excluir as anotações. O trecho de código a seguir mostra o uso do PdfAnnotationEditor para atender ao propósito:



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
## <ins>**Excluir Todas as Anotações por Tipo Especificado**
Você pode usar a classe **PdfAnnotationEditor** para excluir todas as anotações, por um tipo de anotação especificado, do arquivo PDF existente. Para fazer isso, você precisa criar um objeto **PdfAnnotationEditor** e vincular o arquivo PDF de entrada usando o método **BindPdf**. Depois disso, chame o método **DeleteAnnotations**, com o parâmetro string, para deletar todas as anotações do arquivo; o parâmetro string representa o tipo de anotação a ser deletado. Finalmente, use o método **Save** para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como deletar todas as anotações por tipo de anotação especificado.

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
## <ins>**Atualizar/Modificar Anotações em um Arquivo PDF Existente**
Para atualizar ou modificar uma anotação em um documento PDF, você pode usar o método **ModifyAnnotations(...)** da classe **PdfAnnotationEditor**, que aceita um objeto Annotation juntamente com o índice de início e fim das anotações. O trecho de código a seguir demonstra o uso do método **ModifyAnnotations(...)**:

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
```## <ins>**Importar Anotações de XFDF para Arquivo PDF**
O método **ImportAnnotationFromXfdf** da classe **PdfAnnotationEditor** permite que você importe anotações para um arquivo PDF. Para importar anotações, você precisa criar um objeto **PdfAnnotationEditor** e vincular o arquivo PDF usando o método **BindPdf**. Depois disso, você precisa criar uma enumeração de tipos de anotações que deseja importar para o arquivo PDF. Você pode então usar o método **ImportAnnotationFromXfdf** para importar as anotações. E, finalmente, salve o arquivo PDF atualizado usando o método **Save** do objeto **PdfAnnotationEditor**. O trecho de código a seguir mostra como importar anotações do arquivo XFDF.

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
## **Exportar Anotações de Arquivo PDF para XFDF**
O método **ExportAnnotationXfdf** permite que você exporte anotações de um arquivo PDF. Para exportar anotações, você precisa criar um objeto **PdfAnnotationEditor** e vincular o arquivo PDF usando o método **BindPdf**. Depois disso, você precisa criar uma enumeração de tipos de anotações que deseja exportar do arquivo PDF. Você pode então usar o método **ExportAnnotationXfdf** para importar as anotações. E finalmente, salve o arquivo PDF atualizado usando o método **Save** do objeto **PdfAnnotationEditor**. O trecho de código a seguir mostra como exportar anotações para o arquivo XFDF.

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
## <ins>**Extrair Anotações de um Arquivo PDF Existente**
O método **ExtractAnnotations** permite extrair anotações de um arquivo PDF. Para extrair anotações, você precisa criar um objeto **PdfAnnotationEditor** e vincular o arquivo PDF usando o método **BindPdf**. Depois disso, você precisa criar uma enumeração dos tipos de anotações que deseja extrair dos arquivos PDF. Você pode então usar o método **Extract Annotations** para extrair as anotações para um ArrayPtr. Depois disso, você pode percorrer essa lista e obter anotações individuais. E, finalmente, salvar o arquivo PDF atualizado usando o método **Save** do objeto **PdfAnnotationEditor**. O trecho de código a seguir mostra como extrair anotações de arquivos PDF.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load Document where you want to import document
editor->BindPdf(L"..\\Data\\Annotations\\ExtractAnnotations.pdf");
System::ArrayPtr<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType> annotTypes = System::MakeArray<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType>({ Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Text, Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Highlight }); 
// Extract Annotations
System::SharedPtr<System::Collections::Generic::IList<System::SharedPtr<Aspose::Pdf::InteractiveFeatures::Annotations::Annotation>>> annotList = editor->ExtractAnnotations(1, 2, annotTypes);
```