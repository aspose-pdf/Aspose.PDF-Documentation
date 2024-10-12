---
title: Obter Resolução e Dimensões de Imagens Incorporadas usando C++
linktitle: Obter Resolução e Dimensões
type: docs
weight: 40
url: /cpp/get-resolution-and-dimensions-of-embedded-images/
description: Esta seção mostra detalhes sobre como obter a resolução e dimensões de Imagens Incorporadas
lastmod: "2021-12-18"
---

Este tópico explica como usar as classes de operador no namespace Aspose.PDF, que fornecem a capacidade de obter informações de resolução e dimensão sobre imagens sem ter que extraí-las.

Existem diferentes maneiras de conseguir isso. Este artigo explica como usar um `arraylist` e [classes de posicionamento de imagem](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement).

1. Primeiro, carregue o arquivo PDF de origem (com imagens).
1. Em seguida, crie um objeto ArrayList para armazenar os nomes de quaisquer imagens no documento.
1. Obtenha as imagens usando a propriedade Page.Resources.Images.
1. Crie um objeto stack para armazenar o estado gráfico da imagem e use-o para acompanhar diferentes estados da imagem.
1. Crie um objeto ConcatenateMatrix que define a transformação atual. Ele também suporta escalonamento, rotação e inclinação de qualquer conteúdo. Ele concatena a nova matriz com a anterior. Observe que não podemos definir a transformação do zero, mas apenas modificar a transformação existente.
1. Como podemos modificar a matriz com ConcatenateMatrix, também podemos precisar reverter ao estado original da imagem. Use [operador GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) e [operador GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/). Esses operadores são emparelhados, então devem ser chamados juntos. Por exemplo, se você fizer algum trabalho gráfico com transformações complexas e finalmente retornar as transformações ao estado inicial, a abordagem será algo assim:

O trecho de código a seguir mostra como obter as dimensões e resolução de uma imagem sem extrair a imagem do documento PDF.

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
    String _dataDir("C:\\Samples\\");
    // Carregar o arquivo PDF de origem
    auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

    // Definir a resolução padrão para a imagem
    int defaultResolution = 72;
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
    // Definir objeto de lista de array que conterá os nomes das imagens
    auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

    // Inserir um objeto na pilha
    graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

    // Obter todos os operadores na primeira página do documento
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        // Usar operadores GSave/GRestore para reverter as transformações de volta para as anteriormente definidas
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

        // Instanciar objeto ConcatenateMatrix pois ele define a matriz de transformação atual.
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

        // Criar operador Do que desenha objetos a partir de recursos. Ele desenha objetos Form e objetos Image
        auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

        if (opSaveState != nullptr)
        {
            // Salvar estado anterior e empurrar estado atual para o topo da pilha
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
        }
        else if (opRestoreState != nullptr)
        {
            // Descartar estado atual e restaurar o anterior
            graphicsState->Pop();
        }
        else if (opCtm != nullptr)
        {
            auto cm = MakeObject<System::Drawing::Drawing2D::Matrix>(
                (float)opCtm->get_Matrix()->get_A(),
                (float)opCtm->get_Matrix()->get_B(),
                (float)opCtm->get_Matrix()->get_C(),
                (float)opCtm->get_Matrix()->get_D(),
                (float)opCtm->get_Matrix()->get_E(),
                (float)opCtm->get_Matrix()->get_F());

            // Multiplicar matriz atual com a matriz de estado
            System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
            continue;
        }
        else if (opDo != nullptr)
        {
            // No caso de ser um operador de desenho de imagem
            if (imageNames->Contains(opDo->get_Name()))
            {
                auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
                // Criar objeto XImage para conter imagens da primeira página do pdf
                auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

                // Obter dimensões da imagem
                double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
                double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
                // Obter informações de Altura e Largura da imagem
                double originalWidth = image->get_Width();
                double originalHeight = image->get_Height();

                // Calcular resolução com base nas informações acima
                double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                double resVertical = originalHeight * defaultResolution / scaledHeight;

                // Exibir informações de Dimensão e Resolução de cada imagem
                Console::Write(_dataDir);
                Console::Write(u" imagem {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                    opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
            }
        }
    }
}
```