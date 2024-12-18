---
title: Adicionar e Excluir Favoritos
type: docs
weight: 10
url: /pt/cpp/add-and-delete-bookmarks/
---

## <ins>**Adicionar Favorito**
A classe PdfBookmarkEditor permite que você adicione favoritos dentro de um documento PDF. O método CreateBookmarkOfPage oferecido por esta classe permite que você crie um favorito, que será direcionado para o número de página especificado. O trecho de código a seguir demonstra esse recurso da API Aspose.PDF para C++:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateBookmark-1.cpp" >}}
## <ins>**Adicionar Favorito Filho em documento existente**
Você pode adicionar favoritos filhos em um arquivo PDF existente usando a classe **PdfBookmarkEditor**. Para adicionar marcadores filhos, você precisa criar objetos **Bookmarks** e *Bookmark*. Você pode adicionar objetos **Bookmark** individuais no objeto **Bookmarks**. Você também precisa criar um objeto **Bookmark** e definir sua propriedade **ChildItem** para o objeto **Bookmarks**. Em seguida, você precisa passar este objeto **Bookmark** com **ChildItem** para o método **CreateBookmarks**. Finalmente, você precisa salvar o PDF atualizado usando o método **Save** da classe **PdfBookmarkEditor**. O trecho de código a seguir mostra como adicionar marcadores filhos em um arquivo PDF existente.

## <ins>**Excluir todos os marcadores do arquivo PDF**
Você pode excluir todos os marcadores do arquivo PDF usando o método **DeleteBookmarks** sem quaisquer parâmetros. Primeiramente, você precisa criar um objeto da classe **PdfBookmarkEditor** e vincular o arquivo PDF de entrada usando o método **BindPdf**. Depois disso, você precisa chamar o método **DeleteBookmarks** e, em seguida, salvar o arquivo PDF atualizado usando o método **Save**. O trecho de código a seguir mostra como excluir todos os marcadores do arquivo PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteAllBookmarks-1.cpp" >}}
## <ins>**Excluir um Marcador Específico de um Arquivo PDF**
Para excluir um marcador específico, você precisa chamar o método **DeleteBookmarks** com o parâmetro string (título). O **título** aqui representa o marcador a ser excluído do PDF. Crie um objeto da classe **PdfBookmarkEditor** e vincule o arquivo PDF de entrada usando o método **BindPdf**. Depois disso, chame o método **DeleteBookmarks** e, em seguida, salve o arquivo PDF atualizado usando o método **Save**. O trecho de código a seguir mostra como excluir um marcador específico de um arquivo PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteBookmark-1.cpp" >}}