---
title: Trabalhando com Ações em PDF 
linktitle: Ações
type: docs
weight: 20
url: pt/cpp/actions/
description: Esta seção explica como adicionar ações ao documento e campos de formulário programaticamente com C++. 
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Hiperlink em um Arquivo PDF

Documentos PDF são uma ótima maneira de compartilhar informações. Eles são fáceis de ler, editar e distribuir. No entanto, criar links em um documento PDF pode ser desafiador. Vamos mostrar como.

É possível adicionar hiperlinks a arquivos PDF, seja para permitir que os leitores naveguem para outra parte do PDF, ou para conteúdo externo.

Por exemplo, você pode querer adicionar um índice clicável aos seus ebooks, citar recursos externos para o seu artigo, ou rapidamente navegar o leitor para uma página diferente no site para obter mais informações sobre um assunto.

Para criar hiperlinks com alguns cliques, siga estas etapas simples:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).  
1. Obtenha a classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à qual deseja adicionar o link.  
1. Crie um objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) usando os objetos Page e [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/). O objeto rectangle é usado para especificar o local na página onde o link deve ser adicionado.  
1. Defina a propriedade Action para o objeto [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) que especifica a localização do URI remoto.  
1. Para exibir um texto de hyperlink, adicione uma string de texto em um local semelhante ao local onde o objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) está colocado.  
1. Para adicionar um texto livre:

- Instancie um objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation). It also accepts Page and Rectangle objects as argument, so it is possible to provide same values as specified against the LinkAnnotation constructor.  
- Usando a propriedade Contents do objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation), especifique a string que deve ser exibida no PDF de saída.
- Opcionalmente, defina a largura da borda de ambos os objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) e FreeTextAnnotation para 0 para que não apareçam no documento PDF.
- Uma vez que os objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) e [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) tenham sido definidos, adicione esses links à coleção Annotations do objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

- Finalmente, salve o PDF atualizado usando o método Save do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
O trecho de código a seguir mostra como adicionar um hyperlink a um arquivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {

String _dataDir("C:\\Samples\\");

// Abrir documento

auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");

// Criar link

auto page = document->get_Pages()->idx_get(1);

// Criar objeto de anotação de link

auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));

// Criar objeto de borda para LinkAnnotation

auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);

// Definir o valor da largura da borda como 0

border->set_Width(0);

// Definir a borda para LinkAnnotation

link->set_Border(border);

// Especificar o tipo de link como URI remoto

link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

// Adicionar anotação de link à coleção de anotações da primeira página do arquivo PDF

page->get_Annotations()->Add(link);


// Criar anotação de texto livre

auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(


page,


MakeObject<Rectangle>(100, 100, 300, 300),


MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(



FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));


// String a ser adicionada como texto livre

textAnnotation->set_Contents(u"Link para o site da Aspose");

// Definir a borda para Anotação de Texto Livre

textAnnotation->set_Border(border);

// Adicionar anotação de Texto Livre à coleção de anotações da primeira página do Documento

page->get_Annotations()->Add(textAnnotation);


// Salvar documento atualizado

document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## Criar Hiperlink para páginas no mesmo PDF

Aspose.PDF para C++ fornece uma ótima funcionalidade tanto para a criação quanto para a manipulação de PDFs. Ele também oferece a funcionalidade de adicionar links para páginas de PDF, e um link pode direcionar para páginas em outro arquivo PDF, uma URL da web, um link para iniciar um Aplicativo ou até mesmo um link para páginas no mesmo arquivo PDF. Para adicionar hiperlinks locais (links para páginas no mesmo arquivo PDF), uma classe chamada [LocalHyperlink](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink) é adicionada ao namespace Aspose.PDF e esta classe possui uma propriedade chamada TargetPageNumber, que é usada para especificar a página de destino para o hiperlink.

Para adicionar o hiperlink local, precisamos criar um TextFragment para que o link possa ser associado com o TextFragment. A classe [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) possui uma propriedade chamada Hyperlink que é usada para associar uma instância LocalHyperlink. O trecho de código a seguir mostra as etapas para realizar esse requisito.

```cpp
void CreateHyperlinkToPagesInSamePDF() {

String _dataDir("C:\\Samples\\");


// Criar instância de Documento

auto document = MakeObject<Document>();


// Adicionar página à coleção de páginas do arquivo PDF

auto page = document->get_Pages()->Add();


// Criar instância de Text Fragment

auto text = MakeObject<TextFragment>(u"teste de número de página de link para a página 2");


// Criar instância de hyperlink local

auto link = MakeObject<LocalHyperlink>();


// Definir página de destino para a instância de link

link->set_TargetPageNumber(2);


// Definir hyperlink do TextFragment

text->set_Hyperlink(link);


// Adicionar texto à coleção de parágrafos da Página

page->get_Paragraphs()->Add(text);


// Criar nova instância de TextFragment

text = new TextFragment(u"teste de número de página de link para a página 1");


// TextFragment deve ser adicionado sobre nova página

text->set_IsInNewPage(true);


// Criar outra instância de hyperlink local

link = new LocalHyperlink();


// Definir página de destino para o segundo hyperlink

link->set_TargetPageNumber(1);


// Definir link para o segundo TextFragment

text->set_Hyperlink(link);


// Adicionar texto à coleção de parágrafos do objeto página

page->get_Paragraphs()->Add(text);


// Salvar documento atualizado

document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```
## Obter Destino do Hiperlink em PDF (URL)

Os links são representados como anotações em um arquivo PDF e podem ser adicionados, atualizados ou excluídos. O Aspose.PDF para C++ também suporta a obtenção do destino (URL) do hiperlink no arquivo PDF.

Para obter o URL de um link:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Obtenha a [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) da qual você deseja extrair links.
1. Use a classe [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) para extrair todos os objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) da página especificada.
1. Passe o objeto [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) para o método Accept do objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).
1. Obtenha todas as anotações de link selecionadas em um objeto IList usando a propriedade Selected do objeto [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).
1. Finalmente, extraia a Ação LinkAnnotation como GoToURIAction.

O trecho de código a seguir mostra como obter destinos de hiperlink (URL) de um arquivo PDF.

```cpp
void GetPDFHyperlinkDestination() {

String _dataDir("C:\\Samples\\");


auto document = new Document(_dataDir + u"Aspose-app-list.pdf");

// Extrair ações

auto page = document->get_Pages()->idx_get(1);


auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(


MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));

page->Accept(selector);


auto list = selector->get_Selected();

// Iterar através de cada item individual dentro da lista

if (list->get_Count() == 0)


Console::WriteLine(u"Nenhum hiperlink encontrado...");

else {


// Loop através de todos os favoritos


for (auto annot : list) {



auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);



if (la != nullptr) {




auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());




// Imprimir o URL de destino




Console::WriteLine(u"Destino: " + action->get_URI());



}


}

} // fim do else
}
```
## Obter Texto do Hiperlink

Um hiperlink tem duas partes: o texto que aparece no documento e o URL de destino. Em alguns casos, é o texto, e não o URL, que precisamos.

Texto e anotações/ações em um arquivo PDF são representados por diferentes entidades. O texto em uma página é apenas um conjunto de palavras e caracteres, enquanto as anotações trazem alguma interatividade, como a inerente a um hiperlink.

Para encontrar o conteúdo do URL, você precisa trabalhar tanto com a anotação quanto com o texto. O objeto [Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) em si não possui o texto, mas está sob o texto na página. Assim, para obter o texto, a Anotação fornece os limites do URL, enquanto o objeto Texto fornece o conteúdo do URL. Por favor, veja o seguinte trecho de código.

```cpp
  void GetHyperlinkText() {

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"aspose-app-list.pdf");

// Extrair ações

auto page = document->get_Pages()->idx_get(1);


for (auto annot : page->get_Annotations()) {


auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);


if (la != nullptr) {



// Imprimir o URL de cada Anotação de Link



auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());



Console::WriteLine(u"URI: " + action->get_URI());




auto absorber = MakeObject<TextAbsorber>();



absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);



absorber->get_TextSearchOptions()->set_Rectangle(annot->get_Rect());



page->Accept(absorber);



String extractedText = absorber->get_Text();



// Imprimir o texto associado ao hiperlink



Console::WriteLine(extractedText);


}

}
}
```

## Remover Ação de Abertura de Documento de um Arquivo PDF

[Como Especificar Página do PDF ao Visualizar Documento](#how-to-specify-pdf-page-when-viewing-document) explicou como instruir um documento a abrir em uma página diferente da primeira. Ao concatenar vários documentos, e um ou mais têm uma ação GoTo definida, você provavelmente vai querer removê-las. Por exemplo, se combinar dois documentos e o segundo tiver uma ação GoTo que te leva para a segunda página, o documento de saída abrirá na segunda página do segundo documento, em vez da primeira página do documento combinado. Para evitar esse comportamento, remova o comando de ação de abertura.

Para remover uma ação de abertura:

1. Defina a propriedade [OpenAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e) do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) como nulo.
2. Salve o PDF atualizado usando o método Save do objeto Document.

O seguinte trecho de código mostra como remover uma ação de abertura de documento do arquivo PDF.

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{

String _dataDir("C:\\Samples\\");

// Abrir documento

auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");

// Remover ação de abertura de documento

document->set_OpenAction(nullptr);


// Salvar documento atualizado

document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## Como Especificar Página do PDF ao Visualizar Documento {#how-to-specify-pdf-page-when-viewing-document}

Ao visualizar arquivos PDF em um visualizador de PDF, como o Adobe Reader, os arquivos geralmente abrem na primeira página. No entanto, é possível configurar o arquivo para abrir em uma página diferente.

A classe 'XYZExplicitDestination' permite especificar uma página em um arquivo PDF que você deseja abrir. Ao passar o valor do objeto GoToAction para a propriedade OpenAction da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), o documento é aberto na página especificada contra o objeto XYZExplicitDestination. O trecho de código a seguir mostra como especificar uma página como a ação de abertura do documento.

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{

String _dataDir("C:\\Samples\\");

// Carregar o arquivo PDF

auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");

// Obter a instância da segunda página do documento

auto page2 = document->get_Pages()->idx_get(2);

// Criar a variável para definir o fator de zoom da página de destino

double zoom = 1;

// Criar instância de GoToAction

auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);

// Ir para página 2

action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));

// Definir a ação de abertura do documento

document->set_OpenAction(action);

// Salvar documento atualizado

document->Save(_dataDir + u"goto2page_out.pdf");
}
```