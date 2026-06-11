---
title: 追加、削除、および取得注釈 - ファサード
type: docs
weight: 10
url: /ja/cpp/add-delete-and-get-annotation-facades/
---

## <ins>**既存のPDFファイルに注釈を追加する PdfContentEditor を使用して**
**PdfContentEditor** を使用すると、既存のPDFファイルにさまざまなタイプの注釈を追加できます。特定のタイプの注釈を既存のPDFドキュメントに追加するには、**PdfContentEditor** クラスのそれぞれのメソッドを使用します。たとえば、以下のコードスニペットでは、**CreateText(...)** と **CreateFreeText(...)** メソッドを使用して、コメントとフリーテキスト注釈をそれぞれ既存のPDFに追加しています。 **PdfContentEditor** クラスを使用して注釈を追加するには、次の手順を実行する必要があります：

- Facades::PdfContentEditor のオブジェクトを作成します。
- **BindPdf(...)** メソッドを使用して既存のPDFを読み込みます。
- 注釈を作成するためのそれぞれのメソッドを呼び出します。例：**CreateText(...),CreateFreeText(...)** など。
- **Save(...)** メソッドを使用してPDFドキュメントを保存します。
### **既存のPDFドキュメントにコメントを追加する**

次のコードスニペットは、既存のPDFファイルにコメントを追加する方法を示しています。
```

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto editor = MakeObject<Facades::PdfContentEditor>();
editor->BindPdf(L"..\\Data\\Annotations\\input.pdf");

editor->CreateText(System::Drawing::Rectangle(400, 700, 100, 100), L"Title", L"Welcome to Aspose", true, L"Comment", 1);	
editor->Save(L"..\\Data\\Annotations\\input_out.pdf");
```
## <ins>**既存のPDFからすべての注釈を削除**
Aspose.PDF for C++ は、PDFドキュメントからすべての注釈を削除することを可能にする**PdfAnnotationEditor**クラスも提供しています。既存のPDFからすべての注釈を削除するには、**PdfAnnotationEditor**クラスのオブジェクトを作成し、既存のドキュメントを開く必要があります。その後、PdfAnnotationEditorクラスの**DeleteAnnotations(...)**メソッドを使用して注釈を削除できます。以下のコードスニペットは、その目的でPdfAnnotationEditorを使用する方法を示しています。

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
## <ins>**指定されたタイプによるすべての注釈の削除**
**PdfAnnotationEditor**クラスを使用して、既存のPDFファイルから指定された注釈タイプによるすべての注釈を削除できます。 そのためには、**PdfAnnotationEditor** オブジェクトを作成し、**BindPdf** メソッドを使用して入力 PDF ファイルをバインドする必要があります。その後、文字列パラメータを使用して、**DeleteAnnotations** メソッドを呼び出してファイルからすべての注釈を削除します。文字列パラメータは削除する注釈のタイプを表します。最後に、**Save** メソッドを使用して更新された PDF ファイルを保存します。次のコードスニペットは、指定された注釈タイプによってすべての注釈を削除する方法を示しています。

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
## <ins>**既存の PDF ファイル内の注釈の更新/変更**
PDF ドキュメント内の注釈を更新/変更するために、**PdfAnnotationEditor** クラスの **ModifyAnnotations(...)** メソッドを使用できます。このメソッドは、注釈オブジェクトと注釈の開始および終了インデックスを受け取ります。次のコードスニペットは、**ModifyAnnotations(...)** メソッドの使用方法を示します。

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
```## <ins>**XFDFからPDFファイルに注釈をインポートする**
**PdfAnnotationEditor**クラスの**ImportAnnotationFromXfdf**メソッドを使用すると、注釈をPDFファイルにインポートできます。注釈をインポートするには、**PdfAnnotationEditor**オブジェクトを作成し、**BindPdf**メソッドを使用してPDFファイルをバインドする必要があります。その後、PDFファイルにインポートしたい注釈タイプの列挙を作成する必要があります。次に、**ImportAnnotationFromXfdf**メソッドを使用して注釈をインポートできます。そして最後に、**PdfAnnotationEditor**オブジェクトの**Save**メソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、XFDFファイルから注釈をインポートする方法を示しています。

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
## **PDFファイルからXFDFへの注釈をエクスポートする**
**ExportAnnotationXfdf**メソッドを使用すると、PDFファイルから注釈をエクスポートできます。 ドキュメントの注釈をエクスポートするには、**PdfAnnotationEditor** オブジェクトを作成し、**BindPdf** メソッドを使用してPDFファイルをバインドする必要があります。その後、PDFファイルからエクスポートしたい注釈タイプの列挙を作成する必要があります。次に、**ExportAnnotationXfdf** メソッドを使用して注釈をインポートできます。そして最後に、**PdfAnnotationEditor** オブジェクトの **Save** メソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、XFDFファイルに注釈をエクスポートする方法を示しています。

## <ins>**既存のPDFファイルから注釈を抽出する**
**ExtractAnnotations** メソッドは、PDFファイルから注釈を抽出することを可能にします。 ドキュメントから注釈を抽出するには、**PdfAnnotationEditor** オブジェクトを作成し、**BindPdf** メソッドを使用してPDFファイルをバインドする必要があります。その後、PDFファイルから抽出したい注釈タイプの列挙を作成する必要があります。次に、**Extract Annotations** メソッドを使用して、注釈を ArrayPtr に抽出できます。その後、このリストをループして個々の注釈を取得することができます。そして最後に、**PdfAnnotationEditor** オブジェクトの **Save** メソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、PDFファイルから注釈を抽出する方法を示しています。



```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load Document where you want to import document
editor->BindPdf(L"..\\Data\\Annotations\\ExtractAnnotations.pdf");
System::ArrayPtr<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType> annotTypes = System::MakeArray<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType>({ Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Text, Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Highlight }); 
// Extract Annotations
System::SharedPtr<System::Collections::Generic::IList<System::SharedPtr<Aspose::Pdf::InteractiveFeatures::Annotations::Annotation>>> annotList = editor->ExtractAnnotations(1, 2, annotTypes);
```