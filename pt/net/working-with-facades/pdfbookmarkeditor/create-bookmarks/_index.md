---
title: Criar Favoritos
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/create-bookmarks/
description: Esta seção explica como criar favoritos para seu arquivo PDF com Aspose.PDF Facades usando a classe PdfBookmarkEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Bookmarks",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks with PdfBookmarkEditor",
    "abstract": "Apresentando a funcionalidade de favoritos em Aspose.PDF for .NET, projetada para melhorar a navegação em PDF, permitindo que os usuários criem favoritos para páginas inteiras, páginas específicas ou intervalos de páginas com propriedades personalizáveis. Este recurso permite a organização perfeita de documentos PDF, facilitando o acesso e a gestão eficaz do conteúdo. Se você precisa adicionar favoritos simples ou favoritos filhos intricados, a classe Aspose.PDF PdfBookmarkEditor fornece as ferramentas para elevar sua experiência em PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1124",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/create-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Criar Favoritos de Todas as Páginas

Para criar favoritos de todas as páginas, você precisa usar o método [CreateBookmarks](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) sem parâmetros. A classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor) permite que você crie favoritos de todas as páginas de um arquivo PDF. Primeiro, você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em seguida, você deve chamar o método [CreateBookmarks](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) e salvar o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save). O seguinte trecho de código mostra como criar Favoritos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmarksAll.pdf");
        // Create bookmark of all pages
        bookmarkEditor.CreateBookmarks();
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarksOfAllPages_out.pdf");
    }
} 
```

## Criar Favoritos de Todas as Páginas com Propriedades

A classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor) permite que você crie favoritos de todas as páginas de um arquivo PDF e especifique as propriedades (Cor, Negrito, Itálico). Você pode fazer isso com a ajuda do método [CreateBookmarks](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Primeiro, você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em seguida, você deve chamar o método [CreateBookmarks](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) e salvar o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save). O seguinte trecho de código mostra como criar favoritos de todas as páginas com propriedades.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPagesWithProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmarks-PagesProperties.pdf");
        // Create bookmark of all pages
        bookmarkEditor.CreateBookmarks(System.Drawing.Color.Green, true, true);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarks-PagesProperties_out.pdf");
    }
}
```

## Criar Favorito de uma Página Particular

Você pode criar um favorito de uma página particular em um arquivo PDF existente usando o método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). Este método aceita dois argumentos: título do favorito e número da página. Primeiro, você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em seguida, você deve chamar o método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) e salvar o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save). O seguinte trecho de código mostra como criar um favorito de uma página particular.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarkOfAParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmark-Page.pdf");
        // Create bookmark of a particular page
        bookmarkEditor.CreateBookmarkOfPage("Bookmark Name", 2);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmark-Page_out.pdf");
    }
}
```

## Criar Favoritos de um Intervalo de Páginas

A classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor) permite que você crie favoritos de um intervalo de páginas. Você pode usar o método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) com dois parâmetros: lista de favoritos (a lista dos títulos dos favoritos) e lista de páginas (a lista das páginas a serem marcadas). Primeiro, você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em seguida, você deve chamar o método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) e salvar o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save). O seguinte trecho de código mostra como criar favoritos de um intervalo de páginas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfARangeOfPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmark-Page.pdf");
        // Bookmark name list
        string[] bookmarkList = { "First" };
        // Page list
        int[] pageList = { 1 };
        // Create bookmark of a range of pages
        bookmarkEditor.CreateBookmarkOfPage(bookmarkList, pageList);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarkPageRange_out.pdf");
    }
}
```

## Adicionar Favorito em um Arquivo PDF Existente

Você pode adicionar um favorito em um arquivo PDF existente usando a classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor). Para criar o favorito, você precisa criar um objeto [Bookmark](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmark) e definir os atributos necessários do favorito. Depois disso, você precisa passar o objeto [Bookmark](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmark) para o método [CreateBookmarks](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor). Finalmente, você precisa salvar o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save). O seguinte trecho de código mostra como adicionar o favorito em um arquivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
    // Create bookmark
    var bookmark = new Aspose.Pdf.Facades.Bookmark();
    bookmark.PageNumber = 1;
    bookmark.Title = "New Bookmark";
    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "AddBookmark.pdf");
        // Create bookmarks
        bookmarkEditor.CreateBookmarks(bookmark);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "AddBookmark_out.pdf");
    }
}
```

## Adicionar Favorito Filho em um Arquivo PDF Existente

Você pode adicionar favoritos filhos em um arquivo PDF existente usando a classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor). Para adicionar favoritos filhos, você precisa criar objetos [Bookmark](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmark). Você pode adicionar objetos [Bookmark](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmark) individuais no objeto [Bookmarks](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmarks). Você também precisa criar um objeto [Bookmark](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmark) e definir sua propriedade [ChildItem](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmark/properties/childitem) para o objeto [Bookmarks](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmarks). Você então precisa passar este objeto [Bookmark](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmark) com [ChildItem](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/bookmark/properties/childitem) para o método [CreateBookmarks](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Finalmente, você precisa salvar o PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save) da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfbookmarkeditor). O seguinte trecho de código mostra como adicionar favoritos filhos em um arquivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
    // Create bookmarks
    var bookmarks = new Aspose.Pdf.Facades.Bookmarks();
    var childBookmark1 = new Aspose.Pdf.Facades.Bookmark();
    childBookmark1.PageNumber = 1;
    childBookmark1.Title = "First Child";
    var childBookmark2 = new Aspose.Pdf.Facades.Bookmark();
    childBookmark2.PageNumber = 2;
    childBookmark2.Title = "Second Child";
    bookmarks.Add(childBookmark1);
    bookmarks.Add(childBookmark2);
    var bookmark = new Aspose.Pdf.Facades.Bookmark();
    bookmark.Action = "GoTo";
    bookmark.PageNumber = 1;
    bookmark.Title = "Parent";
    bookmark.ChildItems = bookmarks;
    // Create PdfBookmarkEditor class
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "AddChildBookmark.pdf");
        // Create bookmarks
        bookmarkEditor.CreateBookmarks(bookmark);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "AddChildBookmark_out.pdf");
    }
}
```