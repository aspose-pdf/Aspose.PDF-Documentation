---
title: Add, Delete and Get Annotation - Facades
type: docs
weight: 10
url: pt/cpp/add-delete-and-get-annotation-facades/
---

## <ins>**Adicionar Anotação em um arquivo PDF existente usando PdfContentEditor**
**PdfContentEditor** permite que você adicione diferentes tipos de anotações em um arquivo PDF existente. Você pode usar o método correspondente da classe **PdfContentEditor** para adicionar um tipo particular de anotação em um documento PDF existente. Por exemplo, nos trechos de código a seguir, usamos os métodos **CreateText(...)** e **CreateFreeText(...)** para adicionar comentários e anotações de texto livre no PDF existente, respectivamente. Você precisa seguir as seguintes etapas, para adicionar anotações usando a classe **PdfContentEditor**:

- Crie um objeto de Facades::PdfContentEditor.
- Use o método **BindPdf(...)** para carregar um PDF existente.
- Chame o método correspondente para criar a anotação, por exemplo, **CreateText(...), CreateFreeText(...), etc.**
- Salve o documento PDF usando o método **Save(...)**.
### **Adicionar Comentários a um Documento PDF Existente**

O trecho de código a seguir mostra como adicionar um comentário em um arquivo PDF existente.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-AddAnnotation-AddAnnotation.cpp" >}}
## <ins>**Excluir Todas as Anotações de um PDF existente**
Aspose.PDF para C++ também forneceu a classe **PdfAnnotationEditor**, que permite excluir todas as anotações de um documento PDF. Para excluir todas as anotações do PDF existente, você precisa criar um objeto da classe **PdfAnnotationEditor** e abrir o documento existente. Depois disso, você pode usar o método **DeleteAnnotations(...)** da classe PdfAnnotationEditor para excluir as anotações. O trecho de código a seguir mostra o uso do PdfAnnotationEditor para atender ao propósito:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteAllAnnotations-1.cpp" >}}
## <ins>**Excluir Todas as Anotações por Tipo Especificado**
Você pode usar a classe **PdfAnnotationEditor** para excluir todas as anotações, por um tipo de anotação especificado, do arquivo PDF existente. Para fazer isso, você precisa criar um objeto **PdfAnnotationEditor** e vincular o arquivo PDF de entrada usando o método **BindPdf**. Depois disso, chame o método **DeleteAnnotations**, com o parâmetro string, para deletar todas as anotações do arquivo; o parâmetro string representa o tipo de anotação a ser deletado. Finalmente, use o método **Save** para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como deletar todas as anotações por tipo de anotação especificado.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteParticularAnnotation-1.cpp" >}}
## <ins>**Atualizar/Modificar Anotações em um Arquivo PDF Existente**
Para atualizar ou modificar uma anotação em um documento PDF, você pode usar o método **ModifyAnnotations(...)** da classe **PdfAnnotationEditor**, que aceita um objeto Annotation juntamente com o índice de início e fim das anotações. O trecho de código a seguir demonstra o uso do método **ModifyAnnotations(...)**:

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ModifyAnnotations-1.cpp" >}}## <ins>**Importar Anotações de XFDF para Arquivo PDF**
O método **ImportAnnotationFromXfdf** da classe **PdfAnnotationEditor** permite que você importe anotações para um arquivo PDF. Para importar anotações, você precisa criar um objeto **PdfAnnotationEditor** e vincular o arquivo PDF usando o método **BindPdf**. Depois disso, você precisa criar uma enumeração de tipos de anotações que deseja importar para o arquivo PDF. Você pode então usar o método **ImportAnnotationFromXfdf** para importar as anotações. E, finalmente, salve o arquivo PDF atualizado usando o método **Save** do objeto **PdfAnnotationEditor**. O trecho de código a seguir mostra como importar anotações do arquivo XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ImportAnnotations-1.cpp" >}}
## **Exportar Anotações de Arquivo PDF para XFDF**
O método **ExportAnnotationXfdf** permite que você exporte anotações de um arquivo PDF. Para exportar anotações, você precisa criar um objeto **PdfAnnotationEditor** e vincular o arquivo PDF usando o método **BindPdf**. Depois disso, você precisa criar uma enumeração de tipos de anotações que deseja exportar do arquivo PDF. Você pode então usar o método **ExportAnnotationXfdf** para importar as anotações. E finalmente, salve o arquivo PDF atualizado usando o método **Save** do objeto **PdfAnnotationEditor**. O trecho de código a seguir mostra como exportar anotações para o arquivo XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExportAnnotations-1.cpp" >}}
## <ins>**Extrair Anotações de um Arquivo PDF Existente**
O método **ExtractAnnotations** permite extrair anotações de um arquivo PDF. Para extrair anotações, você precisa criar um objeto **PdfAnnotationEditor** e vincular o arquivo PDF usando o método **BindPdf**. Depois disso, você precisa criar uma enumeração dos tipos de anotações que deseja extrair dos arquivos PDF. Você pode então usar o método **Extract Annotations** para extrair as anotações para um ArrayPtr. Depois disso, você pode percorrer essa lista e obter anotações individuais. E, finalmente, salvar o arquivo PDF atualizado usando o método **Save** do objeto **PdfAnnotationEditor**. O trecho de código a seguir mostra como extrair anotações de arquivos PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExtractAnnotations-1.cpp" >}}