---
title: Trabalhando com Operadores usando C++
linktitle: Trabalhando com Operadores
type: docs
weight: 170
url: /pt/cpp/operators/
description: Este tópico explica como usar operadores com Aspose.PDF em C++. As classes de operadores oferecem ótimos recursos para manipulação de PDF.
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introdução aos Operadores de PDF e Seu Uso

Um operador é uma palavra-chave do PDF que especifica alguma ação que deve ser realizada, como desenhar uma forma gráfica na página. Uma palavra-chave de operador é distinguida de um objeto nomeado pela ausência de um caractere solidus inicial (2Fh). Operadores são significativos apenas dentro do fluxo de conteúdo.

Um fluxo de conteúdo é um objeto de fluxo PDF cujos dados consistem em instruções que descrevem os elementos gráficos a serem desenhados em uma página. Mais detalhes sobre operadores de PDF podem ser encontrados na [especificação do PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Detalhes da Implementação

Este tópico explica como usar operadores com Aspose.PDF. O exemplo selecionado adiciona uma imagem em um arquivo PDF para ilustrar o conceito. Para adicionar uma imagem em um arquivo PDF, são necessários diferentes operadores. Este exemplo usa [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix), [Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do), e [GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore).

- O operador **GSave** salva o estado gráfico atual do PDF.
- O operador **ConcatenateMatrix** (concatenar matriz) é usado para definir como uma imagem deve ser posicionada na página do PDF.
- O operador **Do** desenha a imagem na página.
- O operador **GRestore** restaura o estado gráfico.

Para adicionar uma imagem em um arquivo PDF:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) e abra o documento PDF de entrada.
1. Obter a página específica à qual a imagem será adicionada.
1. Adicione a imagem na coleção de Recursos da página.
1. Use os operadores para posicionar a imagem na página:
   - Primeiro, use o operador GSave para salvar o estado gráfico atual.
   - Em seguida, use o operador ConcatenateMatrix para especificar onde a imagem deve ser colocada.
   - Use o operador Do para desenhar a imagem na página.
1. Finalmente, use o operador GRestore para salvar o estado gráfico atualizado.

O trecho de código a seguir mostra como usar operadores PDF.

```cpp
void ExampleUsingOperators()
{
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"PDFOperators.pdf");

    // Definir coordenadas
    int lowerLeftX = 100;
    int lowerLeftY = 100;
    int upperRightX = 200;
    int upperRightY = 200;

    // Obter a página onde a imagem precisa ser adicionada
    auto page = document->get_Pages()->idx_get(1);

    // Carregar imagem no stream
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"PDFOperators.jpg");
    // Adicionar imagem à coleção de Imagens dos Recursos da Página
    page->get_Resources()->get_Images()->Add(imageStream);

    // Usando o operador GSave: este operador salva o estado gráfico atual
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Criar objetos Rectangle e Matrix
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
    auto matrix = MakeObject<Matrix>(
        new double[] {
            rectangle->get_URX() - rectangle->get_LLX(), 0, 0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(),  rectangle->get_LLY() });
    // Usando o operador ConcatenateMatrix (concatenar matriz): define como a imagem deve ser colocada
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());
    // Usando o operador Do: este operador desenha a imagem
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    // Usando o operador GRestore: este operador restaura o estado gráfico
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());


    // Salvar documento atualizado
    document->Save(_dataDir + u"PDFOperators_out.pdf");
}
```
## Draw XForm on Page using Operators

Este tópico demonstra como usar os operadores GSave/GRestore, o operador ContatenateMatrix para posicionar um xForm e o operador Do para desenhar um xForm em uma página.

O código abaixo envolve o conteúdo existente de um arquivo PDF com o par de operadores GSave/GRestore. Esta abordagem ajuda a obter o estado gráfico inicial no final do conteúdo existente. Sem esta abordagem, transformações indesejáveis podem permanecer no final da cadeia de operadores existente.

```cpp
void DrawXFormOnPageUsingOperators() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // O exemplo demonstra
    // Uso dos operadores GSave/GRestore
    // Uso do operador ContatenateMatrix para posicionar o xForm
    // Uso do operador Do para desenhar o xForm na página

    // Envolver o conteúdo existente com o par de operadores GSave/GRestore
    //        isso é para obter o estado gráfico inicial no final do conteúdo existente
    //        caso contrário, podem permanecer algumas transformações indesejáveis no final da cadeia de operadores existente
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Adicionar operador de estado gráfico de salvamento para limpar adequadamente o estado gráfico após novos comandos
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Criar xForm

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Definir largura e altura da imagem
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // Carregar imagem no fluxo
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // Adicionar imagem à coleção de Imagens dos Recursos do XForm
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // Usando o operador Do: este operador desenha a imagem
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Colocar formulário nas coordenadas x=100 y=500
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // Desenhar formulário com o operador Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Colocar formulário nas coordenadas x=100 y=300
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // Desenhar formulário com o operador Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Restaurar estado gráfico com GRestore após o GSave
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## Remover Objetos Gráficos usando Classes de Operadores

As classes de operadores oferecem ótimos recursos para manipulação de PDF. Quando um arquivo PDF contém gráficos que não podem ser removidos usando o método [DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380) da classe [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor), as classes de operadores podem ser usadas para removê-los.

O snippet de código a seguir mostra como remover gráficos. Observe que se o arquivo PDF contiver rótulos de texto para os gráficos, eles podem permanecer no arquivo PDF, usando essa abordagem. Portanto, procure os operadores gráficos para um método alternativo para excluir tais imagens.

```cpp
void RemoveGraphicsObjects() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // Operadores de pintura de caminho usados
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```